numbers = []


def while_loop(a, b, c):
    while a < b:
        print("At the top a is {}".format(a))
        numbers.append(a)

        a += c

        print("Numbers now:", numbers)
        print("At the bottom a is {}".format(a))


def for_loop(a, b, c):
    for a in range(a, b, c):
        print("At the top a is {}".format(a))
        numbers.append(a)

        # This is only required for incrementing top & bottom values of a.
        a += c

        print("Numbers now:", numbers)
        print("At the bottom a is {}".format(a))


print("Choose number:")
x = int(input(">"))
print ("\nChoose larger number:")
y = int(input(">"))
print("\n Choose increment value:")
z = int(input(">"))

# while_loop(x, y, z)
for_loop(x, y, z)

print("The numbers: ")

for num in numbers:
    print(num)
