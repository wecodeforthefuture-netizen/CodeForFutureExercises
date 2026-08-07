# Scripture Memory Trainer

## Code for the Future Final Project

Welcome to the Scripture Memory Trainer project!

In this project, you will build a Python application that helps users practice memorizing Bible verses.

Your application will allow users to view Scripture, choose a verse to practice, answer a memory challenge, and track their progress.

This project is an opportunity to combine the Python concepts you have learned throughout Code for the Future.

---

# Project Goal

Create a Scripture memory application that is:

- Interactive
- Encouraging
- Easy to use
- Faith-centered
- Built with Python

Your goal is not just to make a program that works. Think about how your application could actually help someone spend time in God's Word.

---

# Python Concepts You Will Practice

Your project should use the following concepts:

- Variables
- Strings
- Integers
- Lists
- User Input
- If Statements
- For Loops
- While Loops
- Functions
- f-Strings
- Comments

---

# Required Features

Your application must include all of the following:

## 1. Main Menu

Your program should have a menu that allows the user to choose what they want to do.

For example:

```text
============================================================
              SCRIPTURE MEMORY TRAINER
============================================================

1. Practice a Verse
2. View Verses
3. View Progress
4. Exit

Choose an option:
```

You may customize the menu as long as your program has these basic features.

---

## 2. At Least 5 Bible Verses

Your program must contain at least 5 Bible verses.

Store your verses inside a list.

Example:

```python
verses = [
    "For God so loved the world...",
    "I can do all things through Christ...",
    "The Lord is my shepherd..."
]
```

Choose the verses yourself.

Try to choose verses that would be meaningful or useful for someone who is trying to grow in their faith.

---

## 3. Bible References

Create a second list containing the references for your verses.

Example:

```python
references = [
    "John 3:16",
    "Philippians 4:13",
    "Psalm 23:1"
]
```

The positions in the two lists should match.

For example:

```text
verses[0]      → John 3:16 verse
references[0]  → John 3:16

verses[1]      → Philippians 4:13 verse
references[1]  → Philippians 4:13
```

---

# 4. View Verses

Your program should allow the user to view the Bible verses stored in the application.

Use a `for` loop to display each verse and its reference.

For example:

```text
------------------------------------------------------------
                    BIBLE VERSES
------------------------------------------------------------

1. John 3:16
   For God so loved the world...

2. Philippians 4:13
   I can do all things through Christ...

3. Psalm 23:1
   The Lord is my shepherd...
```

---

# 5. Practice a Verse

Your program should allow the user to select a verse to practice.

The basic process should be:

```text
Choose a verse

        ↓

Display the verse

        ↓

Give the user a memory challenge

        ↓

Get their answer

        ↓

Check their answer

        ↓

Give feedback

        ↓

Update their progress
```

---

# 6. Memory Challenge

Create a simple memory challenge.

For the required version, keep the challenge manageable.

For example:

```text
------------------------------------------------------------
                  MEMORY CHALLENGE
------------------------------------------------------------

Reference: John 3:16

"For God so loved the world..."

What is one word from this verse?

> loved

Correct!

Great job!
```

You could also ask the user to type a specific word.

For example:

```text
What word comes after "For God so"?

> loved
```

The important part is that your program:

1. Asks the user a question.
2. Gets their answer.
3. Uses an `if` statement to check the answer.
4. Gives feedback.
5. Updates the user's progress.

---

# 7. Track Progress

Your application should keep track of the user's progress.

You could create a score system such as:

```text
Current Score: 3
```

Or:

```text
Verses Practiced: 4
Correct Answers: 3
```

You decide how you want your progress system to work.

---

# 8. Functions

Your project must use functions to organize your code.

You should have functions for major parts of your application.

For example:

```python
def display_menu():
    pass


def view_verses():
    pass


def practice_verse():
    pass


def view_progress():
    pass
```

You may create additional functions if they help organize your program.

---

# 9. Loops

Your project must use loops.

## For Loop

Use a `for` loop when you need to go through your list of verses.

For example, you may use a loop to display all of your verses.

## While Loop

Use a `while` loop to keep your main menu running until the user chooses to exit.

Your application should continue showing the menu until the user chooses the Exit option.

