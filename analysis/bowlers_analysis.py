"""
bowlers_analysis.py
-------------------

Professional Bowling Analysis Module for IPL Dashboard.

Responsibilities
----------------
✔ Bowling Summary
✔ Best Bowling Figures
✔ 4-Wicket Hauls
✔ 5-Wicket Hauls

(No Streamlit code)
(No Plotly code)
"""

from __future__ import annotations

import numpy as np
import pandas as pd


# ==========================================================
# Official Bowling Wickets
# ==========================================================

BOWLER_WICKETS = [
    "bowled",
    "caught",
    "lbw",
    "stumped",
    "caught and bowled",
    "hit wicket",
]


# ==========================================================
# Bowling Summary
# ==========================================================

def bowling_summary(deliveries_df: pd.DataFrame) -> pd.DataFrame:
    """
    Generate career bowling statistics for every bowler.
    """

    df = deliveries_df.copy()

    # ------------------------------------------------------
    # Legal Deliveries
    # ------------------------------------------------------

    legal_deliveries = df[
        ~df["extras_type"].isin(
            [
                "wides",
                "noballs",
            ]
        )
    ].copy()

    # ------------------------------------------------------
    # Bowler Wickets
    # ------------------------------------------------------

    wickets_df = df[
        df["dismissal_kind"].isin(BOWLER_WICKETS)
    ]

    wickets = (
        wickets_df
        .groupby("bowler")
        .size()
        .rename("Wickets")
    )

    # ------------------------------------------------------
    # Bowling Summary
    # ------------------------------------------------------

    bowling = (
        legal_deliveries
        .groupby("bowler")
        .agg(
            Balls=("ball", "count"),
            Runs=("total_runs", "sum"),
            Matches=("match_id", "nunique"),
            DotBalls=("total_runs", lambda x: (x == 0).sum()),
        )
    )

    bowling = bowling.join(wickets)

    bowling["Wickets"] = (
        bowling["Wickets"]
        .fillna(0)
        .astype(int)
    )

    # ------------------------------------------------------
    # Overs
    # ------------------------------------------------------

    bowling["Overs"] = (
        bowling["Balls"] / 6
    ).round(1)

    # ------------------------------------------------------
    # Economy
    # ------------------------------------------------------

    bowling["Economy"] = np.where(
        bowling["Overs"] > 0,
        bowling["Runs"] / bowling["Overs"],
        0,
    )

    # ------------------------------------------------------
    # Bowling Average
    # ------------------------------------------------------

    bowling["Average"] = np.where(
        bowling["Wickets"] > 0,
        bowling["Runs"] / bowling["Wickets"],
        np.nan,
    )

    # ------------------------------------------------------
    # Strike Rate
    # ------------------------------------------------------

    bowling["Strike Rate"] = np.where(
        bowling["Wickets"] > 0,
        bowling["Balls"] / bowling["Wickets"],
        np.nan,
    )

    # ------------------------------------------------------
    # Dot Ball %
    # ------------------------------------------------------

    bowling["Dot Ball %"] = (
        bowling["DotBalls"]
        / bowling["Balls"]
        * 100
    )

    bowling = bowling.fillna(0)

    bowling = bowling.round(
        {
            "Economy": 2,
            "Average": 2,
            "Strike Rate": 2,
            "Dot Ball %": 2,
        }
    )

    bowling.reset_index(inplace=True)

    return bowling


# ==========================================================
# Best Bowling Figures
# ==========================================================

def best_bowling_figures(
    deliveries_df: pd.DataFrame
) -> pd.DataFrame:
    """
    Best bowling figures in a single match.
    """

    wickets_df = deliveries_df[
        deliveries_df["dismissal_kind"].isin(BOWLER_WICKETS)
    ]

    wickets = (
        wickets_df
        .groupby(
            [
                "match_id",
                "bowler",
            ]
        )
        .size()
        .rename("Wickets")
    )

    runs = (
        deliveries_df
        .groupby(
            [
                "match_id",
                "bowler",
            ]
        )["total_runs"]
        .sum()
        .rename("Runs")
    )

    figures = pd.concat(
        [
            wickets,
            runs,
        ],
        axis=1,
    ).fillna(0)

    figures.reset_index(inplace=True)

    figures.sort_values(
        [
            "Wickets",
            "Runs",
        ],
        ascending=[False, True],
        inplace=True,
    )

    return figures


# ==========================================================
# Four Wicket Hauls
# ==========================================================

def four_wicket_hauls(
    figures_df: pd.DataFrame
) -> pd.DataFrame:
    """
    Number of 4-wicket hauls.
    """

    return (
        figures_df[
            figures_df["Wickets"] >= 4
        ]
        .groupby("bowler")
        .size()
        .rename("4W")
        .reset_index()
        .sort_values(
            "4W",
            ascending=False,
        )
    )


# ==========================================================
# Five Wicket Hauls
# ==========================================================

def five_wicket_hauls(
    figures_df: pd.DataFrame
) -> pd.DataFrame:
    """
    Number of 5-wicket hauls.
    """

    return (
        figures_df[
            figures_df["Wickets"] >= 5
        ]
        .groupby("bowler")
        .size()
        .rename("5W")
        .reset_index()
        .sort_values(
            "5W",
            ascending=False,
        )
    )
# ==========================================================
# Dashboard KPIs
# ==========================================================

