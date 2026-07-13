"""
5_Toss_Analysis.py
------------------

Professional Toss Analysis Dashboard
"""

from __future__ import annotations

import streamlit as st

from utils.load_data import load_data
from utils.clean_data import clean_data

from components.cards import metric_card

from analysis.toss_analysis import (
    toss_kpis,
    toss_decision_distribution,
    toss_result_distribution,
    toss_wins_by_team,
    toss_success_by_team,
    toss_decision_by_team,
    venue_toss_success,
    season_toss_trend,
    toss_leaderboard,
    filter_team,
    filter_venue,
    filter_season,
)

from charts.toss_charts import (
    toss_decision_chart,
    toss_result_chart,
    toss_team_chart,
    toss_success_chart,
    venue_success_chart,
    season_trend_chart,
    toss_heatmap,
    toss_gauge,
)

# ==========================================================
# PAGE CONFIG
# ==========================================================

st.set_page_config(
    page_title="Toss Analysis",
    page_icon="🪙",
    layout="wide",
)

# ==========================================================
# LOAD DATA
# ==========================================================

matches_df, deliveries_df = load_data()

matches_df, deliveries_df = clean_data(
    matches_df,
    deliveries_df,
)

# ==========================================================
# SIDEBAR
# ==========================================================

st.sidebar.title("🪙 Toss Analysis")

teams = sorted(

    list(

        set(matches_df["team1"])

        |

        set(matches_df["team2"])

    )

)

venues = sorted(

    matches_df["venue"]

    .dropna()

    .unique()

)

seasons = sorted(

    matches_df["season"]

    .unique()

)

selected_team = st.sidebar.selectbox(

    "Select Team",

    ["All Teams"] + teams,

)

selected_venue = st.sidebar.selectbox(

    "Select Venue",

    ["All Venues"] + list(venues),

)

selected_season = st.sidebar.selectbox(

    "Select Season",

    ["All Seasons"] + list(seasons),

)

# ==========================================================
# FILTER DATA
# ==========================================================

filtered_df = filter_team(

    matches_df,

    selected_team,

)

filtered_df = filter_venue(

    filtered_df,

    selected_venue,

)

filtered_df = filter_season(

    filtered_df,

    selected_season,

)

# ==========================================================
# ANALYSIS
# ==========================================================

kpis = toss_kpis(filtered_df)

decision_df = toss_decision_distribution(filtered_df)

result_df = toss_result_distribution(filtered_df)

team_df = toss_wins_by_team(filtered_df)

success_df = toss_success_by_team(filtered_df)

venue_df = venue_toss_success(filtered_df)

season_df = season_toss_trend(filtered_df)

leaderboard_df = toss_leaderboard(filtered_df)

decision_team_df = toss_decision_by_team(filtered_df)

# ==========================================================
# TITLE
# ==========================================================

st.title("🪙 IPL Toss Analysis Dashboard")

st.markdown(
    """
Analyze toss trends, team strategies, venue impact,
and whether winning the toss actually improves the
chances of winning the match.
"""
)

st.divider()

# ==========================================================
# KPI CARDS
# ==========================================================

col1, col2, col3, col4 = st.columns(4)

with col1:

    metric_card(

        "Matches",

        kpis["Total Matches"],

        "🏏",

    )

with col2:

    metric_card(

        "Bat First",

        kpis["Bat First"],

        "🏏",

    )

with col3:

    metric_card(

        "Field First",

        kpis["Field First"],

        "🎯",

    )

with col4:

    metric_card(

        "Toss Win %",

        kpis["Toss Win Percentage"],

        "📈",

    )

st.write("")

# ==========================================================
# ROW 1
# ==========================================================

left, right = st.columns(2)

with left:

    st.plotly_chart(

        toss_decision_chart(

            decision_df,

        ),

        use_container_width=True,

    )

with right:

    st.plotly_chart(

        toss_result_chart(

            result_df,

        ),

        use_container_width=True,

    )

# ==========================================================
# ROW 2
# ==========================================================

left, right = st.columns(2)

