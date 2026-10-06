"""
Descriptive statistics: number of active issuers on January 1st, 1840-1940.

An issuer counts as active on a date if issuer_from <= date <= issuer_until.

Note on placeholder dates: issuer_from = 1000-01-01 and issuer_until = 3999-12-31
mean "unknown start" and "no known end". We treat them as open-ended, i.e. we use
the dates as they are.

Run with:
    source .venv/bin/activate
    python 05_stats_josef.py
"""

from pathlib import Path

import matplotlib.pyplot as plt
import pandas as pd

DATA_FILE = Path("data/iss.csv")
OUTPUT_DIR = Path("output")
FIRST_YEAR = 1840
LAST_YEAR = 1940


def count_active(df, ref_date):
    """Count issuers whose time span includes ref_date (an ISO 'YYYY-MM-DD' string)."""
    return int(((df["issuer_from"] <= ref_date) & (ref_date <= df["issuer_until"])).sum())


# --- Load ---------------------------------------------------------------------
# The dates are read as plain text on purpose: pandas' datetime type cannot hold
# years like 1000 or 3999. ISO dates (YYYY-MM-DD) sort and compare correctly as text.
issuers = pd.read_csv(DATA_FILE, sep=";", dtype={"issuer_from": str, "issuer_until": str})
n_loaded = len(issuers)

# Drop issuers without a known time span
issuers = issuers.dropna(subset=["issuer_from", "issuer_until"])
n_dropped = n_loaded - len(issuers)

# Sanity check: every remaining date must be a zero-padded ISO date
iso_date = r"^\d{4}-\d{2}-\d{2}$"
for column in ["issuer_from", "issuer_until"]:
    assert issuers[column].str.match(iso_date).all(), f"Unexpected date format in {column}"

# --- Count --------------------------------------------------------------------
years = range(FIRST_YEAR, LAST_YEAR + 1)
stats = pd.DataFrame({
    "year": list(years),
    "active_issuers": [count_active(issuers, f"{year}-01-01") for year in years],
})

# --- Save ---------------------------------------------------------------------
OUTPUT_DIR.mkdir(exist_ok=True)
csv_path = OUTPUT_DIR / "active_issuers_per_year.csv"
stats.to_csv(csv_path, index=False)

fig, ax = plt.subplots(figsize=(9, 4.5), facecolor="#fcfcfb")
ax.set_facecolor("#fcfcfb")
ax.plot(stats["year"], stats["active_issuers"], color="#2a78d6", linewidth=2,
        solid_joinstyle="round", solid_capstyle="round")
last = stats.iloc[-1]
ax.annotate(f"{last['active_issuers']:,}", (last["year"], last["active_issuers"]),
            xytext=(6, 0), textcoords="offset points", va="center", color="#0b0b0b")
ax.set_title(f"Active issuers on 1 January, {FIRST_YEAR}–{LAST_YEAR}",
             loc="left", color="#0b0b0b")
ax.set_ylim(bottom=0)
ax.yaxis.set_major_formatter(lambda value, _: f"{value:,.0f}")
ax.grid(axis="y", color="#e4e3df", linewidth=1)
ax.tick_params(colors="#52514e", length=0)
for side in ["top", "right", "left"]:
    ax.spines[side].set_visible(False)
ax.spines["bottom"].set_color("#c3c2b7")
fig.tight_layout()
png_path = OUTPUT_DIR / "active_issuers_per_year.png"
fig.savefig(png_path, dpi=150)

# --- Summary ------------------------------------------------------------------
lowest = stats.loc[stats["active_issuers"].idxmin()]
highest = stats.loc[stats["active_issuers"].idxmax()]
print(f"Loaded {n_loaded} issuers, dropped {n_dropped} without dates.")
print(f"Fewest active: {lowest['active_issuers']} in {lowest['year']}")
print(f"Most active:   {highest['active_issuers']} in {highest['year']}")
print(f"Saved {csv_path} and {png_path}")
