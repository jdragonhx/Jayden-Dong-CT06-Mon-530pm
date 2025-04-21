# print("Hello from lesson 12")

# recap
# not } and } or 

#  e.g.
# power
# cover
# score

# word = input("give me a five letter word:  ")
# contains_o = False
# contains_e = False
# for i in word:
#     # print(word)
#     if word == "o":
#         contains_o = True
#     elif word == "e":
#         contains_e = True

# # outside the loop
# if not (contains_o == True) or (contains_e == True):
#     print("invalid word")
# else:
#     print("good word:  "  +  word)


# # Task 1: Introduction to while loop
# **Task 1a**:
# Due to a pandemic, the government placed a limit to the number
# of visitors a venue can have.

# Using a 'while' loop, create a program that will increase the
# number of visitors by 1 before printing out the number of
# visitors admitted, until number of visitors reaches 50.

# 1. Create a 'visitors' variable and assign '0' to it
# 2. While there is less than 50 visitors,
#     I. Increase the visitor count by 1
#     II. Print the visitor count


# counter = 0
# while counter < 51 :
#     print(counter)
#     counter += 1




# (For Task 1b & 1c)
# Modify your program to account for the number of visitors
# already present at the venue, and the number of maximum visitors
# allowed for the following:

# **Task 1b**:
# Visitors already present: 18
# Max visitors allowed: 30



# counter = 18
# while counter < 31:
#     print(counter)
#     counter += 1





# **Task 1c**:
# Visitors already present: 4
# Max visitors allowed: 25



# Task 3: Order taking using while loop
# Using what you have learnt so far, code a program to take a
# customer's order.

# Declare a variable called 'order' and assign an empty string
# variable "" to it.

# Using a 'while' loop:
# 1. Ask the user to enter their order
# 2. For each order entered, concatenate to the 'order' variable.
# 3. Exit the 'while' loop if the user enters "end"
# 4. On program end, print out the customer's order.

# **Bonus**
# 1. Modify your code to remove the comma (",") that appears
#    either at the start or end of your sentence




# order = ""
# answer = input("what is your order? ")
# while answer != "end":
#     # inside the loop
#     order = order + answer + ", "
#     answer = input("what is your order? ")

# # outside the loop
# print("you have order these items: ")
# print(order)



import random
number1 = random.randint(1, 10)
number2 = random.randint(1, 10)
# what is 3 + 5?
question = "what is "
question = "what is " + str(number1) + 