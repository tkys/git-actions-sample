def add(x,y):
    return x + y


def subtract(x,y):
    return x - y


def multiply(x,y):
    return x * y


def devide(x,y):
    if y == 0:
        raise ValueError("Cannot devide by 0")
    return x / y
