"""
cards.py
--------

Reusable KPI Cards for the IPL Dashboard.
"""

from __future__ import annotations

import streamlit as st


def format_number(value: int | float) -> str:
    """
    Format large numbers.

    Examples
    --------
    1500 -> 1.5K
    1500000 -> 1.5M
    """

    if value >= 1_000_000:
        return f"{value/1_000_000:.1f}M"

    if value >= 1_000:
        return f"{value/1_000:.1f}K"

    return str(value)


def metric_card(title: str, value: int | float, icon: str):
    """
    Display a single KPI card.
    """

    st.markdown(
        f"""
        <div class="metric-card">

<div class="metric-icon">{icon}</div>

<div class="metric-value">{format_number(value)}</div>

<div class="metric-title">{title}</div>

</div>
        """,
        unsafe_allow_html=True,
    )


def display_dashboard_cards(kpis: dict):
    """
    Display dashboard KPI cards in two rows.
    """

    icons = {
        "Total Seasons": "📅",
        "Total Matches": "🏏",
        "Total Teams": "👥",
        "Total Players": "🧑‍🤝‍🧑",
        "Total Runs": "🏃",
        "Total Wickets": "🎯",
        "Total Sixes": "💥",
        "Total Fours": "⚡",
    }

    keys = list(kpis.keys())

    # ---------------- Row 1 ----------------

    cols = st.columns(4)

    for col, key in zip(cols, keys[:4]):
        with col:
            metric_card(
                key,
                kpis[key],
                icons[key]
            )

    st.write("")

    # ---------------- Row 2 ----------------

    cols = st.columns(4)

    for col, key in zip(cols, keys[4:]):
        with col:
            metric_card(
                key,
                kpis[key],
                icons[key]
            )