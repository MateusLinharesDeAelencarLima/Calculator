def multiplication(factor, multiplier):
    product = factor * multiplier

    if (product % 1) == 0:
        return int(product)
    else:
        return product
