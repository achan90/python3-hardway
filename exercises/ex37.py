

def logical_and(arg1, arg2, arg3):
    if arg1 and arg2 > arg3:
        print "%r and %r are greater than %r" % (arg1, arg2, arg3)


def with_as():
    with open(raw_input("File name:")) as f:
        print f.read()


def if_elif_else(arg1):
    if arg1 == 1:
        print "%d is equal to 1" % arg1
    elif arg1 == 2:
        print "%d is equal to 2" % arg1
    else:
        print "%d isn't equal to 1 or 2" % arg1


def run_str_as_python(arg):
    exec "%s" % arg


def for_loop(arg):
    for x in arg:
        print "%s" % x


def import_sys():
    x = raw_input("Do you wish to import full 'sys' module?\n>")

    if x == "yes":
        import sys
    else:
        print "importing only 'exit' from 'sys'"
        from sys import exit

    y = raw_input("Do you wish to kill this script?")

    if y == "yes":
        exit(0)
    else:
        while True:
            list = []
            for f in list:
                print "Choose function:"
                print "%s" % f

                z = raw_input(">")

                if z in list:
                    exec "%s" % z
                else:
                    list = []
                    for f in list:
                        print "Choose function:"
                        print "%s" % f


def test_equality(arg1, arg2):
    print arg1 is arg2


def logical_not():
    x = not True
    print x


def logical_or(arg1, arg2):
    if arg1 > arg2:
        print "%d > %d" % (arg1, arg2)
    elif arg1 < arg2:
        print "%d < %d" % (arg1, arg2)
    else:
        print "%d = %d" % (arg1, arg2)


def print_str(arg):
    print arg


def return_function(arg1, arg2):
    print "%d + %d = %d" % (arg1, arg2, arg1 + arg2)
    return arg1 + arg2


def while_loop():
    x = int(raw_input(">"))
    while x < 10:
        print "%d" % x
        x += 1


def del_function():
    x = [0, 1, 2, 3, 4, 5]
    del x[1:5]
    print x


def lambda_function(n):
    return lambda x: x + n


# def yield_function():


# def pass_function():


# def assert_ensure():


# def break_loop():


# def define_class():


# def continue_loop():


# def try_function():
# def exception():
# def raise_function():
# def finally_do():
