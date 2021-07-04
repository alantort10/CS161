# Author: Alan Tort
# Date: 7/3/2021
# Description: Project 4a
# a function called fall_distance that takes the time in seconds as an argument and returns the distance in meters that
# the object has fallen in that time

def fall_distance(time_in_seconds):
    """A function to calculate the distance in meters an object falls for X amount of seconds, which is derived from
    the formula d = (1/2)gt^2 where g is the constant 9.8"""

    # Formula:
    # d = (1/2) * g * t**2

    # Implementation:
    gravity = 9.8
    distance_in_meters = (1/2) * gravity * (time_in_seconds ** 2)

    return distance_in_meters
