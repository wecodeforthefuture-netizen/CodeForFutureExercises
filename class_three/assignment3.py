# CODE FOR THE FUTURE
# CLASS 3 PRACTICE: BUILD A LOOPING BIBLE QUIZ
#
# Topics:
#   - Lists
#   - List indexing
#   - len()
#   - for loops
#   - range()
#   - input()
#   - if / else
#   - Score tracking
#   - f-strings
#
# HOW TO USE THIS FILE:
#   1. Build each section with your instructor.
#   2. Run the program after every section.
#   3. Do not move ahead until you understand the current step.
# ============================================================


# ------------------------------------------------------------
# STEP 1: CREATE A LIST OF QUESTIONS
# ------------------------------------------------------------
# A list allows us to store several questions in one variable.
#
# IMPORTANT:
# The questions and answers must stay in the same order.
#
# questions[0] matches answers[0]
# questions[1] matches answers[1]



# ------------------------------------------------------------
# STEP 2: CREATE A LIST OF ANSWERS
# ------------------------------------------------------------
# Store all answers in lowercase because we will convert the
# player's response to lowercase before comparing it.



# ------------------------------------------------------------
# STEP 3: CREATE A SCORE VARIABLE
# ------------------------------------------------------------
# The player begins with zero points.



# ------------------------------------------------------------
# STEP 4: PRINT A WELCOME MESSAGE
# ------------------------------------------------------------

print("===================================")
print("        BIBLE QUIZ GAME")
print("===================================")
print()


# ------------------------------------------------------------
# STEP 5: LOOP THROUGH EVERY QUESTION
# ------------------------------------------------------------
# len(questions) tells us how many questions are in the list.
#
# range(len(questions)) produces the indexes:
# 0, 1, 2, 3
#
# The variable i stores the current index during each loop.




# ------------------------------------------------------------
# STEP 6: PRINT THE FINAL SCORE
# ------------------------------------------------------------

print("===================================")
print("           QUIZ COMPLETE")
print("===================================")



# ------------------------------------------------------------
# STEP 7: PRINT A FINAL MESSAGE
# ------------------------------------------------------------



# ============================================================
# IN-CLASS PRACTICE QUESTIONS
# ============================================================
#
# 1. Why do questions and answers need to stay in the same order?
#
# 2. What does len(questions) return?
#
# 3. What values does i hold during this program?
#
# 4. Why do we write questions[i] instead of questions[0]?
#
# 5. Why do we use .lower() on the user's answer?
#
# 6. What line increases the player's score?
#
# 7. What would happen if we added a fifth question but forgot
#    to add a fifth answer?
#
# ============================================================


# ============================================================
# HOMEWORK: IMPROVE YOUR BIBLE QUIZ
# ============================================================
#
# Complete the improvements below in this same file or in the
# assignment file provided by your instructor.
#
# REQUIRED IMPROVEMENTS:
#
# 1. Add at least TWO new questions.
#
# 2. Add the matching answers in the correct order.
#
# 3. Ask the player for their name before the quiz begins.
#
# 4. Use an f-string to print:
#       "Welcome to the Bible Quiz, NAME!"
#
# 5. Change the final message so it includes the player's name.
#
# 6. Add an elif condition:
#
#       Perfect score:
#           "Outstanding!"
#
#       At least half correct:
#           "Nice job!"
#
#       Less than half:
#           "Keep practicing!"
#
# 7. Add at least THREE comments that explain your code.
#
#
# OPTIONAL CHALLENGES:
#
# 1. Use .strip().lower() instead of only .lower().
#
# 2. Print the current score after every question.
#
# 3. Add a title or decoration of your own.
#
# 4. Add a category variable, such as:
#       category = "Old Testament"
#
# 5. Create separate lists for Old Testament and
#    New Testament questions.
#
# ============================================================


