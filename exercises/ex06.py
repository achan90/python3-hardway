# Defines variable as string with inserted integer.
x = "There are {} types of people.".format(10)

# Defines variable as string.
binary = "binary"
do_not = "don't"

# Defines variable as string, with two string variables inserted.
y = "Those who know {} and those who {}.".format(binary, do_not)


# Prints variable.
print(x)
print(y)


# Prints string and inserts raw variable.
print("I said: {}.".format(x))

# Prints string and inserts string variable.
print("I also said: '{}'.".format(y))


# Defines variable as False.
hilarious = False

# Defines variable as string, with undefined raw insertion.
joke_evaluation = "Isn't that joke so funny?! {}"


# Prints variable and uses variable as the raw insertion.
print(joke_evaluation.format(hilarious))


# Defines variable as string.
w = "This is the left side of..."
e = "a string with a right side."


# Prints the variables as single string.
print(w + e)
