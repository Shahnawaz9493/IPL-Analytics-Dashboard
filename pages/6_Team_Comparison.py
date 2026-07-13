"""
6_Team_Comparison.py
--------------------

Professional Team Comparison Dashboard
"""

from __future__ import annotations

import streamlit as st

from utils.load_data import load_data
from utils.clean_data import clean_data

from components.cards import metric_card

from analysis.team_analysis import (
    available_teams,
    head_to_head_summary,
    toss_summary,
    match_ids,
    match_scores,
    score_summary,
    win_percentage,
    home_away_summary,
    powerplay_scores,
    death_over_scores,
    venue_comparison,
    team_kpis,
    comparison_table,
    match_timeline,
)

from charts.team_charts import (
    head_to_head_chart,
    win_percentage_chart,
    toss_comparison_chart,
    average_score_chart,
    highest_score_chart,
    lowest_score_chart,
    powerplay_chart,
    death_over_chart,
    home_away_chart,
    venue_chart,
    radar_chart,
    score_distribution_chart,
    timeline_chart,
    win_percentage_gauge,
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

st.sidebar.header("🏏 Team Comparison")

teams = available_teams(matches_df)

team1 = st.sidebar.selectbox(
    "Select Team 1",
    teams,
    index=0,
)

team2 = st.sidebar.selectbox(
    "Select Team 2",
    teams,
    index=1,
)

if team1 == team2:
    st.warning("Please select two different teams.")
    st.stop()

# ==========================================================
# Analysis
# ==========================================================

summary = head_to_head_summary(
    matches_df,
    team1,
    team2,
)

ids = match_ids(
    matches_df,
    team1,
    team2,
)

scores_df = match_scores(
    deliveries_df,
    ids,
)

score_df = score_summary(
    scores_df,
)

toss_df = toss_summary(
    matches_df,
    team1,
    team2,
)

home_df = home_away_summary(
    matches_df,
    team1,
    team2,
)

pp_df = powerplay_scores(
    deliveries_df,
    ids,
)

death_df = death_over_scores(
    deliveries_df,
    ids,
)

venue_df = venue_comparison(
    matches_df,
    team1,
    team2,
)

compare_df = comparison_table(
    score_df,
    pp_df,
    death_df,
)

timeline_df = match_timeline(
    matches_df,
    team1,
    team2,
)

win_df = win_percentage(
    summary,
    team1,
    team2,
)

kpis = team_kpis(
    summary,
    score_df,
)

# ==========================================================
# Title
# ==========================================================

st.title("⚔ Team Comparison")

st.markdown(
    f"### {team1} 🆚 {team2}"
)

st.divider()

# ==========================================================
# KPI Cards
# ==========================================================

c1, c2, c3, c4 = st.columns(4)

with c1:

    metric_card(
        "Matches",
        kpis["Matches"],
        "🏏",
    )

with c2:

    metric_card(
        team1,
        summary[team1],
        "💙",
    )

with c3:

    metric_card(
        team2,
        summary[team2],
        "❤️",
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

        head_to_head_chart(
            summary,
            team1,
            team2,
        ),

        use_container_width=True,

    )

with col2:

    st.plotly_chart(

        win_percentage_chart(
            win_df
        ),

        use_container_width=True,

    )

# ==========================================================
# Row 2
# ==========================================================

col1, col2 = st.columns(2)

with col1:

    st.plotly_chart(

        toss_comparison_chart(
            toss_df
        ),

        use_container_width=True,

    )

with col2:

    st.plotly_chart(

        average_score_chart(
            score_df
        ),

        use_container_width=True,

    )
# ==========================================================
# Row 3
# Highest & Lowest Scores
# ==========================================================

col1, col2 = st.columns(2)

with col1:

    st.plotly_chart(

        highest_score_chart(
            score_df
        ),

        use_container_width=True,

    )

with col2:

    st.plotly_chart(

        lowest_score_chart(
            score_df
        ),

        use_container_width=True,

    )

# ==========================================================
# Row 4
# Powerplay & Death Overs
# ==========================================================

col1, col2 = st.columns(2)

with col1:

    st.plotly_chart(

        powerplay_chart(
            pp_df
        ),

        use_container_width=True,

    )

with col2:

    st.plotly_chart(

        death_over_chart(
            death_df
        ),

        use_container_width=True,

    )

# ==========================================================
# Row 5
# Home vs Away
# ==========================================================

st.plotly_chart(

    home_away_chart(
        home_df
    ),

    use_container_width=True,

)

# ==========================================================
# Row 6
# Venue Comparison
# ==========================================================

st.plotly_chart(

    venue_chart(
        venue_df
    ),

    use_container_width=True,

)

# ==========================================================
# Row 7
# Radar & Gauge
# ==========================================================

col1, col2 = st.columns(2)

with col1:

    st.plotly_chart(

        radar_chart(
            compare_df
        ),

        use_container_width=True,

    )

with col2:

    st.plotly_chart(

        win_percentage_gauge(
            summary[f"{team1} Win %"]
        ),

        use_container_width=True,

    )

# ==========================================================
# Row 8
# Score Distribution
# ==========================================================

st.plotly_chart(

    score_distribution_chart(
        scores_df
    ),

    use_container_width=True,

)

# ==========================================================
# Row 9
# Timeline
# ==========================================================

st.plotly_chart(

    timeline_chart(
        timeline_df
    ),

    use_container_width=True,

)

# ==========================================================
# Comparison Table
# ==========================================================

st.subheader("📊 Team Performance Comparison")

comparison_display = compare_df.copy()

comparison_display.index = comparison_display.index + 1

st.dataframe(

    comparison_display,

    use_container_width=True,

    height=320,

)

# ==========================================================
# Match Timeline
# ==========================================================

st.subheader("📅 Match Timeline")

timeline_display = timeline_df.copy()

timeline_display.index = timeline_display.index + 1

st.dataframe(

    timeline_display,

    use_container_width=True,

    height=350,

)

# ==========================================================
# Download Report
# ==========================================================

csv = comparison_display.to_csv(index=False).encode("utf-8")

st.download_button(

    label="📥 Download Team Comparison Report",

    data=csv,

    file_name=f"{team1}_vs_{team2}_comparison.csv",

    mime="text/csv",

)

# ==========================================================
# Raw Match Data
# ==========================================================

with st.expander("📋 View Head-to-Head Match Data"):

    matches_between = matches_df[
        (
            ((matches_df["team1"] == team1) & (matches_df["team2"] == team2))
            |
            ((matches_df["team1"] == team2) & (matches_df["team2"] == team1))
        )
    ]

    st.dataframe(

        matches_between,

        use_container_width=True,

        height=450,

    )

# ==========================================================
# Footer
# ==========================================================

st.divider()

st.caption(
    "IPL Analytics Dashboard • Team Comparison • Built using Python, Pandas, Plotly & Streamlit"
)