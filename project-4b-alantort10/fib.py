# Author: Alan Tort
# Date: 7/3/2021
# Description: Project 4b
# A function named fib that takes a positive integer parameter and returns the number at that position of the
# Fibonacci sequence

def fib(positive_integer):
    """Fib takes a positive integer parameter and returns the number at the position of the Fibonacci sequence"""
    # first number is 0 (initially)
    preceding_num = 0
    # second number is 1 (initially)
    following_num = 1

    # current number is 0 (initially)
    current_num = 0

    # loop runs positive_integer times
    for each_number in range(positive_integer):
        preceding_num = following_num
        following_num = current_num
        current_num = preceding_num + following_num

    return current_num
