# Author: Alan Tort
# Date: 6/24/2021
# Description: Project 3c
# A program that prompts the user for an integer target that the player will try to guess.
# prompts messages if the guess is higher or lower than the target, and once the target is guessed
# it returns a string with the amount of tries attempted before the target was guessed.

print("Enter the integer for the player to guess.")
target = int(input())
print("Enter your guess.")
guess = int(input())
count = 1  # count starts at 1 since first correct guess will always be equal to 1 guess
while guess != target:
    if guess > target:
        count += 1
        print("Too high - try again:")
        guess = int(input())
    elif guess < target:
        count += 1
        print("Too low - try again:")
        guess = int(input())

print("You guessed it in", count, "tries.")
