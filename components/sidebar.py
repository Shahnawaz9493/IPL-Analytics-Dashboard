"""
sidebar.py
----------

Reusable sidebar component for the IPL Dashboard.
"""

from __future__ import annotations

from pathlib import Path

import streamlit as st


BASE_DIR = Path(__file__).resolve().parent.parent
ASSETS_DIR = BASE_DIR / "assets"
LOGO_PATH = ASSETS_DIR / "ipl_logo.png"


def render_sidebar() -> None:
    """
    Render the application sidebar.
    """

    with st.sidebar:

        # --------------------------------------------------
        # Logo
        # --------------------------------------------------

        if LOGO_PATH.exists():
            st.image(str(LOGO_PATH), use_container_width=True)

        # --------------------------------------------------
        # Title
        # --------------------------------------------------

        st.title("🏏 IPL Dashboard")

        st.markdown("---")

        st.markdown(
            """
            ### About

            Interactive IPL Data Analysis Dashboard

            **Dataset**

            - Matches
            - Ball-by-Ball Deliveries

            **Built Using**

            - Python
            - Streamlit
            - Pandas
            - Plotly
            """
        )

        st.markdown("---")

        st.success("Ready for Analysis 🚀")

        st.markdown("---")

        st.caption("IPL Data Analysis Dashboard")
        st.caption("Developed using Streamlit")