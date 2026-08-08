# Bible Adventure Game

## Code for the Future Final Project

Welcome to the Bible Adventure Game!

In this project, you will build an interactive text-based adventure game using Python.

The player will travel through a Bible-inspired adventure, make decisions, answer questions, and try to reach the end of the story.

Your goal is to combine the Python concepts you have learned throughout Code for the Future to create an interactive experience.

---

# Project Goal

Create a Bible-inspired adventure game that is:

- Interactive
- Faith-centered
- Creative
- Easy to play
- Built with Python

The player should make choices that affect what happens next in the adventure.

You will use Python to create the story, make decisions, track information, and control the flow of the game.

---

# Python Concepts You Will Practice

Your project should use:

- Variables
- Strings
- Integers
- User Input
- If Statements
- Comparisons
- Lists
- For Loops
- While Loops
- Functions
- Parameters
- Return Values
- f-Strings
- Comments

---

# Required Features

Your game must include all of the following:

- A welcome screen
- A main game loop
- At least 3 adventure sections or locations
- Player choices
- At least 3 decision points
- At least one list
- At least one function
- At least one function with a parameter
- At least one function that returns a value
- At least one `if/elif/else` decision
- At least one `while` loop
- At least one `for` loop
- At least one integer variable
- A way to track player progress
- A winning or ending screen

---

# Game Concept

The Bible Adventure Game is a text-based game.

The player reads a story and makes choices.

For example:

```text
============================================================
                  BIBLE ADVENTURE
============================================================

You find yourself standing at a crossroads.

Two paths are ahead of you.

1. Take the path through the wilderness.
2. Follow the road toward the city.

What do you choose?
```

The player's choice should determine what happens next.

---

# Creating Your Story

You get to decide what your adventure is about.

Your game could be inspired by:

- The journey of the Israelites
- David and Goliath
- The Good Samaritan
- Jonah
- Daniel
- Esther
- Paul's missionary journeys
- A fictional Bible-inspired journey
- Another Bible story or theme

You do not need to recreate a Bible story exactly.

You can create your own adventure inspired by biblical themes.

---

# Important

Your game should be respectful of Scripture.

If you create a fictional story, make it clear that the adventure is fictional and Bible-inspired.

Do not present fictional events as if they are actual events from the Bible.

---

# 1. Welcome Screen

Your game should begin with a welcome message.

For example:

```text
============================================================
                    BIBLE ADVENTURE
============================================================

Welcome, traveler!

Your journey is about to begin.

Make wise choices.
Stay faithful.
Complete your journey.

============================================================
```

You can customize the welcome message.

---

# 2. Player Name

Ask the player for their name.

Example:

```text
What is your name? Sarah
```

Then use their name throughout the game.

For example:

```text
Sarah, your journey begins now.
```

You can use an f-string:

```python
print(f"{name}, your journey begins now.")
```

---

# 3. Player Progress

Create variables to track information about the player.

For example:

```python
faith_points = 0
```

You could also track:

```python
health = 3
```

or:

```python
wisdom = 0
```

You decide what information makes sense for your game.

---

# 4. Adventure Locations

Your game should contain at least 3 different locations or sections.

For example:

```text
1. The Wilderness
2. The Village
3. The Mountain
```

Each location should have its own story or challenge.

---

# 5. Player Choices

The player should make decisions throughout the game.

For example:

```text
You arrive at a fork in the road.

1. Help the traveler.
2. Continue on your journey.

Choose:
```

Use an `if/elif/else` statement to determine what happens.

Example:

```python
if choice == "1":
    print("You decided to help the traveler.")

elif choice == "2":
    print("You continued on your journey.")

else:
    print("That is not a valid choice.")
```

---

# 6. Meaningful Decisions

Your choices should matter.

For example:

```text
You find someone who needs help.

1. Stop and help.
2. Keep walking.
```

If the player helps:

```text
You showed compassion.

Faith Points: +1
```

If they continue:

```text
You continue your journey.
```

The player's choices should affect the game in some way.

---

# 7. Use Comparisons

Use comparisons to make decisions.

For example:

```python
if faith_points >= 3:
    print("You have shown great faith.")
```

You can use:

- `>`
- `<`
- `>=`
- `<=`
- `==`
- `!=`

Think about how these can affect the player's journey.

---

# 8. Use a List

Your game must use at least one list.

You could use a list to store:

- Locations
- Challenges
- Bible verses
- Items
- Questions
- Player inventory
- Encouraging messages

Example:

```python
locations = [
    "The Wilderness",
    "The Village",
    "The Mountain"
]
```

You could then use a loop to display the locations.

---

# 9. Use a For Loop

Use a `for` loop somewhere in your game.

For example, you might use a loop to display the player's inventory:

