from functools import reduce

def factorial(n):
    """
    Calculate the factorial of a number using reduce.

    :param n: A non-negative integer
    :return: Factorial of n
    """
    if n == 0:
        return 1  # The factorial of 0 is 1
    else:
        # Reduce applies the lambda function cumulatively to the items of the iterable
        # from left to right, which in this case is the range from 1 to n.
        # The lambda function multiplies two numbers.
        return reduce(lambda x, y: x * y, range(1, n + 1))

# Example usage
num = 5
print(f"The factorial of {num} is {factorial(num)}")
