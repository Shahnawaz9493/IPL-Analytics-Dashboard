"""
venue_analysis.py
-----------------

Professional Venue Analysis Module.

Responsibilities
----------------
✔ Venue Summary
✔ Highest Score
✔ Lowest Score
✔ Average Score
✔ Total Matches
✔ Venue Statistics

No Streamlit
No Plotly
"""

from __future__ import annotations

import pandas as pd


# ==========================================================
# Match IDs with Venue
# ==========================================================

def venue_matches(
    matches_df: pd.DataFrame,
) -> pd.DataFrame:
    """
    Returns match id with venue.
    """

    return matches_df[
        [
            "id",
            "venue",
            "season",
            "city",
        ]
    ].copy()


# ==========================================================
# Innings Scores
# ==========================================================

def innings_scores(
    deliveries_df: pd.DataFrame,
) -> pd.DataFrame:
    """
    Total innings score for every match.
    """

    scores = (

        deliveries_df

        .groupby(

            [
                "match_id",
                "inning",
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
# Merge Venue + Scores
# ==========================================================

def venue_scores(
    matches_df: pd.DataFrame,
    deliveries_df: pd.DataFrame,
) -> pd.DataFrame:
    """
    Merge venue information with innings scores.
    """

    venue_df = venue_matches(matches_df)

    score_df = innings_scores(deliveries_df)

    merged = score_df.merge(

        venue_df,

        left_on="match_id",

        right_on="id",

        how="left",

    )

    return merged


# ==========================================================
# Venue Summary
# ==========================================================

def venue_summary(
    venue_df: pd.DataFrame,
) -> pd.DataFrame:
    """
    Venue statistics.
    """

    summary = (

        venue_df

        .groupby("venue")

        .agg(

            Matches=("match_id", "nunique"),

            Average=("Score", "mean"),

            Highest=("Score", "max"),

            Lowest=("Score", "min"),

        )

        .round(2)

        .reset_index()

    )

    return summary.sort_values(

        "Matches",

        ascending=False,

    )


# ==========================================================
# Highest Scores
# ==========================================================

def highest_scores(
    venue_df: pd.DataFrame,
    top_n: int = 15,
) -> pd.DataFrame:
    """
    Highest scoring venues.
    """

    return (

        venue_summary(venue_df)

        .sort_values(

            "Highest",

            ascending=False,

        )

        .head(top_n)

    )


# ==========================================================
# Lowest Scores
# ==========================================================

def lowest_scores(
    venue_df: pd.DataFrame,
    top_n: int = 15,
) -> pd.DataFrame:
    """
    Lowest scoring venues.
    """

    return (

        venue_summary(venue_df)

        .sort_values(

            "Lowest",

            ascending=True,

        )

        .head(top_n)

    )


# ==========================================================
# Average Scores
# ==========================================================

def average_scores(
    venue_df: pd.DataFrame,
    top_n: int = 15,
) -> pd.DataFrame:
    """
    Average score by venue.
    """

    return (

        venue_summary(venue_df)

        .sort_values(

            "Average",

            ascending=False,

        )

        .head(top_n)

    )
# ==========================================================
# First Innings Average
# ==========================================================

def first_innings_average(
    venue_df: pd.DataFrame,
) -> pd.DataFrame:
    """
    Average first innings score by venue.
    """

    first = venue_df[
        venue_df["inning"] == 1
    ]

    return (

        first

        .groupby("venue")

        .agg(

            FirstInningsAvg=("Score", "mean")

        )

        .round(2)

        .reset_index()

    )


# ==========================================================
# Second Innings Average
# ==========================================================

def second_innings_average(
    venue_df: pd.DataFrame,
) -> pd.DataFrame:
    """
    Average second innings score by venue.
    """

    second = venue_df[
        venue_df["inning"] == 2
    ]

    return (

        second

        .groupby("venue")

        .agg(

            SecondInningsAvg=("Score", "mean")

        )

        .round(2)

        .reset_index()

    )


# ==========================================================
# Best Batting Grounds
# ==========================================================

def best_batting_grounds(
    venue_df: pd.DataFrame,
    top_n: int = 15,
) -> pd.DataFrame:
    """
    Highest average scoring venues.
    """

    batting = venue_summary(venue_df)

    batting["Batting Rating"] = (

        batting["Average"] * batting["Highest"]

    ) / 100

    return batting.sort_values(

        "Batting Rating",

        ascending=False,

    ).head(top_n)


# ==========================================================
# Best Bowling Grounds
# ==========================================================

def best_bowling_grounds(
    venue_df: pd.DataFrame,
    top_n: int = 15,
) -> pd.DataFrame:
    """
    Lowest average scoring venues.
    """

    bowling = venue_summary(venue_df)

    bowling["Bowling Rating"] = (

        bowling["Average"]

    )

    return bowling.sort_values(

        "Bowling Rating",

        ascending=True,

    ).head(top_n)


# ==========================================================
# Chasing Success
# ==========================================================

def chasing_success(
    matches_df: pd.DataFrame,
) -> pd.DataFrame:
    """
    Venue-wise chasing success.
    """

    chase = matches_df.copy()

    chase["Chased"] = (

        chase["target_runs"].notna()

    )

    summary = (

        chase

        .groupby("venue")

        .agg(

            Matches=("id", "count"),

            SuccessfulChases=("Chased", "sum"),

        )

        .reset_index()

    )

    summary["Chase %"] = (

        summary["SuccessfulChases"]

        /

        summary["Matches"]

        *

        100

    ).round(2)

    return summary.sort_values(

        "Chase %",

        ascending=False,

    )


# ==========================================================
# Toss Success by Venue
# ==========================================================

def toss_success_by_venue(
    matches_df: pd.DataFrame,
) -> pd.DataFrame:
    """
    Toss conversion percentage by venue.
    """

    toss = matches_df.copy()

    toss["Converted"] = (

        toss["toss_winner"]

        ==

        toss["winner"]

    )

    summary = (

        toss

        .groupby("venue")

        .agg(

            Matches=("id", "count"),

            TossConverted=("Converted", "sum"),

        )

        .reset_index()

    )

    summary["Success %"] = (

        summary["TossConverted"]

        /

        summary["Matches"]

        *

        100

    ).round(2)

    return summary.sort_values(

        "Success %",

        ascending=False,

    )


# ==========================================================
# Venue KPIs
# ==========================================================

def venue_kpis(
    venue_summary_df: pd.DataFrame,
) -> dict:
    """
    Dashboard KPI values.
    """

    return {

        "Venues": len(venue_summary_df),

        "Highest Score": int(

            venue_summary_df["Highest"].max()

        ),

        "Lowest Score": int(

            venue_summary_df["Lowest"].min()

        ),

        "Average Score": round(

            venue_summary_df["Average"].mean(),

            2,

        ),

    }


# ==========================================================
# Venue Leaderboard
# ==========================================================

def venue_leaderboard(
    venue_summary_df: pd.DataFrame,
) -> pd.DataFrame:
    """
    Ranked venue statistics.
    """

    leaderboard = venue_summary_df.copy()

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
# Search Venue
# ==========================================================

def search_venue(
    venue_summary_df: pd.DataFrame,
    venue: str,
) -> pd.DataFrame:
    """
    Filter statistics for one venue.
    """

    return venue_summary_df[

        venue_summary_df["venue"] == venue

    ]