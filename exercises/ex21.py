def add(a, b):
    print("ADDING %d + %d".format(a, b))
    return a + b


def subtract(a, b):
    print("SUBTRACTING %d - %d".format(a, b))
    return a - b


def multiply(a, b):
    print("MULTIPLYING %d * %d".format(a, b))
    return a * b


def divide(a, b):
    print("DIVIDING %d / %d".format(a, b))
    return a / b


print("Let's do some math with just functions!")

age = add(30, 5)
height = subtract(78, 4)
weight = multiply(90, 2)
iq = divide(100, 2)

print("Age: %r, Height: %d, Weight: %d, IQ: %d".format(
    age, height, weight, iq))

# a puzzle for the extra credit, type it in anyway.
print("Here is a puzzle.")

what = add(age, subtract(height, multiply(weight, divide(iq, 2))))

print("That becomes: ", what, "Can you do it by hand?")

print("What is 24 + 34 / 100 - 1023")

print(subtract(add(24, divide(34, 100)), 1023))