---

# 10. If Statements

Your project must use `if`, `elif`, and `else` statements.

You will need them to:

- Handle menu choices
- Check answers
- Give feedback
- Handle invalid choices

Example:

```python
if choice == "1":
    practice_verse()

elif choice == "2":
    view_verses()

else:
    print("Invalid choice.")
```

---

# 11. User Input

Your program should interact with the user.

Use `input()` to allow the user to:

- Choose a menu option
- Select a verse
- Answer a memory challenge

Example:

```python
choice = input("Choose an option: ")
```

Remember that `input()` returns a string.

If you need the user to enter a number that you will use as an integer, you may need to convert it.

Example:

```python
choice = int(input("Choose a verse: "))
```

---

# 12. String Methods

You may need to use string methods to make your program easier to use.

For example:

```python
answer = answer.lower()
```

This allows you to compare the user's answer without worrying about capitalization.

For example:

```text
Loved
LOVED
loved
```

can all become:

```text
loved
```

---

# Example Program Flow

Your finished application could work like this:

```text
START

   ↓

Main Menu

   ↓

User chooses "Practice a Verse"

   ↓

Display available verses

   ↓

User selects a verse

   ↓

Display verse

   ↓

Memory Challenge

   ↓

User enters answer

   ↓

Check answer

   ↓

Update Score

   ↓

Return to Main Menu

   ↓

User chooses Exit

   ↓

Goodbye
```

---

# Example Final Program

Your finished program could look something like this:

```text
============================================================
              SCRIPTURE MEMORY TRAINER
============================================================

1. Practice a Verse
2. View Verses
3. View Progress
4. Exit

Choose an option: 1

------------------------------------------------------------
                  PRACTICE A VERSE
------------------------------------------------------------

Choose a verse:

1. John 3:16
2. Philippians 4:13
3. Psalm 23:1
4. Proverbs 3:5
5. Jeremiah 29:11

Choose a verse: 1

------------------------------------------------------------
                  MEMORY CHALLENGE
------------------------------------------------------------

Reference: John 3:16

"For God so loved the world..."

What word comes after "For God so"?

> loved

Correct!

Great job!

Current Score: 1
```

---

# Creativity

Once you have completed all of the required features, make your application your own.

You could:

- Add your favorite Bible verses
- Add encouraging messages
- Add different Scripture categories
- Add a morning and evening option
- Add more verses
- Add a streak counter
- Add a verse of the day
- Add a personalized welcome message
- Improve the menu
- Add additional statistics

Remember that your project should still be understandable and should use the Python concepts we have learned.

---

# OPTIONAL ADVANCED CHALLENGE

## Fill-in-the-Blank Scripture

Finished the required project?

Try making your Scripture Memory Trainer more challenging.

Instead of simply asking the user a question about the verse, create a fill-in-the-blank challenge.

For example:

```text
------------------------------------------------------------
                  MEMORY CHALLENGE
------------------------------------------------------------

"For God so ________ the world..."

What word is missing?

> loved

Correct!
```

Your program should:

1. Select a Bible verse.
2. Create a missing-word challenge.
3. Ask the user for the missing word.
4. Get the user's answer.
5. Check the answer.
6. Give feedback.
7. Track the score.

---

# ADVANCED CHALLENGE: Multiple Missing Words

If you finish the first challenge, make it harder.

Create a verse with multiple missing words.

For example:

```text
"For God so ________ the ________, that he gave
his only begotten ________..."
```

The user must provide all of the missing words.

You can decide how you want to structure this challenge.

Think about how you could use:

- Lists
- Loops
- Functions
- Variables
- If statements

to accomplish this.

---

# EXTRA ADVANCED CHALLENGE: Difficulty Levels

Allow the user to choose a difficulty level.

For example:

```text
Choose a difficulty:

1. Easy
2. Medium
3. Hard
```

You could design the levels like this:

### Easy

One missing word.

### Medium

Two missing words.

### Hard

Three or more missing words.

You decide how the difficulty should affect your program.

---

# PROJECT DEVELOPMENT STEPS

Do not try to build the entire project at once.

Work through the project in this order.

## Step 1: Add Your Verses

Add at least 5 Bible verses to your `verses` list.

