"""
player_analysis.py
------------------

Professional Player Analysis Module.

Responsibilities
----------------
✔ Player List
✔ Batting Statistics
✔ Bowling Statistics
✔ Boundary Statistics
✔ Matches Played

No Streamlit
No Plotly
"""

from __future__ import annotations

import pandas as pd


# ==========================================================
# Available Players
# ==========================================================

def player_list(
    deliveries_df: pd.DataFrame,
) -> list:
    """
    Returns sorted list of players.
    """

    players = sorted(

        deliveries_df["batter"]

        .dropna()

        .unique()

    )

    return players


# ==========================================================
# Batting Statistics
# ==========================================================

def batting_statistics(
    deliveries_df: pd.DataFrame,
    player: str,
) -> dict:
    """
    Complete batting statistics.
    """

    df = deliveries_df[
        deliveries_df["batter"] == player
    ]

    matches = df["match_id"].nunique()

    innings = df.groupby("match_id").ngroups

    runs = df["batsman_runs"].sum()

    balls = len(df)

    fours = (

        df["batsman_runs"] == 4

    ).sum()

    sixes = (

        df["batsman_runs"] == 6

    ).sum()

    outs = (

        df["player_dismissed"] == player

    ).sum()

    average = (

        runs / outs

        if outs

        else runs

    )

    strike_rate = (

        runs * 100 / balls

        if balls

        else 0

    )

    highest = (

        df.groupby("match_id")

        ["batsman_runs"]

        .sum()

        .max()

    )

    return {

        "Matches": matches,

        "Innings": innings,

        "Runs": int(runs),

        "Highest": int(highest),

        "Average": round(average, 2),

        "Strike Rate": round(strike_rate, 2),

        "Fours": int(fours),

        "Sixes": int(sixes),

        "Balls": balls,

        "Dismissals": int(outs),

    }


# ==========================================================
# Bowling Statistics
# ==========================================================

def bowling_statistics(
    deliveries_df: pd.DataFrame,
    player: str,
) -> dict:
    """
    Bowling statistics.
    """

    df = deliveries_df[
        deliveries_df["bowler"] == player
    ]

    wickets = (

        df["is_wicket"]

    ).sum()

    runs = df["total_runs"].sum()

    balls = len(df)

    overs = round(

        balls / 6,

        1,

    )

    economy = (

        runs / overs

        if overs

        else 0

    )

    average = (

        runs / wickets

        if wickets

        else 0

    )

    return {

        "Overs": overs,

        "Runs": int(runs),

        "Wickets": int(wickets),

        "Economy": round(economy, 2),

        "Average": round(average, 2),

    }


# ==========================================================
# Boundary Statistics
# ==========================================================

def boundary_statistics(
    deliveries_df: pd.DataFrame,
    player: str,
) -> pd.DataFrame:
    """
    Boundary summary.
    """

    df = deliveries_df[
        deliveries_df["batter"] == player
    ]

    fours = (

        df["batsman_runs"] == 4

    ).sum()

    sixes = (

        df["batsman_runs"] == 6

    ).sum()

    dots = (

        df["batsman_runs"] == 0

    ).sum()

    return pd.DataFrame({

        "Type": [

            "Dot Balls",

            "Fours",

            "Sixes",

        ],

        "Count": [

            dots,

            fours,

            sixes,

        ]

    })


# ==========================================================
# Runs by Match
# ==========================================================

def runs_by_match(
    deliveries_df: pd.DataFrame,
    player: str,
) -> pd.DataFrame:
    """
    Match-wise runs.
    """

    df = deliveries_df[
        deliveries_df["batter"] == player
    ]

    summary = (

        df

        .groupby("match_id")

        .agg(

            Runs=("batsman_runs", "sum")

        )

        .reset_index()

    )

    return summary
# ==========================================================
# Wickets by Match
# ==========================================================

def wickets_by_match(
    deliveries_df: pd.DataFrame,
    player: str,
) -> pd.DataFrame:
    """
    Match-wise wickets.
    """

    df = deliveries_df[
        deliveries_df["bowler"] == player
    ]

    summary = (

        df

        .groupby("match_id")

        .agg(

            Wickets=("is_wicket", "sum")

        )

        .reset_index()

    )

    return summary