def bowling_kpis(df: pd.DataFrame) -> dict:
    """
    Dashboard KPI metrics.
    """

    return {

        "Bowlers": int(df.shape[0]),

        "Total Wickets": int(df["Wickets"].sum()),

        "Average Economy": round(
            df["Economy"].mean(),
            2
        ),

        "Average Strike Rate": round(
            df["Strike Rate"].replace(0, np.nan).mean(),
            2
        ),

    }


# ==========================================================
# Top Wicket Takers
# ==========================================================

def top_wicket_takers(
    df: pd.DataFrame,
    top_n: int = 10,
):

    return (
        df.nlargest(
            top_n,
            "Wickets"
        )
    )


# ==========================================================
# Best Economy
# ==========================================================

def best_economy(
    df: pd.DataFrame,
    min_overs: float = 20,
    top_n: int = 10,
):
    """
    Best economy (minimum overs bowled).
    """

    filtered = df[
        df["Overs"] >= min_overs
    ]

    return (
        filtered.nsmallest(
            top_n,
            "Economy"
        )
    )


# ==========================================================
# Best Bowling Average
# ==========================================================

def best_average(
    df: pd.DataFrame,
    min_wickets: int = 20,
    top_n: int = 10,
):

    filtered = df[
        df["Wickets"] >= min_wickets
    ]

    return (
        filtered.nsmallest(
            top_n,
            "Average"
        )
    )


# ==========================================================
# Best Strike Rate
# ==========================================================

def best_strike_rate(
    df: pd.DataFrame,
    min_wickets: int = 20,
    top_n: int = 10,
):

    filtered = df[
        df["Wickets"] >= min_wickets
    ]

    return (
        filtered.nsmallest(
            top_n,
            "Strike Rate"
        )
    )


# ==========================================================
# Most Dot Balls
# ==========================================================

def most_dot_balls(
    df: pd.DataFrame,
    top_n: int = 10,
):

    return (
        df.nlargest(
            top_n,
            "DotBalls"
        )
    )


# ==========================================================
# Best Dot Ball Percentage
# ==========================================================

def best_dot_ball_percentage(
    df: pd.DataFrame,
    min_overs: float = 20,
    top_n: int = 10,
):

    filtered = df[
        df["Overs"] >= min_overs
    ]

    return (
        filtered.nlargest(
            top_n,
            "Dot Ball %"
        )
    )


# ==========================================================
# Maiden Overs
# ==========================================================

def maiden_overs(
    deliveries_df: pd.DataFrame
) -> pd.DataFrame:
    """
    Calculate maiden overs.

    Maiden Over:
    Six legal deliveries with zero runs conceded.
    """

    df = deliveries_df.copy()

    legal = df[
        ~df["extras_type"].isin(
            [
                "wides",
                "noballs"
            ]
        )
    ]

    over_runs = (

        legal

        .groupby(
            [
                "match_id",
                "bowler",
                "inning",
                "over"
            ]
        )

        .agg(

            Runs=("total_runs", "sum"),

            Balls=("ball", "count")

        )

        .reset_index()

    )

    maiden = over_runs[

        (over_runs["Runs"] == 0)

        &

        (over_runs["Balls"] == 6)

    ]

    maiden = (

        maiden

        .groupby("bowler")

        .size()

        .rename("Maidens")

        .reset_index()

        .sort_values(

            "Maidens",

            ascending=False

        )

    )

    return maiden


# ==========================================================
# Bowling Leaderboard
# ==========================================================

def bowling_leaderboard(
    df: pd.DataFrame
):

    leaderboard = df.copy()

    leaderboard.insert(

        0,

        "Rank",

        range(

            1,

            len(leaderboard) + 1

        )

    )

    return leaderboard.sort_values(

        "Rank"

    )


# ==========================================================
# Player Search
# ==========================================================

def player_statistics(
    df: pd.DataFrame,
    bowler: str,
):

    return (

        df[

            df["bowler"] == bowler

        ]

    )


# ==========================================================
# Merge Extra Bowling Records
# ==========================================================

def merge_bowling_records(
    summary_df: pd.DataFrame,
    figures_df: pd.DataFrame,
) -> pd.DataFrame:
    """
    Merge Best Figures,
    4W,
    5W into bowling summary.
    """

    best = (

        figures_df

        .drop_duplicates(

            "bowler"

        )

        [["bowler", "Wickets", "Runs"]]

        .rename(

            columns={

                "Wickets": "Best Wickets",

                "Runs": "Best Runs"

            }

        )

    )

    best["Best Figures"] = (

        best["Best Wickets"]

        .astype(str)

        +

        "/"

        +

        best["Best Runs"]

        .astype(str)

    )

    four = four_wicket_hauls(

        figures_df

    )

    five = five_wicket_hauls(

        figures_df

    )

    summary = summary_df.merge(

        best[

            [

                "bowler",

                "Best Figures"

            ]

        ],

        on="bowler",

        how="left"

    )

    summary = summary.merge(

        four,

        on="bowler",

        how="left"

    )

    summary = summary.merge(

        five,

        on="bowler",

        how="left"

    )

    summary.fillna(

        {

            "4W": 0,

            "5W": 0,

            "Best Figures": "-"

        },

        inplace=True

    )

    summary["4W"] = summary["4W"].astype(int)

    summary["5W"] = summary["5W"].astype(int)

    return summary