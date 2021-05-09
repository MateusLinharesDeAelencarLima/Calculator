def subtraction(additive, subtractive):
    difference = additive - subtractive

    if (difference % 1) == 0:
        return int(difference)
    else:
        return difference
