# Worksheet 1.2: Task 2 Solution
import util as U
from sys import exit

num_list = []

num_list = U.read_numbers()
if not num_list:
    exit("Error: no numbers provided")
else:
    num_list.sort()
    print(num_list)
    print(f"Minimum: {min(num_list)}")
    print(f"Maximum: {max(num_list)}")
    print(f"Mean: {sum(num_list)/len(num_list)}")
    median = 0
    if len(num_list) % 2:
        median = num_list[len(num_list)//2]
    else:
        median = (num_list[len(num_list)//2 - 1] + num_list[ + len(num_list)//2]) /2
    print(f"Median: {median}")