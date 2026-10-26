
def func_1(lst_value): 
    ''' 
    write your docstring to explain the function

    calculate the sum and size of the list
    use those values to calculate the mean
    ''' 

    sum = 0 
    num_of_value = len(lst_value) 
    for value in lst_value: 
    sum = sum + value 
    return sum/num_of_value 