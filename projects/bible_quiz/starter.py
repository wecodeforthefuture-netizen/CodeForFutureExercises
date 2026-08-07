"""
===============================================
Code for the Future
Final Project

Bible Quiz Deluxe

Student Name(s):
===============================================
"""

from ui import *


#################################################
# TODO:
# Add at least 10 Bible questions.
#
# Make sure each question is a STRING.
#
# Example:
# questions = [
#     "Who built the ark?",
#     "Who defeated Goliath?"
# ]
#################################################

questions = [

]


#################################################
# TODO:
# Add the answers that match each question.
#
# The answer at position 0 should match
# the question at position 0.
#
# Example:
# answers = [
#     "noah",
#     "david"
# ]
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
# TODO:
def start_quiz():

    # Step 1:
    # Create a variable named score.
    # Start the score at 0.
    #
    # YOUR CODE HERE



    # Step 2:
    # Use a for loop to go through each question.
    #
    # HINT:
    # You will need the range() and len() functions.
    #
    # YOUR CODE HERE



        # Step 3:
        # Print the current question.
        #
        # YOUR CODE HERE


        # Step 4:
        # Ask the user for their answer.
        #
        # YOUR CODE HERE


        # Step 5:
        # Convert the user's answer to lowercase.
        #
        # YOUR CODE HERE


        # Step 6:
        # Compare the user's answer with the
        # correct answer.
        #
        # YOUR CODE HERE


        # Step 7:
        # If the answer is correct:
        #   - Print a message
        #   - Increase the score
        #
        # Otherwise:
        #   - Tell the user the correct answer.
        #
        # YOUR CODE HERE


    # Step 8:
    # Print the player's final score.
    #
    # YOUR CODE HERE



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
