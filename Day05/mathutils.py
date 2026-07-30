# def average(nums):
#     if not nums :
#         return 0
#     return sum(nums) / len(nums)

# def biggest(nums):
#     if not nums :
#         return None
#     return max(nums)

# def is_prime(n) :
#     if n <= 1 :
#         return False

#     for i in range(2, int(n**0.5) + 1) :
#         if n % i == 0:
#             return False
#     return True


# """Utility functions for basic mathematical operations."""
# def average(nums: list[float]) -> float :
#     """Retuns the mean of a list of numbers.

#     Args :
#         nums : a list of numbers, may be empty.

#     Returns :
#         The mean as a float, or 0.0 of the list is empty.

#     """
#     if not nums :
#         return 0.0
#     return sum(nums) / len(nums)

# def biggest(nums: list[float]) -> float :
#     '''Returns the largest number in a list.

#     Args :
#         A list of numbers. May be empty.

#     Returns :
#         The largest number, or None if the list is empty.
#     '''
#     if not nums :
#         return None
#     return max(nums)

# def is_prime(n: int) -> bool :
#     '''Returns whether a number is prime.

#     Args :
#         n : an integer to test

#     Returns :
#         True if the number is prime, otherwise False.
#         Returns False for numbers less than 2.
#     '''
#     if n < 2 :
#         return False

#     for i in range(2, int(n**0.5)+1):
#         if n % i == 0:
#             return False
#     return True
# import mathutils
# help(mathutils)


# from typing import Optional
# def average (nums: list[float]) -> float :
#     if not nums :
#         return 0.0
#     return sum(nums) / len(nums)

# def biggest (nums: list[int]) -> Optional[int] :
#     if not nums :
#         return None
#     return max(nums)

# def is_prime(n: int) -> bool:
#     if n < 2 :
#         return False

#     for i in range(2, int(n**0.5) + 1):
#         if n % i == 0:
#             return False
#     return True


import os
import math
import random


def average(nums: list[float]) -> float:
    return sum(nums) / len(nums)


def biggest(nums: list[float]) -> float:
    return max(nums)


def is_prime(n: int) -> bool:
    return True
