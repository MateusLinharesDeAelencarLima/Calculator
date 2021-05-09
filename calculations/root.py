def root(rooting, index):
    if index == 0:
        error = "Zero nao pode ser uma raiz."

        return error
    else:
        root = rooting ** (1/index)

        if (root % 1) == 0:
            return int(root)
        else:
            return root
