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
    standingsTable = PrettyTable(["Team", "Win", "Loss", "Tie", "Points"])
    standingsTable.add_row(["A", "0", "0", "0", "0"])
    standingsTable.add_row(["B", "0", "0", "0", "0"])
    standingsTable.add_row(["C", "0", "0", "0", "0"])
    standingsTable.add_row(["D", "0", "0", "0", "0"])
    standingsTable.add_row(["E", "0", "0", "0", "0"])
 
    print("Welcome to the League Standing")
    print(standingsTable)
    print("Enter each team that played and the points they earned")
    print("Wins = 3 points, Ties = 1 point and losses = 0 points")


def input_results():
    """
    introducing the teams in the league, the point structure
    of for wins, loses and ties
    """
    while True:
        
        n = int(1)
        team1 = {}
        for i in range(n):
            key = input("Enter the letter for the first team: ").upper()
            value = input("How many points did they earn: ")
            team1[key] = value
        print(team1)

        team2 = {}
        for i in range(n):
            key = input("Enter the letter of the second team: ").upper()
            value = input("How many points did they earn: ")
            team2[key] = value
        print(team2)
        
        if validate_input(input_results):
            print("data is valid")
            break
    return input_results


def validate_input(key, value):
    """
    Inside the try, Raises ValueError if incorrect repsonses are given.
    """
    try:
        if key not in "ABCDE":
            raise ValueError(
                "Please enter a valid team in the league"
            )
        if value not in "013":
            raise ValueError(
                "Invalid data, please enter a point amount "
            )
    except ValueError as e:
        print(f"Invalid data: {e}, please try again.\n")
        return False

    return True


def main():
    """
    Run all program functions
    """
    standing()
    input_results()
    validate_input()


main()