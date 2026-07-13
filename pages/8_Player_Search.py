"""
8_Player_Search.py
------------------

Professional Player Search Dashboard.
"""

from __future__ import annotations

import streamlit as st

from utils.load_data import load_data
from utils.clean_data import clean_data

from components.cards import metric_card

from analysis.player_analysis import (
    player_list,
    batting_statistics,
    bowling_statistics,
    boundary_statistics,
    runs_by_match,
    wickets_by_match,
    dismissal_analysis,
    opponent_runs,
    opponent_wickets,
    season_runs,
    season_wickets,
    career_summary,
    player_kpis,
)

from charts.player_charts import (
    runs_match_chart,
    wickets_match_chart,
    boundary_chart,
    dismissal_chart,
    opponent_runs_chart,
    opponent_wickets_chart,
    season_runs_chart,
    season_wickets_chart,
    career_summary_chart,
    radar_chart,
    strike_rate_gauge,
    economy_gauge,
    career_distribution,
    performance_timeline,
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
# Sidebar
# ==========================================================

st.sidebar.header("🔍 Player Search")

players = player_list(deliveries_df)

selected_player = st.sidebar.selectbox(
    "Select Player",
    players,
)

# ==========================================================
# Analysis
# ==========================================================

batting_stats = batting_statistics(
    deliveries_df,
    selected_player,
)

bowling_stats = bowling_statistics(
    deliveries_df,
    selected_player,
)

boundary_df = boundary_statistics(
    deliveries_df,
    selected_player,
)

runs_df = runs_by_match(
    deliveries_df,
    selected_player,
)

wickets_df = wickets_by_match(
    deliveries_df,
    selected_player,
)

dismissal_df = dismissal_analysis(
    deliveries_df,
    selected_player,
)

opponent_runs_df = opponent_runs(
    deliveries_df,
    selected_player,
)

opponent_wickets_df = opponent_wickets(
    deliveries_df,
    selected_player,
)

season_runs_df = season_runs(
    deliveries_df,
    matches_df,
    selected_player,
)

season_wickets_df = season_wickets(
    deliveries_df,
    matches_df,
    selected_player,
)

career_df = career_summary(
    batting_stats,
    bowling_stats,
)

kpis = player_kpis(
    batting_stats,
    bowling_stats,
)

# ==========================================================
# Title
# ==========================================================

st.title("👤 Player Search")

st.markdown(f"## {selected_player}")

st.divider()

# ==========================================================
# KPI Cards
# ==========================================================

c1, c2, c3, c4 = st.columns(4)

with c1:

    metric_card(
        "Runs",
        kpis["Runs"],
        "🏏",
    )

with c2:

    metric_card(
        "Wickets",
        kpis["Wickets"],
        "🎯",
    )

with c3:

    metric_card(
        "Strike Rate",
        kpis["Strike Rate"],
        "⚡",
    )

with c4:

    metric_card(
        "Economy",
        kpis["Economy"],
        "📉",
    )

st.write("")

# ==========================================================
# Row 1
# ==========================================================

col1, col2 = st.columns(2)

with col1:

    st.plotly_chart(

        runs_match_chart(
            runs_df,
        ),

        use_container_width=True,

    )

with col2:

    st.plotly_chart(

        wickets_match_chart(
            wickets_df,
        ),

        use_container_width=True,

    )

# ==========================================================
# Row 2
# ==========================================================

col1, col2 = st.columns(2)

with col1:

    st.plotly_chart(

        boundary_chart(
            boundary_df,
        ),

        use_container_width=True,

    )

with col2:

    st.plotly_chart(

        dismissal_chart(
            dismissal_df,
        ),

        use_container_width=True,

    )
# ==========================================================
# Row 3
# Opponent Analysis
# ==========================================================

col1, col2 = st.columns(2)

with col1:

    st.plotly_chart(

        opponent_runs_chart(
            opponent_runs_df
        ),

        use_container_width=True,

    )

with col2:

    st.plotly_chart(

        opponent_wickets_chart(
            opponent_wickets_df
        ),

        use_container_width=True,

    )

# ==========================================================
# Row 4
# Season-wise Performance
# ==========================================================

col1, col2 = st.columns(2)

with col1:

    st.plotly_chart(

        season_runs_chart(
            season_runs_df
        ),

        use_container_width=True,

    )

with col2:

    st.plotly_chart(

        season_wickets_chart(
            season_wickets_df
        ),

        use_container_width=True,

    )

# ==========================================================
# Row 5
# Performance Overview
# ==========================================================

col1, col2 = st.columns(2)

with col1:

    st.plotly_chart(

        radar_chart(
            batting_stats,
            bowling_stats,
        ),

        use_container_width=True,

    )

with col2:

    st.plotly_chart(

        performance_timeline(
            runs_df,
            wickets_df,
        ),

        use_container_width=True,

    )

# ==========================================================
# Row 6
# KPI Gauges
# ==========================================================

col1, col2 = st.columns(2)

with col1:

    st.plotly_chart(

        strike_rate_gauge(
            batting_stats["Strike Rate"]
        ),

        use_container_width=True,

    )

with col2:

    st.plotly_chart(

        economy_gauge(
            bowling_stats["Economy"]
        ),

        use_container_width=True,

    )

# ==========================================================
# Row 7
# Career Summary & Distribution
# ==========================================================

col1, col2 = st.columns(2)

with col1:

    st.plotly_chart(

        career_summary_chart(
            career_df
        ),

        use_container_width=True,

    )

with col2:

    st.plotly_chart(

        career_distribution(
            runs_df
        ),

        use_container_width=True,

    )

# ==========================================================
# Career Summary Table
# ==========================================================

st.subheader("📋 Career Summary")

career_display = career_df.copy()

career_display.index = career_display.index + 1

st.dataframe(

    career_display,

    use_container_width=True,

    height=420,

)

# ==========================================================
# Download Report
# ==========================================================

csv = career_display.to_csv(index=False).encode("utf-8")

st.download_button(

    label="📥 Download Player Report",

    data=csv,

    file_name=f"{selected_player}_career_summary.csv",

    mime="text/csv",

)

# ==========================================================
# Raw Match-wise Batting Data
# ==========================================================

with st.expander("🏏 Match-wise Batting Performance"):

    batting_table = runs_df.copy()

    batting_table.index = batting_table.index + 1

    st.dataframe(

        batting_table,

        use_container_width=True,

        height=350,

    )

# ==========================================================
# Raw Match-wise Bowling Data
# ==========================================================

with st.expander("🎯 Match-wise Bowling Performance"):

    bowling_table = wickets_df.copy()

    bowling_table.index = bowling_table.index + 1

    st.dataframe(

        bowling_table,

        use_container_width=True,

        height=350,

    )

# ==========================================================
# Footer
# ==========================================================

st.divider()

st.caption(
    "IPL Analytics Dashboard • Player Search • Built using Python, Pandas, Plotly & Streamlit"
)