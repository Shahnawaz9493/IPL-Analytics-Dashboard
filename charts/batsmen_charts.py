"""
batsmen_charts.py
-----------------

Professional Plotly charts for the Batsmen Dashboard.

Responsibilities
----------------
✔ Top Run Scorers
✔ Highest Average
✔ Strike Rate
✔ Most Sixes
✔ Most Fours
✔ Highest Score
✔ Boundary %
✔ Dot Ball %
✔ Scatter Plot
"""

from __future__ import annotations

import pandas as pd
import plotly.express as px
import plotly.graph_objects as go


# ==========================================================
# Common Theme
# ==========================================================

def apply_layout(fig: go.Figure, title: str) -> go.Figure:
    """
    Apply common styling to all charts.
    """

    fig.update_layout(

        title={
            "text": title,
            "x": 0.5,
            "font": dict(
                size=22,
                color="white"
            ),
        },

        template="plotly_dark",

        paper_bgcolor="#0b1220",

        plot_bgcolor="#0b1220",

        font=dict(
            family="Poppins",
            color="white"
        ),

        height=500,

        margin=dict(
            l=20,
            r=20,
            t=60,
            b=20
        ),

        hovermode="closest"

    )

    return fig


# ==========================================================
# Top Run Scorers
# ==========================================================

def runs_chart(df: pd.DataFrame):

    fig = px.bar(

        df,

        x="Runs",

        y="batter",

        orientation="h",

        text="Runs",

        color="Runs",

        color_continuous_scale="Turbo"

    )

    fig.update_layout(

        yaxis=dict(
            categoryorder="total ascending"
        )

    )

    return apply_layout(
        fig,
        "Top Run Scorers"
    )


# ==========================================================
# Batting Average
# ==========================================================

def average_chart(df: pd.DataFrame):

    fig = px.bar(

        df,

        x="Average",

        y="batter",

        orientation="h",

        text="Average",

        color="Average",

        color_continuous_scale="Viridis"

    )

    fig.update_layout(

        yaxis=dict(
            categoryorder="total ascending"
        )

    )

    return apply_layout(
        fig,
        "Highest Batting Average"
    )


# ==========================================================
# Strike Rate
# ==========================================================

def strike_rate_chart(df: pd.DataFrame):

    fig = px.bar(

        df,

        x="Strike Rate",

        y="batter",

        orientation="h",

        text="Strike Rate",

        color="Strike Rate",

        color_continuous_scale="Plasma"

    )

    fig.update_layout(

        yaxis=dict(
            categoryorder="total ascending"
        )

    )

    return apply_layout(
        fig,
        "Highest Strike Rate"
    )


# ==========================================================
# Most Sixes
# ==========================================================

def sixes_chart(df: pd.DataFrame):

    fig = px.bar(

        df,

        x="Sixes",

        y="batter",

        orientation="h",

        text="Sixes",

        color="Sixes",

        color_continuous_scale="Inferno"

    )

    fig.update_layout(

        yaxis=dict(
            categoryorder="total ascending"
        )

    )

    return apply_layout(
        fig,
        "Most Sixes"
    )


# ==========================================================
# Most Fours
# ==========================================================

def fours_chart(df: pd.DataFrame):

    fig = px.bar(

        df,

        x="Fours",

        y="batter",

        orientation="h",

        text="Fours",

        color="Fours",

        color_continuous_scale="Blues"

    )

    fig.update_layout(

        yaxis=dict(
            categoryorder="total ascending"
        )

    )

    return apply_layout(
        fig,
        "Most Fours"
    )


# ==========================================================
# Highest Score
# ==========================================================

def highest_score_chart(df: pd.DataFrame):

    fig = px.bar(

        df,

        x="Highest Score",

        y="batter",

        orientation="h",

        text="Highest Score",

        color="Highest Score",

        color_continuous_scale="Magma"

    )

    fig.update_layout(

        yaxis=dict(
            categoryorder="total ascending"
        )

    )

    return apply_layout(
        fig,
        "Highest Individual Scores"
    )


# ==========================================================
# Boundary Percentage
# ==========================================================

def boundary_chart(df: pd.DataFrame):

    fig = px.bar(

        df,

        x="Boundary %",

        y="batter",

        orientation="h",

        text="Boundary %",

        color="Boundary %",

        color_continuous_scale="Aggrnyl"

    )

    fig.update_layout(

        yaxis=dict(
            categoryorder="total ascending"
        )

    )

    return apply_layout(
        fig,
        "Boundary Percentage"
    )


# ==========================================================
# Dot Ball Percentage
# ==========================================================

def dot_ball_chart(df: pd.DataFrame):

    fig = px.bar(

        df,

        x="Dot Ball %",

        y="batter",

        orientation="h",

        text="Dot Ball %",

        color="Dot Ball %",

        color_continuous_scale="RdPu"

    )

    fig.update_layout(

        yaxis=dict(
            categoryorder="total ascending"
        )

    )

    return apply_layout(
        fig,
        "Dot Ball Percentage"
    )


# ==========================================================
# Scatter Plot
# ==========================================================

def batting_scatter(df: pd.DataFrame):

    fig = px.scatter(

        df,

        x="Strike Rate",

        y="Average",

        size="Runs",

        color="Runs",

        hover_name="batter",

        color_continuous_scale="Turbo"

    )

    return apply_layout(
        fig,
        "Average vs Strike Rate"
    )