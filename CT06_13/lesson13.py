print("Hello from lesson 13")

# for entertament

num = 0
while not num == 4:
    num = random.randint(1, 100000000)
    print(num)
    if num == 4:
        break
else:
    print("end of loop")