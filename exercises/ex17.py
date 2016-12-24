from sys import argv
# from os.path import exists

script, from_file, to_file = argv

print("Copying from {} to {}".format(from_file, to_file))

# We could do these two on one line, how?
# in_file = open(from_file)
# indata = in_file.read()
# The solution could be put on one line, but on python that would be bad form.
with open(from_file) as in_file:
    indata = in_file.read()

# print "The input is %d bytes long" % len (indata)

# Removed as annoying.
# print("Does the output file exist? {}".format(exists(to_file)))
# print("Ready, hit ENTER to continue, CTRL-C to abort")
# input()

with open(to_file, 'w') as out_file:
    out_file.write(indata)

# Removed as apparently it's annoying.
# print("All right, all done.")

# These were made redundant by the use of 'with open'.
# out_file.close()
# in_file.close()
