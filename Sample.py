import pandas as pd
import matplotlib.pyplot as plt
from datetime import datetime
import os


class TeamMatchAnalyzer:
    def __init__(self, filename="team_matches.csv"):
        self.filename = filename
        self._initialize_file()

    def _initialize_file(self):
        """Create CSV file if it doesn't exist"""
        if not os.path.exists(self.filename):
            df = pd.DataFrame(columns=["date", "opponent", "goals_for", "goals_against", "result"])
            df.to_csv(self.filename, index=False)

    def load_data(self):
        """Load match data from CSV"""
        try:
            return pd.read_csv(self.filename)
        except Exception as e:
            print(f"Error loading file: {e}")
            return pd.DataFrame(columns=["date", "opponent", "goals_for", "goals_against", "result"])

    def save_data(self, df):
        """Save match data to CSV"""
        try:
            df.to_csv(self.filename, index=False)
        except Exception as e:
            print(f"Error saving file: {e}")

    def add_match(self):
        """Add a new match record"""
        try:
            opponent = input("Opponent Team: ").strip()
            gf = int(input("Goals For: "))
            ga = int(input("Goals Against: "))

            if gf > ga:
                result = "Win"
            elif gf < ga:
                result = "Loss"
            else:
                result = "Draw"

            today = datetime.now().strftime("%Y-%m-%d")

            df = self.load_data()
            new = pd.DataFrame([[today, opponent, gf, ga, result]], columns=df.columns)
            df = pd.concat([df, new], ignore_index=True)
            self.save_data(df)
            print("✅ Match added successfully!")
        except ValueError:
            print("❌ Invalid input. Please enter numeric values for goals.")
        except Exception as e:
            print(f"❌ Error adding match: {e}")

    def show_stats(self):
        """Display season statistics"""
        df = self.load_data()
        if df.empty:
            print("⚠️ No match data yet.")
            return

        try:
            print("\n📊 Season Summary")
            print(f"Total Matches: {len(df)}")
            print(f"Wins: {sum(df['result'] == 'Win')}")
            print(f"Draws: {sum(df['result'] == 'Draw')}")
            print(f"Losses: {sum(df['result'] == 'Loss')}")
            print(f"Goals Scored: {df['goals_for'].sum()}")
            print(f"Goals Conceded: {df['goals_against'].sum()}")
            print(f"Win %: {round((sum(df['result']=='Win')/len(df))*100, 2)}%")
        except Exception as e:
            print(f"❌ Error calculating stats: {e}")

    def plot_graphs(self):
        """Plot performance graphs"""
        df = self.load_data()
        if df.empty:
            print("⚠️ No data to plot.")
            return

        try:
            # Pie chart
            df["result"].value_counts().plot(kind="pie", autopct="%1.1f%%", title="Match Results")
            plt.ylabel("")
            plt.show()

            # Line chart
            df[["goals_for", "goals_against"]].plot(kind="line", marker="o", title="Team Performance Over Matches")
            plt.xlabel("Match Index")
            plt.ylabel("Goals")
            plt.show()
        except Exception as e:
            print(f"❌ Error plotting graphs: {e}")

    def run(self):
        """Main menu loop"""
        while True:
            print("\n=== Team Match Analyzer ⚽ ===")
            print("1. Add Match")
            print("2. Show Season Stats")
            print("3. Show Graphs")
            print("4. Exit")

            choice = input("Enter choice: ").strip()
            if choice == "1":
                self.add_match()
            elif choice == "2":
                self.show_stats()
            elif choice == "3":
                self.plot_graphs()
            elif choice == "4":
                print("👋 Goodbye!")
                break
            else:
                print("❌ Invalid choice, try again.")


if __name__ == "__main__":
    analyzer = TeamMatchAnalyzer()
    analyzer.run()