with left:

    st.plotly_chart(

        toss_team_chart(

            team_df,

        ),

        use_container_width=True,

    )

with right:

    st.plotly_chart(

        toss_success_chart(

            success_df,

        ),

        use_container_width=True,

    )

# ==========================================================
# ROW 3
# ==========================================================

left, right = st.columns(2)

with left:

    st.plotly_chart(

        venue_success_chart(

            venue_df,

        ),

        use_container_width=True,

    )

with right:

    st.plotly_chart(

        season_trend_chart(

            season_df,

        ),

        use_container_width=True,

    )
# ==========================================================
# ROW 4
# Heatmap & Gauge
# ==========================================================

left, right = st.columns(2)

with left:

    st.plotly_chart(

        toss_heatmap(
            decision_team_df,
        ),

        use_container_width=True,

    )

with right:

    st.plotly_chart(

        toss_gauge(
            kpis["Toss Win Percentage"],
        ),

        use_container_width=True,

    )

# ==========================================================
# Leaderboard
# ==========================================================

st.divider()

st.subheader("🏆 Team Toss Success Leaderboard")

leaderboard = leaderboard_df.copy()

leaderboard.index = leaderboard.index + 1

st.dataframe(

    leaderboard,

    use_container_width=True,

    height=420,

)

# ==========================================================
# Download Leaderboard
# ==========================================================

csv = leaderboard.to_csv(index=False).encode("utf-8")

st.download_button(

    label="📥 Download Leaderboard",

    data=csv,

    file_name="toss_leaderboard.csv",

    mime="text/csv",

)

# ==========================================================
# Team Toss Statistics
# ==========================================================

st.divider()

st.subheader("📊 Toss Statistics by Team")

team_display = success_df.copy()

team_display.index = team_display.index + 1

st.dataframe(

    team_display,

    use_container_width=True,

    height=350,

)

# ==========================================================
# Venue Statistics
# ==========================================================

st.divider()

st.subheader("🏟 Venue Toss Statistics")

venue_display = venue_df.copy()

venue_display.index = venue_display.index + 1

st.dataframe(

    venue_display,

    use_container_width=True,

    height=350,

)

# ==========================================================
# Toss Decision Distribution Table
# ==========================================================

with st.expander("🪙 Toss Decision Distribution"):

    decision_table = decision_df.copy()

    decision_table.index = decision_table.index + 1

    st.dataframe(

        decision_table,

        use_container_width=True,

    )

# ==========================================================
# Toss Result Distribution Table
# ==========================================================

with st.expander("🏆 Toss Winner vs Match Winner"):

    result_table = result_df.copy()

    result_table.index = result_table.index + 1

    st.dataframe(

        result_table,

        use_container_width=True,

    )

# ==========================================================
# Season-wise Toss Trend
# ==========================================================

with st.expander("📅 Season-wise Toss Trend"):

    season_table = season_df.copy()

    season_table.index = season_table.index + 1

    st.dataframe(

        season_table,

        use_container_width=True,

        height=350,

    )

# ==========================================================
# Raw Match Data
# ==========================================================

st.divider()

with st.expander("🗂 View Filtered Match Data"):

    raw = filtered_df.copy()

    raw.index = raw.index + 1

    st.dataframe(

        raw,

        use_container_width=True,

        height=500,

    )

# ==========================================================
# Quick Insights
# ==========================================================

st.divider()

st.subheader("📌 Quick Insights")

col1, col2 = st.columns(2)

with col1:

    st.info(
        f"""
**Total Matches Analysed:** {kpis["Total Matches"]}

**Bat First Decisions:** {kpis["Bat First"]}

**Field First Decisions:** {kpis["Field First"]}
"""
    )

with col2:

    st.success(
        f"""
**Toss Winner also Won Match:** {kpis["Toss Win Percentage"]:.2f}%

This metric indicates how often winning the toss translated into winning the match.
"""
    )

# ==========================================================
# Footer
# ==========================================================

st.divider()

st.caption(
    "🏏 IPL Analytics Dashboard • Toss Analysis • Built with Python, Pandas, Plotly & Streamlit"
)