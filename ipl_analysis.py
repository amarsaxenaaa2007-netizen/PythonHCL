
import pandas as pd

# Load IPL dataset
df = pd.read_csv("matches.csv")

def total_analysis():
    print("\n===== IPL MATCH OVERVIEW =====")
    print("Total Matches:", len(df))
    print("Total Seasons:", df["season"].nunique())
    print("Total Cities:", df["city"].nunique())
    print("Total Venues:", df["venue"].nunique())

def team_analysis():
    print("\n===== TEAM ANALYSIS =====")

    wins = df["winner"].value_counts()
    matches_played = pd.concat(
        [df["team1"], df["team2"]]
    ).value_counts()

    for team in wins.index:
        played = matches_played.get(team, 0)
        won = wins.get(team, 0)
        win_percent = (won / played * 100) if played else 0

        print(f"\nTeam: {team}")
        print("Matches Played:", played)
        print("Matches Won:", won)
        print("Win Percentage:", round(win_percent, 2), "%")

    print("\n===== MOST SUCCESSFUL TEAMS =====")
    print(wins.head(10))

def toss_analysis():
    print("\n===== TOSS ANALYSIS =====")

    print("\nToss Decisions:")
    print(df["toss_decision"].value_counts())

    print("\nToss Winners:")
    print(df["toss_winner"].value_counts().head(10))

    toss_match_wins = df[
        df["toss_winner"] == df["winner"]
    ]

    valid_matches = df.dropna(subset=["winner", "toss_winner"])

    print("\nMatches where toss winner also won match:",
          len(toss_match_wins))

    if len(valid_matches) > 0:
        percentage = (
            len(toss_match_wins) / len(valid_matches) * 100
        )
        print("Percentage:",
              round(percentage, 2), "%")

def player_analysis():
    print("\n===== PLAYER ANALYSIS =====")

    print("\nTop Player of the Match Awards:")
    print(df["player_of_match"].value_counts().head(10))

def venue_analysis():
    print("\n===== VENUE ANALYSIS =====")

    print("\nMost Used Venues:")
    print(df["venue"].value_counts().head(10))

    print("\nCity-wise Matches:")
    print(df["city"].value_counts().head(10))

def season_analysis():
    print("\n===== SEASON ANALYSIS =====")

    for season in sorted(df["season"].dropna().unique()):
        season_data = df[df["season"] == season]

        winners = season_data["winner"].dropna()

        print(f"\nSeason: {season}")

        if len(winners) > 0:
            print("Most Match Wins:",
                  winners.value_counts().idxmax())

        print("Matches:", len(season_data))

def head_to_head():
    print("\n===== HEAD TO HEAD =====")

    teams = sorted(
        set(df["team1"].dropna()) |
        set(df["team2"].dropna())
    )

    print("\nAvailable Teams:")
    for team in teams:
        print("-", team)

    team_a = input("\nEnter first team: ").strip()
    team_b = input("Enter second team: ").strip()

    matches = df[
        ((df["team1"] == team_a) & (df["team2"] == team_b)) |
        ((df["team1"] == team_b) & (df["team2"] == team_a))
    ]

    print("\nTotal Head-to-Head Matches:", len(matches))

    if len(matches) == 0:
        print("No matches found.")
        return

    print("\nResults:")
    print(matches["winner"].value_counts())

    print("\nNo Result Matches:",
          matches["winner"].isna().sum())

def search_team():
    print("\n===== TEAM DETAILS =====")
    team = input("Enter team name: ").strip()

    matches = df[
        (df["team1"] == team) |
        (df["team2"] == team)
    ]

    wins = matches[matches["winner"] == team]

    print("\nTeam:", team)
    print("Matches Played:", len(matches))
    print("Matches Won:", len(wins))
    print("Matches Lost:",
          len(matches[matches["winner"].notna()]) - len(wins))

    print("\nSeason-wise Matches:")
    print(matches.groupby("season").size())

    print("\nSeason-wise Wins:")
    print(wins.groupby("season").size())

def main():
    while True:
        print("\n" + "=" * 45)
        print("       IPL MATCH ANALYSIS SYSTEM")
        print("=" * 45)

        print("1. Overall Match Analysis")
        print("2. Team Analysis")
        print("3. Toss Analysis")
        print("4. Player Analysis")
        print("5. Venue Analysis")
        print("6. Season Analysis")
        print("7. Head-to-Head Analysis")
        print("8. Search Team Details")
        print("9. Exit")

        choice = input("\nEnter your choice (1-9): ")

        if choice == "1":
            total_analysis()

        elif choice == "2":
            team_analysis()

        elif choice == "3":
            toss_analysis()

        elif choice == "4":
            player_analysis()

        elif choice == "5":
            venue_analysis()

        elif choice == "6":
            season_analysis()

        elif choice == "7":
            head_to_head()

        elif choice == "8":
            search_team()

        elif choice == "9":
            print("\nThank you for using IPL Analysis!")
            break

        else:
            print("\nInvalid choice! Please try again.")

if __name__ == "__main__":
    main()