```python
for item in inventory:
    print(item)
```

Or you could use a loop to display available locations.

Think creatively about where a loop makes sense.

---

# 10. Use a While Loop

Your game should continue running until the player reaches the end or chooses to quit.

For example:

```python
playing = True

while playing:

    # Game code

    if player_finished:
        playing = False
```

The exact structure is up to you.

---

# 11. Functions

Your project must use functions to organize your code.

You should create functions for major parts of the game.

For example:

```python
def display_menu():
    pass


def start_adventure():
    pass


def show_location():
    pass
```

Do not put your entire game inside one giant block of code.

Use functions to organize different parts of your adventure.

---

# 12. Functions With Parameters

At least one function should use a parameter.

Example:

```python
def greet_player(name):
    print(f"Welcome, {name}!")
```

Then:

```python
greet_player(player_name)
```

Think about what information your functions need.

---

# 13. Functions With Return Values

At least one function should return a value.

Example:

```python
def add_points(points):
    return points
```

You could also create a function that determines what happens based on the player's choice.

For example:

```python
def make_choice(choice):
    if choice == "1":
        return "help"

    elif choice == "2":
        return "continue"

    return "invalid"
```

Your returned value can then be used elsewhere in your program.

---

# 14. Game Ending

Your game must have an ending.

For example:

```text
============================================================
                    JOURNEY COMPLETE
============================================================

Congratulations, Sarah!

You completed your journey.

Faith Points: 5

Your choices showed courage, wisdom, and compassion.

Thank you for playing!

============================================================
```

You can create multiple endings if you want.

---

# Example Game Flow

Your game could follow a structure like this:

```text
START
  |
  v
Welcome Screen
  |
  v
Ask Player Name
  |
  v
Begin Adventure
  |
  v
Location 1
  |
  v
Player Makes Choice
  |
  v
Update Player Progress
  |
  v
Location 2
  |
  v
Player Makes Choice
  |
  v
Update Player Progress
  |
  v
Location 3
  |
  v
Final Challenge
  |
  v
Determine Ending
  |
  v
Game Over / Victory
```

---

# Suggested Game Structure

Here is one possible structure you can use.

You do not have to follow this exact story.

## Location 1: The Crossroads

The player must decide which path to take.

Possible choices:

```text
1. Take the difficult path.
2. Take the easy path.
```

The choice affects the player's progress.

---

## Location 2: The Traveler

The player encounters someone who needs help.

Possible choices:

```text
1. Stop and help.
2. Continue your journey.
```

The player's decision affects their points.

---

## Location 3: The Challenge

The player faces a final challenge.

You could ask a Bible question.

For example:

```text
Who built the ark?

1. Moses
2. Noah
3. David
4. Solomon
```

The player earns points for a correct answer.

---

## Final Ending

Use the player's progress to determine the ending.

For example:

```python
if faith_points >= 5:
    print("You completed the journey with great wisdom!")

elif faith_points >= 3:
    print("You completed the journey!")

else:
    print("Your journey is complete. Keep growing and learning!")
```

---

# Suggested Menu

You can create a menu such as:

```text
1. Start Adventure
2. Instructions
3. View Progress
4. Exit
```

You can also create your own menu.

---

# Creativity

Once you have completed the required features, customize your game.

You could add:

- Multiple endings
- A health system
- Faith points
- Wisdom points
- An inventory
- Bible questions
- Scripture references
- Different locations
- Random events
- A character class
- Difficulty levels
- A replay option
- A scoring system
- A final boss or challenge
- Different paths through the story

---

# OPTIONAL ADVANCED CHALLENGE

## Multiple Endings

Create multiple possible endings based on the player's decisions.

For example:

```text
Faith Points: 6

ENDING: FAITHFUL TRAVELER
```

or:

```text
Faith Points: 2

ENDING: THE JOURNEY CONTINUES
```

Your program should determine the ending using `if`, `elif`, and `else`.

---

# ADVANCED CHALLENGE: Inventory

Create an inventory system.

For example:

```python
inventory = [
    "Bread",
    "Water",
    "Scroll"
]
```

Allow the player to collect items throughout the game.

The player could then use those items later.

For example:

```text
You found a Scroll!

The Scroll has been added to your inventory.
```

Later:

```text
Your inventory:

1. Bread
2. Water
3. Scroll
```

---

# ADVANCED CHALLENGE: Bible Quiz

Add Bible questions to your adventure.

Store your questions in a list.

Example:

```python
questions = [
    "Who built the ark?",
    "Who defeated Goliath?",
    "Who was swallowed by a great fish?"
]
```

Create a matching list of answers.

Then use a loop to ask the player questions.

Correct answers could increase the player's points.

---

# EXTRA ADVANCED CHALLENGE: Multiple Paths

Create different paths through the game.

