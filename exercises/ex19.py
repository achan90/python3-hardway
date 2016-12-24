# Defines the function.
# def cheese_and_crackers(cheese_count, boxes_of_crackers):
#    #Prints the string with argument formatted in as integer.
#    print("You have {} cheeses!".format(cheese_count))
#    print("You have {} boxes of crackers!".format(boxes_of_crackers))
#    #Prints the string.
#    print("Man that's enough for a party!")
#    print("Get a blanket. \n")

# Prints the string.
# print("We can just give the funtion numbers directly:")
# Sets integers as arguments for the script and runs it.
# cheese_and_crackers(20,30)


# Prints the string
# print(OR, we can use variables from our script:")
# Sets value to variable.
# amount_of_cheese = 10
# amount_of_crackers = 50

# Sets variables as arguments for the script and runs it.
# cheese_and_crackers(amount_of_cheese, amount_of_crackers)


# Prints the string.
# print("We can even do math inside too:")
# Sets equations as arguments for the script and runs it.
# cheese_and_crackers(10 + 20, 5 + 6)


# Prints the string.
# print("And we can combine the two, variables and math:")
# Combines math and variables as arguments for the script and runs it.
# cheese_and_crackers(amount_of_cheese + 100, amount_of_crackers + 1000)


# Defines the function.
def function(arg1, arg2, arg3):
    print("So you are {} years old,".format(arg1),
          "and you live at {}".format(arg2),
          "If I add 10 years to your age I get {}".format(arg3))


print("\nCall number 01\n")
function(26, "Hamina", 26 + 10)


print("\nCall number 02\n")
x, y, z = (26, "Hamina", 36)
function(x, y, z)


print("\nCall number 03\n")
function(z - 10, y, x + 10)


print("\nCall number 04\n")
age = input("How old are you? ")
home = raw_input("Where do you live? ")
function(age, home, age + 10)


print("\nCall number 05\n")
age2 = float(raw_input("How old are you? "))
home2 = raw_input("Where do you live? ")
function(age2, home2, age2 + 10)
