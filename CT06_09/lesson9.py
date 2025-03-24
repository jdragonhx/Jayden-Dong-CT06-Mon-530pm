# print("Hello from lesson 9")

# task 3a
import random

somenumber = random.radint(1,10)


answer = input("guess a number from 1 to 10")
answer = int(answer)


if answer == somenumber:
    print("congratulations!")
