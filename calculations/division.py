def division(dividend, divider):
    quotient = dividend / divider

    if (quotient % 1) == 0:
        return int(quotient)
    else:
        return quotient
