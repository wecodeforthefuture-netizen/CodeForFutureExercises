"""
============================================================
Code for the Future
Final Project

SCRIPTURE MEMORY TRAINER

Student Name(s):
============================================================

PROJECT GOAL:

Build a Python application that helps users practice
memorizing Bible verses.

Remember to complete the REQUIRED features first.

If you finish early, try the OPTIONAL ADVANCED CHALLENGE
at the bottom of this file.
"""

from ui import *


############################################################
# BIBLE VERSES
############################################################

# TODO:
# Add at least 5 Bible verses to this list.
#
# Each verse should be a STRING.
#
# Example:
#
# verses = [
#     "For God so loved the world...",
#     "I can do all things through Christ...",
#     "The Lord is my shepherd..."
# ]
#
# Choose verses that are meaningful to you.
############################################################

verses = [

]


############################################################
# BIBLE REFERENCES
############################################################

# TODO:
# Add the Bible references that match your verses.
#
# IMPORTANT:
# The positions in both lists should match.
#
# For example:
#
# verses[0] should match references[0]
# verses[1] should match references[1]
#
# Example:
#
# references = [
#     "John 3:16",
#     "Philippians 4:13",
#     "Psalm 23:1"
# ]
############################################################

references = [

]


############################################################
# PROGRESS VARIABLES
############################################################

# TODO:
# Create variables to keep track of the user's progress.
#
# You might need:
#
# - A score
# - Number of verses practiced
# - Number of correct answers
#
# Start your numbers at 0.
############################################################

score = 0

verses_practiced = 0


############################################################
# DISPLAY MENU
############################################################

def display_menu():
    """
    Displays the main menu.
    """

    title("Scripture Memory Trainer")

    print("1. Practice a Verse")
    print("2. View Verses")
    print("3. View Progress")
    print("4. Exit")

    divider()


############################################################
# VIEW VERSES
############################################################

def view_verses():
    """
    Displays all of the Bible verses in the program.
    """

    section("Bible Verses")

    # TODO:
    #
    # Use a FOR LOOP to go through the verses list.
    #
    # Display:
    #
    # 1. Bible reference
    #    Bible verse
    #
    # 2. Bible reference
    #    Bible verse
    #
    # HINT:
    #
    # You may want to use:
    #
    # range()
    # len()
    #
    # You will also need to access items
    # in your lists using an index.
    #
    # YOUR CODE HERE



    pause()


############################################################
# PRACTICE A VERSE
############################################################

def practice_verse():
    """
    Allows the user to choose and practice a verse.
    """

    global score
    global verses_practiced

    section("Practice a Verse")

    # TODO:
    #
    # First, check whether there are any verses
    # in your verses list.
    #
    # If there are no verses, tell the user
    # to add some verses first.
    #
    # HINT:
    #
    # You can check the length of a list using len().
    #
    # YOUR CODE HERE



    # TODO:
    #
    # Display the available verses.
    #
    # Example:
    #
    # 1. John 3:16
    # 2. Philippians 4:13
    # 3. Psalm 23:1
    #
    # Use a LOOP.
    #
    # YOUR CODE HERE



    # TODO:
    #
    # Ask the user which verse they would
    # like to practice.
    #
    # Store their answer in a variable.
    #
    # YOUR CODE HERE



    # TODO:
    #
    # Convert the user's choice from a STRING
    # into an INTEGER.
    #
    # Remember that list indexes start at 0.
    #
    # If the user chooses 1, the list index
    # should be 0.
    #
    # YOUR CODE HERE



    # TODO:
    #
    # Get the selected verse from the verses list.
    #
    # Also get the matching reference from
    # the references list.
    #
    # YOUR CODE HERE



    # TODO:
    #
    # Display the selected Bible verse.
    #
    # Example:
    #
    # Reference: John 3:16
    #
    # "For God so loved the world..."
    #
    # YOUR CODE HERE



    # TODO:
    #
    # Create a SIMPLE memory challenge.
    #
    # You can start by asking the user
    # a question about the verse.
    #
    # Example:
    #
    # What is one word from this verse?
    #
    # OR:
    #
    # What word comes after "For God so"?
    #
    # YOUR CODE HERE



    # TODO:
    #
    # Get the user's answer.
    #
    # YOUR CODE HERE



    # TODO:
    #
    # Convert the user's answer to lowercase.
    #
    # This makes it easier to compare answers.
    #
    # Example:
    #
    # answer = answer.lower()
    #
    # YOUR CODE HERE



    # TODO:
    #
    # Check whether the user's answer is correct.
    #
    # Use an IF/ELSE statement.
    #
    # If the answer is correct:
    #
    #     Print an encouraging message.
    #     Increase the score.
    #
    # Otherwise:
    #
    #     Tell the user they can try again.
    #
    # YOUR CODE HERE



    # TODO:
    #
    # Increase the number of verses practiced.
    #
    # YOUR CODE HERE



    pause()


############################################################
# VIEW PROGRESS
############################################################

def view_progress():
    """
    Displays the user's current progress.
    """

    section("Your Progress")

    # TODO:
    #
    # Display the user's current score.
    #
    # Example:
    #
    # Current Score: 3
    #
    # YOUR CODE HERE


    # TODO:
    #
    # Display the number of verses practiced.
    #
    # Example:
    #
    # Verses Practiced: 5
    #
    # YOUR CODE HERE


    pause()


############################################################
# MAIN PROGRAM
############################################################

running = True

while running:

    display_menu()

    choice = input("Choose an option: ")

    if choice == "1":

        practice_verse()

    elif choice == "2":

        view_verses()

    elif choice == "3":

        view_progress()

    elif choice == "4":

        goodbye()

        running = False

    else:

        error("Invalid choice. Please choose 1, 2, 3, or 4.")


############################################################
# OPTIONAL ADVANCED CHALLENGE
############################################################

"""
============================================================
OPTIONAL ADVANCED CHALLENGE
============================================================

Finished the required project?

Try creating a FILL-IN-THE-BLANK Scripture challenge.

Instead of simply asking the user about a verse,
remove one or more words from the verse.

Example:

"For God so ________ the world..."

The user must type:

loved

If they are correct, increase their score.

------------------------------------------------------------
ADVANCED CHALLENGE
------------------------------------------------------------

Create MULTIPLE missing words.

Example:

"For God so ________ the ________, that he gave
his only begotten ________..."

The user must provide all of the missing words.

------------------------------------------------------------
EXTRA ADVANCED CHALLENGE
------------------------------------------------------------

Allow the user to choose a difficulty.

1. Easy
2. Medium
3. Hard

Easy:
One missing word.

Medium:
Two missing words.

Hard:
Three or more missing words.

------------------------------------------------------------
IMPORTANT:

Do NOT work on the advanced challenge until the
required project is completely finished and working.

============================================================
"""
