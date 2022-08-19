import gspread
from google.oauth2.service_account import Credentials

SCOPE = [
    "https://www.googleapis.com/auth/spreadsheets",
    "https://www.googleapis.com/auth/drive.file",
    "https://www.googleapis.com/auth/drive"
    ]

CREDS = Credentials.from_service_account_file('creds.json')
SCOPED_CREDS = CREDS.with_scopes(SCOPE)
GSPREAD_CLIENT = gspread.authorize(SCOPED_CREDS)
SHEET = GSPREAD_CLIENT.open('league_standings')


# Changed from having a table to a dictionary for the standings
# using a list for the values. I prefer the way a table looks to 
# a dictionary when printed, but as long as it works...

standings = {
    "Team": ["Win", "Loss", "Tie", "Points"],
    "A": [0, 0, 0, 0],
    "B": [0, 0, 0, 0],
    "C": [0, 0, 0, 0],
    "D": [0, 0, 0, 0],
    "E": [0, 0, 0, 0],
}

print("Welcome to the League Standing")
print(standings)
print("Enter each team that played and the points they earned")
print("Wins = 3 points, Ties = 1 point and losses = 0 points")

# saving the users input into a dictionary: single letter each 
#and a point value for each team to indicate the outcome of the match
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


# this function is to validate that the correct information is 
# used and providing an error message if not (this function is 
# incomplete)
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

# This is where I am trying to figure out how to add the inputed
# points value from the user into the exting standings dictionary
# My thought is to add single values to the W,L,T list-values in the 
# dict, while simulatenously increasing the points total with the 
# respective user input points value -> if that makes sense
def update_standings():
    """
    Updating the standings dictionary Win, Loss, Tie and Points
    values for each key using the Users input dictionary values
    """
# This is where things go to hell...I cant figure out if I should 
# loop off the key and add user points to the [-1] for the list-vlaue?
# But this is where I am completly lost... 
    standings.update(team1)
    for key in keys:
        if "key" == "A":
            if value == 3:
                [0] += 1,
                [-1] += 3,
            if value == 1:
                [2] += 1, 
            if value == 0:
                [1] += 1, 
        print(standings)    


# The thought is to record the users input on to one sheet
# and the standing on a second sheet. ALTHOUGH, as this is 
# not a requirement, i might delete this step altogether
def update_spreadsheet():
    pass


# I am trying to figure how to use the sort function off the last 
# listed colomns for each each key to determine the order of keys
# from highest value to lowest
def sort_descending_standings():
    pass


#This is just to show the most updated version of the standings 
# table.
def print_updated_standings():
    pass


# This function is to house all call functions, this function 
# is incomplete
def main():
    """
    A function to run all program functions
    """
    standings()
    input_results()
    validate_input()


main()