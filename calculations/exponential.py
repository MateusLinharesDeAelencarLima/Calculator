def exponential(base, exponent):
    power = base ** exponent

    if (power % 1) == 0:
        return int(power)
    else:
        return power
