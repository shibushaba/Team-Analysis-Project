import pandas as pd
import matplotlib.pyplot as plt
from datetime import datetime
import os

FILE = "team_matches.csv"

if not os.path.exists(FILE):
    df = pd.DataFrame(columns=["date","opponent","goals_for","goals_against","result"])
    df.to_csv(FILE, index=False)


def load_data():
    return pd.read_csv(FILE)


def save_data(df):
    df.to_csv(FILE, index=False)


def add_match():
    opponent = input("Opponent Team: ")
    gf = int(input("Goals For: "))
    ga = int(input("Goals Against: "))
    
    if gf > ga:
        result = "Win"
    elif gf < ga:
        result = "Loss"
    else:
        result = "Draw"
    
    today = datetime.now().strftime("%Y-%m-%d")
    
    df = load_data()
    new = pd.DataFrame([[today, opponent, gf, ga, result]], columns=df.columns)
    df = pd.concat([df, new], ignore_index=True)
    save_data(df)
    print("Match added successfully!")


def show_stats():
    df = load_data()
    if df.empty:
        print("No match data yet.")
        return
    
    print("\nSeason Summary")
    print(f"Total Matches: {len(df)}")
    print(f"Wins: {sum(df['result']=='Win')}")
    print(f"Draws: {sum(df['result']=='Draw')}")
    print(f"Losses: {sum(df['result']=='Loss')}")
    print(f"Goals Scored: {df['goals_for'].sum()}")
    print(f"Goals Conceded: {df['goals_against'].sum()}")
    print(f"Win %: {round((sum(df['result']=='Win')/len(df))*100, 2)}%")


def plot_graphs():
    df = load_data()
    if df.empty:
        print("No data to plot.")
        return
    
    
    df["result"].value_counts().plot(kind="pie", autopct="%1.1f%%", title="Match Results")
    plt.ylabel("")
    plt.show()
    
    
    df[["goals_for","goals_against"]].plot(kind="line", marker="o", title="Team Performance Over Matches")
    plt.xlabel("Match Index")
    plt.ylabel("Goals")
    plt.show()


while True:
    print("\n=== Team Match Analyzer ⚽ ===")
    print("1. Add Match")
    print("2. Show Season Stats")
    print("3. Show Graphs")
    print("4. Exit")
    
    choice = input("Enter choice: ")
    if choice == "1":
        add_match()
    elif choice == "2":
        show_stats()
    elif choice == "3":
        plot_graphs()
    elif choice == "4":
        print("Goodbye! 👋")
        break
    else:
        print("Invalid choice, try again.")