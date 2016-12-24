# Start import string.
from sys import argv

# Unpack argv to variables.
script, filename = argv

# Print the string, format variable in as raw.
print("We're going to erase {}".format(filename))
# Print the string.
print("If you don't want that, hit CTRL-C.")
print("If you do want that, hit ENTER")

# Prompt for user input.
# raw_input("?")

# Print the string.
print("Opening the files...")
# Open target file in write mode.
target = open(filename, 'w')


# Print the string.
print("Truncating the file. Goodbye!")
# Truncate target file, omitted out as pointless due to opening in write mode.
# target.truncate

# Print the string.
print("Now I'm going to ask you for three lines.")

# Define variable with user input prompt.
line1 = input("line 1: ")
line2 = input("line 2: ")
line3 = input("line 3: ")

# Print the string.
print("I'm going to write these to the file.")
# Write string, with string variables formatted in to the target file.
target.write("\n%s \n%s \n%s \n" % (line1, line2, line3))

# Print the string.
print("And finally, we close it.")
# Close target file.
target.close()

# Read the file that you created and print it, using with open so it gets
# automatically closed.
with open(filename) as txt:
    print(txt.read())
