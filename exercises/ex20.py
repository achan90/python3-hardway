# Imports argv from package.
from sys import argv

# Unpacks argv to variables.
script, input_file = argv


# Defines function with one variable.
def print_all(f):
    # Prints the input of file pointed by variable.
    print(f.read())


# Defines function with one variable.
def rewind(f):
    # Moves you to the 0 byte of file. (the first byte on the file.)
    f.seek(0)


# Defines function with two variables.
def print_a_line(line_count, f):
    # Reads and prints the line pointed by variable,
    # from file pointed by variable.
    print(line_count, f.readline())


# Opens file pointed by variable and sets it as variables value.
current_file = open(input_file)

# Prints the string.
print("First let's print the whole file:\n")

# Runs the function.
print_all(current_file)

# Prints the string.
print("Now let's rewind, kind of like a tape.")

# Runs the function.
rewind(current_file)

# Prints the string.
print("Let's print three lines:")

# Sets value to variable.
current_line = 1
# Runs the function.
print_a_line(current_line, current_file)

# Sets new value to variable. (adds 1 to it. 1 + 1 = 2)
current_line += 1
# Runs the function.
print_a_line(current_line, current_file)

# Sets new value to variable. (adds 1 to it. 2 + 1 = 3)
current_line += 1
# Runs the function.
print_a_line(current_line, current_file)

# Closes the file pointed by variable, added because it's considered good form.
current_file.close()
