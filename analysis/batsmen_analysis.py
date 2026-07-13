"""
batsmen_analysis.py
-------------------

Professional batting analysis module for IPL Dashboard.

Responsibilities
----------------
✔ Batting Summary
✔ Top Run Scorers
✔ Highest Average
✔ Highest Strike Rate
✔ Most Fours
✔ Most Sixes
✔ Boundary %
✔ Dot Ball %
✔ Highest Score
✔ 50s
✔ 100s
✔ Player Search
✔ Dashboard KPIs

No Streamlit code.
No Plotly code.
"""

from __future__ import annotations

import numpy as np
import pandas as pd


# ==========================================================
# Create Complete Batting Summary
# ==========================================================

def batting_summary(deliveries_df: pd.DataFrame) -> pd.DataFrame:
    """
    Creates a professional batting summary for every player.
    """

    df = deliveries_df.copy()

    # ------------------------------------------------------
    # Runs scored in every innings
    # ------------------------------------------------------

    innings = (
        df.groupby(["match_id", "batter"])
        .agg(
            Runs=("batsman_runs", "sum"),
            Balls=("ball", "count")
        )
        .reset_index()
    )

    # Highest Score

    highest_score = (
        innings.groupby("batter")["Runs"]
        .max()
        .rename("Highest Score")
    )

    # 50s

    fifties = (
        innings[innings["Runs"].between(50, 99)]
        .groupby("batter")
        .size()
        .rename("50s")
    )

    # 100s

    hundreds = (
        innings[innings["Runs"] >= 100]
        .groupby("batter")
        .size()
        .rename("100s")
    )

    # ------------------------------------------------------
    # Career Statistics
    # ------------------------------------------------------

    summary = (
        df.groupby("batter")
        .agg(
            Runs=("batsman_runs", "sum"),
            Balls=("ball", "count"),
            Matches=("match_id", "nunique"),
            Fours=("batsman_runs", lambda x: (x == 4).sum()),
            Sixes=("batsman_runs", lambda x: (x == 6).sum()),
            DotBalls=("batsman_runs", lambda x: (x == 0).sum()),
        )
    )

    # Innings

    summary["Innings"] = innings.groupby("batter").size()

    # Dismissals

    dismissals = (
        df[df["player_dismissed"].notna()]
        .groupby("player_dismissed")
        .size()
    )

    summary["Dismissals"] = dismissals

    summary["Dismissals"] = (
        summary["Dismissals"]
        .fillna(0)
        .astype(int)
    )

    # Merge

    summary = summary.join(highest_score)

    summary = summary.join(fifties)

    summary = summary.join(hundreds)

    summary.fillna(
        {
            "50s": 0,
            "100s": 0
        },
        inplace=True
    )

    # ------------------------------------------------------
    # Batting Average
    # ------------------------------------------------------

    summary["Average"] = np.where(
        summary["Dismissals"] > 0,
        summary["Runs"] / summary["Dismissals"],
        np.nan
    )

    # ------------------------------------------------------
    # Strike Rate
    # ------------------------------------------------------

    summary["Strike Rate"] = (
        summary["Runs"] /
        summary["Balls"] * 100
    )

    # ------------------------------------------------------
    # Boundary %
    # ------------------------------------------------------

    boundary_runs = (
        summary["Fours"] * 4 +
        summary["Sixes"] * 6
    )

    summary["Boundary %"] = (
        boundary_runs /
        summary["Runs"] * 100
    )

    # ------------------------------------------------------
    # Dot Ball %
    # ------------------------------------------------------

    summary["Dot Ball %"] = (
        summary["DotBalls"] /
        summary["Balls"] * 100
    )

    summary = summary.fillna(0)

    summary = summary.round(
        {
            "Average": 2,
            "Strike Rate": 2,
            "Boundary %": 2,
            "Dot Ball %": 2,
        }
    )

    summary.reset_index(inplace=True)

    summary.sort_values(
        "Runs",
        ascending=False,
        inplace=True
    )

    return summary


# ==========================================================
# Dashboard KPIs
# ==========================================================

def batting_kpis(df: pd.DataFrame):

    return {

        "Players": df.shape[0],

        "Total Runs": int(df["Runs"].sum()),

        "Overall Average": round(
            df["Average"].mean(),
            2
        ),

        "Overall Strike Rate": round(
            df["Strike Rate"].mean(),
            2
        ),

    }


# ==========================================================
# Top Run Scorers
# ==========================================================

def top_run_scorers(df, top_n=10):
    return df.nlargest(top_n, "Runs")


# ==========================================================
# Highest Average
# ==========================================================

def highest_average(df, min_innings=20, top_n=10):

    return (
        df[df["Innings"] >= min_innings]
        .nlargest(top_n, "Average")
    )


# ==========================================================
# Highest Strike Rate
# ==========================================================

def highest_strike_rate(df, min_balls=200, top_n=10):

    return (
        df[df["Balls"] >= min_balls]
        .nlargest(top_n, "Strike Rate")
    )


# ==========================================================
# Most Sixes
# ==========================================================

def most_sixes(df, top_n=10):

    return df.nlargest(top_n, "Sixes")


# ==========================================================
# Most Fours
# ==========================================================

def most_fours(df, top_n=10):

    return df.nlargest(top_n, "Fours")


# ==========================================================
# Highest Scores
# ==========================================================

def highest_scores(df, top_n=10):

    return df.nlargest(top_n, "Highest Score")


# ==========================================================
# Best Boundary Hitters
# ==========================================================

def boundary_hitters(df, top_n=10):

    return df.nlargest(top_n, "Boundary %")


# ==========================================================
# Dot Ball Percentage
# ==========================================================

def dot_ball_percentage(df, top_n=10):

    return df.nlargest(top_n, "Dot Ball %")


# ==========================================================
# Player Search
# ==========================================================

def player_statistics(df, player):

    return df[df["batter"] == player]