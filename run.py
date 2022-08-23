import operator


standings = {
    "Team": ["Win", "Loss", "Tie", "Points"],
    "A": [0, 0, 0, 0],
    "B": [0, 0, 0, 0],
    "C": [0, 0, 0, 0],
    "D": [0, 0, 0, 0],
    "E": [0, 0, 0, 0],
}
team1 = {}
team2 = {}

print("Welcome to the League Standing")
print(standings)
print("Enter each team that played and the points they earned")
print("Wins = 3 points, Ties = 1 point and losses = 0 points")


# saving the users input into a dictionary: single letter each
# and a point value for each team to indicate the outcome of the match
def input_results():
    """
    introducing the teams in the league, the point structure
    of for wins, loses and ties
    """
    while True:     
        team1 = {}
        key = input("Enter the letter for the first team: ").upper()
        value = input("How many points did they earn: ")
        team1[key] = value
        print(team1)

        team2 = {}
        key = input("Enter the letter of the second team: ").upper()
        # value = input("How many points did they earn: ")
        team2[key] = value
        print(team2)
        
        if validate_input(team1, team2):
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
            print("Please enter a valid team in the league")
        return False       
        if value not in "013":
            print("Invalid data, please enter a point amount")
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
# loop off the key and add user points to the [-1] for the
# dictionary key value list?
# But this is where I am completly lost...
    for key in team1.keys():
        if key in standings.keys():
            if team1[key] == 3:
                standings[key][0] += 1
                standings[key][-1] += 3
            if team1[key] == 1:
                standings[key][2] += 1
            if team1[key] == 0:
                standings[key][1] += 1

    for key in team2.keys():
        if key in standings.keys():
            if team2[key] == 3:
                standings[key][0] += 1
                standings[key][-1] += 3
            if team2[key] == 1:
                standings[key][2] += 1
            if team2[key] == 0:
                standings[key][1] += 1

    # if W:
        # standings[team1][0]++
        # standings[team2][1]++
    # elif l:
        # standings[team2][0]++
        # standings[team1][1]++
    #else:
        # standings[team1][3]++
        # standings[team2][3]++
                
    return update_standings

# I am trying to figure how to use the sort function off the last
# listed colomns for each each key to determine the order of keys
# from highest value to lowest
def sort_descending_standings():
    """
    Sorting the standings dictionary from highest 'point value'
    to lowest based on users input
    """
    sorted_standings = sorted(update_standings.items(), key=operator.itemgetter(-1), reverse=True)
    print(sorted_standings)

    return sorted_standings

# This function is to house all call functions, this function
# is incomplete


def main():
    """
    A function to run all program functions
    """
    # standings()
    input_results()
    update_standings()
    sort_descending_standings()


main()
print(sorted_standings)