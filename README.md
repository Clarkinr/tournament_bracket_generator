# Single Elimination Tournament Generator
This project is an application which creates and runs the rounds of a single elimintaion tournament and determines a winner. The application creates a team list for a round, randomizes the list (in order to make next round draw), takes user input for game scores and then repeats the cycle until a winner is determined.

## Reasons for creation
The reason for creating tihs project was due to my interest and involvement in sports clubs throughout my life. I have taken part in many tournaments and have been looking for a way to reduce the need for manually recording games, scores, draws etc. 

## The Functions
__teams_taking_part()__
- This function was intended to complete two main objectives 1. Request number of teams from the user 2. Request team names from the user
- The function then takes these inputs and generates a team_list and adds teams called "BYE" if the number of teams is not equal to 4,8 or 16. This function was written so that the size could be increased later on but for the purpose of this project 16 was chosen as an adequate maximum
![teams-taking-part-code](/media/images/teams.png)

__gen_num_games()__
- This function shuffles the team list in order to provide random matchups for the next round.
- The function then returns the variable match list, which separates the team list into individual games.
![gen_num_games_code](/media/images/num_games.png)

__round_matches()__
- This function prints out the games in the next round and requests that the user confirm they are ready to move to the next round.
![round-matches-code](/media/images/round-match.png)

__advance_round()__
- This is the function accepts user inputed scores and then determines which team advances to the next round. 
- The function also calls the validate_input() function which validates that the score entered by the user is an integer before moving on.
- Finally the function requests that the user signal if they are ready to move onto the next game until the round is complete. 
![advance-round-code](/media/images/advance.png)

__validate_input()__
- This function takes the scores inputed in advance_round() and ensures they are integers.
- If the functions are not integers an error is given to the user and the advance_round() function is repeated until the input is the correct type.
- This function was adapted from the Code Institute Love Sandwiches project.
![validate_code](/media/images/validate.png)

__main()__
- This is the function which runs application. 
- The function contains a while loop which loops through all other functions aside from the intitial teams_taking part function until the list or teams has been reduced to one and then declares that the one remaining team is the winner of the tournament. 
![main-code](/media/images/main.png)

## Features left to implement
- Initially the aim for this project was to allow for the user to be able to choose from multiple tournament types including: Double Elimination and Round Robin Tournaments. These proved more complicated to implement and will be revisited at a later stage. 
- Currently the user is required to enter a score for a team named "BYE" instructions are provided to the user to only enter 0 for these teams and to enter 1 for an teams opposing. The author would like to make it so that if one team is called by they automatically lose the game.

## Known bugs 
- Any score can be entered for a team named "BYE" so technically they can win rounds

## Code Validation 
- Code was checked for convnentional formatting using the pycodestyle function built into gitpod (this was formerly pep8). The output from this can be seen in the image below.
- All Errors were removed and the code now passes without any changes suggested.
![pycodestyle-check-image](/media/images/pep8_initial.png)

## Deplyoment
- The application was deployed using Heroku by connecting it to github.
- Two buildpacks were added heroku/python and heroku/node.js
- A config VAR was required to be added too key PORT and VALUE 8000.
- Automatic deploys were enabled 
![Heroku-deployment-screen](/media/images/heroku_deploy.png)
![Heroku-settings-screen](/media/images/heroku_settings.png)

## Credits
- The Data validation used for the scores was adapted from the code institute love sandwiches project. 