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
    return x ** 0.5

def reci(x):
    return 1 / x if x != 0 else "Undefined (division by zero)"

def sqrt(x):
    return math.sqrt(x)

def power(x, y):
    return math.pow(x, y)

def fact(x):
    return math.factorial(x)

def log(x):
    return math.log(x) if x > 0 else "Not defined"

def exp(x):
    return math.exp(x)

def _10pow(x):
    return math.pow(10, x)

def cube(x):
    return x ** 3

def cbrt(x):
    return x ** (1 / 3)

def _2pow(x):
    return math.pow(2, x)

def absolute(x):
    return abs(x)

def lbasey(x, y):
    return math.log(x, y) if x > 0 and y > 0 and y != 1 else "Undefined (invalid log base)"

def sin(x):
    return math.sin(math.radians(x))

def cos(x):
    return math.cos(math.radians(x))

def tan(x):
    return math.tan(math.radians(x))

def cosec(x):
    return 1 / math.sin(math.radians(x)) if math.sin(math.radians(x)) != 0 else "Undefined"

def sec(x):
    return 1 / math.cos(math.radians(x)) if math.cos(math.radians(x)) != 0 else "Undefined"

def cot(x):
    return 1 / math.tan(math.radians(x)) if math.tan(math.radians(x)) != 0 else "Undefined"

def hypo(x, y):
    return math.hypot(x, y)

def isin(x):
    return math.degrees(math.asin(x)) if -1 <= x <= 1 else "Undefined"

def icos(x):
    return math.degrees(math.acos(x)) if -1 <= x <= 1 else "Undefined"

def itan(x):
    return math.degrees(math.atan(x))

def icosec(x):
    return math.degrees(math.asin(1 / x)) if abs(x) >= 1 else "Undefined"

def isec(x):
    return math.degrees(math.acos(1 / x)) if abs(x) >= 1 else "Undefined"

def icot(x):
    return math.degrees(math.atan(1 / x)) if x != 0 else "Undefined"

def pi():
    return math.pi

def euler():
    return math.e
