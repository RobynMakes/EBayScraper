import math

# Returns the average of an array of numbers
# average = (n1 + n2 + n3...) / n_length
def average(array):
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


# Returns the median of an array of numbers
# median = the value in the middle position of a data set
def median(array):
    sorted_array = sorted(array)
    half_length = (len(sorted_array) - 1) / 2
    if half_length.is_integer():
        med = sorted_array[int(half_length)]
    else:
        med = average([sorted_array[math.floor(half_length)], sorted_array[math.ceil(half_length)]])
    return med

