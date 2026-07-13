"""
clean_data.py
-------------

This module is responsible for cleaning and preprocessing the IPL datasets.

Responsibilities
----------------
✔ Remove duplicate records
✔ Handle missing values
✔ Convert data types
✔ Standardize text columns
✔ Create additional useful features
"""

from __future__ import annotations

import pandas as pd


# -----------------------------------------------------------
# Matches Dataset Cleaning
# -----------------------------------------------------------

def clean_matches(matches_df: pd.DataFrame) -> pd.DataFrame:
    """
    Clean the IPL matches dataset.

    Parameters
    ----------
    matches_df : pd.DataFrame

    Returns
    -------
    pd.DataFrame
    """

    df = matches_df.copy()

    # Remove duplicate rows
    df.drop_duplicates(inplace=True)

    # Convert date column
    df["date"] = pd.to_datetime(df["date"])

    # Extract useful date features
    df["year"] = df["date"].dt.year
    df["month"] = df["date"].dt.month
    df["day"] = df["date"].dt.day

    # Standardize team names
    team_replacements = {
        "Delhi Daredevils": "Delhi Capitals",
        "Kings XI Punjab": "Punjab Kings",
        "Rising Pune Supergiant": "Rising Pune Supergiants"
    }

    columns = [
        "team1",
        "team2",
        "winner",
        "toss_winner"
    ]

    for col in columns:
        df[col] = df[col].replace(team_replacements)

    # Fill missing values
    df["winner"] = df["winner"].fillna("No Result")
    df["city"] = df["city"].fillna("Unknown")
    df["method"] = df["method"].fillna("Normal")

    return df


# -----------------------------------------------------------
# Deliveries Dataset Cleaning
# -----------------------------------------------------------

def clean_deliveries(deliveries_df: pd.DataFrame) -> pd.DataFrame:
    """
    Clean the deliveries dataset.
    """

    df = deliveries_df.copy()

    # Remove duplicates
    df.drop_duplicates(inplace=True)

    # Standardize team names
    team_replacements = {
        "Delhi Daredevils": "Delhi Capitals",
        "Kings XI Punjab": "Punjab Kings",
        "Rising Pune Supergiant": "Rising Pune Supergiants"
    }

    df["batting_team"] = df["batting_team"].replace(team_replacements)
    df["bowling_team"] = df["bowling_team"].replace(team_replacements)

    # Replace missing values
    df["extras_type"] = df["extras_type"].fillna("None")
    df["player_dismissed"] = df["player_dismissed"].fillna("Not Out")
    df["dismissal_kind"] = df["dismissal_kind"].fillna("None")
    df["fielder"] = df["fielder"].fillna("None")

    return df


# -----------------------------------------------------------
# Complete Cleaning Pipeline
# -----------------------------------------------------------

def clean_data(
    matches_df: pd.DataFrame,
    deliveries_df: pd.DataFrame
) -> tuple[pd.DataFrame, pd.DataFrame]:
    """
    Clean both IPL datasets.

    Returns
    -------
    tuple
        (clean_matches, clean_deliveries)
    """

    matches_df = clean_matches(matches_df)
    deliveries_df = clean_deliveries(deliveries_df)

    return matches_df, deliveries_df