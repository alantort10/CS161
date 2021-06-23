# Author: Alan Tort
# Date: 6/22/2021
# Description: Project 2c
# A program that asks for an integer number of cents from 0 to 99 and outputs
# how many of each type of coin would represent that amount with the fewest
# total coins

print("Please enter an amount in cents less than a dollar.")
cents = int(input())
# check to see if number of cents is within 0 to 99
if cents < 0 or cents > 99:
    print("Please start the program again and enter"
          " an integer between 0 and 99 inclusive.")
else:
    print("Your change will be:")
    print("Q:", cents // 25)
    cents %= 25
    print("D:", cents // 10)
    cents %= 10
    print("N:", cents // 5)
    cents %= 5
    print("P:", cents // 1)
