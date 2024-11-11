# Cooper Lilly
# UWYO COSC 1010
# Submission Date
# Lab 08
# Lab Section: 13
# Sources, people worked with, help given to:
# your
# comments
# here


# Write a function that will properly check strings to see if they are an int or float, and convert them if so
# If they can't be converted return false
# Other wise return the converted int or float 
# Floats should only have one decimal point in them 
def str_convert(num):
    negative = False
    if num[0] == "-":
        negative = True
        num = num.replace("-","")

    if "." in num:
        num_split = num.split(".")
        if len(num_split) == 2 and num_split[0].isdigit() and num_split.isdigit():
            if negative:
                return -1*float(num)
            else:
                return float(num)
        else:
            return False

    elif num.isdigit():
        if negative:
            return -1*int(num)
        else:
            return int(num)
    return False


print("*" * 75)

# Point-slope y = mx + b
# This is used in mathematics to determine what the value y would be for any given x
# Where b is the y-intercept, where the line crosses the y-axis (x = 0)
# m is the slope of the line, the rate of change, how steep the line is
# x is the variable, and is determined by which point on the graph you wish to evaluate
# Create a function slope_intercept that takes in four parameters
    # m, the slope
    # b, the intercept
    # a lower x bound
    # an upper x bound
# Return a list for all values of y for the given x range, inclusive (whole number X's only)
# Check to make sure that the lower bound is less than or equal to the upper bound
# m, b can be floats or integers
# the bounds must be integers, if not return false

# Create a while loop to prompt users for their input for the four variables
# Exit on the word exit
# Remember all inputs are strings, but the function needs ints or floats
# Call your function and print the resulting list

def slope_intercept(m,b,lbx,ubx):
    y = []
    if type(lbx) is int and type(ubx) is int and lbx <= ubx:
        for x in range(lbx, ubx+1):
            y.append(m+x+b)
    else:
        return False
    return y

while True:
    m = input("Enter an m value for y=mx+b (type 'exit' for exit): ")
    if m == "exit":
        break
    ubx = input("Enter a value for upper x bound of y=mx+b: ")
    lbx = input("Enter a value for lower x bound of y=mx+b: ")
    b = input("Enter a value for b of y=mx+b: ")
    m = str_convert(m)
    ubx = str_convert(ubx)
    lbx = str_convert(lbx)
    b = str_convert(b)
    y = slope_intercept(m.b.lbx,ubx)
    print(y)
    break


print("*" * 75)


# Write a function to solve the quadratic formula
# https://en.wikipedia.org/wiki/Quadratic_formula
# Accept inputs for a, b, c
# Remember that this returns two values
# Create a loop like above to prompt the user for input for the three values
# Create a second function that just does the square root operation 
    # If the number you are trying to take the square root of is negative, return null


def quadratic(a,b,c):
    if type(b) is int and type(a) is int and type(c) is int:
        inner = ((b**2) - (4*a*c))**0.5
        val_add = (-b + inner)/(2*a)
        val_minus = (-b - inner)/(2*a)
        return [val_add, val_minus]
    return False

while True:
    b = input("enter b value of quadratic formula ('exit' to exit)")
    a = input("enter an a value of quadratic formula")
    c = input("enter c value of quadratic formula")

    b=str_convert(b)
    a=str_convert(a)
    c=str_convert(c)
    results = quadratic(b,a,c)
    val_add = results[0]
    val_minus = results[1]
    print(f"{val_minus} and {val_add} are both possible answers")
    break