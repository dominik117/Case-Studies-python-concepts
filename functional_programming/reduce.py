from functools import reduce
import math

def gcd_of_list(numbers):
    """
    Calculate the greatest common divisor (GCD) of a list of numbers.

    :param numbers: List of integers
    :return: GCD of all numbers in the list
    """
    return reduce(math.gcd, numbers)

# Example usage
numbers = [24, 108, 90, 42]
result = gcd_of_list(numbers)

print(f"The GCD of {numbers} is {result}")
