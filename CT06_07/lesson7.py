## Recap 1: Debugging Average Score Program

### There is a total of 3 bugs in the following program.
### Identify and fix the bugs:

# score_one = 80
# score_two = 90
# score_three = 75

# total = score_one + score_two + score_three

# average_score = total / 3

# student_name = "Alex"

# print("Average score for " + student_name + " is: " + str(average_score))



## Task 1: For Loop: 1 to 10 using range(start, stop)

# Use a 'for' loop to print numbers from 1 to 10.
# for i in range (1, 10):
#     print(i)

## Task 2: Even Numbers 2-20 Loop using
##         range(start, stop, step)

# Print all even numbers between 2 and 20 using a 'for' loop and
# range().

# for i in range (2, 22, 2):
#     print(i)

## Task 3: Countdown From 10 For Loop

# Use a 'for' loop and range() to count down from 10 to 1.

# for i in range (10, 1, -1):
#     print(i)


## Task 4: Word Repetition Input Loop

# Ask the user for a word and a number n. Print the word repeated
# n times (on separate lines).

# Example:
# What word would you like to repeat? <>
# How many times would you like to repeat? << 3 >>

# output:
# burger
# burger
# burger

# word = input("give me a word")
# number_n = int(input("give me a number"))
# for i in range(number_n):
#     print(word)

## Task 5: Personalized Greeting Loop

# Ask for a user's name and an integer n, then print a
# personalized greeting n times.

# Example:
# What is your name? <>
# How many times would you like to repeat? << 3 >>

# output:
# Nice to meet you, burger
# Nice to meet you, burger
# Nice to meet you, burger

# word = input("what is your name?")
# number_n = int(input("how many times would you like to repeat?"))
# for i in range(number_n):
#     print("nice to meet you, " + word)


## Task 6: Sum of Five User Inputs

# Ask the user to input 5 numbers, one at a time, and print the
# sum of these numbers.

# Example:
# What is number #1? <<5>>
# What is number #2? <<2>>
# What is number #3? <<4>>
# What is number #4? <<1>>
# What is number #5? <<7>>

# output:
# Sum of the 5 numbers is 19 

# num1 = int(input("what is number #1?"))
# num2 = int(input("what is number #2?"))
# num3 = int(input("what is number #3?"))
# num4 = int(input("what is number #4?"))

# print(num1 + num2 + num3 + num4)


## Task 7: Multiplication Table Generator

# Ask the user for a number, then print the multiplication table
# for that number from 1 to 12.

# Example:
# What number for the timestable? > << 5 >>
# output:
# 5 x 1 = 5
# 5 x 2 = 10
# ....
# ..
# 5 x 12 = 60
