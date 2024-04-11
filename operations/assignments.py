# Basic Assignment
x = 10  # Assigning an integer value
y = "Hello"  # Assigning a string value
z = 3.14  # Assigning a float value

# Multiple Assignment
a, b, c = 5, 3.2, "Python"  # Assigning multiple variables in one line

# Unpacking
data = [1, 2, 3]  # List containing three values
d, e, f = data  # Unpacking the list into three variables

# Swapping Values
g, h = 10, 20
g, h = h, g  # Swapping the values of g and h

# Augmented Assignment
i = 5
i += 2  # Equivalent to i = i + 2

# Chain Assignment
j = k = l = 50  # Assigning the same value to multiple variables

# Using _ for Unwanted Variables
_, m = [1, 2]  # When you only want the second value

# * for Extended Unpacking (Python 3+)
n, *o, p = [1, 2, 3, 4, 5]  # n = 1, o = [2, 3, 4], p = 5

# Using globals() and locals() for Dynamic Variable Names
for q in range(3):
    globals()[f'var_{q}'] = q * 10  # Creates var_0, var_1, var_2 dynamically

# Using exec for Dynamic Assignments (Not Recommended for Safety Reasons)
exec("r = 100")  # Assigns 100 to variable r

# Dictionary Unpacking for Function Arguments
def func(arg1, arg2):
    return arg1 + arg2

args = {'arg1': 10, 'arg2': 20}
result = func(**args)  # Calls func(10, 20)

# Assigning Function to Variable
def my_function():
    return "Hello!"

s = my_function  # Assigning function, not calling it

# Using := Operator (Walrus Operator, Python 3.8+)
# Useful in loops and conditions for assignment and return in the same expression
while (t := input("Enter a number (type 'exit' to stop): ")) != "exit":
    print(f"You entered: {t}")

# Note: This is just an overview. Python's assignment mechanisms can be more complex and powerful,
# especially when dealing with mutable data types like lists and dictionaries, or when dealing with scopes.
