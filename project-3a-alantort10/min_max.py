# Author: Alan Tort
# Date: 06/24/2021
# Description: Project 3a Min-Max calculation program
# Prompts the user to enter an amount of integers they would like to enter
# Then prompts the user to enter the integers
# Then the program calculates the minimum and maximum of all the integers entered

print("How many integers would you like to enter?")
number_of_ints = int(input())

if number_of_ints <= 0:
    print("Please start the program again and enter an integer greater or equal to 1.")
else:
    print("Please enter", number_of_ints, "integers.")
    minimum = int(input())
    maximum = minimum
    for element in range(1, number_of_ints):  # start from 1 since we already captured 0 element
        current = int(input())
        if current > maximum:
            maximum = current
        elif current < minimum:
            minimum = current

    print("min:", minimum)
    print("max:", maximum)
