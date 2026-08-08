"""
============================================================
Code for the Future
Shared Terminal UI

Bible Adventure Game

Students do NOT need to modify this file.

This file provides the visual formatting and reusable
functions for the student project.

Students can use these functions by writing:

    from ui import *

============================================================
"""


WIDTH = 60


# ============================================================
# BASIC FORMATTING
# ============================================================

def divider():
    """
    Prints a large horizontal divider.
    """

    print("=" * WIDTH)


def line():
    """
    Prints a smaller horizontal divider.
    """

    print("-" * WIDTH)


def title(text):
    """
    Displays a large centered title.
    """

    print()
    divider()
    print(text.center(WIDTH))
    divider()
    print()


def section(text):
    """
    Displays a section heading.
    """

    print()
    line()
    print(text.center(WIDTH))
    line()
    print()


# ============================================================
# MESSAGES
# ============================================================

def success(message):
    """
    Displays a success message.
    """

    print()
    print("[SUCCESS] " + message)
    print()


def error(message):
    """
    Displays an error message.
    """

    print()
    print("[ERROR] " + message)
    print()


def info(message):
    """
    Displays an informational message.
    """

    print()
    print("[INFO] " + message)
    print()


def warning(message):
    """
    Displays a warning message.
    """

    print()
    print("[WARNING] " + message)
    print()


# ============================================================
# CHOICE MESSAGES
# ============================================================

def choice_header():
    """
    Displays a heading for player choices.
    """

    print()
    line()
    print("MAKE YOUR CHOICE".center(WIDTH))
    line()
    print()


def invalid_choice():
    """
    Displays an invalid-choice message.
    """

    print()
    print("That is not a valid choice.")
    print("Please try again.")
    print()


# ============================================================
# ADVENTURE MESSAGES
# ============================================================

def adventure_start():
    """
    Displays the beginning of the adventure.
    """

    print()
    divider()
    print("YOUR ADVENTURE BEGINS".center(WIDTH))
    divider()
    print()


def journey_complete():
    """
    Displays a journey-complete message.
    """

    print()
    divider()
    print("JOURNEY COMPLETE".center(WIDTH))
    divider()
    print()


def victory():
    """
    Displays a victory message.
    """

    print()
    line()
    print("VICTORY!".center(WIDTH))
    line()
    print()
    print("You completed your journey!")
    print()


def try_again():
    """
    Displays an encouraging message.
    """

    print()
    line()
    print("THE JOURNEY CONTINUES".center(WIDTH))
    line()
    print()
    print("Every journey gives us an opportunity to learn.")
    print()


# ============================================================
# PLAYER PROGRESS
# ============================================================

def display_points(points):
    """
    Displays the player's current points.
    """

    print()
    line()
    print(f"Faith Points: {points}".center(WIDTH))
    line()
    print()


def display_stat(name, value):
    """
    Displays a player statistic.

    Example:

    Faith Points: 5
    """

    print(f"{name}: {value}")


# ============================================================
# INVENTORY
# ============================================================

def inventory_header():
    """
    Displays the inventory heading.
    """

    print()
    line()
    print("INVENTORY".center(WIDTH))
    line()
    print()


def display_inventory(inventory):
    """
    Displays items in the player's inventory.

    This function accepts a list of items.
    """

    inventory_header()

    if len(inventory) == 0:

        print("Your inventory is empty.")

    else:

        for item in inventory:

            print(f"- {item}")

    print()


# ============================================================
# BIBLE VERSE
# ============================================================

def display_verse(reference, verse):
    """
    Displays a Bible verse.
    """

    print()
    line()

    print(f"Reference: {reference}")

    print()

    print(f'"{verse}"')

    line()
    print()


# ============================================================
# QUIZ
# ============================================================

def quiz_header():
    """
    Displays the Bible quiz heading.
    """

    print()
    line()
    print("BIBLE CHALLENGE".center(WIDTH))
    line()
    print()


def correct():
    """
    Displays a correct-answer message.
    """

    print()
    print("Correct!")
    print("You earned a point!")
    print()


def incorrect():
    """
    Displays an incorrect-answer message.
    """

    print()
    print("Not quite.")
    print("Keep learning and try again!")
    print()


# ============================================================
# PAUSE
# ============================================================

def pause():
    """
    Pauses the program until the user presses ENTER.
    """

    print()
    input("Press ENTER to continue...")


# ============================================================
# WELCOME
# ============================================================

def welcome():
    """
    Displays the game's welcome screen.
    """

    print()
    divider()
    print("BIBLE ADVENTURE".center(WIDTH))
    divider()

    print()
    print("An interactive journey inspired by Scripture.".center(WIDTH))
    print("Make wise choices. Stay faithful. Keep learning.".center(WIDTH))
    print()

    divider()
    print()


# ============================================================
# GOODBYE
# ============================================================

def goodbye():
    """
    Displays the goodbye screen.
    """

    print()
    divider()
    print("THANK YOU FOR PLAYING!".center(WIDTH))
    print()
    print("Keep learning. Keep growing. Keep serving.".center(WIDTH))
    divider()
    print()
