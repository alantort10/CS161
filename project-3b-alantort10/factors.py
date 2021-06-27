# Author: Alan Tort
# Date: 06/24/2021
# Description: Project 3b
# A program that asks the user to enter a positive integer then prints
# a list of all positive integers that divide that number evenly,
# including itself and , in ascending order

positive_integer = int(input("Please enter a positive integer: "))
if positive_integer <= 0:
    print("Please run the program again and enter a positive integer")
else:
    print("The factors of", positive_integer, "are:")
    # we want to loop from 1 to the number (inclusive)
    for element in range(1, positive_integer + 1):
        # if the number when divided by the element has a remainder of 0, then
        # the element is a factor of the number
        if positive_integer % element == 0:
            print(element)
