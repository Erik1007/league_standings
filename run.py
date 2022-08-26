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


def input_results():
    """
    registering the users input for which team played and how many
    points were earned  
    """
    while True:   
        team1 = {}
        key = input("Enter the letter for the first team: ").upper()
        value = input("Did they Win (W), lose (L) or Draw (D): ").upper()
        team1[key] = value
        print(team1)

        team2 = {}
        key = input("Enter the letter of the second team: ").upper()
        team2[key] = value
        print(team2)
        
        if validate_input(team1, team2):
            print("data is valid")
            break
    return input_results


def validate_input(key, value):
    """
    Inside the function, errors are raised if incorrect repsonses are given.
    """
    if key not in "ABCDE":
        print("Please enter a valid team in the league")
        return False
    if value not in "WLD":
        print("Invalid data, please enter the correct result")
        return False

    return True


# This is where I am trying to figure out how to add the inputed
# points value from the user into the exting standings dictionary
# My thought is to add single values to the W,L,T list-values in the
# dict, while simulatenously increasing the points total with the
# respective user input points value
# But this is where I am completly lost..


def update_standings():
    """
    Updating the standings dictionary Win, Loss, Tie and Points
    values for each key using the Users input dictionary values
    """
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
# listed value for each each key to determine the order of keys
# from highest point value to lowest
def sort_descending_standings():
    """
    Sorting the standings dictionary from highest 'point value'
    to lowest based on users input
    """
    sorted_standings = sorted(update_standings.items(), key=operator.itemgetter(-1), reverse=True)
    print(sorted_standings)

    return sorted_standings


def main():
    """
    A function to run all program functions
    """
    input_results()
    update_standings()
    sort_descending_standings()


main()
print(sorted_standings)