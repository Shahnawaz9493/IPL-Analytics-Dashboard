"""
Main entry point of the IPL Dashboard.
"""

from pathlib import Path

import streamlit as st

from components.sidebar import render_sidebar
from utils.clean_data import clean_data
from utils.load_data import load_data


# -------------------------------------------------------
# Page Configuration
# -------------------------------------------------------

st.set_page_config(
    page_title="IPL Data Analysis Dashboard",
    page_icon="🏏",
    layout="wide",
    initial_sidebar_state="expanded",
)

# -------------------------------------------------------
# Load CSS
# -------------------------------------------------------

CSS_FILE = Path("style.css")

if CSS_FILE.exists():
    with open(CSS_FILE) as css:
        st.markdown(
            f"<style>{css.read()}</style>",
            unsafe_allow_html=True,
        )

# -------------------------------------------------------
# Load Data
# -------------------------------------------------------

matches_df, deliveries_df = load_data()

matches_df, deliveries_df = clean_data(
    matches_df,
    deliveries_df,
)

# -------------------------------------------------------
# Sidebar
# -------------------------------------------------------

render_sidebar()

# -------------------------------------------------------
# Home Screen
# -------------------------------------------------------

st.title("🏏 IPL Data Analysis Dashboard")

st.markdown(
    """
Welcome to the **IPL Data Analysis Dashboard**.

Use the navigation menu on the left to explore:

- 🏠 Home
- 🏏 Best Batsmen
- 🎯 Best Bowlers
- 👑 Winning Captains
- 🪙 Toss Analysis
- ⚔ Team Comparison
- 🏟 Venue Analysis
- 🔍 Player Search

This dashboard provides interactive insights into IPL history using
match-level and ball-by-ball data.
"""
)

st.info(
    "Project structure initialized successfully. Start building the pages from the Pages folder."
)