# ==========================================================
# Dismissal Analysis
# ==========================================================

def dismissal_analysis(
    deliveries_df: pd.DataFrame,
    player: str,
) -> pd.DataFrame:
    """
    Types of dismissals.
    """

    df = deliveries_df[

        deliveries_df["player_dismissed"] == player

    ]

    summary = (

        df

        .groupby("dismissal_kind")

        .size()

        .reset_index(name="Count")

        .sort_values(

            "Count",

            ascending=False,

        )

    )

    return summary


# ==========================================================
# Opponent-wise Runs
# ==========================================================

def opponent_runs(
    deliveries_df: pd.DataFrame,
    player: str,
) -> pd.DataFrame:
    """
    Runs scored against every bowling team.
    """

    df = deliveries_df[

        deliveries_df["batter"] == player

    ]

    summary = (

        df

        .groupby("bowling_team")

        .agg(

            Runs=("batsman_runs", "sum")

        )

        .reset_index()

        .sort_values(

            "Runs",

            ascending=False,

        )

    )

    return summary


# ==========================================================
# Opponent-wise Wickets
# ==========================================================

def opponent_wickets(
    deliveries_df: pd.DataFrame,
    player: str,
) -> pd.DataFrame:
    """
    Wickets against every batting team.
    """

    df = deliveries_df[

        deliveries_df["bowler"] == player

    ]

    summary = (

        df

        .groupby("batting_team")

        .agg(

            Wickets=("is_wicket", "sum")

        )

        .reset_index()

        .sort_values(

            "Wickets",

            ascending=False,

        )

    )

    return summary


# ==========================================================
# Season-wise Runs
# ==========================================================

def season_runs(
    deliveries_df: pd.DataFrame,
    matches_df: pd.DataFrame,
    player: str,
) -> pd.DataFrame:
    """
    Runs scored season-wise.
    """

    df = deliveries_df.merge(

        matches_df[
            [
                "id",
                "season",
            ]
        ],

        left_on="match_id",

        right_on="id",

        how="left",

    )

    df = df[

        df["batter"] == player

    ]

    summary = (

        df

        .groupby("season")

        .agg(

            Runs=("batsman_runs", "sum")

        )

        .reset_index()

    )

    return summary


# ==========================================================
# Season-wise Wickets
# ==========================================================

def season_wickets(
    deliveries_df: pd.DataFrame,
    matches_df: pd.DataFrame,
    player: str,
) -> pd.DataFrame:
    """
    Wickets taken season-wise.
    """

    df = deliveries_df.merge(

        matches_df[
            [
                "id",
                "season",
            ]
        ],

        left_on="match_id",

        right_on="id",

        how="left",

    )

    df = df[

        df["bowler"] == player

    ]

    summary = (

        df

        .groupby("season")

        .agg(

            Wickets=("is_wicket", "sum")

        )

        .reset_index()

    )

    return summary


# ==========================================================
# Career Summary
# ==========================================================

def career_summary(
    batting_stats: dict,
    bowling_stats: dict,
) -> pd.DataFrame:
    """
    Career overview table.
    """

    return pd.DataFrame({

        "Metric": [

            "Matches",
            "Runs",
            "Highest",
            "Average",
            "Strike Rate",
            "Fours",
            "Sixes",
            "Wickets",
            "Economy",

        ],

        "Value": [

            batting_stats["Matches"],
            batting_stats["Runs"],
            batting_stats["Highest"],
            batting_stats["Average"],
            batting_stats["Strike Rate"],
            batting_stats["Fours"],
            batting_stats["Sixes"],
            bowling_stats["Wickets"],
            bowling_stats["Economy"],

        ]

    })


# ==========================================================
# Player KPI Cards
# ==========================================================

def player_kpis(
    batting_stats: dict,
    bowling_stats: dict,
) -> dict:
    """
    KPI values for dashboard.
    """

    return {

        "Runs": batting_stats["Runs"],

        "Wickets": bowling_stats["Wickets"],

        "Strike Rate": batting_stats["Strike Rate"],

        "Economy": bowling_stats["Economy"],

    }