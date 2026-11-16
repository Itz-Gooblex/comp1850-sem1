# Week 4, Session 1: 

# You are given an incomplete function isBond with a docstring. Your task
# is to complete the function based on the details in the docstring.


def isBond(intList):
    """
    This function accepts a list of integers and returns True if the
    sequence 0, 0, 7 appears in the list, in that order. Return False
    otherwise. The numbers do not need to be consecutive, but must appear
    in the specified order.
    """

    # pass is a Python keyword used as a placeholder for future code,
    # meaning you need to delete pass to write your code.
    # Nothing happens when pass is executed.

    if len(intList) < 3:
        return False

    nums = 0
    for num in intList: #Iterate through list to find sequence 007
        match nums:
            case 0 | 1: #Case of finding 1st | 2nd digit
                if num == 0:
                    nums += 1
            case 2: #Case of finding 3rd digit
                if num == 7:
                    nums += 1
                    break
    return nums == 3 #007 is found is all 3 digits are found


# Check if the following lines of code produce the correct output
print(isBond([1, 2, 4, 0, 0, 7, 5]))   # True
print(isBond([1, 0, 2, 4, 0, 5, 7]))   # True
print(isBond([1, 7, 2, 0, 4, 5, 0]))   # False
