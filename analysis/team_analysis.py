"""
team_analysis.py
----------------

Professional Team Comparison Analysis Module.

Responsibilities
----------------
✔ Head-to-head records
✔ Team statistics
✔ Average Score
✔ Highest Score
✔ Lowest Score
✔ Toss Analysis

No Streamlit
No Plotly
"""

from __future__ import annotations

import pandas as pd
import numpy as np


# ==========================================================
# Head to Head Matches
# ==========================================================

def head_to_head_matches(
    matches_df: pd.DataFrame,
    team1: str,
    team2: str,
) -> pd.DataFrame:
    """
    Returns all matches played between two teams.
    """

    return matches_df[
        (
            (matches_df["team1"] == team1)
            &
            (matches_df["team2"] == team2)
        )
        |
        (
            (matches_df["team1"] == team2)
            &
            (matches_df["team2"] == team1)
        )
    ].copy()


# ==========================================================
# Head-to-Head Summary
# ==========================================================

def head_to_head_summary(
    matches_df: pd.DataFrame,
    team1: str,
    team2: str,
) -> dict:
    """
    Summary of head-to-head matches.
    """

    matches = head_to_head_matches(
        matches_df,
        team1,
        team2,
    )

    total_matches = len(matches)

    team1_wins = (
        matches["winner"] == team1
    ).sum()

    team2_wins = (
        matches["winner"] == team2
    ).sum()

    no_result = (
        matches["winner"].isna()
    ).sum()

    return {

        "Total Matches": total_matches,

        team1: int(team1_wins),

        team2: int(team2_wins),

        "No Result": int(no_result),

        f"{team1} Win %": round(
            team1_wins / total_matches * 100,
            2
        ) if total_matches else 0,

        f"{team2} Win %": round(
            team2_wins / total_matches * 100,
            2
        ) if total_matches else 0,

    }


# ==========================================================
# Toss Summary
# ==========================================================

def toss_summary(
    matches_df: pd.DataFrame,
    team1: str,
    team2: str,
) -> pd.DataFrame:
    """
    Toss wins between two teams.
    """

    matches = head_to_head_matches(
        matches_df,
        team1,
        team2,
    )

    summary = (

        matches

        .groupby("toss_winner")

        .size()

        .reset_index(name="Toss Wins")

    )

    return summary


# ==========================================================
# Match IDs
# ==========================================================

def match_ids(
    matches_df: pd.DataFrame,
    team1: str,
    team2: str,
):

    matches = head_to_head_matches(
        matches_df,
        team1,
        team2,
    )

    return matches["id"].tolist()


# ==========================================================
# Match Scores
# ==========================================================

def match_scores(
    deliveries_df: pd.DataFrame,
    match_list: list,
) -> pd.DataFrame:
    """
    Total innings score.
    """

    df = deliveries_df[
        deliveries_df["match_id"].isin(match_list)
    ]

    scores = (

        df

        .groupby(
            [
                "match_id",
                "batting_team",
            ]
        )

        .agg(
            Score=("total_runs", "sum")
        )

        .reset_index()

    )

    return scores


# ==========================================================
# Team Score Summary
# ==========================================================

def score_summary(
    scores_df: pd.DataFrame,
) -> pd.DataFrame:
    """
    Average score statistics.
    """

    summary = (

        scores_df

        .groupby("batting_team")

        .agg(

            Average=("Score", "mean"),

            Highest=("Score", "max"),

            Lowest=("Score", "min"),

            Matches=("Score", "count"),

        )

        .reset_index()

    )

    summary = summary.round(2)

    return summary.sort_values(

        "Average",

        ascending=False,

    )


# ==========================================================
# Win Percentage
# ==========================================================

def win_percentage(
    summary: dict,
    team1: str,
    team2: str,
) -> pd.DataFrame:

    return pd.DataFrame({

        "Team": [

            team1,

            team2

        ],

        "Win %": [

            summary[f"{team1} Win %"],

            summary[f"{team2} Win %"]

        ]

    })
# ==========================================================
# Home Wins
# ==========================================================

