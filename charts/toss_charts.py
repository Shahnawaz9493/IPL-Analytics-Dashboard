"""
charts/toss_charts.py
---------------------

Professional Plotly Charts for Toss Analysis

No Streamlit
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

    fig.update_layout(

        title=dict(
            text=title,
            x=0.5,
            font=dict(
                size=22,
                color="white",
            ),
        ),

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

        legend=dict(
            orientation="h",
            y=1.05,
            x=0.5,
            xanchor="center",
        )

    )

    return fig
# ==========================================================
# Toss Decision Distribution
# ==========================================================

def toss_decision_chart(
    df: pd.DataFrame,
):

    fig = px.pie(

        df,

        names="Decision",

        values="Count",

        hole=0.60,

        color="Decision",

        color_discrete_sequence=px.colors.qualitative.Set2,

    )

    return apply_layout(
        fig,
        "Toss Decision Distribution",
    )
# ==========================================================
# Toss Winner vs Match Winner
# ==========================================================

def toss_result_chart(
    df: pd.DataFrame,
):

    fig = px.pie(

        df,

        names="Outcome",

        values="Count",

        hole=0.55,

        color="Outcome",

        color_discrete_sequence=px.colors.qualitative.Bold,

    )

    return apply_layout(
        fig,
        "Toss Winner vs Match Winner",
    )
# ==========================================================
# Toss Wins by Team
# ==========================================================

def toss_team_chart(
    df: pd.DataFrame,
):

    fig = px.bar(

        df,

        x="Toss Wins",

        y="Team",

        orientation="h",

        color="Toss Wins",

        text="Toss Wins",

        color_continuous_scale="Turbo",

    )

    fig.update_layout(

        yaxis=dict(

            categoryorder="total ascending"

        )

    )

    return apply_layout(
        fig,
        "Most Toss Wins",
    )
# ==========================================================
# Toss Success %
# ==========================================================

def toss_success_chart(
    df: pd.DataFrame,
):

    fig = px.bar(

        df,

        x="Win %",

        y="toss_winner",

        orientation="h",

        color="Win %",

        text="Win %",

        color_continuous_scale="Viridis",

    )

    fig.update_layout(

        yaxis=dict(

            categoryorder="total ascending"

        )

    )

    return apply_layout(
        fig,
        "Toss Success Percentage",
    )
# ==========================================================
# Venue Toss Success
# ==========================================================

def venue_success_chart(
    df: pd.DataFrame,
):

    fig = px.bar(

        df,

        x="Success %",

        y="venue",

        orientation="h",

        color="Success %",

        text="Success %",

        color_continuous_scale="Plasma",

    )

    fig.update_layout(

        yaxis=dict(

            categoryorder="total ascending"

        )

    )

    return apply_layout(
        fig,
        "Venue Toss Success",
    )
# ==========================================================
# Season Trend
# ==========================================================

def season_trend_chart(
    df: pd.DataFrame,
):

    fig = px.line(

        df,

        x="season",

        y="Matches",

        color="toss_decision",

        markers=True,

    )

    return apply_layout(
        fig,
        "Season-wise Toss Trend",
    )
# ==========================================================
# Toss Decision Heatmap
# ==========================================================

def toss_heatmap(
    df: pd.DataFrame,
):

    pivot = (

        df

        .pivot_table(

            index="toss_winner",

            columns="toss_decision",

            values="Matches",

            aggfunc="sum",

            fill_value=0,

        )

    )

    fig = px.imshow(

        pivot,

        text_auto=True,

        aspect="auto",

        color_continuous_scale="Turbo",

    )

    return apply_layout(
        fig,
        "Toss Decision Heatmap",
    )
# ==========================================================
# Toss Win Gauge
# ==========================================================

def toss_gauge(
    percentage: float,
):

    fig = go.Figure(

        go.Indicator(

            mode="gauge+number",

            value=percentage,

            number={"suffix": "%"},

            title={

                "text": "Toss Win Conversion"

            },

            gauge={

                "axis": {

                    "range": [0, 100]

                },

                "bar": {

                    "color": "#00CC96"

                },

            },

        )

    )

    return apply_layout(
        fig,
        "Toss Conversion",
    )