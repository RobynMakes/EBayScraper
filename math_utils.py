"""A set of functions for various math operations that are not included in the math library"""
import math


def average(array):
    """Calculates the average value from an array of numbers

    Keyword arguments:
        array: the array to calculate the average from

    Returns:
        the average of the given array
    """
    pos = 0
    total = 0

    # Summing all array values
    while True:
        total += array[pos]
        pos += 1

        # if the value of pos == length of the array -> break the loop
        if pos == len(array):
            break

    avg = total / len(array)
    return avg


def median(array):
    """Calculates the median value from an array of numbers

    Keyword arguments:
        array: the array to calculate the median from

    Returns:
        the median of the given array
    """
    sorted_array = sorted(array)
    half_length = (len(sorted_array) - 1) / 2
    if half_length.is_integer():
        med = sorted_array[int(half_length)]
    else:
        med = average([sorted_array[math.floor(half_length)], sorted_array[math.ceil(half_length)]])
    return med


def pythag(a: float, b: float):
    """Performs the Pythagorean Theorem\n
    c^2 = a^2 + b^2

    Keyword arguments:
        a: the length of side A
        b: the length of side B

    Returns:
        the length of side c^2
    """
    return a**2 + b**2


def dist(x1: float, y1: float, x2: float, y2: float):
    """Calculates the distance between two 2D vector positions

    Keyword arguments:
        x1: the x position of the first point
        y1: the y position of the first point
        x2: the x position of the second point
        y2: the y position of the second point

    Returns:
        the distance between point1 and point2
    """
    width = x2 - x1
    height = y2 - y1

    c_squared = pythag(width, height)

    c = math.sqrt(c_squared)

    return c
