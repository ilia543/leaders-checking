def is_divisible(*arg):
    for i in range(1, len(arg)):
        if arg[0] % arg[i] != 0:
            return False
    return True 