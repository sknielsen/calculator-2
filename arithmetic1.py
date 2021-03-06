def add(num1, num2):
    """Return the sum of two numbers"""
    return num1 + num2


def subtract(num1, num2):
    """Return the difference of two numbers"""
    return num1 - num2


def multiply(num1, num2):
    """Return the product of two numbers"""
    return num1 * num2


def divide(num1, num2):
    """Return the quotient of two numbers as a float"""
    return float(num1) / float(num2)


def square(num):
    """Return the square of a number"""
    return num * num


def cube(num):
    """Return the cube of a number"""
    return square(num) * num


def power(num, exponent):
    """Return num raised to the power of exponent"""
    answer = num
    while exponent > 1:
        answer *= num
        exponent -= 1
    return answer
    # num ** exponent is another option for this


def mod(num1, num2):
    """Return remainder of num1 divided by num2"""
    return num1 % num2
