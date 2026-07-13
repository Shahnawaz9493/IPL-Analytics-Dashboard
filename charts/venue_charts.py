"""
venue_charts.py
---------------

Professional Plotly Charts for Venue Analysis.

Responsibilities
----------------
✔ Average Score
✔ Highest Score
✔ Lowest Score
✔ Best Batting Grounds
✔ Best Bowling Grounds

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
    Apply common dashboard theme.
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

        margin=dict(
            l=20,
            r=20,
            t=60,
            b=20,
        ),

        height=500,

    )

    return fig


# ==========================================================
# Average Score
# ==========================================================

def average_score_chart(
    df: pd.DataFrame,
):
    """
    Venue average scores.
    """

    top = df.nlargest(15, "Average")

    fig = px.bar(

        top,

        x="Average",

        y="venue",

        orientation="h",

        text="Average",

        color="Average",

        color_continuous_scale="Turbo",

    )

    fig.update_layout(

        yaxis=dict(

            categoryorder="total ascending"

        )

    )

    return apply_layout(
        fig,
        "Highest Average Scoring Venues",
    )


# ==========================================================
# Highest Score
# ==========================================================

def highest_score_chart(
    df: pd.DataFrame,
):
    """
    Highest innings score by venue.
    """

    top = df.nlargest(15, "Highest")

    fig = px.bar(

        top,

        x="Highest",

        y="venue",

        orientation="h",

        text="Highest",

        color="Highest",

        color_continuous_scale="Viridis",

    )

    fig.update_layout(

        yaxis=dict(

            categoryorder="total ascending"

        )

    )

    return apply_layout(
        fig,
        "Highest Scores by Venue",
    )


# ==========================================================
# Lowest Score
# ==========================================================

def lowest_score_chart(
    df: pd.DataFrame,
):
    """
    Lowest innings score by venue.
    """

    top = df.nsmallest(15, "Lowest")

    fig = px.bar(

        top,

        x="Lowest",

        y="venue",

        orientation="h",

        text="Lowest",

        color="Lowest",

        color_continuous_scale="Reds",

    )

    fig.update_layout(

        yaxis=dict(

            categoryorder="total ascending"

        )

    )

    return apply_layout(
        fig,
        "Lowest Scores by Venue",
    )


# ==========================================================
# Best Batting Grounds
# ==========================================================

def batting_ground_chart(
    df: pd.DataFrame,
):
    """
    Best batting grounds.
    """

    fig = px.bar(

        df,

        x="Batting Rating",

        y="venue",

        orientation="h",

        text="Batting Rating",

        color="Batting Rating",

        color_continuous_scale="Turbo",

    )

    fig.update_layout(

        yaxis=dict(

            categoryorder="total ascending"

        )

    )

    return apply_layout(
        fig,
        "Best Batting Grounds",
    )


# ==========================================================
# Best Bowling Grounds
# ==========================================================

def bowling_ground_chart(
    df: pd.DataFrame,
):
    """
    Best bowling grounds.
    """

    fig = px.bar(

        df,

        x="Bowling Rating",

        y="venue",

        orientation="h",

        text="Bowling Rating",

        color="Bowling Rating",

        color_continuous_scale="Blues",

    )

    fig.update_layout(

        yaxis=dict(

            categoryorder="total ascending"

        )

    )

    return apply_layout(
        fig,
        "Best Bowling Grounds",
    )
# ==========================================================
# First Innings Average
# ==========================================================

def first_innings_chart(
    df: pd.DataFrame,
):
    """
    First innings average score by venue.
    """

    fig = px.bar(

        df,

        x="FirstInningsAvg",

        y="venue",

        orientation="h",

        text="FirstInningsAvg",

        color="FirstInningsAvg",

        color_continuous_scale="Turbo",

    )

    fig.update_layout(

        yaxis=dict(

            categoryorder="total ascending"

        )

    )

    return apply_layout(
        fig,
        "Average First Innings Score",
    )


# ==========================================================
# Second Innings Average
# ==========================================================

def second_innings_chart(
    df: pd.DataFrame,
):
    """
    Second innings average score by venue.
    """

    fig = px.bar(

        df,

        x="SecondInningsAvg",

        y="venue",

        orientation="h",

        text="SecondInningsAvg",

        color="SecondInningsAvg",

        color_continuous_scale="Viridis",

    )

    fig.update_layout(

        yaxis=dict(

            categoryorder="total ascending"

        )

    )

    return apply_layout(
        fig,
        "Average Second Innings Score",
    )


# ==========================================================
# Chasing Success
# ==========================================================

def chasing_success_chart(
    df: pd.DataFrame,
):
    """
    Venue-wise chasing success.
    """

    top = df.nlargest(15, "Chase %")

    fig = px.bar(

        top,

        x="Chase %",

        y="venue",

        orientation="h",

        text="Chase %",

        color="Chase %",

        color_continuous_scale="Plasma",

    )

    fig.update_layout(

        yaxis=dict(

            categoryorder="total ascending"

        )

    )

    return apply_layout(
        fig,
        "Best Chasing Venues",
    )


# ==========================================================
# Toss Success
# ==========================================================

def toss_success_chart(
    df: pd.DataFrame,
):
    """
    Toss success percentage by venue.
    """

    top = df.nlargest(15, "Success %")

    fig = px.bar(

        top,

        x="Success %",

        y="venue",

        orientation="h",

        text="Success %",

        color="Success %",

        color_continuous_scale="Turbo",

    )

    fig.update_layout(

        yaxis=dict(

            categoryorder="total ascending"

        )

    )

    return apply_layout(
        fig,
        "Toss Success by Venue",
    )


# ==========================================================
# Venue Heatmap
# ==========================================================

def venue_heatmap(
    df: pd.DataFrame,
):
    """
    Heatmap of average scores.
    """

    fig = px.density_heatmap(

        df,

        x="Matches",

        y="venue",

        z="Average",

        color_continuous_scale="Turbo",

    )

    return apply_layout(
        fig,
        "Venue Score Heatmap",
    )


# ==========================================================
# Venue Scatter Plot
# ==========================================================

def venue_scatter(
    df: pd.DataFrame,
):
    """
    Venue performance scatter plot.
    """

    fig = px.scatter(

        df,

        x="Matches",

        y="Average",

        size="Highest",

        color="Average",

        hover_name="venue",

        color_continuous_scale="Turbo",

    )

    return apply_layout(
        fig,
        "Venue Performance",
    )


# ==========================================================
# Matches Played
# ==========================================================

def matches_chart(
    df: pd.DataFrame,
):
    """
    Matches hosted by venue.
    """

    top = df.nlargest(15, "Matches")

    fig = px.bar(

        top,

        x="Matches",

        y="venue",

        orientation="h",

        text="Matches",

        color="Matches",

        color_continuous_scale="Blues",

    )

    fig.update_layout(

        yaxis=dict(

            categoryorder="total ascending"

        )

    )

    return apply_layout(
        fig,
        "Matches Hosted by Venue",
    )


# ==========================================================
# KPI Gauge
# ==========================================================

def average_score_gauge(
    average_score: float,
):
    """
    Gauge chart for overall average score.
    """

    fig = go.Figure(

        go.Indicator(

            mode="gauge+number",

            value=average_score,

            title={

                "text": "Overall Average Score"

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
        "Average Venue Score",
    )


# ==========================================================
# Venue Distribution
# ==========================================================

def venue_distribution(
    df: pd.DataFrame,
):
    """
    Distribution of venue averages.
    """

    fig = px.box(

        df,

        y="Average",

        points="all",

    )

    return apply_layout(
        fig,
        "Venue Score Distribution",
    )