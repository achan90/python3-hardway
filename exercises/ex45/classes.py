from random import randrange


class GameOver(object):

    death = ["\nGET REKT.",
             "\nBITCH PLEASE",
             "\nGG NUB",
             "\nKYS",
             "\nYOU SUCK",
             "\nCOME ON",
             "\nWHY THE FUCK DID YOU DO THAT?",
             "\nARE YOU EVEN TRYING?"
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
            # game = Engine("Scene2")
            return "Scene2"

        else:
            print("\nScene1 Outcome2 description")
            # game = Engine("GameOver")
            return "GameOver"


class Scene2(object):
    def start(self):
        print("\nScene2 description")

        action = input("\n>")

        if action == "1":
            print("\nScene2 Outcome1 description")
            # game = Engine("Scene3")
            return "Scene3"

        else:
            print("\nScene2 Outcome2 description")
            # game = Engine("GameOver")
            return "GameOver"


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
            # game = Engine("GameOver")
            return "GameOver"


class Engine(object):
    def __init__(self, scene):
        self.scene = scene

    def play(self):
        current = self.scene.first()
        final = self.scene.following("GameOver")

        while current is not final:
            scene = current.start()
            current = self.scene.following(scene)

        current.start()


class Map(object):
    scenes = {
        "Scene1": Scene1(),
        "Scene2": Scene2(),
        "Scene3": Scene3(),
        "GameOver": GameOver(),
    }

    def __init__(self, scene):
        self.scene = scene

    def first(self):
        return self.following(self.scene)

    def following(self, next_scene):
        value = self.scenes.get(next_scene)
        return value
