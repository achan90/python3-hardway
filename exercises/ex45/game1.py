from sys import exit
from random import randrange


class GameOver(object):

    death = ["\nGET REKT.",
             "\nBITCH PLEASE",
             "\nGG NUB",
             "\nKYS",
             "\nYOU SUCK",
             "\nCOME ON",
             "\nWHY THE FUCK DID YOU DO THAT?",
             "\nARE YOU EVEN TRYING?",
             ]

    def start(self):
        print(self.death[randrange(0, len(self.death))])
        exit()


class Scene1(object):
    def start(self):
        print("\nScene1 description")

        action = input("\n>")

        if action == "1":
            print("\nScene1 Outcome1 description")
            return Engine("Scene2")

        else:
            print("\nScene1 Outcome2 description")
            return Engine("GameOver")


class Scene2(object):
    def start(self):
        print("\nScene2 description")

        action = input("\n>")

        if action == "1":
            print("\nScene2 Outcome1 description")
            return Engine("Scene3")

        else:
            print("\nScene2 Outcome2 description")
            return Engine("GameOver")


class Scene3(object):
    def start(self):
        print("\nScene3 description")

        action = input("\n>")

        if action == "1":
            print("\nScene3 Outcome1 description")
            print("YOU WON")
            exit()

        else:
            print("\nScene3 Outcome2 description")
            return Engine("GameOver")


class Engine(object):
    def __init__(self, scene):
        self.scene = scene

        if self.scene == "GameOver":
            game = GameOver()
            game.start()
        elif self.scene == "Scene1":
            game = Scene1()
            game.start()
        elif self.scene == "Scene2":
            game = Scene2()
            game.start()
        elif self.scene == "Scene3":
            game = Scene3()
            game.start()


game = Scene1()
game.start()
