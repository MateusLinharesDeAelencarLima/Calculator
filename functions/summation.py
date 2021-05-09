def summation(additive1, additive2):
    total = additive1 + additive2

    if (total % 1) == 0:
        return int(total)
    else:
        return total
