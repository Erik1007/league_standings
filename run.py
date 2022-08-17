import gspread
from google.oauth2.service_account import Credentials
from prettytable import PrettyTable

SCOPE = [
    "https://www.googleapis.com/auth/spreadsheets",
    "https://www.googleapis.com/auth/drive.file",
    "https://www.googleapis.com/auth/drive"
    ]

CREDS = Credentials.from_service_account_file('creds.json')
SCOPED_CREDS = CREDS.with_scopes(SCOPE)
GSPREAD_CLIENT = gspread.authorize(SCOPED_CREDS)
SHEET = GSPREAD_CLIENT.open('league_standings')


class standing():
    """
    Creates the intro for the league standings
    """
    # Specify the Column Names while initializing the Table
    standingsTable = PrettyTable(["Team", "Win", "Loss", "Tie", "Points"])
 
    # Add rows
    standingsTable.add_row(["TeamA", "0", "0", "0", "0"])
    standingsTable.add_row(["TeamB", "0", "0", "0", "0"])
    standingsTable.add_row(["TeamC", "0", "0", "0", "0"])
    standingsTable.add_row(["TeamD", "0", "0", "0", "0"])
    standingsTable.add_row(["TeamE", "0", "0", "0", "0"])
 
    print("Welcome to the League Standing")
    print(standingsTable)
    print("Enter each team that played and the points they earned")
    print("Wins = 3 points, Ties = 1 point and losses = 0 points")


def record_results():
    """
    introducing the teams in the league, the point structure
    of for wins, loses and ties
    """
    while True:
        
        n = int(1)
        team1 = {}
        for i in range(n):
            key = input("Enter the first team that played:  ")
            value = input("How many points did they earn: ")
            team1[key] = value
        print(team1)

        team2 = {}
        for i in range(n):
            key = input("Enter the second team that played: ")
            value = input("How many points did they earn: ")
            team2[key] = value
        print(team2)


def main():
    """
    Run all program functions
    """
    standing()
    record_results()


main()