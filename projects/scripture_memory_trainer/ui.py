"""
============================================================
Code for the Future
Shared Terminal UI

This file provides the visual design for the student
projects.

Students do NOT need to modify this file.

The functions in this file can be imported into a project
using:

    from ui import *

============================================================
"""


# ============================================================
# TERMINAL FORMATTING
# ============================================================

WIDTH = 60


def divider():
    """
    Prints a horizontal divider.
    """

    print("=" * WIDTH)


def line():
    """
    Prints a smaller horizontal line.
    """

    print("-" * WIDTH)


def title(text):
    """
    Displays a large title.
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
# GAME / QUIZ MESSAGES
# ============================================================

def correct():
    """
    Displays a correct-answer message.
    """

    print()
    print("Correct!")
    print("Great job!")
    print()


def incorrect():
    """
    Displays an incorrect-answer message.
    """

    print()
    print("Not quite.")
    print("Keep practicing!")
    print()


# ============================================================
# SCORE DISPLAY
# ============================================================

def score_display(score, total):
    """
    Displays a score.

    Example:

    Score: 4 / 5
    """

    print()
    line()
    print(f"Score: {score} / {total}".center(WIDTH))
    line()
    print()


def progress_display(score, practiced):
    """
    Displays user progress.
    """

    print()
    line()
    print("YOUR PROGRESS".center(WIDTH))
    line()

    print(f"Score: {score}")
    print(f"Verses Practiced: {practiced}")

    line()
    print()


# ============================================================
# VERSE DISPLAY
# ============================================================

def display_verse(reference, verse):
    """
    Displays a Bible verse in a formatted section.

    Example:

    Reference: John 3:16

    "For God so loved the world..."
    """

    print()
    line()

    print(f"Reference: {reference}")

    print()

    print(f'"{verse}"')

    line()
    print()


# ============================================================
# MENU DISPLAY
# ============================================================

def menu_option(number, text):
    """
    Displays a single menu option.

    Example:

    1. Practice a Verse
    """

    print(f"{number}. {text}")


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
# GOODBYE
# ============================================================

def goodbye():
    """
    Displays the goodbye message.
    """

    print()
    divider()
    print("Thank you for using the Scripture Memory Trainer!".center(WIDTH))
    print("Keep God's Word in your heart!".center(WIDTH))
    divider()
    print()


# ============================================================
# WELCOME
# ============================================================

def welcome():
    """
    Displays a welcome message.
    """

    title("Scripture Memory Trainer")

    print("Grow in God's Word.".center(WIDTH))
    print("Practice. Remember. Apply.".center(WIDTH))

    print()


# ============================================================
# MEMORY CHALLENGE
# ============================================================

def challenge_header():
    """
    Displays the memory challenge header.
    """

    print()
    line()
    print("MEMORY CHALLENGE".center(WIDTH))
    line()
    print()


# ============================================================
# FINAL MESSAGE
# ============================================================

def final_message():
    """
    Displays an encouraging final message.
    """

    print()
    divider()
    print("Keep studying God's Word!".center(WIDTH))
    print("Great work!".center(WIDTH))
    divider()
    print()
