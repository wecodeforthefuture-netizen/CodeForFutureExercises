name = "Ayo"
#name is a variable
# "Ayo" is a string
# type of name = string


age = 15

# age is a variable
# 15 is an integer
# type of age = integer

is_cool = False
# is_cool is a variable
# False is a boolean
# type of is_cool = boolean
# school = "Central High"


# print("Hello my name is " + name + " and I am " + str(age))
# print(f"Hello my name is {name} and I am {age}")






# Create a variable called school and store your school name in it.
# Print the sentence "My name is --- and I attend _______" using your variable.

# print("My name is " + name + " and I attend " + school)
# print(f"My name is {name} and I attend {school}")
 









# ============================================================
# name = "Sarah"
# age = 15
# school = "Central High"

# print("Hello " + name + ".")
# print("You are " + str(age) + " years old.")
# print("You attend " + school + ".")


# print(f"Hello my name is {name}. I am {age} years old. I attend {school}.")

# print(f"hi {name}")

print(100>1)

num_one = 23
value_two = "23"

print(num_one == value_two)




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

print("========================================")
print("      BIBLE VERSE ENCOURAGEMENT APP")
print("========================================")


# ------------------------------------------------------------
# SECTION 2: Ask for the User's Name
# ------------------------------------------------------------
# Use input() to ask the user for their name.
# Store the answer in a variable called name.
#
# Example:
# name = input("What is your name? ")

# YOUR CODE HERE
name = input("What is your name? ")



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
print("This is the menu")
print("1 - I feel worried")
print("2 - I feel tired")
print("3 - I feel thankful")



# ------------------------------------------------------------
# SECTION 4: Get the User's Choice
# ------------------------------------------------------------
# Ask the user to enter a number from 1 to 5.
#
# IMPORTANT:
# input() returns a STRING, so compare the answer to
# "1", "2", "3", "4", or "5" using quotation marks.

# YOUR CODE HERE

choice = input("Enter a number from 1 to 3: ")
# Choice will store a string number




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
if choice == "1":
  print(f"My name is {name} and I feel worried")
if choice == "2":
  print(f"My name is {name} and I feel tired")
if choice == "3":
  print(f"My name is {name} and I feel thankful")
  
# score = 40

score = int(input("Enter your score: "))

# Using input will make score a string so we have to convert it to an integer by putting int()
if score > 90:
  print("You got an A")
elif score > 80:
  print("You got a B")
elif score > 70:
  print("You got a C")
else:
  print("Keep practicing")


# ------------------------------------------------------------
# SECTION 6: Boolean Check
# ------------------------------------------------------------
# Create a Boolean variable called valid_choice.
# Create a score and set to 0 and increment by 10 for each correct answer
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

score = 0
if choice == "1" or choice == "2" or choice == "3":
  valid_choice = True
  score += 10
print(score)
  



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
question = input("Would you like to save this verse for later? yes or no: ")
if question.lower() == "yes":
  print("Great!")
else:
  print("Okay")


# ============================================================
# GREAT JOB!
# You created an interactive program that makes decisions.
# ============================================================
