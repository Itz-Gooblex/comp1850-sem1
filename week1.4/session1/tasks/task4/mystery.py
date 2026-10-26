# Week 4, Session 1

# You are given the function mystery_func. 
# Inspect the code in the function
# Your task is to write a corresponding docstring
# - what the function does
## returns the number of uppercase and lowercase numbers in the string
# - what is the input data and type
## input is a string of type string
# - what is the return value and type
## return value is a tuple of integers in the form (numb of uppers, number of lowers)


# function implementation

def mystery_func(string):
    upper = 0
    lower = 0

    for ch in string:
        if ch.isupper():
            upper += 1
        if ch.islower():
            lower += 1
    return (upper, lower)


# testing

print(mystery_func("abc"))
print(mystery_func("The quick Brown Fox!"))
print(mystery_func("012345"))
print(mystery_func("ABC"))


# Can you predict the output of the following lines of code?
# Uncomment the lines of code one by one and run the program
# to see if you are right?

# print(mystery_func("X"))
# print(mystery_func("[2, 3]"))
