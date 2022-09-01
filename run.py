from pprint import pprint


teams = {
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


def input_team_name(prompt):
    """
    Enter the team name for the game
    """
    team_name = None

    while True:
        team_name = input(prompt).upper()
        if team_name_exists(team_name):
            break
        print('Please enter a valid team name')

    return team_name


def team_name_exists(name):
    """
    check if team is in the league
    """
    return name in teams.keys()


def input_results():
    """
    registering the users input for which team played and the
    results of the match
    """
    team1 = {}
    team2 = {}
    while True:
        team1_name = input_team_name("Enter the letter for the first team: ")
        team1_result = input_team_result(
            "Did they Win (W), lose (L) or Tie (T)")
        team2_name = input_team_name('Enter the letter of the second team: ')

        if validate_input(team1_name, team1_result):
            team1[team1_name] = score_map_dict[team1_result]
            if validate_game(team1_name, team2_name):
                if team1_name != team2_name:
                    print("data is valid")

                    if team1_result == 'W':
                        team2[team2_name] = 'LOSSES'
                    if team1_result == 'L':
                        team2[team2_name] = 'WINS'
                    if team1_result == 'T':
                        team2[team2_name] = 'TIES'
                    return (team1, team2)
                break


def input_team_result(prompt):
    """
    validating result input
    """
    while True:
        result = input(prompt).upper()
        if result in 'WLT':
            break
        print('Invalid input, pleae try again')
    return result


def validate_input(team_name, team_result):
    """
    Inside the function, prompts are given if responses are invalid.
    """
    if team_result not in "WLT":
        print()
        return False
    
    return True


def validate_game(team1_name, team2_name):
    """
    Checking that the team names are different
    """
    if team1_name == team2_name:
        print('Teams cannot play themself, please enter a valid name')
        return False
    return True


def update_team_standings(team1, team2):
    """
    Updating the teams dictionary Win, Loss, and Tie
    values for each key using the Users input dictionary values
    """
    team_1_key = list(team1.keys())[0]
    team_2_key = list(team2.keys())[0]

    team_1_value = team1[team_1_key]
    team_2_value = team2[team_2_key]

    teams[team_1_key][team_1_value] += 1
    teams[team_2_key][team_2_value] += 1


def show_sorted_standings():
    """
    Sorting the standings dictionary for the team with the most
    wins to the lowest based on users input
    """
    sorted_standings = []
    for item in sorted(
            teams.items(), key=lambda item: item[1]['WINS'], reverse=True):
        sorted_standings.append(item)
        
    pprint(show_sorted_standings)


def main():
    """
    This function holds all of the function calls to run the program and
    determine the amount of times the program runs
    """
    print('Welcome to the League Standings \n')
    print('In this tournament, There are 5 teams, each team plays 8 games')
    pprint(teams)
    print('To start the 40 game tournament: \n')
    print('Enter the teams that played and the outcome of the game')
    counter = 1
    while counter < 40:
        counter += 1
        team1, team2 = input_results()
        update_team_standings(team1, team2)
        pprint(teams)
    show_sorted_standings()


if __name__ == '__main__':
    main()
