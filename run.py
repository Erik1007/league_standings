standings = {
    "Team": {"Wins": 0, "Losses": 0, "Ties": 0, "Points": 0},
    "A": {"wins": 0, "losses": 0, "ties": 0, "points": 0},
    "B": {"wins": 0, "losses": 0, "ties": 0, "points": 0},
    "C": {"wins": 0, "losses": 0, "ties": 0, "points": 0},
    "D": {"wins": 0, "losses": 0, "ties": 0, "points": 0},
    "E": {"wins": 0, "losses": 0, "ties": 0, "points": 0},
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
        value = input("Did they Win (W), lose (L) or Draw (D): ").upper()
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


def sorted_standings():
    """
    Sorting the standings dictionary from highest 'point value'
    to lowest based on users input
    """
    table = []
    while len(standings.keys()) > 0:
        max_points = -1
        top_team = None
        for team in standings.keys():
            if standings[team]['points'] > max_points:
                top_team = team
                max_points = standings[team]['points']
        table.append({'team': top_team, 'points': max_points})
        del standings[top_team]

    print(standings)
    print(table)


def main():
    """
    A function to run all program functions
    """
    input_results()
    update_standings()
    sorted_standings()


main()
print(sorted_standings)