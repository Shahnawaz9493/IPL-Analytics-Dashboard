"""
bowlers_charts.py
-----------------

Professional Plotly charts for the Bowlers Dashboard.

Responsibilities
----------------
✔ Top Wicket Takers
✔ Best Economy
✔ Best Bowling Average
✔ Best Strike Rate
✔ Dot Balls
✔ Dot Ball %
✔ 4W Hauls
✔ 5W Hauls
✔ Scatter Plot

No Streamlit code.
"""

from __future__ import annotations

import pandas as pd
import plotly.express as px
import plotly.graph_objects as go


# ==========================================================
# Common Layout
# ==========================================================

def apply_layout(fig: go.Figure, title: str) -> go.Figure:

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
# Top Wickets
# ==========================================================

def wickets_chart(df: pd.DataFrame):

    fig = px.bar(

        df,

        x="Wickets",

        y="bowler",

        orientation="h",

        text="Wickets",

        color="Wickets",

        color_continuous_scale="Turbo"

    )

    fig.update_layout(

        yaxis=dict(
            categoryorder="total ascending"
        )

    )

    return apply_layout(
        fig,
        "Top Wicket Takers"
    )


# ==========================================================
# Economy
# ==========================================================

def economy_chart(df: pd.DataFrame):

    fig = px.bar(

        df,

        x="Economy",

        y="bowler",

        orientation="h",

        text="Economy",

        color="Economy",

        color_continuous_scale="Viridis_r"

    )

    fig.update_layout(
        yaxis=dict(
            categoryorder="total descending"
        )
    )

    return apply_layout(
        fig,
        "Best Economy"
    )


# ==========================================================
# Bowling Average
# ==========================================================

def average_chart(df: pd.DataFrame):

    fig = px.bar(

        df,

        x="Average",

        y="bowler",

        orientation="h",

        text="Average",

        color="Average",

        color_continuous_scale="Plasma_r"

    )

    fig.update_layout(
        yaxis=dict(
            categoryorder="total descending"
        )
    )

    return apply_layout(
        fig,
        "Best Bowling Average"
    )


# ==========================================================
# Strike Rate
# ==========================================================

def strike_rate_chart(df: pd.DataFrame):

    fig = px.bar(

        df,

        x="Strike Rate",

        y="bowler",

        orientation="h",

        text="Strike Rate",

        color="Strike Rate",

        color_continuous_scale="Magma_r"

    )

    fig.update_layout(
        yaxis=dict(
            categoryorder="total descending"
        )
    )

    return apply_layout(
        fig,
        "Best Bowling Strike Rate"
    )


# ==========================================================
# Dot Balls
# ==========================================================

def dot_ball_chart(df: pd.DataFrame):

    fig = px.bar(

        df,

        x="DotBalls",

        y="bowler",

        orientation="h",

        text="DotBalls",

        color="DotBalls",

        color_continuous_scale="Blues"

    )

    fig.update_layout(
        yaxis=dict(
            categoryorder="total ascending"
        )
    )

    return apply_layout(
        fig,
        "Most Dot Balls"
    )


# ==========================================================
# Dot Ball %
# ==========================================================

def dot_percentage_chart(df: pd.DataFrame):

    fig = px.bar(

        df,

        x="Dot Ball %",

        y="bowler",

        orientation="h",

        text="Dot Ball %",

        color="Dot Ball %",

        color_continuous_scale="Aggrnyl"

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
# Four Wicket Hauls
# ==========================================================

def four_wicket_chart(df: pd.DataFrame):

    fig = px.bar(

        df,

        x="4W",

        y="bowler",

        orientation="h",

        text="4W",

        color="4W",

        color_continuous_scale="Inferno"

    )

    fig.update_layout(
        yaxis=dict(
            categoryorder="total ascending"
        )
    )

    return apply_layout(
        fig,
        "Four Wicket Hauls"
    )


# ==========================================================
# Five Wicket Hauls
# ==========================================================

def five_wicket_chart(df: pd.DataFrame):

    fig = px.bar(

        df,

        x="5W",

        y="bowler",

        orientation="h",

        text="5W",

        color="5W",

        color_continuous_scale="OrRd"

    )

    fig.update_layout(
        yaxis=dict(
            categoryorder="total ascending"
        )
    )

    return apply_layout(
        fig,
        "Five Wicket Hauls"
    )


# ==========================================================
# Scatter Plot
# ==========================================================

def bowling_scatter(df: pd.DataFrame):

    fig = px.scatter(

        df,

        x="Economy",

        y="Strike Rate",

        size="Wickets",

        color="Wickets",

        hover_name="bowler",

        color_continuous_scale="Turbo"

    )

    return apply_layout(
        fig,
        "Economy vs Strike Rate"
    )


# ==========================================================
# Pie Chart
# ==========================================================

def wicket_share_chart(df: pd.DataFrame):

    top10 = df.nlargest(10, "Wickets")

    fig = px.pie(

        top10,

        names="bowler",

        values="Wickets",

        hole=0.55,

        color_discrete_sequence=px.colors.qualitative.Bold

    )

    return apply_layout(
        fig,
        "Top 10 Wicket Share"
    )