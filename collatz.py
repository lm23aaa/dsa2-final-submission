"""
collatz.py

Author: Liam Mills
Created: 2025-10-15
Last Modified: 2025-10-16

Implements recursive and iterative functions related to the Collatz conjecture.

Functions:
    collatz(n): Return the result of the Collatz sequence starting from n down to 1.
"""

def collatz(n: int) -> int:
    """
    Recursive function that runs through the Collatz conjecture
    mathematical problem

    Collatz states that for any positive integer n,
    we can arrive to the integer 1 by following these rules:
        - If n is odd, the function is called again using
          3n + 1 as the arguement.
        - If n is even, the function is called again using
          n / 2 as the arguement.

    Args:
        n (integer): Positive integer larger than one.

    Returns:
        integer: The final value of 1. If a number lower than 1
        is supplied, -1 is returned.

    Side Effects:
        Prints the value of n at each iteration, or an error
        message if a number lower than 1 is supplied.
    """

    if n < 1:
        print(f"Err: The number supplied was lower than one ({n}).")
        return -1
    elif n == 1:
        print("Success, the function has got to n=1.")
        return n
    elif n % 2 == 0:
        print(f"n={n}.")
        return collatz(n // 2)
    else: 
        print(f"n={n}.")
        return collatz(3 * n + 1)