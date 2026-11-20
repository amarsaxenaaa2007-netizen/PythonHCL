# IPL Match Analysis System

## Overview

The IPL Match Analysis System is a terminal-based Python project that
analyzes IPL match data from a CSV file. It provides a menu-driven
interface to explore match, team, toss, player, venue, season, and
head-to-head statistics.

## Objective

-   Explore and summarize IPL match data.
-   Compare team performance using wins and win percentages.
-   Analyze toss decisions and the relationship between toss winners and
    match winners.
-   Identify leading players by Player of the Match awards.
-   Explore venue, city, and season-level statistics.
-   Provide an easy-to-use, terminal-only analysis tool.

## Technology Used

-   **Python** --- programming language
-   **Pandas** --- data loading and data analysis
-   **CSV** --- dataset format
-   **Terminal / Command Prompt / Git Bash** --- program interface

## Dataset

-   **File:** `matches.csv`
-   **Format:** CSV (comma-separated values)
-   **Content:** Match-level IPL records, including columns such as
    season, teams, city, venue, toss information, winner, and Player of
    the Match (depending on the dataset's available fields).

The program expects `matches.csv` to be in the same folder as
`ipl_analysis.py`.

## Features

1.  Overall match overview (total matches, seasons, cities, venues).
2.  Team analysis (matches played, wins, and win percentage).
3.  Toss analysis (toss decisions, toss winners, and toss winner/match
    winner comparison).
4.  Player analysis (top Player of the Match awards).
5.  Venue analysis (most-used venues and city-wise match counts).
6.  Season analysis (match count and team with the most wins in each
    season).
7.  Head-to-head analysis between two teams.
8.  Search team details and season-wise performance.

## How to Run

### 1. Requirements

Install Python 3 and ensure it is available in your terminal.

### 2. Place the files together

Keep these two files in the same directory:

``` text
IPL_Analysis/
├── ipl_analysis.py
└── matches.csv
```

### 3. Install Pandas

Run this command in the terminal:

``` bash
python -m pip install pandas
```

### 4. Start the program

Navigate to the project folder and run:

``` bash
python ipl_analysis.py
```

### 5. Use the menu

Choose an option from the displayed menu by entering its number, then
follow the prompts. Enter `9` to exit.

## Limitations

This is match-level analysis. It does not contain ball-by-ball data, so
it does not calculate player batting strike rates, bowling economy
rates, or ball-by-ball scoring patterns.

## Your Name

**Amar CSE 02**
