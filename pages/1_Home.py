"""
1_Home.py
---------

Home Dashboard for IPL Data Analysis
"""

from __future__ import annotations

import streamlit as st

from analysis.home_analysis import (
    dashboard_kpis,
    matches_per_season,
    toss_decision_distribution,
    result_distribution,
    top_venues,
    top_cities,
    top_player_of_match,
)

from charts.home_charts import (
    matches_per_season_chart,
    toss_decision_chart,
    result_distribution_chart,
    top_venues_chart,
    top_cities_chart,
    player_of_match_chart,
)

from components.cards import display_dashboard_cards

from utils.load_data import load_data
from utils.clean_data import clean_data


# ==========================================================
# Load Data
# ==========================================================

matches_df, deliveries_df = load_data()
matches_df, deliveries_df = clean_data(
    matches_df,
    deliveries_df
)

# ==========================================================
# Dashboard Title
# ==========================================================

st.title("🏏 IPL Data Analysis Dashboard")

st.markdown(
    """
Explore IPL history using interactive analytics,
advanced visualizations and player statistics.
"""
)

st.divider()

# ==========================================================
# KPI CARDS
# ==========================================================

kpis = dashboard_kpis(matches_df, deliveries_df)

display_dashboard_cards(kpis)

st.markdown("<br>", unsafe_allow_html=True)

# ==========================================================
# Matches Per Season
# ==========================================================

season_df = matches_per_season(matches_df)

season_chart = matches_per_season_chart(season_df)

st.plotly_chart(
    season_chart,
    use_container_width=True
)

# ==========================================================
# Toss & Result Distribution
# ==========================================================

col1, col2 = st.columns(2)

with col1:

    toss_df = toss_decision_distribution(matches_df)

    toss_chart = toss_decision_chart(toss_df)

    st.plotly_chart(
        toss_chart,
        use_container_width=True
    )

with col2:

    result_df = result_distribution(matches_df)

    result_chart = result_distribution_chart(result_df)

    st.plotly_chart(
        result_chart,
        use_container_width=True
    )

# ==========================================================
# Venue & City Analysis
# ==========================================================

col1, col2 = st.columns(2)

with col1:

    venue_df = top_venues(matches_df)

    venue_chart = top_venues_chart(venue_df)

    st.plotly_chart(
        venue_chart,
        use_container_width=True
    )

with col2:

    city_df = top_cities(matches_df)

    city_chart = top_cities_chart(city_df)

    st.plotly_chart(
        city_chart,
        use_container_width=True
    )

# ==========================================================
# Player of Match Leaders
# ==========================================================

pom_df = top_player_of_match(matches_df)

pom_chart = player_of_match_chart(pom_df)

st.plotly_chart(
    pom_chart,
    use_container_width=True
)

# ==========================================================
# Footer
# ==========================================================

st.divider()

st.caption(
    "🏏 IPL Data Analysis Dashboard | Built with Streamlit & Plotly"
)