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
    print("Welcome to your bank! ")
    print("chose the following:")
    print("1. Withdraw Cash")
    print("2. Deposit Cash")
    print("3. Show Balence")
    print("4. Exit")
    reply = input("")
    reply = int(reply)
    if reply == 4:
        print("Thank you for banking with us! ")
        break
    elif reply == 1:
        answer = input("how much to withdraw? ")
        