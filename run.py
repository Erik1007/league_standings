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
 
    print(standingsTable)


def new_game():
    """
    introducing the teams in the league, the point structure
    of for wins, loses and ties
    """
    while True:
        print("Welcome to the League Standing")
        print("Wins = 3 points, Ties = 1 point and losses = 0 points")
        print("Please enter the teams that played and their scores")
        print(" for example: Team 1 = A, Team 1's score = 2")

        team1_str = input("Please enter Team 1: \n")
        team1_int = input("Please enter Team 1's score: \n")


def main():
    """
    Run all program functions
    """
    standing()
    new_game()


main()