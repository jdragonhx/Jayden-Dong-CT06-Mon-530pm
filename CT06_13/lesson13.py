print("Hello from lesson 13")

# # for entertament
# import random
# num = 0
# while not num == 4:
#     num = random.randint(1, 1000000000) # one billion
#     print(num)
#     if num == 4:
#         break
# else:
#     print("end of loop")


# # recap Q1
# # ATM Sim
# balence = 1000
# while True:
#     print("Welcome to your bank! ")
#     print("chose the following:")
#     print("1. Withdraw Cash")
#     print("2. Deposit Cash")
#     print("3. Show Balence")
#     print("4. Exit")
#     reply = input("")
#     reply = int(reply)
#     if reply == 4:
#         print("Thank you for banking with us! ")
#         break
#     elif reply == 1:
#         answer = input("how much to withdraw? ")
#         answer = int(answer)
#         break

# grocerys = ["apple", "bread" , "carrots", "dates", "eggs", "herbs"]
# print(grocerys[5])

# for name in grocerys:
#     print(name)

# grocerys.pop()
# for name in grocerys:
#     print(name)

# del(grocerys[1])

# for name in grocerys:
#     print(name)


# for item in grocerys:
#     if item == "Apples":
#         print(item + ": I need 5 of these")
#     if 


#test q1 (revision)
while counter < 150:
    print(counter)
    counter = counter + 12
else:
    print("end of list")

secret = "blastoff!"
answer = input("tell me today's password? ")
if answer == secret:
    print("its matched")
else:   
    print("go away i will tell the police!")