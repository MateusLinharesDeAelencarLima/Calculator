def root(rooting, index):
    root = rooting ** (1/index)

    if (root % 1) == 0:
        return int(root)
    else:
        return root
