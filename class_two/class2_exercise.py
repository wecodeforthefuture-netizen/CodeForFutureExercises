# CODE FOR THE FUTURE
# CLASS 2 EXERCISE: Bible Verse Encouragement App
#
# Topics:
#   - print()
#   - variables
#   - input()
#   - string formatting with f-strings
#   - comparison operators
#   - if / elif / else
#   - logical operators
#
# HOW TO USE THIS FILE:
#   1. Follow along with your instructor.
#   2. Write code where you see: YOUR CODE HERE
#   3. Run the program after each section.
#   4. Read error messages carefully and ask questions.
# ============================================================


# ------------------------------------------------------------
# SECTION 1: Welcome Message
# ------------------------------------------------------------
# Print a title for the app.
#
# Example:
# ========================================
#       BIBLE VERSE ENCOURAGEMENT APP
# ========================================

# YOUR CODE HERE



# ------------------------------------------------------------
# SECTION 2: Ask for the User's Name
# ------------------------------------------------------------
# Use input() to ask the user for their name.
# Store the answer in a variable called name.
#
# Example:
# name = input("What is your name? ")

# YOUR CODE HERE



# ------------------------------------------------------------
# SECTION 3: Display a Menu
# ------------------------------------------------------------
# Show the user the following choices:
#
# 1 - I feel worried
# 2 - I feel tired
# 3 - I feel thankful
# 4 - I need courage
# 5 - I need guidance

# YOUR CODE HERE



# ------------------------------------------------------------
# SECTION 4: Get the User's Choice
# ------------------------------------------------------------
# Ask the user to enter a number from 1 to 5.
#
# IMPORTANT:
# input() returns a STRING, so compare the answer to
# "1", "2", "3", "4", or "5" using quotation marks.

# YOUR CODE HERE



# ------------------------------------------------------------
# SECTION 5: Make a Decision
# ------------------------------------------------------------
# Use if / elif / else to display a Bible verse and an
# encouraging message based on the user's choice.
#
# Suggested verses:
#
# 1 - Philippians 4:6-7
#     "Do not be anxious about anything..."
#
# 2 - Matthew 11:28
#     "Come to me, all you who are weary..."
#
# 3 - Psalm 100:4
#     "Enter his gates with thanksgiving..."
#
# 4 - Joshua 1:9
#     "Be strong and courageous..."
#
# 5 - Proverbs 3:5-6
#     "Trust in the Lord with all your heart..."
#
# Use an f-string to include the user's name.
#
# Example:
#
# if choice == "1":
#     print(f"\n{name}, remember Philippians 4:6-7.")
#     print("You can bring every worry to God.")
#
# Add the remaining choices with elif.
# Add an else for invalid input.

# YOUR CODE HERE



# ------------------------------------------------------------
# SECTION 6: Boolean Check
# ------------------------------------------------------------
# Create a Boolean variable called valid_choice.
#
# It should be True when the user's choice is one of:
# "1", "2", "3", "4", or "5"
#
# Use the logical operator or.
#
# Example pattern:
# valid_choice = choice == "1" or choice == "2"
#
# Continue the pattern for all five choices.
# Then print the value of valid_choice.

# YOUR CODE HERE



# ------------------------------------------------------------
# SECTION 7: Closing Message
# ------------------------------------------------------------
# If valid_choice is True, print:
# "Thank you for using the Bible Verse Encouragement App!"
#
# Otherwise, print:
# "Please run the program again and choose a number from 1 to 5."

# YOUR CODE HERE



# ============================================================
# OPTIONAL CHALLENGE
# ============================================================
# Ask the user:
# "Would you like to save this verse for later? yes or no: "
#
# Use .lower() so YES, Yes, and yes are treated the same.
#
# If the answer is "yes", print an encouraging response.
# If the answer is "no", print a different response.
# Otherwise, print "Please enter yes or no."

# YOUR CODE HERE



# ============================================================
# GREAT JOB!
# You created an interactive program that makes decisions.
# ============================================================


