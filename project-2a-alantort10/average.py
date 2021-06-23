# Author: Alan Tort
# Date: 6/22/2021
# Description: Project 2a,
# A program that asks the user for five numbers and then prints out the average
# of those numbers

print("Please enter five numbers.")
# save individual floats to individual variables
num_1 = float(input())
num_2 = float(input())
num_3 = float(input())
num_4 = float(input())
num_5 = float(input())
# save the total of floats to variable
total = num_1 + num_2 + num_3 + num_4 + num_5
# save the average of total to variable
avg = total / 5
print("The average of those numbers is:")
print(avg)
