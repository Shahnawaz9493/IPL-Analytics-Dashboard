"""
home_analysis.py
----------------

Analysis module for the Home Dashboard.

Responsibilities
----------------
✔ Dashboard KPIs
✔ Matches Per Season
✔ Toss Decision Distribution
✔ Match Result Distribution
✔ Top Venues
✔ Top Cities
✔ Player of the Match Leaders

No Streamlit code.
No Plotly code.
"""

from __future__ import annotations

import pandas as pd


# ==========================================================
# Dashboard KPIs
# ==========================================================

def dashboard_kpis(
    matches_df: pd.DataFrame,
    deliveries_df: pd.DataFrame,
) -> dict:
    """
    Compute dashboard overview metrics.
    """

    total_seasons = matches_df["season"].nunique()

    total_matches = matches_df["id"].nunique()

    total_teams = len(
        pd.concat(
            [
                matches_df["team1"],
                matches_df["team2"],
            ]
        ).dropna().unique()
    )

    total_players = len(
        pd.concat(
            [
                deliveries_df["batter"],
                deliveries_df["bowler"],
            ]
        ).dropna().unique()
    )

    total_runs = int(deliveries_df["total_runs"].sum())

    total_wickets = int(deliveries_df["is_wicket"].sum())

    total_sixes = int(
        (deliveries_df["batsman_runs"] == 6).sum()
    )

    total_fours = int(
        (deliveries_df["batsman_runs"] == 4).sum()
    )

    return {
        "Total Seasons": total_seasons,
        "Total Matches": total_matches,
        "Total Teams": total_teams,
        "Total Players": total_players,
        "Total Runs": total_runs,
        "Total Wickets": total_wickets,
        "Total Sixes": total_sixes,
        "Total Fours": total_fours,
    }


# ==========================================================
# Matches Per Season
# ==========================================================

def matches_per_season(
    matches_df: pd.DataFrame,
) -> pd.DataFrame:
    """
    Number of matches played each season.
    """

    df = (
        matches_df
        .groupby("season", as_index=False)
        .agg(Matches=("id", "count"))
        .sort_values("season")
    )

    return df


# ==========================================================
# Toss Decision Distribution
# ==========================================================

def toss_decision_distribution(
    matches_df: pd.DataFrame,
) -> pd.DataFrame:
    """
    Distribution of toss decisions.
    """

    df = (
        matches_df["toss_decision"]
        .value_counts()
        .rename_axis("Decision")
        .reset_index(name="Count")
    )

    return df


# ==========================================================
# Match Result Distribution
# ==========================================================

def result_distribution(
    matches_df: pd.DataFrame,
) -> pd.DataFrame:
    """
    Distribution of match results.
    """

    df = (
        matches_df["result"]
        .fillna("Normal")
        .value_counts()
        .rename_axis("Result")
        .reset_index(name="Count")
    )

    return df


# ==========================================================
# Top Venues
# ==========================================================

def top_venues(
    matches_df: pd.DataFrame,
    top_n: int = 10,
) -> pd.DataFrame:
    """
    Top venues by matches hosted.
    """

    df = (
        matches_df["venue"]
        .dropna()
        .value_counts()
        .head(top_n)
        .rename_axis("Venue")
        .reset_index(name="Matches")
    )

    return df


# ==========================================================
# Top Cities
# ==========================================================

def top_cities(
    matches_df: pd.DataFrame,
    top_n: int = 10,
) -> pd.DataFrame:
    """
    Top cities by matches hosted.
    """

    df = (
        matches_df["city"]
        .fillna("Unknown")
        .value_counts()
        .head(top_n)
        .rename_axis("City")
        .reset_index(name="Matches")
    )

    return df


# ==========================================================
# Player of the Match Leaders
# ==========================================================

def top_player_of_match(
    matches_df: pd.DataFrame,
    top_n: int = 10,
) -> pd.DataFrame:
    """
    Players with the most Player of the Match awards.
    """

    df = (
        matches_df["player_of_match"]
        .dropna()
        .value_counts()
        .head(top_n)
        .rename_axis("Player")
        .reset_index(name="Awards")
    )

    return df