For example:

```text
Path A
  |
  v
Village
  |
  v
Mountain
  |
  v
Ending A
```

while another choice leads to:

```text
Path B
  |
  v
Wilderness
  |
  v
River
  |
  v
Ending B
```

The player's decisions determine which path they follow.

---

# Project Development Steps

Do not try to build everything at once.

Build your project in stages.

## Step 1: Create Your Story

Before coding, decide:

- What is your game about?
- Who is the player?
- Where does the adventure take place?
- What are the major locations?
- What choices will the player make?
- How does the player win?
- How can the player lose or reach another ending?

Write down your plan before coding.

---

## Step 2: Create Your Variables

Decide what information your game needs.

For example:

```python
player_name = ""
faith_points = 0
playing = True
```

---

## Step 3: Create Your Lists

Add lists for information your game needs.

For example:

```python
locations = [
    "The Wilderness",
    "The Village",
    "The Mountain"
]
```

---

## Step 4: Create Your Functions

Break your game into smaller pieces.

For example:

```python
def display_menu():
    pass


def start_adventure():
    pass


def show_location(location):
    pass
```

---

## Step 5: Build Your First Location

Get one location working before building the entire game.

Make sure:

- The story displays.
- The player can make a choice.
- The choice produces the correct result.

---

## Step 6: Add Your Other Locations

Once the first location works, add the rest of your adventure.

---

## Step 7: Add Progress

Add your points, inventory, health, or other game information.

---

## Step 8: Add Your Ending

Create a clear ending for the player.

---

## Step 9: Test Your Game

Play through your entire game.

Test every possible choice.

Make sure your game does not crash.

---

## Step 10: Add Advanced Features

Only after your required project works should you add advanced features.

Try:

- Multiple endings
- Inventory
- Bible quiz
- Multiple paths
- Difficulty levels

---

# Testing Your Program

Test every part of your game.

Make sure:

- The welcome screen works.
- The player's name is saved.
- The first location displays.
- Choices work.
- Invalid choices are handled.
- Points update correctly.
- Lists work.
- Loops work.
- Functions work.
- The game reaches an ending.
- The player can exit.
- The program does not crash.

Also test unexpected input.

For example:

```text
Choose an option: pizza
```

Your program should handle this appropriately.

---

# Code Quality

Your code should:

- Use meaningful variable names.
- Include comments where helpful.
- Use functions to organize your code.
- Avoid unnecessary repeated code.
- Be properly indented.
- Be easy for another person to understand.
- Run without errors.

---

# Submission Checklist

Before submitting your project, make sure:

- [ ] My program runs without errors.
- [ ] I have a welcome screen.
- [ ] I ask the player for their name.
- [ ] I have at least 3 adventure sections.
- [ ] The player makes at least 3 choices.
- [ ] My choices affect the game.
- [ ] I use variables.
- [ ] I use strings.
- [ ] I use integers.
- [ ] I use user input.
- [ ] I use if/elif/else statements.
- [ ] I use comparisons.
- [ ] I use at least one list.
- [ ] I use a for loop.
- [ ] I use a while loop.
- [ ] I use functions.
- [ ] I use a function with a parameter.
- [ ] I use a function with a return value.
- [ ] I track player progress.
- [ ] My game has an ending.
- [ ] I added comments.
- [ ] I tested my game.
- [ ] I customized my adventure.

---

# Final Presentation

During the Code for the Future Final Showcase, you will demonstrate your Bible Adventure Game.

Be prepared to explain:

## 1. What Your Game Does

Give a short explanation of your adventure.

## 2. Why You Chose Your Story

Explain the Bible story, theme, or biblical principle that inspired your game.

## 3. How You Used Variables

Show how you tracked information about the player.

## 4. How You Used Lists

Explain what information you stored in a list.

## 5. How You Used Loops

Explain where you used your `for` and `while` loops.

## 6. How You Used Functions

Explain how functions helped organize your game.

## 7. How Your Decisions Work

Show how player choices affect what happens.

## 8. A Challenge You Encountered

Explain something that was difficult and how you solved it.

## 9. Something You Learned

Share one programming concept or lesson you learned.

---

# Final Showcase Tips

During your presentation:

1. Introduce your game.
2. Explain the story.
3. Explain what inspired it.
4. Demonstrate the game.
5. Show an interesting piece of code.
6. Explain one challenge you overcame.
7. Explain how your game connects to serving God and others.

You do not need to explain every line of code.

Focus on the parts you are most proud of.

---

# Remember the Mission

Code for the Future is about more than learning how to program.

Our goal is:

**Using technology to serve God and others.**

Think about how your game can encourage players to learn about biblical principles while having fun.

Build something creative.

Build something meaningful.

Keep learning.

**Good luck!**
