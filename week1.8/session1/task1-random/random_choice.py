import random

# Read names from a file

with open("names.txt") as infile:
    names = [ line.strip() for line in infile ]

# Ask user to enter a number, then randomly choose that many names
# from the list, avoiding any duplicate choices
sample_size = int(input("How many names would you like to choose? \n"))

sample = random.sample(names, sample_size)

# Display the chosen names, one per line
for line in sample:
    print(line)