standings = {
    "A": {"Wins": 0, "Losses": 0, "Ties": 0},
    "B": {"Wins": 0, "Losses": 0, "Ties": 0},
    "C": {"Wins": 0, "Losses": 0, "Ties": 0},
    "D": {"Wins": 0, "Losses": 0, "Ties": 0},
    "E": {"Wins": 0, "Losses": 0, "Ties": 0},
}

score_map_dict = {
    'W': 'Wins',
    'L': 'Losses',
    'T': 'Ties',
}

team1 = {}
team2 = {}

print("Welcome to the League Standing",
      standings,
      "Enter the teams that played and the outcome of the game",
      sep='\n')


def input_results():
    """
    registering the users input for which team played and how many
    points were earned
    """
    while True:
        key = input("Enter the letter for the first team: ").upper()
        value = input("Did they Win (W), lose (L) or Tie (T): ").upper()
        team1[key] = score_map_dict[value]  # Returns Wins, Losses, or Ties
        print(team1)

        if validate_input(key, value):
            print("data is valid")

        key = input("Enter the letter of the second team: ").upper()
        value = input("Did they Win (W), lose (L) or Tie (T): ").upper()
        team2[key] = score_map_dict[value]
        print(team2)
      
        if validate_input(key, value):
            print("data is valid")
            break


def validate_input(key, value):
    """
    Inside the function, errors are raised if incorrect repsonses are given.
    """
    if key not in "ABCDE":
        print("Please enter a valid team in the league")
        return False
    if value not in "WLT":
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
            if team1[key] == 'W':
                standings[key][0] += 1
                standings[key][3] += 3
            if team1[key] == 'T':
                standings[key][2] += 1
                standings[key][3] += 1
            if team1[key] == 'L':
                standings[key][1] += 1

    for key in team2.keys():
        if key in standings.keys():
            if team2[key] == 'W':
                standings[key][0] += 1
                standings[key][3] += 3
            if team2[key] == 'T':
                standings[key][2] += 1
                standings[key][3] += 1
            if team2[key] == 'L':
                standings[key][1] += 1


def sorted_standings():
    """
    Sorting the standings dictionary from highest 'point value'
    to lowest based on users input
    """
    table = []
    while len(standings.keys()) > 0:
        max_wins = -1
        top_team = None
        for team in standings.keys():
            if standings[team]['Wins'] > max_wins:
                top_team = team
                max_wins = standings[team]['Wins']
        table.append({'team': top_team, 'wins': max_wins})
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