Add the matching references to your `references` list.

Test your program.

---

## Step 2: Build Your Menu

Make sure your main menu displays correctly.

Test every menu option.

At this stage, some options may not work yet.

That is okay.

---

## Step 3: Build "View Verses"

Use a `for` loop to display your verses and references.

Make sure the correct reference appears with each verse.

---

## Step 4: Build "Practice a Verse"

Allow the user to select a verse.

Remember:

Python list indexes start at `0`.

If the user chooses:

```text
1. John 3:16
```

the corresponding list index is:

```python
0
```

You will need to think about how to convert the user's choice into the correct list index.

---

## Step 5: Build the Memory Challenge

Create a simple question about the selected verse.

Ask the user for an answer.

Use an `if` statement to determine whether the answer is correct.

Give encouraging feedback.

---

## Step 6: Add Progress

Create variables that track the user's performance.

For example:

```python
score = 0
verses_practiced = 0
```

Update these variables when the user practices a verse.

---

## Step 7: Test Your Program

Go through every feature.

Make sure:

- The menu works.
- The verses display correctly.
- The user can select a verse.
- The memory challenge works.
- The score updates.
- The progress displays.
- The program exits correctly.

---

## Step 8: Add Creativity

Only after your required features work should you add additional features.

Try one of the optional challenges or create your own feature.

---

# Testing Your Program

Before you consider your project finished, test every menu option.

Try:

```text
1. Practice a Verse
2. View Verses
3. View Progress
4. Exit
```

Also test what happens if the user enters something unexpected.

For example:

```text
Choose an option: hello
```

Your program should handle invalid input without crashing.

You can also test:

- An incorrect answer
- A correct answer
- Choosing the first verse
- Choosing the last verse
- Practicing multiple verses
- Exiting the program

---

# Code Quality

Your code should:

- Use meaningful variable names.
- Include comments where helpful.
- Use functions to organize your code.
- Avoid repeating the same code unnecessarily.
- Be easy for another person to understand.
- Be properly indented.
- Run without errors.

---

# Submission Checklist

Before submitting your project, make sure:

- [ ] My program runs without errors.
- [ ] I have at least 5 Bible verses.
- [ ] I have a list of Bible verses.
- [ ] I have a list of Bible references.
- [ ] I have a main menu.
- [ ] I can view my verses.
- [ ] I can practice a verse.
- [ ] My program accepts user input.
- [ ] I use `if`, `elif`, and `else`.
- [ ] I use a `for` loop.
- [ ] I use a `while` loop.
- [ ] I use functions.
- [ ] I track progress or a score.
- [ ] I added comments.
- [ ] I tested every menu option.
- [ ] My program handles invalid choices.
- [ ] My program does not crash during normal use.
- [ ] I customized my application.

---

# Final Presentation

During the Code for the Future Final Showcase, you will demonstrate your application.

Be prepared to explain:

## 1. What Your Application Does

Give a short explanation of your project.

## 2. Why You Chose This Project

Explain why you wanted to build a Scripture memory application.

## 3. How You Used Lists

Show where you stored your verses and references.

## 4. How You Used Loops

Explain where you used your `for` and `while` loops.

## 5. How You Used Functions

Explain how functions helped organize your program.

## 6. How You Used If Statements

Show how your program makes decisions.

## 7. How Your Score Works

Explain how you track the user's progress.

## 8. A Challenge You Encountered

Explain something that was difficult while building the application and how you solved it.

## 9. Something You Learned

Share one programming concept or lesson you learned while building the project.

---

# Final Showcase Tips

During your presentation:

1. Introduce your application.
2. Explain what problem it solves.
3. Demonstrate the application.
4. Show one interesting piece of your code.
5. Explain one challenge you overcame.
6. Explain how your project connects to serving God and others.

Keep your demonstration focused.

You do not need to explain every line of code.

---

# Remember the Mission

Code for the Future is about more than learning how to program.

Our goal is:

**Using technology to serve God and others.**

Think about how your application can encourage someone to spend more time reading, studying, and remembering God's Word.

Your project does not have to be perfect.

Build something useful.

Be creative.

Help someone.

Keep learning.

**Good luck!**
