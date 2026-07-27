# CODE FOR THE FUTURE
# ASSIGNMENT 2: Bible Knowledge Quiz
#
# Topics:
#   - print()
#   - variables
#   - input()
#   - int()
#   - f-strings
#   - booleans
#   - comparison operators
#   - if / elif / else
#   - logical operators
#   - score tracking
#
# Name: ______________________________________
#
# DIRECTIONS:
#   1. Complete every required section.
#   2. Write code where you see: YOUR CODE HERE
#   3. Run your program after each question.
#   4. Fix all errors before submitting.
#   5. Submit this completed .py file to Google Classroom.
# ============================================================


# ------------------------------------------------------------
# SECTION 1: Welcome the Player
# ------------------------------------------------------------
# Print a title for your quiz.
#
# Ask the player for:
#   - their name
#   - their age
#
# HINT:
# Use input()

# Convert the age to an integer using int().
# HINT:
# count = int(input()) 
# count is originally a string, but we put int() in front of it to convert to an integer.
# 
#Then use an f-string to welcome the player.
# Example:
# Welcome, Mary! You are 14 years old.

# YOUR CODE HERE



# ------------------------------------------------------------
# SECTION 2: Create the Score
# ------------------------------------------------------------
# Create a variable called score and set it equal to 0.

# YOUR CODE HERE



# ------------------------------------------------------------
# QUESTION 1
# ------------------------------------------------------------
# Ask:
# Who built the ark?
#
# a - Moses
# b - Noah
# c - David
#
# Use input() to collect the answer.
# Use .lower() so B and b are both accepted.

#Example:
# text = "Hello WORLD!"
# lowercase_text = text.lower()
# uppercase_text = text.upper()
# If you print(lowercase_text), the result will be "hello world". This means .lower() converts string to lowercase. 
# The opposite is .upper(); it will convert the string to uppercase
# Look at class2_exercise.py in the challenge section to see how we use .lower() in the code.



# If the answer is b:
#   - print "Correct!"
#   - add 1 to score
#HINT: To add 1 to the score, type the code below.
#score = score + 1 
# Look at class2_exercise.py to see how to use score in your homework
# Otherwise:
#   - print "Incorrect. The answer is Noah."

# YOUR CODE HERE



# ------------------------------------------------------------
# QUESTION 2
# ------------------------------------------------------------
# Ask:
# Who defeated Goliath?
#
# a - David
# b - Peter
# c - Joshua
#
# Use if / else.
# Add 1 to score for the correct answer.

# YOUR CODE HERE



# ------------------------------------------------------------
# QUESTION 3
# ------------------------------------------------------------
# Ask:
# What is the first book of the Bible?
#
# a - Matthew
# b - Psalms
# c - Genesis
#
# Use if / else.
# Add 1 to score for the correct answer.

# YOUR CODE HERE



# ------------------------------------------------------------
# QUESTION 4
# ------------------------------------------------------------
# Ask:
# Jesus was born in which city?
#
# a - Bethlehem
# b - Jerusalem
# c - Nazareth
#
# Use if / else.
# Add 1 to score for the correct answer.

# YOUR CODE HERE



# ------------------------------------------------------------
# QUESTION 5
# ------------------------------------------------------------
# Ask:
# How many disciples did Jesus choose?
#
# a - 7
# b - 10
# c - 12
#
# Use if / else.
# Add 1 to score for the correct answer.

# YOUR CODE HERE



# ------------------------------------------------------------
# SECTION 3: Display the Final Score
# ------------------------------------------------------------
# Print the player's name and final score using an f-string.
#
# Example:
# Mary, you scored 4 out of 5!

# YOUR CODE HERE



# ------------------------------------------------------------
# SECTION 4: Give Feedback
# ------------------------------------------------------------
# Use if / elif / else to print one result:
#
# Score of 5:
# "Excellent! You got every question correct!"
#
# Score of 3 or 4:
# "Great job! Keep studying God's Word!"
#
# Score of 0, 1, or 2:
# "Good effort! Keep learning and try again!"
#
# IMPORTANT:
# Check the highest score first.

# YOUR CODE HERE



# ------------------------------------------------------------
# SECTION 5: Boolean Reflection
# ------------------------------------------------------------
# Create a Boolean variable called passed.
#
# passed should be True when score is greater than or equal to 3.
#
# Print:
# Passed quiz: True
# or
# Passed quiz: False
#
# Use an f-string.

# YOUR CODE HERE



# ------------------------------------------------------------
# SECTION 6: Age-Based Encouragement - BONUS POINTS
# ------------------------------------------------------------
# Use the player's age and score together.
# Look at class slides to help you
#
# If the player is under 13 AND scored at least 3:
#     print "Amazing work for a young Bible scholar!"
#
# Elif the player is 13 or older AND scored at least 3:
#     print "Excellent work! Keep growing in wisdom!"
#
# Else:
#     print "Keep practicing—you are still learning!"
#
# Use the logical operator and.

# YOUR CODE HERE



# ============================================================
# CHALLENGE SECTION (OPTIONAL)
# ============================================================
# Add a sixth question of your own.
#
# Requirements:
#   - It must be Bible-based.
#   - It must have at least three answer choices.
#   - It must use input().
#   - It must use if / else.
#   - It must add 1 to score when correct.
#
# After adding the question, update the final score message
# so it says "out of 6" instead of "out of 5."

# YOUR CODE HERE



# ============================================================
# BONUS CHALLENGE (OPTIONAL)
# ============================================================
# Ask the player to choose a difficulty:
#
# 1 - Beginner
# 2 - Advanced
#
# If they choose Beginner, print:
# "You chose the Beginner quiz."
#
# If they choose Advanced, print:
# "You chose the Advanced quiz."
#
# Otherwise, print:
# "Invalid choice."
#
# You do not need to create separate questions for each level yet.

# YOUR CODE HERE



# ============================================================
# SUBMISSION CHECKLIST
# ============================================================
# Before submitting, make sure:
#
# [ ] Your name is written at the top.
# [ ] All five required questions work.
# [ ] Your score increases for correct answers.
# [ ] Your program uses if / elif / else.
# [ ] Your program uses at least one Boolean.
# [ ] Your program uses at least one logical operator.
# [ ] Your program runs without errors.
#
# Great work! Keep using technology to serve God and others.
# ============================================================

