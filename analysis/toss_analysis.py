"""
analysis/toss_analysis.py
-------------------------

Professional Toss Analysis Module

Responsibilities
----------------
✔ Toss KPIs
✔ Toss Decision Analysis
✔ Toss Success Analysis
✔ Venue Analysis
✔ Team Analysis
✔ Season Analysis

No Streamlit
No Plotly
"""

from __future__ import annotations

import pandas as pd


# ==========================================================
# Toss KPI
# ==========================================================

def toss_kpis(matches_df: pd.DataFrame) -> dict:
    """
    Dashboard KPI values.
    """

    total_matches = len(matches_df)

    bat_first = (
        matches_df["toss_decision"] == "bat"
    ).sum()

    field_first = (
        matches_df["toss_decision"] == "field"
    ).sum()

    toss_match_win = (
        matches_df["toss_winner"] == matches_df["winner"]
    ).sum()

    toss_win_percentage = round(

        toss_match_win / total_matches * 100,

        2,

    )

    return {

        "Total Matches": total_matches,

        "Bat First": int(bat_first),

        "Field First": int(field_first),

        "Toss Win Percentage": toss_win_percentage,

    }


# ==========================================================
# Toss Decision Distribution
# ==========================================================

def toss_decision_distribution(
    matches_df: pd.DataFrame,
) -> pd.DataFrame:

    return (

        matches_df["toss_decision"]

        .value_counts()

        .rename_axis("Decision")

        .reset_index(name="Count")

    )


# ==========================================================
# Toss Winner vs Match Winner
# ==========================================================

def toss_result_distribution(
    matches_df: pd.DataFrame,
) -> pd.DataFrame:

    df = matches_df.copy()

    df["Outcome"] = df.apply(

        lambda x:

        "Won Match"

        if x["toss_winner"] == x["winner"]

        else "Lost Match",

        axis=1,

    )

    return (

        df["Outcome"]

        .value_counts()

        .rename_axis("Outcome")

        .reset_index(name="Count")

    )


# ==========================================================
# Toss Wins by Team
# ==========================================================

def toss_wins_by_team(
    matches_df: pd.DataFrame,
) -> pd.DataFrame:

    return (

        matches_df["toss_winner"]

        .value_counts()

        .rename_axis("Team")

        .reset_index(name="Toss Wins")

    )
# ==========================================================
# Toss Decision by Team
# ==========================================================

def toss_decision_by_team(
    matches_df: pd.DataFrame,
) -> pd.DataFrame:

    return (

        matches_df

        .groupby(

            [

                "toss_winner",

                "toss_decision",

            ]

        )

        .size()

        .reset_index(name="Matches")

    )


# ==========================================================
# Toss Success by Team
# ==========================================================

def toss_success_by_team(
    matches_df: pd.DataFrame,
) -> pd.DataFrame:

    df = matches_df.copy()

    df["Won"] = (

        df["toss_winner"]

        ==

        df["winner"]

    )

    summary = (

        df

        .groupby("toss_winner")

        .agg(

            Tosses=("id", "count"),

            Wins=("Won", "sum"),

        )

        .reset_index()

    )

    summary["Win %"] = round(

        summary["Wins"]

        /

        summary["Tosses"]

        *

        100,

        2,

    )

    return summary.sort_values(

        "Win %",

        ascending=False,

    )


# ==========================================================
# Venue Toss Success
# ==========================================================

def venue_toss_success(
    matches_df: pd.DataFrame,
) -> pd.DataFrame:

    df = matches_df.copy()

    df["Won"] = (

        df["toss_winner"]

        ==

        df["winner"]

    )

    summary = (

        df

        .groupby("venue")

        .agg(

            Matches=("id", "count"),

            TossWins=("Won", "sum"),

        )

        .reset_index()

    )

    summary["Success %"] = round(

        summary["TossWins"]

        /

        summary["Matches"]

        *

        100,

        2,

    )

    return summary


# ==========================================================
# Season Trend
# ==========================================================

def season_toss_trend(
    matches_df: pd.DataFrame,
) -> pd.DataFrame:

    return (

        matches_df

        .groupby(

            [

                "season",

                "toss_decision",

            ]

        )

        .size()

        .reset_index(name="Matches")

    )
# ==========================================================
# Team Leaderboard
# ==========================================================

def toss_leaderboard(
    matches_df: pd.DataFrame,
) -> pd.DataFrame:

    leaderboard = toss_success_by_team(

        matches_df

    )

    leaderboard.insert(

        0,

        "Rank",

        range(

            1,

            len(leaderboard) + 1,

        ),

    )

    return leaderboard


# ==========================================================
# Team Filter
# ==========================================================

def filter_team(
    matches_df: pd.DataFrame,
    team: str,
) -> pd.DataFrame:

    if team == "All Teams":

        return matches_df

    return matches_df[

        (matches_df["team1"] == team)

        |

        (matches_df["team2"] == team)

    ]


# ==========================================================
# Venue Filter
# ==========================================================

def filter_venue(
    matches_df: pd.DataFrame,
    venue: str,
) -> pd.DataFrame:

    if venue == "All Venues":

        return matches_df

    return matches_df[

        matches_df["venue"] == venue

    ]


# ==========================================================
# Season Filter
# ==========================================================

def filter_season(
    matches_df: pd.DataFrame,
    season,
) -> pd.DataFrame:

    if season == "All Seasons":

        return matches_df

    return matches_df[

        matches_df["season"] == season

    ]