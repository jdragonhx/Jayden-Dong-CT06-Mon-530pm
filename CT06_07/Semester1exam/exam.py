# Q1
# name = input("what is you name?") # ask user for name
# print("nice to meet you " + (name)) # print nice to meet you plus name

# Q2
start = int(input("what number do you want to start with?"))
end = int(input("what number to you want to end at?"))
step = int(input("what number do you want to increment by?"))

for i in range(start, end, step):
    print(i)