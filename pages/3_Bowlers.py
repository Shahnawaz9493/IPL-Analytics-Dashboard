"""
3_Bowlers.py
------------

Professional IPL Bowling Dashboard
"""

from __future__ import annotations

import streamlit as st

from utils.load_data import load_data
from utils.clean_data import clean_data

from components.cards import metric_card

from analysis.bowlers_analysis import (
    bowling_summary,
    bowling_kpis,
    best_bowling_figures,
    merge_bowling_records,
    top_wicket_takers,
    best_economy,
    best_average,
    best_strike_rate,
    most_dot_balls,
    best_dot_ball_percentage,
    four_wicket_hauls,
    five_wicket_hauls,
    player_statistics,
)

from charts.bowlers_charts import (
    wickets_chart,
    economy_chart,
    average_chart,
    strike_rate_chart,
    dot_ball_chart,
    dot_percentage_chart,
    four_wicket_chart,
    five_wicket_chart,
    bowling_scatter,
    wicket_share_chart,
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
# Bowling Summary
# ==========================================================

summary_df = bowling_summary(deliveries_df)

figures_df = best_bowling_figures(deliveries_df)

summary_df = merge_bowling_records(
    summary_df,
    figures_df,
)

# ==========================================================
# Page Title
# ==========================================================

st.title("🎯 Best Bowlers Analysis")

st.markdown(
    "Comprehensive bowling analytics for every IPL bowler."
)

st.divider()

# ==========================================================
# Sidebar Filters
# ==========================================================

st.sidebar.header("Bowling Filters")

min_wickets = st.sidebar.slider(
    "Minimum Wickets",
    0,
    int(summary_df["Wickets"].max()),
    20,
)

bowler = st.sidebar.selectbox(
    "Search Bowler",
    ["All Bowlers"]
    + sorted(summary_df["bowler"].unique())
)

filtered_df = summary_df.copy()

filtered_df = filtered_df[
    filtered_df["Wickets"] >= min_wickets
]

if bowler != "All Bowlers":

    filtered_df = player_statistics(
        filtered_df,
        bowler,
    )

# ==========================================================
# KPI Cards
# ==========================================================

kpis = bowling_kpis(filtered_df)

col1, col2, col3, col4 = st.columns(4)

with col1:

    metric_card(
        "Bowlers",
        kpis["Bowlers"],
        "🎯",
    )

with col2:

    metric_card(
        "Total Wickets",
        kpis["Total Wickets"],
        "🏏",
    )

with col3:

    metric_card(
        "Avg Economy",
        kpis["Average Economy"],
        "📉",
    )

with col4:

    metric_card(
        "Strike Rate",
        kpis["Average Strike Rate"],
        "⚡",
    )

st.write("")

# ==========================================================
# Charts
# ==========================================================

col1, col2 = st.columns(2)

with col1:

    st.plotly_chart(

        wickets_chart(

            top_wicket_takers(filtered_df)

        ),

        use_container_width=True,

    )

with col2:

    st.plotly_chart(

        economy_chart(

            best_economy(filtered_df)

        ),

        use_container_width=True,

    )

# ----------------------------------------------------------

col1, col2 = st.columns(2)

with col1:

    st.plotly_chart(

        average_chart(

            best_average(filtered_df)

        ),

        use_container_width=True,

    )

with col2:

    st.plotly_chart(

        strike_rate_chart(

            best_strike_rate(filtered_df)

        ),

        use_container_width=True,

    )

# ----------------------------------------------------------

col1, col2 = st.columns(2)

with col1:

    st.plotly_chart(

        dot_ball_chart(

            most_dot_balls(filtered_df)

        ),

        use_container_width=True,

    )

with col2:

    st.plotly_chart(

        dot_percentage_chart(

            best_dot_ball_percentage(filtered_df)

        ),

        use_container_width=True,

    )
# ----------------------------------------------------------
# Four & Five Wicket Hauls
# ----------------------------------------------------------

four_df = four_wicket_hauls(figures_df)
five_df = five_wicket_hauls(figures_df)

col1, col2 = st.columns(2)

with col1:

    st.plotly_chart(

        four_wicket_chart(four_df),

        use_container_width=True,

    )

with col2:

    st.plotly_chart(

        five_wicket_chart(five_df),

        use_container_width=True,

    )

# ----------------------------------------------------------
# Scatter Plot
# ----------------------------------------------------------

st.plotly_chart(

    bowling_scatter(filtered_df),

    use_container_width=True,

)

# ----------------------------------------------------------
# Wicket Share Donut
# ----------------------------------------------------------

st.plotly_chart(

    wicket_share_chart(

        top_wicket_takers(filtered_df)

    ),

    use_container_width=True,

)

# ----------------------------------------------------------
# Bowling Leaderboard
# ----------------------------------------------------------

st.subheader("🏏 Bowling Leaderboard")

display_columns = [

    "bowler",

    "Matches",

    "Overs",

    "Runs",

    "Wickets",

    "Economy",

    "Average",

    "Strike Rate",

    "DotBalls",

    "Dot Ball %",

    "Best Figures",

    "4W",

    "5W",

]

leaderboard = filtered_df[display_columns].copy()

leaderboard.index = leaderboard.index + 1

st.dataframe(

    leaderboard,

    use_container_width=True,

    height=600,

)

# ----------------------------------------------------------
# Download CSV
# ----------------------------------------------------------

csv = leaderboard.to_csv(index=False).encode("utf-8")

st.download_button(

    label="📥 Download Bowling Statistics",

    data=csv,

    file_name="ipl_bowling_statistics.csv",

    mime="text/csv",

)

# ----------------------------------------------------------
# Footer
# ----------------------------------------------------------

st.divider()

st.caption(
    "IPL Analytics Dashboard • Bowling Analysis • Built using Python, Pandas, Plotly & Streamlit"
)