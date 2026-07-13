"""
home_charts.py
--------------

Interactive Plotly charts for the Home Dashboard.

Responsibilities
----------------
✔ Matches per Season
✔ Toss Decision Distribution
✔ Match Result Distribution
✔ Top Venues
✔ Top Cities
✔ Player of the Match Leaders
"""

from __future__ import annotations

import plotly.express as px
import plotly.graph_objects as go
import pandas as pd


# ==========================================================
# Common Layout
# ==========================================================

def apply_layout(fig: go.Figure, title: str) -> go.Figure:
    """
    Apply a common theme to all Plotly charts.
    """

    fig.update_layout(
        title={
            "text": title,
            "x": 0.5,
            "font": {
                "size": 22,
                "color": "white"
            }
        },
        template="plotly_dark",
        paper_bgcolor="#0b1220",
        plot_bgcolor="#0b1220",
        font=dict(
            family="Poppins",
            color="white"
        ),
        margin=dict(
            l=30,
            r=30,
            t=60,
            b=30
        ),
        hovermode="x unified",
        height=450,
        showlegend=True
    )

    return fig


# ==========================================================
# Matches Per Season
# ==========================================================

def matches_per_season_chart(df: pd.DataFrame):

    fig = px.line(
        df,
        x="season",
        y="Matches",
        markers=True
    )

    fig.update_traces(
        line=dict(width=4),
        marker=dict(size=9)
    )

    return apply_layout(
        fig,
        "Matches Played Per Season"
    )


# ==========================================================
# Toss Decision
# ==========================================================

def toss_decision_chart(df: pd.DataFrame):

    fig = px.pie(
        df,
        names="Decision",
        values="Count",
        hole=0.55
    )

    return apply_layout(
        fig,
        "Toss Decision Distribution"
    )


# ==========================================================
# Match Result
# ==========================================================

def result_distribution_chart(df: pd.DataFrame):

    fig = px.pie(
        df,
        names="Result",
        values="Count",
        hole=0.45
    )

    return apply_layout(
        fig,
        "Match Result Distribution"
    )


# ==========================================================
# Top Venues
# ==========================================================

def top_venues_chart(df: pd.DataFrame):

    fig = px.bar(
        df,
        x="Matches",
        y="Venue",
        orientation="h",
        text="Matches"
    )

    fig.update_layout(yaxis=dict(categoryorder="total ascending"))

    return apply_layout(
        fig,
        "Top 10 IPL Venues"
    )


# ==========================================================
# Top Cities
# ==========================================================

def top_cities_chart(df: pd.DataFrame):

    fig = px.bar(
        df,
        x="Matches",
        y="City",
        orientation="h",
        text="Matches"
    )

    fig.update_layout(yaxis=dict(categoryorder="total ascending"))

    return apply_layout(
        fig,
        "Top IPL Cities"
    )


# ==========================================================
# Player of the Match
# ==========================================================

def player_of_match_chart(df: pd.DataFrame):

    fig = px.bar(
        df,
        x="Awards",
        y="Player",
        orientation="h",
        text="Awards"
    )

    fig.update_layout(yaxis=dict(categoryorder="total ascending"))

    return apply_layout(
        fig,
        "Most Player of the Match Awards"
    )