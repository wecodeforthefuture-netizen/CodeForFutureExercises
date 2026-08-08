"""
============================================================
Code for the Future
Final Project

BIBLE ADVENTURE GAME

Student Name(s):
============================================================

PROJECT GOAL:

Build an interactive Bible-inspired adventure game.

The player will make choices, travel through different
locations, earn points, and reach an ending.

Complete the REQUIRED features first.

If you finish early, try the OPTIONAL ADVANCED CHALLENGES
at the bottom of this file.
"""

from ui import *


############################################################
# GAME DATA
############################################################

# TODO:
#
# Create a list containing at least 3 locations
# for your adventure.
#
# Example:
#
# locations = [
#     "The Wilderness",
#     "The Village",
#     "The Mountain"
# ]
#
# YOUR CODE HERE

locations = [

]


############################################################
# PLAYER VARIABLES
############################################################

# TODO:
#
# Create a variable to store the player's name.
#
# YOUR CODE HERE


# TODO:
#
# Create an integer variable to keep track
# of the player's progress.
#
# You could call this:
#
# faith_points
#
# or:
#
# wisdom_points
#
# or create your own system.
#
# YOUR CODE HERE


# TODO:
#
# Create a Boolean variable that will control
# whether the game is still running.
#
# Example:
#
# playing = True
#
# YOUR CODE HERE


############################################################
# FUNCTION: WELCOME
############################################################

def welcome_player():

    """
    Displays the welcome screen and gets
    the player's name.
    """

    welcome()

    # TODO:
    #
    # Ask the player for their name.
    #
    # Store their answer in a variable.
    #
    # YOUR CODE HERE


    # TODO:
    #
    # Use an f-string to welcome the player.
    #
    # Example:
    #
    # print(f"Welcome, {player_name}!")
    #
    # YOUR CODE HERE


############################################################
# FUNCTION: DISPLAY MENU
############################################################

def display_menu():

    """
    Displays the main game menu.
    """

    title("Bible Adventure")

    print("1. Start Adventure")
    print("2. Instructions")
    print("3. View Progress")
    print("4. Exit")

    divider()


############################################################
# FUNCTION: INSTRUCTIONS
############################################################

def instructions():

    """
    Displays the game instructions.
    """

    section("Instructions")

    print("Welcome to the Bible Adventure Game!")
    print()
    print("Make choices as you travel through the adventure.")
    print("Your decisions may affect your progress.")
    print("Try to reach the end of the journey!")

    pause()


############################################################
# FUNCTION: SHOW LOCATION
############################################################

def show_location(location):

    """
    Displays the current location.

    This function uses a PARAMETER.

    The location parameter should contain
    the name of the current location.
    """

    # TODO:
    #
    # Display the location using the UI.
    #
    # You can use:
    #
    # section(location)
    #
    # YOUR CODE HERE


############################################################
# FUNCTION: MAKE CHOICE
############################################################

def make_choice():

    """
    Gets a choice from the player.

    This function should RETURN the player's choice.
    """

    # TODO:
    #
    # Display two or more choices.
    #
    # Example:
    #
    # print("1. Take the difficult path")
    # print("2. Take the easy path")
    #
    # YOUR CODE HERE


    # TODO:
    #
    # Ask the player for their choice.
    #
    # YOUR CODE HERE


    # TODO:
    #
    # RETURN the player's choice.
    #
    # YOUR CODE HERE


############################################################
# FUNCTION: FIRST LOCATION
############################################################

def first_location():

    """
    Runs the first section of the adventure.
    """

    # TODO:
    #
    # Display the first location.
    #
    # YOUR CODE HERE


    # TODO:
    #
    # Tell the player what is happening.
    #
    # Create an interesting story.
    #
    # YOUR CODE HERE


    # TODO:
    #
    # Ask the player to make a choice.
    #
    # You should call your make_choice()
    # function.
    #
    # YOUR CODE HERE


    # TODO:
    #
    # Use if/elif/else to determine
    # what happens based on the player's choice.
    #
    # YOUR CODE HERE


############################################################
# FUNCTION: SECOND LOCATION
############################################################

