# Week 1.5, Session 2: Task 5
from data import *
# Write a program here to create a Dataset containing data
# from a file named by the user

# Your program should display dataset size, mean and median,
# followed by the individual values (using a for loop)

test = Dataset("test_data.csv")
print(test.data)
print(len(test))
print(test[0])
print(test.mean())
print(test.median())