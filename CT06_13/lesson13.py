print("Hello from lesson 13")

# for entertament
import random
num = 0
while not num == 4:
    num = random.randint(1, 1000000000) # one billion
    print(num)
    if num == 4:
        break
else:
    print("end of loop")


# recap Q1
# ATM Sim
balence = 1000
while True:
    print("Welcome to Y")