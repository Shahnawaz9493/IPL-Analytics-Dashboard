"""
2_Batsmen.py
------------

Professional IPL Batting Dashboard
"""

from __future__ import annotations

import streamlit as st

from utils.load_data import load_data
from utils.clean_data import clean_data

from components.cards import metric_card

from analysis.batsmen_analysis import (
    batting_summary,
    batting_kpis,
    top_run_scorers,
    highest_average,
    highest_strike_rate,
    most_sixes,
    most_fours,
    highest_scores,
    boundary_hitters,
    dot_ball_percentage,
    player_statistics,
)

from charts.batsmen_charts import (
    runs_chart,
    average_chart,
    strike_rate_chart,
    sixes_chart,
    fours_chart,
    highest_score_chart,
    boundary_chart,
    dot_ball_chart,
    batting_scatter,
)

# -----------------------------------------------------
# Load Data
# -----------------------------------------------------

matches_df, deliveries_df = load_data()
matches_df, deliveries_df = clean_data(
    matches_df,
    deliveries_df
)

batting_df = batting_summary(deliveries_df)

# -----------------------------------------------------
# Page Title
# -----------------------------------------------------

st.title("🏏 Best Batsmen Analysis")

st.markdown(
    "Comprehensive batting analytics of every IPL batter."
)

st.divider()

# -----------------------------------------------------
# Sidebar Filters
# -----------------------------------------------------

st.sidebar.header("Batting Filters")

min_runs = st.sidebar.slider(
    "Minimum Runs",
    0,
    int(batting_df["Runs"].max()),
    500,
)

player = st.sidebar.selectbox(
    "Search Player",
    ["All Players"] + sorted(
        batting_df["batter"].unique().tolist()
    )
)

filtered_df = batting_df.copy()

filtered_df = filtered_df[
    filtered_df["Runs"] >= min_runs
]

if player != "All Players":
    filtered_df = player_statistics(
        filtered_df,
        player
    )

# -----------------------------------------------------
# KPI Cards
# -----------------------------------------------------

kpis = batting_kpis(filtered_df)

col1, col2, col3, col4 = st.columns(4)

with col1:
    metric_card("Players", kpis["Players"], "🏏")

with col2:
    metric_card("Total Runs", kpis["Total Runs"], "🏃")

with col3:
    metric_card("Average", kpis["Overall Average"], "📈")

with col4:
    metric_card(
        "Strike Rate",
        kpis["Overall Strike Rate"],
        "⚡",
    )

st.write("")

# -----------------------------------------------------
# Charts
# -----------------------------------------------------

col1, col2 = st.columns(2)

with col1:

    st.plotly_chart(
        runs_chart(
            top_run_scorers(filtered_df)
        ),
        use_container_width=True,
    )

with col2:

    st.plotly_chart(
        average_chart(
            highest_average(filtered_df)
        ),
        use_container_width=True,
    )

# -----------------------------------------------------

col1, col2 = st.columns(2)

with col1:

    st.plotly_chart(
        strike_rate_chart(
            highest_strike_rate(filtered_df)
        ),
        use_container_width=True,
    )

with col2:

    st.plotly_chart(
        highest_score_chart(
            highest_scores(filtered_df)
        ),
        use_container_width=True,
    )

# -----------------------------------------------------

col1, col2 = st.columns(2)

with col1:

    st.plotly_chart(
        fours_chart(
            most_fours(filtered_df)
        ),
        use_container_width=True,
    )

with col2:

    st.plotly_chart(
        sixes_chart(
            most_sixes(filtered_df)
        ),
        use_container_width=True,
    )

# -----------------------------------------------------

col1, col2 = st.columns(2)

with col1:

    st.plotly_chart(
        boundary_chart(
            boundary_hitters(filtered_df)
        ),
        use_container_width=True,
    )

with col2:

    st.plotly_chart(
        dot_ball_chart(
            dot_ball_percentage(filtered_df)
        ),
        use_container_width=True,
    )

# -----------------------------------------------------

st.plotly_chart(

    batting_scatter(filtered_df),

    use_container_width=True

)

# -----------------------------------------------------
# Statistics Table
# -----------------------------------------------------

st.subheader("📋 Complete Batting Statistics")

st.dataframe(

    filtered_df,

    use_container_width=True,

    hide_index=True,

)

# -----------------------------------------------------
# Download
# -----------------------------------------------------

csv = filtered_df.to_csv(index=False).encode("utf-8")

st.download_button(

    "⬇ Download Batting Statistics",

    csv,

    "ipl_batting_statistics.csv",

    "text/csv",

)