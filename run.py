# Your code goes here.
# You can delete these comments, but do not change the name of this file
# Write your code to expect a terminal of 80 characters wide and 24 rows high

import random
team_list = []
round_1 = []
round_2 = []
round_3 = []

def teams_taking_part():
    num_teams = int(input("How many teams are taking part you can have up to 16: \n"))
    for i in range(0, num_teams):
        i += 1
        team_name = team_list.append(str(input(f"Please enter team no {i}: \n")))
    return team_list
teams_taking_part()

def gen_num_games(team_list):

    rd1_games = len(team_list) // 2
    print(f"There will be {rd1_games} games in round 1\n")
gen_num_games(team_list)

