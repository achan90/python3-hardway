print("""
You enter a dark room with two doors. Do you go through door #1 or door #2?""")

door = input(">")

if door == "1":
    print("There's a giant bear here eating a cheese cake. what do you do?")
    print("1. take the cake.")
    print("2. Scream at the bear.")

    bear = input(">")

    if bear == "1":
        print("The bear eats your face off. Good job!")
    elif bear == "2":
        print("The bear eats your legs off. Good job!")
    else:
        print("Well, doing {} is probably better. Bear runs away.".format(
            bear))
        print("\nWhat will you do next?")
        print("1. Go back to door #2.")
        print("2. Follow the bear.")

        x = input(">")

        if x == "1":
            print("You stare into the endless abyss at Cthulhu's retina.")
            print("1. Blueberries.")
            print("2. Yellow jacket clothespins.")
            print("3. Understanding revolvers yelling melodies.")

            insanity = input(">")

            if insanity == "1" or insanity == "2":
                print("Your body survies powered by a mind of jello.",
                      "Good job!")

            else:
                print("The insanity rots your eyes into a pool of muck.")
                print("Good job!")
        else:
            print("You ran after the bear and reach it.")
            print("What do you do?")
            print("1. Confront the bear.")
            print("2. Flee the bear.")

            bear = input(">")

            if bear == "1":
                print("The bear mauls you to death. Good job!")

            elif bear == "Shoot the bear":
                print("""
                You shoot the bear between the eyes killing it instantly.""")
                print("You are now able to return home safely. Good job!")

            else:
                print("The bear catches you and rips you apart. Good job!")


elif door == "2":
    print("You stare into the endless abyss at Cthulhu's retina.")
    print("1. Blueberries.")
    print("2. Yellow jacket clothespins.")
    print("3. Understanding revolvers yelling melodies.")

    insanity = input(">")

    if insanity == "1" or insanity == "2":
        print("Your body survies powered by a mind of jello. Good job!")
    else:
        print("The insanity rots your eyes into a pool of muck. Good job!")

else:
    print("You stumble around and fall on a knife and die. Good job!")
