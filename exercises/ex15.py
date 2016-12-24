# Starts the script to import value for argv from user input.
from sys import argv

# Defines variable(s) as the input of argv. Number of variables after
# script determines, how many strings of user input is required to run the
# script without errors. script part is the name of the .py file that
# starts the script.
script, filename = argv

# Defines variable as something that is read from opened file. The name of
# the file that gets opened and then read is the value of variable.
txt = open(filename)

# Prints the string and imports variable in as raw.
print("Here's your file {}:".format(filename))

# Prints the variable.
print(txt.read())


# Prints the string.
print("Type the filename:")

# Defines the variable as prompted user input.
file_again = raw_input(">")


# Defines variable as something that is read from opened file. The name of
# the file that gets opened and then read is the value of variable.
txt_again = open(file_again)


# Prints the variable.
print(txt_again.read())

# Closes the file(s) opened by the script.
txt.close()
txt_again.close()
