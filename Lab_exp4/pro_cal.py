import math

def add(x, y):
    return x + y

def sub(x, y):
    return x - y

def mul(x, y):
    return x * y

def div(x, y):
    return x / y

def mod(x, y):
    return x % y

def sq(x):
    return x ** 2

def sqr(x):
    return x ** (1 / 2)

def reci(x):
    return 1 / x if x != 0 else "Undefined (division by zero)"

def band(x, y):
    return int(x) & int(y)

def bor(x, y):
    return int(x) | int(y)

def bxor(x, y):
    return int(x) ^ int(y)

def bnot(x):
    return ~int(x)

def lshift(x, positions=2):
    return int(x) << positions

def rshift(x, positions=2):
    return int(x) >> positions

def binary(x):
    return bin(int(x))

def octal(x):
    return oct(int(x))

def hexadecimal(x):
    return hex(int(x))

def btodecimal(x):
    return int(x, 2)

def otodecimal(x):
    return int(x, 8)

def htodecimal(x):
    return int(x, 16)
