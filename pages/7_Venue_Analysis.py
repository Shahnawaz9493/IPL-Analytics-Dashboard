"""
7_Venue_Analysis.py
-------------------

Professional Venue Analysis Dashboard
"""

from __future__ import annotations

import streamlit as st

from utils.load_data import load_data
from utils.clean_data import clean_data

from components.cards import metric_card

from analysis.venue_analysis import (
    venue_scores,
    venue_summary,
    highest_scores,
    lowest_scores,
    average_scores,
    first_innings_average,
    second_innings_average,
    best_batting_grounds,
    best_bowling_grounds,
    chasing_success,
    toss_success_by_venue,
    venue_kpis,
    venue_leaderboard,
    search_venue,
)

from charts.venue_charts import (
    average_score_chart,
    highest_score_chart,
    lowest_score_chart,
    batting_ground_chart,
    bowling_ground_chart,
    first_innings_chart,
    second_innings_chart,
    chasing_success_chart,
    toss_success_chart,
    venue_heatmap,
    venue_scatter,
    matches_chart,
    average_score_gauge,
    venue_distribution,
)

# ==========================================================
# Load Data
# ==========================================================

matches_df, deliveries_df = load_data()

matches_df, deliveries_df = clean_data(
    matches_df,
    deliveries_df,
)

# ==========================================================
# Analysis
# ==========================================================

venue_df = venue_scores(
    matches_df,
    deliveries_df,
)

summary_df = venue_summary(
    venue_df,
)

highest_df = highest_scores(
    venue_df,
)

lowest_df = lowest_scores(
    venue_df,
)

average_df = average_scores(
    venue_df,
)

first_df = first_innings_average(
    venue_df,
)

second_df = second_innings_average(
    venue_df,
)

batting_df = best_batting_grounds(
    venue_df,
)

bowling_df = best_bowling_grounds(
    venue_df,
)

chasing_df = chasing_success(
    matches_df,
)

toss_df = toss_success_by_venue(
    matches_df,
)

leaderboard_df = venue_leaderboard(
    summary_df,
)

kpis = venue_kpis(
    summary_df,
)

# ==========================================================
# Sidebar
# ==========================================================

st.sidebar.header("🏟 Venue Analysis")

venues = sorted(
    summary_df["venue"].unique()
)

selected_venue = st.sidebar.selectbox(

    "Search Venue",

    ["All Venues"] + venues,

)

if selected_venue != "All Venues":

    summary_df = search_venue(
        summary_df,
        selected_venue,
    )

# ==========================================================
# Page Title
# ==========================================================

st.title("🏟 IPL Venue Analysis")

st.markdown(
    "Comprehensive venue-wise performance analytics across IPL seasons."
)

st.divider()

# ==========================================================
# KPI Cards
# ==========================================================

c1, c2, c3, c4 = st.columns(4)

with c1:

    metric_card(
        "Venues",
        kpis["Venues"],
        "🏟",
    )

with c2:

    metric_card(
        "Highest Score",
        kpis["Highest Score"],
        "🔥",
    )

with c3:

    metric_card(
        "Lowest Score",
        kpis["Lowest Score"],
        "🛡",
    )

with c4:

    metric_card(
        "Average Score",
        kpis["Average Score"],
        "📈",
    )

st.write("")

# ==========================================================
# Row 1
# ==========================================================

col1, col2 = st.columns(2)

with col1:

    st.plotly_chart(

        average_score_chart(
            average_df,
        ),

        use_container_width=True,

    )

with col2:

    st.plotly_chart(

        highest_score_chart(
            highest_df,
        ),

        use_container_width=True,

    )

# ==========================================================
# Row 2
# ==========================================================

col1, col2 = st.columns(2)

with col1:

    st.plotly_chart(

        lowest_score_chart(
            lowest_df,
        ),

        use_container_width=True,

    )

with col2:

    st.plotly_chart(

        matches_chart(
            summary_df,
        ),

        use_container_width=True,

    )
# ==========================================================
# Row 3
# Best Batting & Bowling Grounds
# ==========================================================

col1, col2 = st.columns(2)

with col1:

    st.plotly_chart(

        batting_ground_chart(
            batting_df
        ),

        use_container_width=True,

    )

with col2:

    st.plotly_chart(

        bowling_ground_chart(
            bowling_df
        ),

        use_container_width=True,

    )

# ==========================================================
# Row 4
# First Innings vs Second Innings
# ==========================================================

col1, col2 = st.columns(2)

with col1:

    st.plotly_chart(

        first_innings_chart(
            first_df
        ),

        use_container_width=True,

    )

with col2:

    st.plotly_chart(

        second_innings_chart(
            second_df
        ),

        use_container_width=True,

    )

# ==========================================================
# Row 5
# Chasing & Toss Success
# ==========================================================

col1, col2 = st.columns(2)

with col1:

    st.plotly_chart(

        chasing_success_chart(
            chasing_df
        ),

        use_container_width=True,

    )

with col2:

    st.plotly_chart(

        toss_success_chart(
            toss_df
        ),

        use_container_width=True,

    )

# ==========================================================
# Row 6
# Venue Heatmap
# ==========================================================

st.plotly_chart(

    venue_heatmap(
        summary_df
    ),

    use_container_width=True,

)

# ==========================================================
# Row 7
# Venue Scatter Plot
# ==========================================================

st.plotly_chart(

    venue_scatter(
        summary_df
    ),

    use_container_width=True,

)

# ==========================================================
# Row 8
# Gauge & Distribution
# ==========================================================

col1, col2 = st.columns(2)

with col1:

    st.plotly_chart(

        average_score_gauge(
            kpis["Average Score"]
        ),

        use_container_width=True,

    )

with col2:

    st.plotly_chart(

        venue_distribution(
            summary_df
        ),

        use_container_width=True,

    )

# ==========================================================
# Venue Leaderboard
# ==========================================================

st.subheader("🏆 Venue Leaderboard")

leaderboard_display = leaderboard_df.copy()

leaderboard_display.index = leaderboard_display.index + 1

st.dataframe(

    leaderboard_display,

    use_container_width=True,

    height=500,

)

# ==========================================================
# Download Report
# ==========================================================

csv = leaderboard_display.to_csv(index=False).encode("utf-8")

st.download_button(

    label="📥 Download Venue Report",

    data=csv,

    file_name="venue_analysis.csv",

    mime="text/csv",

)

# ==========================================================
# Raw Venue Statistics
# ==========================================================

with st.expander("📋 View Venue Statistics"):

    st.dataframe(

        summary_df,

        use_container_width=True,

        height=450,

    )

# ==========================================================
# Footer
# ==========================================================

st.divider()

st.caption(
    "IPL Analytics Dashboard • Venue Analysis • Built using Python, Pandas, Plotly & Streamlit"
)