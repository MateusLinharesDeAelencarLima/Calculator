def division(dividend, divider):
    if divider == 0:
        error = "Zero não pode ser um divisor."

        return error

    else:
        quotient = dividend / divider

        if (quotient % 1) == 0:
            return int(quotient)
        else:
            return quotient
