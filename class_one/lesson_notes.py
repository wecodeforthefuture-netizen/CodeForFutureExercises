# ============================================================
#  LESSON 1 REFERENCE GUIDE -- Read this alongside bible_app.py
#  Run this file anytime to see the examples in action!
# ============================================================


# ------------------------------------------------------------
# CONCEPT 1: print()
# ------------------------------------------------------------
# print() is a FUNCTION -- it does a job for you.
# Its job: display text on the screen.
# Text inside quotes is called a STRING.

print("--- CONCEPT 1: print() ---")
print("God is good!")
print("All the time!")

# You can print multiple things separated by a comma:
print("Chapter", 1, "Verse", 1)


# ------------------------------------------------------------
# CONCEPT 2: Strings
# ------------------------------------------------------------
# A STRING is any text wrapped in quotes.
# You can use single quotes '' or double quotes ""

print("")
print("--- CONCEPT 2: Strings ---")
print("This is a string with double quotes")
print('This is a string with single quotes')

# Strings can hold Bible verses, names, sentences -- anything text!
print("In the beginning God created the heavens and the earth.")


# ------------------------------------------------------------
# CONCEPT 3: Variables
# ------------------------------------------------------------
# A VARIABLE is a named container that holds a value.
# You create one using the = sign (called "assignment").
#
#   variable_name = value
#
# Rules for naming variables:
#   - No spaces (use underscores instead: my_verse)
#   - No special characters like ! or @
#   - Start with a letter, not a number

print("")
print("--- CONCEPT 3: Variables ---")

greeting = "Peace be with you"
verse_reference = "John 3:16"
chapter_number = 3

print(greeting)
print(verse_reference)
print(chapter_number)

# You can change a variable's value anytime:
greeting = "Grace and peace to you"
print(greeting)


# ------------------------------------------------------------
# CONCEPT 4: input()
# ------------------------------------------------------------
# input() pauses the program and waits for the user to type.
# Whatever they type is saved as a STRING.
#
#   name = input("Ask a question here: ")
#
# NOTE: The text inside input() is the PROMPT -- what the
# user sees before they type. Always end it with a space!

print("")
print("--- CONCEPT 4: input() ---")

name = input("What is your name? ")
print("Nice to meet you,", name)


# ------------------------------------------------------------
# CONCEPT 5: f-strings (formatted strings)
# ------------------------------------------------------------
# An f-string lets you drop variables RIGHT INTO your text.
# Put  f  before the opening quote, then use { } around
# any variable you want to include.
#
#   print(f"Hello, {name}!")

print("")
print("--- CONCEPT 5: f-strings ---")

book = input("What book of the Bible are you reading? ")

print(f"Hi {name}! Reading {book} is a great choice!")
print(f"May God speak to you through {book} today.")


# ============================================================
#  Remember: The best way to learn is to experiment!
#  Change the code, break things, and try again.
#  Romans 8:28 -- all things work together for good!
# ============================================================