def second_location():

    """
    Runs the second section of the adventure.
    """

    # TODO:
    #
    # Display the second location.
    #
    # YOUR CODE HERE


    # TODO:
    #
    # Create the story for this location.
    #
    # YOUR CODE HERE


    # TODO:
    #
    # Ask the player to make a choice.
    #
    # YOUR CODE HERE


    # TODO:
    #
    # Use if/elif/else to determine
    # what happens.
    #
    # YOUR CODE HERE


############################################################
# FUNCTION: THIRD LOCATION
############################################################

def third_location():

    """
    Runs the third section of the adventure.
    """

    # TODO:
    #
    # Display the third location.
    #
    # YOUR CODE HERE


    # TODO:
    #
    # Create the story for this location.
    #
    # YOUR CODE HERE


    # TODO:
    #
    # Ask the player to make a choice.
    #
    # YOUR CODE HERE


    # TODO:
    #
    # Use if/elif/else to determine
    # what happens.
    #
    # YOUR CODE HERE


############################################################
# FUNCTION: START ADVENTURE
############################################################

def start_adventure():

    """
    Starts the player's adventure.
    """

    section("Your Adventure Begins")

    # TODO:
    #
    # Call your location functions in the
    # order you want the player to experience them.
    #
    # YOUR CODE HERE


############################################################
# FUNCTION: VIEW PROGRESS
############################################################

def view_progress():

    """
    Displays the player's current progress.
    """

    section("Player Progress")

    # TODO:
    #
    # Display the player's name.
    #
    # YOUR CODE HERE


    # TODO:
    #
    # Display the player's current points.
    #
    # YOUR CODE HERE


############################################################
# FUNCTION: FINAL ENDING
############################################################

def final_ending():

    """
    Displays the ending of the adventure.
    """

    section("Journey Complete")

    # TODO:
    #
    # Display an ending message.
    #
    # Use the player's name.
    #
    # YOUR CODE HERE


    # TODO:
    #
    # Use if/elif/else to determine the ending
    # based on the player's points.
    #
    # Example:
    #
    # if faith_points >= 5:
    #     ...
    #
    # elif faith_points >= 3:
    #     ...
    #
    # else:
    #     ...
    #
    # YOUR CODE HERE


    pause()


############################################################
# MAIN PROGRAM
############################################################

welcome_player()

playing = True

while playing:

    display_menu()

    choice = input("Choose an option: ")

    if choice == "1":

        start_adventure()

        final_ending()

    elif choice == "2":

        instructions()

    elif choice == "3":

        view_progress()

    elif choice == "4":

        goodbye()

        playing = False

    else:

        error("Invalid choice. Please choose 1, 2, 3, or 4.")


############################################################
# OPTIONAL ADVANCED CHALLENGES
############################################################

"""
============================================================
OPTIONAL ADVANCED CHALLENGE 1
MULTIPLE ENDINGS
============================================================

Create multiple possible endings.

Your ending should depend on the player's choices
or points.

For example:

High score:
The player completes the journey successfully.

Medium score:
The player completes the journey but still has
lessons to learn.

Low score:
The journey ends with an opportunity to try again.

Use:

    if
    elif
    else

to create the different endings.


============================================================
OPTIONAL ADVANCED CHALLENGE 2
INVENTORY
============================================================

Create an inventory system.

Example:

inventory = [
    "Bread",
    "Water"
]

Allow the player to collect items during the adventure.

Later in the game, allow the player to view
their inventory.

Use a FOR LOOP to display the items.


============================================================
OPTIONAL ADVANCED CHALLENGE 3
BIBLE QUIZ
============================================================

Add Bible questions to your adventure.

Create a list of questions.

Example:

questions = [
    "Who built the ark?",
    "Who defeated Goliath?",
    "Who was swallowed by a great fish?"
]

Create a matching list of answers.

Ask the player questions and give them points
for correct answers.

You should use:

    Lists
    Loops
    If statements
    Functions


============================================================
OPTIONAL ADVANCED CHALLENGE 4
MULTIPLE PATHS
============================================================

Create different paths through your adventure.

For example:

Choice 1
    |
    v
Village
    |
    v
Mountain
    |
    v
Ending A


Choice 2
    |
    v
Wilderness
    |
    v
River
    |
    v
Ending B

The player's choices should determine
which path they follow.


============================================================
IMPORTANT
============================================================

Do NOT work on the advanced challenges until
your required project is complete and working.

A simple working game is better than a complicated
game that does not work.

============================================================
"""
