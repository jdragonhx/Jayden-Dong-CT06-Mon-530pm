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

num = random.randint(2, 4)



# **Task 2b**:
# Using the 'random' library, create 20 numbers between 0 and
# 9999 randomly.