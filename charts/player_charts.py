"""
player_charts.py
----------------

Professional Plotly Charts for Player Search Dashboard.

Responsibilities
----------------
✔ Runs Per Match
✔ Wickets Per Match
✔ Boundary Distribution
✔ Dismissal Analysis
✔ Opponent Runs

No Streamlit code.
"""

from __future__ import annotations

import pandas as pd
import plotly.express as px
import plotly.graph_objects as go


# ==========================================================
# Common Layout
# ==========================================================

def apply_layout(
    fig: go.Figure,
    title: str,
) -> go.Figure:
    """
    Apply common dashboard styling.
    """

    fig.update_layout(

        title={
            "text": title,
            "x": 0.5,
            "font": {
                "size": 22,
                "color": "white",
            },
        },

        template="plotly_dark",

        paper_bgcolor="#0b1220",

        plot_bgcolor="#0b1220",

        font=dict(
            family="Poppins",
            color="white",
        ),

        height=500,

        margin=dict(
            l=20,
            r=20,
            t=60,
            b=20,
        ),

    )

    return fig


# ==========================================================
# Runs Per Match
# ==========================================================

def runs_match_chart(
    df: pd.DataFrame,
):

    fig = px.line(

        df,

        x="match_id",

        y="Runs",

        markers=True,

    )

    return apply_layout(
        fig,
        "Runs per Match",
    )


# ==========================================================
# Wickets Per Match
# ==========================================================

def wickets_match_chart(
    df: pd.DataFrame,
):

    fig = px.line(

        df,

        x="match_id",

        y="Wickets",

        markers=True,

    )

    return apply_layout(
        fig,
        "Wickets per Match",
    )


# ==========================================================
# Boundary Distribution
# ==========================================================

def boundary_chart(
    df: pd.DataFrame,
):

    fig = px.pie(

        df,

        names="Type",

        values="Count",

        hole=0.60,

        color_discrete_sequence=px.colors.qualitative.Bold,

    )

    return apply_layout(
        fig,
        "Boundary Distribution",
    )


# ==========================================================
# Dismissal Analysis
# ==========================================================

def dismissal_chart(
    df: pd.DataFrame,
):

    fig = px.bar(

        df,

        x="dismissal_kind",

        y="Count",

        text="Count",

        color="Count",

        color_continuous_scale="Turbo",

    )

    return apply_layout(
        fig,
        "Dismissal Analysis",
    )


# ==========================================================
# Opponent Runs
# ==========================================================

def opponent_runs_chart(
    df: pd.DataFrame,
):

    fig = px.bar(

        df,

        x="Runs",

        y="bowling_team",

        orientation="h",

        text="Runs",

        color="Runs",

        color_continuous_scale="Turbo",

    )

    fig.update_layout(

        yaxis=dict(
            categoryorder="total ascending"
        )

    )

    return apply_layout(
        fig,
        "Runs Against Opponents",
    )
# ==========================================================
# Opponent Wickets
# ==========================================================

def opponent_wickets_chart(
    df: pd.DataFrame,
):
    """
    Wickets against each batting team.
    """

    fig = px.bar(

        df,

        x="Wickets",

        y="batting_team",

        orientation="h",

        text="Wickets",

        color="Wickets",

        color_continuous_scale="Viridis",

    )

    fig.update_layout(

        yaxis=dict(

            categoryorder="total ascending"

        )

    )

    return apply_layout(
        fig,
        "Wickets Against Opponents",
    )


# ==========================================================
# Season-wise Runs
# ==========================================================

def season_runs_chart(
    df: pd.DataFrame,
):
    """
    Runs scored season-wise.
    """

    fig = px.line(

        df,

        x="season",

        y="Runs",

        markers=True,

        text="Runs",

    )

    return apply_layout(
        fig,
        "Season-wise Runs",
    )


# ==========================================================
# Season-wise Wickets
# ==========================================================

def season_wickets_chart(
    df: pd.DataFrame,
):
    """
    Wickets taken season-wise.
    """

    fig = px.line(

        df,

        x="season",

        y="Wickets",

        markers=True,

        text="Wickets",

    )

    return apply_layout(
        fig,
        "Season-wise Wickets",
    )


# ==========================================================
# Career Summary
# ==========================================================

def career_summary_chart(
    df: pd.DataFrame,
):
    """
    Career summary visualization.
    """

    fig = px.bar(

        df,

        x="Metric",

        y="Value",

        text="Value",

        color="Value",

        color_continuous_scale="Turbo",

    )

    return apply_layout(
        fig,
        "Career Summary",
    )


# ==========================================================
# Performance Radar
# ==========================================================

def radar_chart(
    batting_stats: dict,
    bowling_stats: dict,
):
    """
    Player performance radar.
    """

    categories = [

        "Runs",

        "Strike Rate",

        "Average",

        "Wickets",

        "Economy",

    ]

    values = [

        batting_stats["Runs"],

        batting_stats["Strike Rate"],

        batting_stats["Average"],

        bowling_stats["Wickets"],

        bowling_stats["Economy"],

    ]

    fig = go.Figure()

    fig.add_trace(

        go.Scatterpolar(

            r=values,

            theta=categories,

            fill="toself",

            name="Performance",

        )

    )

    return apply_layout(
        fig,
        "Performance Radar",
    )


# ==========================================================
# Strike Rate Gauge
# ==========================================================

def strike_rate_gauge(
    strike_rate: float,
):
    """
    Strike rate gauge.
    """

    fig = go.Figure(

        go.Indicator(

            mode="gauge+number",

            value=strike_rate,

            title={

                "text": "Strike Rate"

            },

            gauge={

                "axis": {

                    "range": [0, 250]

                },

                "bar": {

                    "color": "#00CC96"

                },

            },

        )

    )

    return apply_layout(
        fig,
        "Strike Rate",
    )


# ==========================================================
# Economy Gauge
# ==========================================================

def economy_gauge(
    economy: float,
):
    """
    Bowling economy gauge.
    """

    fig = go.Figure(

        go.Indicator(

            mode="gauge+number",

            value=economy,

            title={

                "text": "Economy Rate"

            },

            gauge={

                "axis": {

                    "range": [0, 15]

                },

                "bar": {

                    "color": "#FFA15A"

                },

            },

        )

    )

    return apply_layout(
        fig,
        "Economy Rate",
    )


# ==========================================================
# Career Distribution
# ==========================================================

def career_distribution(
    runs_df: pd.DataFrame,
):
    """
    Distribution of match scores.
    """

    fig = px.box(

        runs_df,

        y="Runs",

        points="all",

    )

    return apply_layout(
        fig,
        "Runs Distribution",
    )


# ==========================================================
# Performance Timeline
# ==========================================================

def performance_timeline(
    runs_df: pd.DataFrame,
    wickets_df: pd.DataFrame,
):
    """
    Combined batting and bowling timeline.
    """

    fig = go.Figure()

    fig.add_trace(

        go.Scatter(

            x=runs_df["match_id"],

            y=runs_df["Runs"],

            mode="lines+markers",

            name="Runs",

        )

    )

    fig.add_trace(

        go.Scatter(

            x=wickets_df["match_id"],

            y=wickets_df["Wickets"],

            mode="lines+markers",

            name="Wickets",

        )

    )

    return apply_layout(
        fig,
        "Performance Timeline",
    )