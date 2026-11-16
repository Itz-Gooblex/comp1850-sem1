import random

# Get user to input how many random numbers they want
try:
    size = int(input("How many different numbers do you want?\n"))
except:
    print("Integer Expected")

# Generate this many random numbers
numbs = [random.randrange(1,100) for a in range(size)]
print(numbs)

# Write the random numbers to a file named random.txt, one number per line
with open("random.txt","w") as file:
    for numb in numbs:
        file.write(str(numb)+"\n")
