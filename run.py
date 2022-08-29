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

welcome_message = f"""\
Welcome to the League Standing
{standings}
Enter the teams that played and the outcome of the game
"""

print(welcome_message)


def input_results():
    """
    registering the users input for which team played and how many
    points were earned
    """
    team1 = {}
    team2 = {}
    while True:
        team1 = {}
        key = str(input("Enter the letter for the first team: ").upper())
        value = str(input("Did they Win (W), lose (L) or Tie (T): ").upper())
        team1[key] = value
        print(team1)

        if validate_input(key, value):
            print("data is valid")

        team2 = {}
        key = str(input("Enter the letter of the second team: ").upper())
        value = str(input("Did they Win (W), lose (L) or Tie (T): ").upper())
        team2[key] = value
        print(team2)
      
        if validate_input(key, value):
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
    if value not in "WLT":
        print("Invalid data, please enter the correct result")
        return False
    return True


def update_standings(team1, team2):
    """
    Updating the standings dictionary Win, Loss, and Tie
    values for each key using the Users input dictionary values
    """
    team_1_key = list(team1.keys())[0]
    team_2_key = list(team2.keys())[0]

    team_1_value = team1[team_1_key]
    team_2_value = team2[team_2_key]

    standings[team_1_key][team_1_value] += 1
    standings[team_2_key][team_2_value] += 1

    pprint(standings)


def show_sorted_standings():
    """
    Sorting the standings dictionary for the team with the most
    wins to the lowest based on users input
    """
    while len(standings.keys()) > 0:
        max_wins = -1
        top_team = None
        for team in standings.keys():
            if standings[team]['Wins'] > max_wins:
                top_team = team
                max_wins = standings[team]['Wins']
        table.append({'team': top_team, 'wins': max_wins})
        del standings[top_team]

    # print(standings)
    # print(table)


def main():
    """
    A function to run all program functions
    """
    counter = 0
    while counter < 5:
        counter += 1
        team1, team2 = input_results()
        update_standings(team1, team2)
    show_sorted_standings()


main()
