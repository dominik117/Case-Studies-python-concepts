# While-else and For-else are constructs in Python that might seem unusual at first,
# but they offer a more nuanced way to handle loops and their termination conditions.

# Let's start with the 'while-else' construct.

# Example 1: While-Else
# The 'else' block after a while loop is executed only when the loop completes normally,
# i.e., it didn't terminate due to a 'break' statement.

counter = 5
while counter > 0:
    print("Counter is:", counter)
    counter -= 1
else:
    # This will execute because the while loop completed normally.
    print("While loop ended without a break.")

# Example 2: While-Else with break
# Here, we will use a break statement to terminate the while loop,
# and observe that the else block doesn't execute.

counter = 3
while counter > 0:
    print("Counter is:", counter)
    if counter == 2:
        print("Breaking out of loop")
        break
    counter -= 1
else:
    # This will NOT execute because the loop terminated due to a break.
    print("While loop ended without a break.")

# Now, let's move on to the 'for-else' construct.

# Example 3: For-Else
# Similar to the while-else, the else block after a for loop is executed only when
# the for loop exhausts iterating over the iterable.

for i in range(5):
    print("Value is:", i)
else:
    # This will execute as the loop runs its normal course.
    print("For loop completed.")

# Example 4: For-Else with break
# Using a break in a for loop to show that the else part will not be executed.

for i in range(5):
    print("Value is:", i)
    if i == 3:
        print("Breaking at 3")
        break
else:
    # This will NOT execute because the loop was broken out of prematurely.
    print("For loop completed.")

# These constructs are particularly useful when searching for items in iterables.
# The else block can act as a neat way to handle cases where the item was not found.
