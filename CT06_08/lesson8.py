import time
import random
## Task 1: 'time' library

# **Task 1a**:
# Import the 'time' library and make use of the 'time.sleep()'
# function to create a 10 seconds countdown timer that counts
# to 1, printing the number of seconds remaining every second.

# for i in range(10, 0, -1):
#     print(i)
#     time.sleep(1)  #Wait for 1 second between each number

# print("liftoff!")  #This will be printed after the countdown


# **Task 1b**:
# Modify your code from Task 1a to include an 'input()' function
# asking the user for the number to countdown from, before
# counting down every second from the number given by the user.

# start = int(input("what number do you want to coundown from?"))
# end = int(input("what number do you want to end with"))

# for i in range(10, 0, -1):
#     print(i)
#     time.sleep(1)  #Wait for 1 second between each number

# print("liftoff!")  #This will be printed after the countdown


## Task 2: 'random' library

# **Task 2a**:
# Import the 'random' library and create a program that randomly
# output a number between 1 to 6

# num = random.randint(2, 4)
# print(num)


# **Task 2b**:
# Using the 'random' library, create 20 numbers between 0 and
# 9999 randomly.

# for i in range(20):
#     num = random.randint(0, 9999)
#     print(num)

## Task 3: Print Boolean Value & Condition

# **Task 3a**:
# Assign a boolean value to a variable and print it.

# raining = true

# **Task 3b**:
# Create 2 variables both holding the "True" boolean.
# Print out the result of comparing the 2 variables using
# the "==" operator.

# a = True
# b = True
# print(a == b)

# **Task 3c**:
# Now, assign 1 variable the "True" boolean, and assign another
# variable the "False" boolean.
# Print out the result of comparing the 2 variables using
# the "==" operator.

# a = True
# b = False
# print(a == b)


## Task 4:

# **Task 4a**: Math Question Generator
# Using the 'random' library, generate 2 numbers between 1 and 50
# that the user must add together.

# The output should be one of the following:
# 1. True (If the answer is correct)
# 2. False (If the answer is wrong)

# Example:
# What is 2 + 5? << 7 >>
# True

# yay did everything myself
num1 = random.randint(1, 50)
num2 = random.randint(1, 50)
question = ("what is" + str(num1) + " + " + str(num2) + "?")
reply = input(question)
reply = int(reply)
hidden = num1 + num2 
print(reply == hidden)


# **Task 4b**: Range Guesser
# Create a program that generates a random number between 1 and
# 50.

# The user should input a range (two numbers: start and end).

# The program checks if the random number falls within the user's
# range.

# The output should be one of the following:
# 1. True (If the answer is correct)
# 2. False (If the answer is wrong)

in