
# function implementation

def rectangle_area(length:float, width:float) -> float:  # define suitable input data             # implement the function
    return (length*width if length > 0 and width > 0 else "Non-existent")        # return an appropriate value

# testing the function

print(f"Area is {rectangle_area(2.2, -3)}")   # provide suitable data matching your inputs
