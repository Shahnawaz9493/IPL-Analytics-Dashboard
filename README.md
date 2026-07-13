<div align="center">

# 🏏 IPL Cricket Data Analysis Dashboard

### An interactive, multi-page analytics dashboard exploring 15+ years of IPL data

[![Python](https://img.shields.io/badge/Python-3.9+-3776AB?style=for-the-badge&logo=python&logoColor=white)](https://www.python.org/)
[![Streamlit](https://img.shields.io/badge/Streamlit-FF4B4B?style=for-the-badge&logo=streamlit&logoColor=white)](https://ipl-analytics-dashboard-zb9xbmxaejewwxw3xptwm9.streamlit.app/)
[![Pandas](https://img.shields.io/badge/Pandas-150458?style=for-the-badge&logo=pandas&logoColor=white)](https://pandas.pydata.org/)
[![Plotly](https://img.shields.io/badge/Plotly-3F4F75?style=for-the-badge&logo=plotly&logoColor=white)](https://plotly.com/)
[![License](https://img.shields.io/badge/License-MIT-green?style=for-the-badge)](LICENSE)
[![Live Demo](https://img.shields.io/badge/🚀_Live_Demo-Click_Here-brightgreen?style=for-the-badge)](https://ipl-analytics-dashboard-zb9xbmxaejewwxw3xptwm9.streamlit.app/)

[**🔗 View Live Demo**](https://ipl-analytics-dashboard-zb9xbmxaejewwxw3xptwm9.streamlit.app/) · [Report Bug](#) · [Request Feature](#)

</div>

---

## 📖 Table of Contents

- [Overview](#-overview)
- [Features](#-features)
- [Tech Stack](#-tech-stack)
- [Project Structure](#-project-structure)
- [Installation](#-installation)
- [Usage](#-usage)
- [Dashboard Pages](#-dashboard-pages)
- [Data](#-data)
- [Architecture](#-architecture)
- [Key Learnings](#-key-learnings)
- [Roadmap](#-roadmap)
- [Contributing](#-contributing)
- [License](#-license)
- [Contact](#-contact)

---

## 🎯 Overview

The **IPL Cricket Data Analysis Dashboard** is a full-featured, production-structured Streamlit application built to explore and visualize Indian Premier League (IPL) data across seasons, teams, and players. It goes beyond a single-page chart dump — the app is organized into **eight dedicated analysis pages**, each backed by its own analysis and charting modules, with a clean dark-themed UI.

The goal of this project was to practice building a **real-world, layered data application** — the kind of structure you'd find in production data products — rather than a single monolithic script.

> 💡 This project uses synthetic data generated to match the schema of the popular [IPL Kaggle dataset](https://www.kaggle.com/datasets), so it can run fully offline without any external data dependency.

---

## 🌐 Live Demo

**👉 [ipl-analytics-dashboard-zb9xbmxaejewwxw3xptwm9.streamlit.app](https://ipl-analytics-dashboard-zb9xbmxaejewwxw3xptwm9.streamlit.app/)**

Hosted for free on **Streamlit Community Cloud** — no installation needed, just open the link and explore.

> ⏳ Note: Streamlit Community Cloud apps sleep after periods of inactivity. If the dashboard shows a "waking up" screen, give it 30–60 seconds to spin back up.

---

## ✨ Features

- 🏠 **Overview Dashboard** — league-wide KPIs, season trends, and quick stat cards
- 🏏 **Batsmen Analysis** — run distributions, strike rates, boundary %, most consistent scorers
- 🎯 **Bowlers Analysis** — wickets, economy, bowling averages, death-over specialists
- 👑 **Captain Analysis** — win % by captain, toss decisions, captaincy impact on outcomes
- 🪙 **Toss Analysis** — toss-decision trends and their correlation with match results
- 🏟️ **Venue Analysis** — ground-wise scoring patterns, chasing vs. defending success rates
- ⚔️ **Team Analysis** — head-to-head records, season standings, points table trends
- 🧑‍🤝‍🧑 **Player Comparison** — side-by-side player stat comparison across seasons
- 🌗 **Dark-themed custom UI** — consistent, polished visual language across all pages
- ⚡ **Modular, cached data pipeline** for fast page loads even with large datasets

---

## 🛠️ Tech Stack

| Category | Technology |
|---|---|
| **Framework** | Streamlit (multi-page app) |
| **Language** | Python 3.9+ |
| **Data Processing** | Pandas, NumPy |
| **Visualization** | Plotly (interactive charts), Plotly Express |
| **Styling** | Custom CSS injection (dark theme), `st.markdown` unsafe HTML components |
| **Caching** | `st.cache_data` / `st.cache_resource` for fast page loads |
| **Deployment** | Streamlit Community Cloud |
| **Version Control** | Git & GitHub |
| **Dev Tooling** | Black (formatting), Flake8 (linting), pytest (testing) |
| **Environment** | `venv` / `requirements.txt` for reproducible installs |

> 🔧 Swap out any dev-tooling row above to match what you actually use — e.g. if you're using `ruff` instead of Flake8, or `poetry` instead of `venv`, just say so and I'll update it.

---

## 📁 Project Structure

```
ipl-cricket-dashboard/
│
├── app.py                          # Main entry point
├── requirements.txt
├── README.md
│
├── pages/                          # Streamlit multi-page app pages
│   ├── 1_🏠_Overview.py
│   ├── 2_🏏_Batsmen.py
│   ├── 3_🎯_Bowlers.py
│   ├── 4_👑_Captain.py
│   ├── 5_🪙_Toss.py
│   ├── 6_🏟️_Venue.py
│   ├── 7_⚔️_Team.py
│   └── 8_🧑‍🤝‍🧑_Player_Comparison.py
│
├── utils/                          # Core utilities
│   ├── data_loader.py               # Loading & caching raw data
│   ├── data_cleaning.py             # Cleaning & preprocessing
│   └── calculations.py              # Shared statistical calculations
│
├── analysis/                       # Business-logic layer
│   ├── batsmen_analysis.py
│   ├── bowlers_analysis.py
│   ├── captain_analysis.py
│   ├── toss_analysis.py
│   ├── team_analysis.py
│   ├── venue_analysis.py
│   └── player_analysis.py
│
├── charts/                          # Plotly chart builders
│   ├── batting_charts.py
│   ├── bowling_charts.py
│   ├── team_charts.py
│   └── venue_charts.py
│
├── components/                     # Reusable UI components
│   ├── stat_card.py
│   ├── sidebar_filters.py
│   └── header.py
│
├── assets/
│   ├── style.css                    # Dark theme styling
│   └── screenshots/
│
└── data/
    └── ipl_synthetic_data.csv       # Kaggle-schema-matched synthetic dataset
```

---

## ⚙️ Installation

1. **Clone the repository**
   ```bash
   git clone https://github.com/<your-username>/ipl-cricket-dashboard.git
   cd ipl-cricket-dashboard
   ```

2. **Create a virtual environment** (recommended)
   ```bash
   python -m venv venv
   source venv/bin/activate      # On Windows: venv\Scripts\activate
   ```

3. **Install dependencies**
   ```bash
   pip install -r requirements.txt
   ```

4. **Run the app**
   ```bash
   streamlit run app.py
   ```

5. Open your browser at `http://localhost:8501` 🎉

---

## 🚀 Usage

> 🌐 Prefer not to install anything? Use the **[live hosted version](https://ipl-analytics-dashboard-zb9xbmxaejewwxw3xptwm9.streamlit.app/)** instead of running locally.

- Use the **sidebar filters** to slice data by season, team, or venue.
- Navigate between the **eight analysis pages** using the sidebar page selector.
- Hover over any Plotly chart for detailed tooltips.
- Use the **Player Comparison** page to benchmark two players head-to-head across multiple metrics.

---

## 🗂️ Dashboard Pages

| # | Page | What it Shows |
|---|------|----------------|
| 1 | **Overview** | League KPIs, season-wise run/wicket trends, top performers snapshot |
| 2 | **Batsmen** | Top run-scorers, strike rate vs. average, boundary breakdown |
| 3 | **Bowlers** | Top wicket-takers, economy trends, death-overs performance |
| 4 | **Captain** | Win percentage by captain, captaincy-decision impact |
| 5 | **Toss** | Toss decision trends and win correlation |
| 6 | **Venue** | Venue-wise average scores, chasing vs. defending win rates |
| 7 | **Team** | Head-to-head records, season standings |
| 8 | **Player Comparison** | Side-by-side stat comparison tool |

---

## 📊 Data

This project uses a **synthetic dataset engineered to mirror the schema** of the well-known IPL ball-by-ball and match-summary datasets on Kaggle — including fields like `match_id`, `season`, `batting_team`, `bowling_team`, `batsman`, `bowler`, `runs`, `wicket_type`, `venue`, and `toss_decision`.

This design choice means:
- ✅ The app runs fully offline, with no external data downloads required
- ✅ It's easy to swap in the real Kaggle dataset by matching the same column schema
- ✅ Contributors can test the full pipeline without needing dataset access

---

## 🏗️ Architecture

The app follows a **layered architecture** to separate concerns and keep the codebase maintainable:

```
UI Layer (pages/)
      │
      ▼
Chart Layer (charts/)  ──uses──▶  Analysis Layer (analysis/)
                                          │
                                          ▼
                                  Utils Layer (utils/)
                                          │
                                          ▼
                                   Raw Data (data/)
```

- **Utils** handle raw data loading, cleaning, and shared calculations
- **Analysis modules** transform cleaned data into page-specific insights (e.g., batsmen stats, toss trends)
- **Chart modules** turn analysis outputs into Plotly figures
- **Pages** compose components, charts, and filters into the final UI

This separation made it much easier to debug and extend individual pages without breaking others.

---

## 💡 Key Learnings

- Designing a **multi-layer Streamlit app** (rather than a single script) to keep logic testable and reusable
- Handling a **pandas version compatibility issue**: newer pandas versions changed how `value_counts().reset_index()` names output columns. Fixed by standardizing on the `.rename_axis().reset_index(name=...)` pattern across all analysis modules for consistent, version-proof column naming
- Building **synthetic data generators** that faithfully match a real-world dataset schema for offline development and testing
- Structuring a **dark-themed custom CSS layer** for a consistent, professional look across every Streamlit page

---

## 🗺️ Roadmap

- [ ] Add live data refresh from a real IPL API
- [ ] Add player career trend charts across multiple seasons
- [ ] Add ball-by-ball match replay visualization
- [ ] Deploy to Streamlit Community Cloud
- [ ] Add unit tests for analysis modules

---

## 🤝 Contributing

Contributions are welcome! Feel free to open an issue or submit a pull request.

1. Fork the project
2. Create your feature branch (`git checkout -b feature/AmazingFeature`)
3. Commit your changes (`git commit -m 'Add some AmazingFeature'`)
4. Push to the branch (`git push origin feature/AmazingFeature`)
5. Open a Pull Request

---

## 📬 Contact

**Mohammad Shahnawaz**

- GitHub: [@Shahnawaz9493](https://github.com/Shahnawaz9493)
- LinkedIn: [Mohammad Shahnawaz](https://www.linkedin.com/in/mohammad-shahnawaz-22981121a?utm_source=share_via&utm_content=profile&utm_medium=member_android)

---

<div align="center">

⭐ If you found this project useful, consider giving it a star!

</div>
