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

    # Step 1
    # Create a variable named score and set it to 0.



    # Step 2
    # Use a for loop to go through every question.



    # Step 3
    # Print the current question.



    # Step 4
    # Ask the user for an answer.



    # Step 5
    # Convert the user's answer to lowercase.



    # Step 6
    # Compare the user's answer with the correct answer.



    # Step 7
    # If correct:
    #    Increase the score by 1
    # Otherwise:
    #    Tell them the correct answer.



    # Step 8
    # Print the final score.


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
