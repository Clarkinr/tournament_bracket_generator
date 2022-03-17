# Your code goes here.
# You can delete these comments, but do not change the name of this file
# Write your code to expect a terminal of 80 characters wide and 24 rows high

import random

team_list = []
match_split = list()
round_1_win = []
round_2_win = []
round_3_win = []

def teams_taking_part():
    """
    Requests team names from the user one by one and adds them to the team_list
    """
    num_teams = int(input("How many teams are taking part you can have up to 16: \n"))
    for i in range(0, num_teams):
        i += 1
        team_name = team_list.append(str(input(f"Please enter team no {i}: \n")))
    return team_list
teams_taking_part()

def gen_num_games(team_list):
    """
    Shuffle the team list in order to have randomly assigned games
    Splits team list into groups of two for games.
    """
    random.shuffle(team_list)
    game_size = 2
    for i in range(0, len(team_list), game_size):
        match_split.append(team_list[i:i+game_size])
    return match_split
gen_num_games(team_list)

def round_one_matches(match_split):
    rd1_games = len(team_list) // 2
    print(f"There will be {rd1_games} games in round 1: \n")
    for i in range(0, len(match_split)):
        print(f"Game {i+1}: {match_split[i][0]} VS {match_split[i][1]}\n")
        i += 1

round_one_matches(match_split)