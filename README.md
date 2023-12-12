# yahtzee_final
EECE 2140 Final Project - Yahtzee Game

To play this interactive Yahtzee Game, you MUST have PySimpleGUI installed.
If you do not, the code will not run properly.

To install, please enter the following command into your computer's terminal

pip install pysimplegui
or
pip3 install pysimplegui

--------------------------------------------------------------------------------------------------------------
This program will define the way you should represent inputs
Please follow the program's directions for inputs
If you incorrectly input information, the program will give you one more chance before crashing the program.
This is done to allow mistakes and corrections to them, but also provides a way to force close the application.

All inputs in the GUI are expected to be represented as numbers
A string of '123' for dice rerolls will reroll the first, second, and third dice. 
To exit a GUI and send the string, simply hit the button at the bottom of the screen.

--------------------------------------------------------------------------------------------------------------
Play-by-play on how to use the program:

This program will initially ask for your name in the terminal. Player 1 and 2 must input their names and hit enter.
After this, everything will be run in GUI.
The first window will ask you to enter your board. Descriptions of each board are given and represented as 1, 2, or 3.
After choosing a board, gameplay will begin. An initial diceroll will be made and displayed. 
You will get two rerolls. Each time a reroll happens, you must enter which dice you want to reroll as digits (per above section)
If you do not want to reroll any dice, you CAN leave that section blank and no dice will be rolled.
After completing the three rolls, you must enter a move that is being displayed to determine how you will score your dice. 
This will end your turn. After all moves have been made, the game is over and your scorecard will be printed in a document
called 'pythonyahtzee.txt'.
