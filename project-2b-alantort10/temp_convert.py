# Author: Alan Tort
# Date: 6/22/2021
# Description: Project 2b
# A program that converts Celsius temperatures to Fahrenheit temperatures
# using the formula: F = (9/5)C + 32

print("Please enter a Celsius temperature.")
celsius_temp = float(input())  # float is saved to variable
fahrenheit_temp = ((9 / 5) * celsius_temp) + 32  # conversion
print("The equivalent Fahrenheit temperature is:")
print(fahrenheit_temp)
