# A League 'Standings' Table


# Table of contents
1. [Introduction](#introduction)
2. [Program Features](#program_features)
3. [Future Implementations](#future_implementations)
4. [Testing and Validation](#testing)
5. [Unfixed Bugs](#unfixedbugs)
6. [Deployment](#deployment)
7. [Credits](#code-credits)

# Introduction

This program is a designed to be an adaptable and open structure for anyone that needs an automatic 'league standings' program. 

These days there is an almost endless amount of need for an adaptable standings table; from fantasy leagues, to little leagues, and hundreds of miscellaneous sports leagues. This basic structure for a league standings table is designed to be adaptable for anyone and any situation.

Anyone that finds themself in an administrative situation for athletic groups, tournaments, and social activities; this adaptable league standings structure would be a massive time and stress saver. With small changes and adaptations this basic code can be used to meet anyones needs, and help make someones life better.




## Program Features:

### League Introduction 

This league is modelled after a regular season where there are 5 teams and each team will play a total of 8 games for a total of 40 games in the season/tournament. (Of course all of this can be easily adjusted byt the user to match their individual needs.) 

The first is a basic intoduction and explanation of the League Standings structure with welcomings information. The blank league standings is printed out with generic team identificaitons. After the standing, the user is prompted to provide information concerning the match.
(SCREENSHOT)

The user is encouraged to input an identification for the first team (A, B, C, etc.) and the result of the match: a 'w' for win, a 'l' for loss or a 't' for a tied match result. As well to enter the information for the seond team in the match. Once the second team has been identified, the program displays the match outcome based off of team 1's results. (for example, if team 1 wins, team 2 loses, etc.)
(SCREENSHOT)



### Input Validation

There are multiple validation functions to make sure that the information the user provides is correct and accurate, for example:

There is an input validation function to check if the team names that are entered are part of the team standings with a prompt for the user to use a valid input incase they entered the wrong key. 

There is a second input validation checking that the match result information is correct with a prompt for the user to use a valid input incase they entered the wrong key. 

A third validation checking that the team name is not entered more than once per match with a prompt letting the user know that a team cannot play itself.

A fourth validation function counts the amount of games that a team has been involved in and provides a prompt alerting the user if the team has played too much.
(SCREENSHOT)



### Updated Standings

Once the users information has been validated as correct, the program automatically updates the League Standings with the new match outcome information. The teams that played in the game have their records updated.
(SCREENSHOT)



### Tournament Conclusion

At the end of the tournament, the overall standings are displayed with the team that has the most 'Wins' on the top of the standings and the rest of the teams in decending order. The amount of mathes can be set at different numbers depending on the size of the tournement and the amount of games each team plays.
(SCREENSHOT)


## Future Features and Implemetations


This basic structure is designed to adated to suit the needs of who ever needs or wants to use it. The team names are generic and adaptable to meet the users needs for the league. Additionally the amount of teams is also easily adaptable to suit the needs of the new user. 

This code could be the foundation for an entire league standings site including live game scores, accrued points totals, player profiles, and every level of sport specific statistics for the sport in question. Depending on the users needs, this basic code can be adapted and expanded to be used for players statistics, win/loss percentages, and more.



## Testing 

Testing of the code was primarily done by executing the code in the terminal server then debugging and trouble shooting error codes through google/stackoverflow and w3school searches.



## Validation Test with screenshots

The website Pep8 [http://pep8online.com/checkresult] was used for python code validation and error debugging.
(screenshot)



## Unfixed bugs

There have been a number of bugs identified and solved through development process of this project. There are no bugs that prevent the program from executing to conclusion as planned. That being said, there is one error message for a line being too long. However, this does not interfere with the program.


## Deployment process


## Code Credits:

1. The Code Institute 'Love Sndwiches' walk through project was heavily referenced for help with code that was used in the overall structure of this program as well as in the development of the input results and validate input funcitons. 

2. [w3resource](https://www.w3resource.com/python-exercises/dictionary/python-data-type-dictionary-exercise-1.php#:~:text=Use%20dict.,based%20on%20the%20second%20argument.) was used for help with iterating input into dicitonaries in the input results and update standings functions.

3. [thispointer] (https://thispointer.com/python-dictionary-with-multiple-values-per-key/) was used for help with dictionary setup and updating key values in the update standings function.

4. [stackoverflow] (https://stackoverflow.com/questions/14147369/make-a-dictionary-in-python-from-input-values) was heavily relied upon for code and understanding for looping input into dicitonaries in the update standings function, the validation function and the input results function.

5. [Github] (https://docs.github.com/en/get-started/writing-on-github/getting-started-with-writing-and-formatting-on-github/basic-writing-and-formatting-syntax) was havily used for help with writing the read me page.

6. [progrmiz] (https://www.programiz.com/python-programming/methods/built-in/sorted) was used for help with code for sorting dicitonary values based on user input.

7. [w3] (https://www.w3schools.com/python/python_lambda.asp) was used for code and explanations on how to use lambda, that was used in the show sorted standings function.

8. [stackoverflow] (https://stackoverflow.com/questions/613183/how-do-i-sort-a-dictionary-by-value) was used for code and understanding for help with sorting values in a dictionary in reverse.

9. [realpython] (https://realpython.com/python-lambda/) was used for lambda understanding, explanation, code and useage in the sorted standings function.

10. [geeksforgeeks] (https://www.geeksforgeeks.org/pprint-data-pretty-printer-python/) was used for code to find a better way to print out the standings dictionary after updating in the show sorted standings function as well as in the update standings function.

11. [pybit] (https://pybit.es/articles/dict-ordering/) was used for code to assist in the de-alphabizing of he value-list print out order in the update standings and show sorted standings function.

12. for better understading of lambda, used [towardsdatascience] (https://towardsdatascience.com/lambda-functions-with-practical-examples-in-python-45934f3653a8)

13. [stackoverflow](https://stackoverflow.com/questions/40302580/same-input-twice-not-to-be-entered-twice) was used to help with code and understanding on creating the max_games and played_all_games functions that count how many games each team has played.

14. [stackoverflow](https://stackoverflow.com/questions/11948245/markdown-to-create-pages-and-table-of-contents) help with setting up the readme for better readability

15. Code Institute Tutor Assistance significantly helped with trouble shooting, error tracking and debugging, naming advice,  and structure.