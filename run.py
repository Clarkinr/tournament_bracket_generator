# Your code goes here.
# You can delete these comments, but do not change the name of this file
# Write your code to expect a terminal of 80 characters wide and 24 rows high

import random

team_list = []
match_split = list()



def teams_taking_part():
    """
    Requests team names from the user one by one and adds them to the team_list
    Creates an team called 'BYE' while the tournament size does not divide into 
    the appropriate number of games
    """ 
    num_teams = int(input("Welcome to the Tournament Generator: \n\nHow many teams are taking part you can have between 4 & 16: \n\n"))
    
    for i in range(0, num_teams):
        i += 1
        team_name = team_list.append(str(input(f"\nPlease enter name for team no {i}: \n\n>")))

    while len(team_list) not in [4, 8, 16]:
        add_bye = team_list.append("BYE")

    return team_list
    


def gen_num_games(team_list):
    """
    Shuffle the team list for the new round in order to have randomly assigned games
    Splits team list into groups of two for games.
    """
    random.shuffle(team_list)
    clear_split = match_split.clear()
    game_size = 2
    
    for i in range(0, len(team_list), game_size):
        match_split.append(team_list[i:i+game_size])

    return match_split



def round_matches(match_split):
    """
    Shows each of the games to be played in round one
    """
    rd_games = len(match_split)
    print("-------------------------------------------------------------------------------\n")
    print(f"There will be {rd_games} games in this round: \n")
    
    for i in range(0, len(match_split)):
        print(f"Game {i+1}: {match_split[i][0]} VS {match_split[i][1]}\n")
        i += 1
    
    print("-------------------------------------------------------------------------------\n")
    start_rd = input("Are you ready to start the round?\n(y/n)\n\n")

    if start_rd != "y":            
            input("Ok please press the return key when you are ready to advance\n")
    else:
        return rd_games



def advance_round(match_split):
    """
    Requests score input for each game in the round from the user,
    Creates list of teams advancing to the next round
    """
    clear_list = team_list.clear()

    for i in range(0, len(match_split)):        
        print("-------------------------------------------------------------------------------\n")
        print(f"What was the score for game {i+1}?\n\n")

        while True:
            result_1 = input(f"How many goals did {match_split[i][0]} score: \n\n>")
            result_2 = input(f"How many goals did {match_split[i][1]} score: \n\n>")
            if validate_input(result_1) and validate_input(result_2):
                break

        if result_1 > result_2:
            print("-------------------------------------------------------------------------------\n")
            print(f"\n{match_split[i][0]} advances to next round\n")
            print("-------------------------------------------------------------------------------\n")
            list_update = team_list.append(match_split[i][0])

        else:        
            print("-------------------------------------------------------------------------------\n")
            print(f"\n{match_split[i][1]} advances to next round\n")
            print("-------------------------------------------------------------------------------\n")
            list_update = team_list.append(match_split[i][1])

        next_game = input("Are you ready to move on?\n(y/n)\n\n>")

        if next_game != "y":
            input("Ok please press the return key when you are ready to advance\n>")
            print("-------------------------------------------------------------------------------\n")

        else:
            i += 1

    print("\n\nThis round has been completed")

def validate_input(value):
    """
    Adds a try statement to make sure all scores entered are integers
    returns an error message to the user if a score entered was not an integer
    """
    try: 
        if type(int(value)) != int:
            raise ValueError(
                "Scores provided must be integers\n"
            )
    except ValueError as e:
        print(f"{e}\n")
        return False
        
    return True


def main():
    """
    Runs all functions for torunamnent bracket generator
    """
    teams_taking_part()

    while len(team_list) > 1:
        gen_num_games(team_list)
        round_matches(match_split)
        advance_round(match_split)
    else: 
        print("-------------------------------------------------------------------------------\n")
        print(f"{team_list[0]} is the Winner!\n")
        print("-------------------------------------------------------------------------------\n")

main()