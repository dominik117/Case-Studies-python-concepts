def factorial(n):
    # Base case: factorial of 0 is 1
    if n == 0:
        return 1

    # Recursive case: n! = n * (n-1)!
    else:
        return n * factorial(n-1)

# Example usage
print(factorial(5))  # Output: 120


def fibonacci(n):
    # Handling Edge Cases: Fibonacci Sequence
    # Handle edge cases: first two numbers of the sequence
    if n <= 0:
        return 0
    elif n == 1:
        return 1

    # Recursive case: Fibonacci(n) = Fibonacci(n-1) + Fibonacci(n-2)
    else:
        return fibonacci(n-1) + fibonacci(n-2)

# Example usage
print(fibonacci(10))  # Output: 55


def fibonacci_memo(n, memo={}):
    # Optimizing with Memoization: Fibonacci Sequence
    # Check if value already computed
    if n in memo:
        return memo[n]

    # Base cases and recursive case
    if n <= 0:
        memo[n] = 0
    elif n == 1:
        memo[n] = 1
    else:
        memo[n] = fibonacci_memo(n-1, memo) + fibonacci_memo(n-2, memo)

    return memo[n]

# Example usage
print(fibonacci_memo(100))  # Efficient even for large n


"""
Limitations: Python Recursion Depth Limit
Python has a maximum recursion depth, typically set to a limit (like 1000) to avoid infinite recursion. We can see this limit and modify it if necessary.
"""

import sys

# Check the current recursion limit
current_limit = sys.getrecursionlimit()
print("Current recursion limit:", current_limit)

# Example of exceeding the recursion limit
try:
    print(factorial(2000))  # This may cause a RecursionError
except RecursionError as e:
    print("Recursion error:", e)

# Increasing the recursion limit (use with caution)
sys.setrecursionlimit(3000)
print("New recursion limit:", sys.getrecursionlimit())