def home_away_summary(
    matches_df: pd.DataFrame,
    team1: str,
    team2: str,
) -> pd.DataFrame:
    """
    Calculates home and away wins for both teams based on team1/team2
    designation in the dataset.
    """

    matches = head_to_head_matches(
        matches_df,
        team1,
        team2,
    )

    results = []

    for team in [team1, team2]:

        home_matches = matches[
            matches["team1"] == team
        ]

        away_matches = matches[
            matches["team2"] == team
        ]

        results.append({

            "Team": team,

            "Home Matches": len(home_matches),

            "Home Wins": (
                home_matches["winner"] == team
            ).sum(),

            "Away Matches": len(away_matches),

            "Away Wins": (
                away_matches["winner"] == team
            ).sum(),

        })

    return pd.DataFrame(results)


# ==========================================================
# Powerplay Score
# ==========================================================

def powerplay_scores(
    deliveries_df: pd.DataFrame,
    match_list: list,
) -> pd.DataFrame:
    """
    Average Powerplay Score (Overs 1-6)
    """

    df = deliveries_df[
        deliveries_df["match_id"].isin(match_list)
    ]

    pp = df[
        df["over"] <= 6
    ]

    summary = (

        pp

        .groupby(
            [
                "match_id",
                "batting_team",
            ]
        )

        .agg(
            Powerplay=("total_runs", "sum")
        )

        .reset_index()

    )

    return (

        summary

        .groupby("batting_team")

        .agg(
            AveragePowerplay=("Powerplay", "mean")
        )

        .round(2)

        .reset_index()

    )


# ==========================================================
# Death Overs Score
# ==========================================================

def death_over_scores(
    deliveries_df: pd.DataFrame,
    match_list: list,
) -> pd.DataFrame:
    """
    Average score in death overs (16-20).
    """

    df = deliveries_df[
        deliveries_df["match_id"].isin(match_list)
    ]

    death = df[
        df["over"] >= 16
    ]

    summary = (

        death

        .groupby(
            [
                "match_id",
                "batting_team",
            ]
        )

        .agg(
            DeathRuns=("total_runs", "sum")
        )

        .reset_index()

    )

    return (

        summary

        .groupby("batting_team")

        .agg(
            AverageDeath=("DeathRuns", "mean")
        )

        .round(2)

        .reset_index()

    )


# ==========================================================
# Venue Comparison
# ==========================================================

def venue_comparison(
    matches_df: pd.DataFrame,
    team1: str,
    team2: str,
) -> pd.DataFrame:
    """
    Venue-wise win comparison.
    """

    matches = head_to_head_matches(
        matches_df,
        team1,
        team2,
    )

    venue = (

        matches

        .groupby(
            [
                "venue",
                "winner",
            ]
        )

        .size()

        .reset_index(name="Wins")

    )

    return venue


# ==========================================================
# Team KPI Summary
# ==========================================================

def team_kpis(
    summary: dict,
    score_summary_df: pd.DataFrame,
) -> dict:
    """
    Dashboard KPIs.
    """

    return {

        "Matches": summary["Total Matches"],

        "Highest Score": int(
            score_summary_df["Highest"].max()
        ),

        "Lowest Score": int(
            score_summary_df["Lowest"].min()
        ),

        "Average Score": round(
            score_summary_df["Average"].mean(),
            2,
        ),

    }


# ==========================================================
# Team Comparison Table
# ==========================================================

def comparison_table(
    score_df: pd.DataFrame,
    powerplay_df: pd.DataFrame,
    death_df: pd.DataFrame,
) -> pd.DataFrame:
    """
    Merge all team comparison statistics.
    """

    comparison = score_df.merge(

        powerplay_df,

        on="batting_team",

        how="left",

    )

    comparison = comparison.merge(

        death_df,

        on="batting_team",

        how="left",

    )

    comparison.rename(

        columns={

            "batting_team": "Team"

        },

        inplace=True,

    )

    return comparison.round(2)


# ==========================================================
# Head-to-Head Timeline
# ==========================================================

def match_timeline(
    matches_df: pd.DataFrame,
    team1: str,
    team2: str,
) -> pd.DataFrame:
    """
    Chronological results between two teams.
    """

    matches = head_to_head_matches(
        matches_df,
        team1,
        team2,
    )

    timeline = matches[
        [
            "season",
            "date",
            "winner",
            "venue",
        ]
    ].sort_values("date")

    return timeline.reset_index(drop=True)


# ==========================================================
# Team Search
# ==========================================================

def available_teams(
    matches_df: pd.DataFrame,
) -> list:
    """
    Returns sorted team list.
    """

    teams = sorted(

        pd.concat(
            [
                matches_df["team1"],
                matches_df["team2"],
            ]
        )

        .dropna()

        .unique()

    )

    return teams