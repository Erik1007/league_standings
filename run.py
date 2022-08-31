from pprint import pprint

standings = {
    "A": {"WINS": 0, "TIES": 0, "LOSSES": 0},
    "B": {"WINS": 0, "TIES": 0, "LOSSES": 0},
    "C": {"WINS": 0, "TIES": 0, "LOSSES": 0},
    "D": {"WINS": 0, "TIES": 0, "LOSSES": 0},
    "E": {"WINS": 0, "TIES": 0, "LOSSES": 0},
}

score_map_dict = {
    'W': 'WINS',
    'L': 'LOSSES',
    'T': 'TIES'
}

print('Welcome to the League Standings \n')
print('In this basic structure, there are 5 teams, each team plays 8 games')
pprint(standings)
print('To start the 40 game tournament: \n')
print('Enter the teams that played and the outcome of the game')


def input_results():
    """
    registering the users input for which team played and the
    results of the match
    """
    team1 = {}
    team2 = {}
    while True:
        team1_name = input("Enter the letter for the first team: ").upper()
        team1_score = input("Did they Win (W), lose (L) or Tie (T): ").upper()
        team2_name = input("Enter the letter of the second team: ").upper()

        # TODO: ensure that a match is not recorded twice,
        # that applies that a team does not host same team twice

        if validate_input(
                team1_name, team1_score) and validate_team(team2_name):
            print("data is valid")
            team1[team1_name] = score_map_dict[team1_score]

            if team1_score == 'W':
                team2[team2_name] = 'LOSSES'
            if team1_score == 'L':
                team2[team2_name] = 'WINS'
            if team1_score == 'T':
                team2[team2_name] = 'TIES'
            print(team1, team2)
            return (team1, team2)
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


def validate_team(name):
    """
    check if team is in the league
    """
    if name not in "ABCDE":
        print("Please enter a valid team in the league")
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
    sorted_standings = []
    for item in sorted(
            standings.items(), key=lambda item: item[1]['WINS'], reverse=True):
        sorted_standings.append(item)

    pprint(sorted_standings)


def main():
    """
    This function holds all of the function calls to run the program and
    determine the amount of times the program runs
    """
    counter = 1
    while counter < 40:
        counter += 1
        team1, team2 = input_results()
        update_standings(team1, team2)
    show_sorted_standings()


# TODO: find out how to run the app only via python run.py not in the interactive shell
main()
