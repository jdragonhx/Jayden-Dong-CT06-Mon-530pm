# Task 1
# Print numbers from 10 to 200 using the while loop
# Your numbers must be in multiples of 10.
# 10 must be first number printed, and 200 the last number.

# Example: 10, 20, 30 ..... 180, 190, 200.
# Note that the numbers do not need to be printed in one line.
# Write your code here
# counter = 1
# while counter < 201:
#     print(counter)
#     counter += 1


# Task 2
# Code a password checker to protect your code!

# Assign a password "superpass123" to a variable
# Ask the user to enter a password
# If the password matches, print “Access Granted”
# If the password does not match, print “Access Denied”

# password = "superpass123"
# user_enter = input("please enter the password")
# if user_enter == password:
#     print("Access Granted!")
# else:
#     print("Acess Denied")


# Q2
# Task 1
# planets = ["mercury","venus", "earth", "mars", "jupiter", "saturn", "uranus" ]
# print(planets[2])

# planets.append("neptune")
# print(planets)
# planets.pop(3)
# planets.insert(3, "muskworld")
# print(planets)

import turtle
window = turtle.Screen()
window.setup(width = 600, height = 400)

for i in range(6):
    turtle.forward(55)
    turtle.left(120)