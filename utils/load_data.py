"""
load_data.py
------------

This module is responsible for loading the IPL datasets.

Responsibilities:
- Read matches.csv
- Read deliveries.csv
- Cache the datasets for better performance
- Return DataFrames for use across the application
"""

from pathlib import Path

import pandas as pd
import streamlit as st


# -------------------------------------------------------------------
# File Paths
# -------------------------------------------------------------------

BASE_DIR = Path(__file__).resolve().parent.parent

DATA_DIR = BASE_DIR / "data"

MATCHES_FILE = DATA_DIR / "matches.csv"
DELIVERIES_FILE = DATA_DIR / "deliveries.csv"


# -------------------------------------------------------------------
# Load Matches Dataset
# -------------------------------------------------------------------

@st.cache_data(show_spinner=False)
def load_matches() -> pd.DataFrame:
    """
    Load the IPL matches dataset.

    Returns
    -------
    pd.DataFrame
        Matches dataframe.
    """

    if not MATCHES_FILE.exists():
        raise FileNotFoundError(
            f"Could not find '{MATCHES_FILE}'."
        )

    return pd.read_csv(MATCHES_FILE)


# -------------------------------------------------------------------
# Load Deliveries Dataset
# -------------------------------------------------------------------

@st.cache_data(show_spinner=False)
def load_deliveries() -> pd.DataFrame:
    """
    Load the IPL deliveries dataset.

    Returns
    -------
    pd.DataFrame
        Deliveries dataframe.
    """

    if not DELIVERIES_FILE.exists():
        raise FileNotFoundError(
            f"Could not find '{DELIVERIES_FILE}'."
        )

    return pd.read_csv(DELIVERIES_FILE)


# -------------------------------------------------------------------
# Load Both Datasets
# -------------------------------------------------------------------

@st.cache_data(show_spinner=False)
def load_data() -> tuple[pd.DataFrame, pd.DataFrame]:
    """
    Load both IPL datasets.

    Returns
    -------
    tuple
        (matches_df, deliveries_df)
    """

    matches = load_matches()
    deliveries = load_deliveries()

    return matches, deliveries