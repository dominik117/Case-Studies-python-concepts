# Define a custom exception class (event class)
class MyCustomError(Exception):
    pass

try:
    # Code that might raise an exception
    x = 10
    y = 0
    assert y != 0, "y should not be zero"
    result = x / y
except ZeroDivisionError as e:
    # Handling specific exception
    print(f"ZeroDivisionError occurred: {e}")
except AssertionError as e:
    # Handling assertion errors -> assert y != 0, "y should not be zero"
    print(f"AssertionError occurred: {e}")
except (TypeError, ValueError) as e:
    # Handling multiple exceptions
    print(f"A TypeError or ValueError occurred: {e}")
except Exception as e:
    # Catching any other exception
    print(f"An exception occurred: {e}")
else:
    # Executes if no exception in try block
    print("No exceptions occurred!")
finally:
    # Always executes
    print("Execution complete.")

# Raising a custom exception
try:
    raise MyCustomError("A custom error occurred!")
except MyCustomError as e:
    print(f"Caught MyCustomError: {e.args}")


# Define a custom exception with additional arguments
class CustomError(Exception):
    def __init__(self, message, code):
        super().__init__(message, code)
        self.message = message
        self.code = code

try:
    # Raise the custom exception with specific arguments
    raise CustomError("An error occurred", 500)
except CustomError as e:
    # Access the args property
    print(f"Error message: {e.args[0]}")  # Error message
    print(f"Error code: {e.args[1]}")     # Error code

