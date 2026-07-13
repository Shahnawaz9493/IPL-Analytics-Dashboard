"""
team_charts.py
--------------

Professional Plotly Charts for Team Comparison.

Responsibilities
----------------
✔ Head-to-Head Wins
✔ Win Percentage
✔ Toss Wins
✔ Average Score
✔ Highest Score

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
    Apply a common dashboard theme.
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
            b=20,
        ),

    )

    return fig


# ==========================================================
# Head-to-Head Wins
# ==========================================================

def head_to_head_chart(
    summary: dict,
    team1: str,
    team2: str,
):

    df = pd.DataFrame({

        "Team": [
            team1,
            team2,
        ],

        "Wins": [
            summary[team1],
            summary[team2],
        ],

    })

    fig = px.bar(

        df,

        x="Team",

        y="Wins",

        text="Wins",

        color="Wins",

        color_continuous_scale="Turbo",

    )

    return apply_layout(
        fig,
        "Head-to-Head Wins",
    )


# ==========================================================
# Win Percentage
# ==========================================================

def win_percentage_chart(
    df: pd.DataFrame,
):

    fig = px.pie(

        df,

        names="Team",

        values="Win %",

        hole=0.60,

        color="Team",

        color_discrete_sequence=px.colors.qualitative.Bold,

    )

    return apply_layout(
        fig,
        "Win Percentage",
    )


# ==========================================================
# Toss Wins
# ==========================================================

def toss_comparison_chart(
    df: pd.DataFrame,
):

    fig = px.bar(

        df,

        x="toss_winner",

        y="Toss Wins",

        color="Toss Wins",

        text="Toss Wins",

        color_continuous_scale="Viridis",

    )

    return apply_layout(
        fig,
        "Toss Wins",
    )


# ==========================================================
# Average Score
# ==========================================================

def average_score_chart(
    df: pd.DataFrame,
):

    fig = px.bar(

        df,

        x="batting_team",

        y="Average",

        color="Average",

        text="Average",

        color_continuous_scale="Blues",

    )

    return apply_layout(
        fig,
        "Average Score",
    )


# ==========================================================
# Highest Score
# ==========================================================

def highest_score_chart(
    df: pd.DataFrame,
):

    fig = px.bar(

        df,

        x="batting_team",

        y="Highest",

        text="Highest",

        color="Highest",

        color_continuous_scale="Turbo",

    )

    return apply_layout(
        fig,
        "Highest Team Score",
    )
# ==========================================================
# Lowest Score
# ==========================================================

def lowest_score_chart(
    df: pd.DataFrame,
):
    """
    Lowest score comparison.
    """

    fig = px.bar(

        df,

        x="batting_team",

        y="Lowest",

        text="Lowest",

        color="Lowest",

        color_continuous_scale="Reds",

    )

    return apply_layout(
        fig,
        "Lowest Team Score",
    )


# ==========================================================
# Powerplay Comparison
# ==========================================================

def powerplay_chart(
    df: pd.DataFrame,
):
    """
    Average powerplay score comparison.
    """

    fig = px.bar(

        df,

        x="batting_team",

        y="AveragePowerplay",

        text="AveragePowerplay",

        color="AveragePowerplay",

        color_continuous_scale="Teal",

    )

    return apply_layout(
        fig,
        "Average Powerplay Score",
    )


# ==========================================================
# Death Overs Comparison
# ==========================================================

def death_over_chart(
    df: pd.DataFrame,
):
    """
    Average death over score comparison.
    """

    fig = px.bar(

        df,

        x="batting_team",

        y="AverageDeath",

        text="AverageDeath",

        color="AverageDeath",

        color_continuous_scale="Sunset",

    )

    return apply_layout(
        fig,
        "Average Death Overs Score",
    )


# ==========================================================
# Home vs Away Wins
# ==========================================================

def home_away_chart(
    df: pd.DataFrame,
):
    """
    Home vs Away wins comparison.
    """

    chart_df = df.melt(

        id_vars="Team",

        value_vars=["Home Wins", "Away Wins"],

        var_name="Category",

        value_name="Wins",

    )

    fig = px.bar(

        chart_df,

        x="Team",

        y="Wins",

        color="Category",

        barmode="group",

        text="Wins",

        color_discrete_sequence=px.colors.qualitative.Set2,

    )

    return apply_layout(
        fig,
        "Home vs Away Wins",
    )


# ==========================================================
# Venue Comparison
# ==========================================================

def venue_chart(
    df: pd.DataFrame,
):
    """
    Venue-wise wins.
    """

    fig = px.bar(

        df,

        x="venue",

        y="Wins",

        color="winner",

        barmode="group",

    )

    fig.update_xaxes(
        tickangle=-45
    )

    return apply_layout(
        fig,
        "Venue-wise Comparison",
    )


# ==========================================================
# Radar Comparison
# ==========================================================

def radar_chart(
    comparison_df: pd.DataFrame,
):
    """
    Radar comparison of teams.
    """

    fig = go.Figure()

    metrics = [
        "Average",
        "Highest",
        "Lowest",
        "AveragePowerplay",
        "AverageDeath",
    ]

    for _, row in comparison_df.iterrows():

        fig.add_trace(

            go.Scatterpolar(

                r=[
                    row["Average"],
                    row["Highest"],
                    row["Lowest"],
                    row["AveragePowerplay"],
                    row["AverageDeath"],
                ],

                theta=metrics,

                fill="toself",

                name=row["Team"],

            )

        )

    return apply_layout(
        fig,
        "Team Performance Radar",
    )


# ==========================================================
# Score Distribution
# ==========================================================

def score_distribution_chart(
    scores_df: pd.DataFrame,
):
    """
    Distribution of team scores.
    """

    fig = px.box(

        scores_df,

        x="batting_team",

        y="Score",

        color="batting_team",

        points="all",

    )

    return apply_layout(
        fig,
        "Score Distribution",
    )


# ==========================================================
# Timeline Chart
# ==========================================================

def timeline_chart(
    df: pd.DataFrame,
):
    """
    Match results across seasons.
    """

    timeline = (

        df

        .groupby(
            [
                "season",
                "winner",
            ]
        )

        .size()

        .reset_index(name="Wins")

    )

    fig = px.line(

        timeline,

        x="season",

        y="Wins",

        color="winner",

        markers=True,

    )

    return apply_layout(
        fig,
        "Head-to-Head Timeline",
    )


# ==========================================================
# KPI Gauge
# ==========================================================

def win_percentage_gauge(
    percentage: float,
):
    """
    Displays win percentage gauge.
    """

    fig = go.Figure(

        go.Indicator(

            mode="gauge+number",

            value=percentage,

            title={

                "text": "Winning Percentage"

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
        "Winning Percentage",
    )