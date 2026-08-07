"""
===============================================
Code for the Future
Final Project

Bible Quiz Deluxe

Students Names:
===============================================
"""

from ui import *

#################################################
# TODO:
# Add at least 10 Bible questions.
#################################################

questions = [

]

#################################################
# TODO:
# Add the answers that match each question.
#################################################

answers = [

]


#################################################
# FUNCTION
#################################################

def display_menu():
    """Displays the main menu."""

    title("Bible Quiz Deluxe")

    print("1. Start Quiz")
    print("2. Instructions")
    print("3. Exit")

    divider()


#################################################
# FUNCTION
#################################################

def instructions():

    section("Instructions")

    print("Answer each Bible question.")
    print("Type your answer and press ENTER.")
    print("You earn one point for every correct answer.")

    pause()


#################################################
# FUNCTION
#################################################

def start_quiz():

    #################################################
    # TODO:
    #
    # Create a score variable.
    #################################################

    score = 0

    #################################################
    # TODO:
    #
    # Loop through every question.
    #################################################

    # YOUR CODE HERE



    #################################################
    # TODO:
    #
    # Print the final score.
    #################################################

    print()

    divider()

    print("Quiz Finished!")

    divider()

    # YOUR CODE HERE

    pause()


#################################################
# PROGRAM STARTS HERE
#################################################

running = True

while running:

    display_menu()

    choice = input("Choose an option: ")

    if choice == "1":

        start_quiz()

    elif choice == "2":

        instructions()

    elif choice == "3":

        goodbye()

        running = False

    else:

        error("Invalid choice.")
