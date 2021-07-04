# Author: Alan Tort
# Date: 7/3/2021
# Description: Project 4c
# A hailstone sequence starts with some positive integer. If that integer is even, then you divide it by two to get the
# next integer in the sequence, but if it is odd, then you multiply it by three and add one to get the next integer in
# the sequence. Then you use the value you just generated to find the next value, according to the same rules.
# For example, if our initial number is 3, the subsequent numbers will be: 10, 5, 16, 8, 4, 2, 1.

# this is a function called hailstone takes a positive integer parameter as the initial number of a hailstone sequence
# and returns how many steps it takes to reach 1

def hailstone(positive_integer):
    """Hailstone function returns the amount of steps it takes to get to 1"""

    # initialize counter
    count = 0

    # loop until positive_integer is equal to 1
    while positive_integer != 1:
        # if even
        if positive_integer % 2 == 0:
            positive_integer = positive_integer / 2

        else:  # if not even, then odd
            positive_integer = (positive_integer * 3) + 1

        # increment counter
        count += 1

    return count
