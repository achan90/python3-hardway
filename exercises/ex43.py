from sys import exit
from random import randrange


class Death(object):

    quips = ["\nGET REKT.",
             "\nBITCH PLEASE",
             "\nGG NUB",
             "\nKYS",
             "\nYOU SUCK",
             "\nCOME ON",
             "\nWHY THE FUCK DID YOU DO THAT?",
             "\nARE YOU EVEN TRYING?"
             ]

    def enter(self):
        print(Death.quips[randrange(0, len(Death.quips))])
        print("\nGAME OVER\n")
        exit()


class CentralCorridor(object):

    def enter(self):
        print(
            "\nThe Gothons of Planet Percal #25 have invaded your ship",
            "\nand destroyed your entire crew.",

            "\n\nYou are the last surviving member",
            "and your last mission is to get",

            "\nthe neutron destruct bomb from the Weapons Armory,",

            "\nput it in the bridge, and blow the ship up"
            "after getting into an Escape Pod",

            "\n\nYou are running down the Central Corridor,"
            "to the Weapons Armory when",

            "\na Gothon jumps out, red scaly skin, dark grimy teeth,",
            "and evil clown costume",

            "\nflowing around his hate filled body.",

            "\n\nHe's blocking the door to the",

            "\nWeapons Armory and about to pull a weapon to blast you."
        )

        action = input("\n>")

        if action == "shoot":
            print(
                "\nQuick on the draw you yank out your blaster"
                "and fire it at the Gothon.",

                "\n\nHis clown costume is flowing and moving around his body,",
                "which throws of your aim.",

                "\nYour laster hits his costume but misses the creature.",

                "\n\nThis completely ruins his brand new costume"
                "his mother bought him,",

                "\nwhich makes him fly into an insane rage and shoot you"
                "repeatedly in the face.",

                "\n\nShortly your smoldering corpse drops down to the floor",
                "\nand the creature starts feasting on your entrails."
            )
            return "death"

        elif action == "dodge":
            print(
                "\nLike a world class boxer you dodge, weave, slip and slide"
                "right",

                "\nas the Gothon's blaster cranks a laser past your head.",

                "\n\nIn the middle of your artful dodge",
                "your foot slips and you",

                "\nband your head on the metal wall and pass out.",

                "\n\nYou wake up shortly after only to see the creatures"
                "foot descend",

                "\nas he curb stomps your head against the floor,",
                " painting it with your brain matter."
            )
            return "death"

        elif action == "joke":
            print(
                "\nLucky for you they made you learn Gothon's language in the academy.",
                "\nYou tell the creature the only Gothon joke you know:",

                "\n\n'Lbhe zbgure cf fb sng, jura fur fvgf nebhag gur ubhfr, fur fvgf nebhag gur ubhfr.'",

                "\n\nThe Gothon stops, tries not to laugh, then busts out laughing and can't move.",

                "\n\nWhile he's laughing you run up and shoot him straight in the head.",
                "\nYou then jump over his smoldering corpse and make your way through the door."
            )
            return "laser_weapon_armory"

        else:
            print("DOES NOT COMPUTE!")
            return "central_corridor"


class LaserWeaponArmory(object):

    def enter(self):
        print(
            "\nYou do a dive roll into the Weapon Armory, crouch and scan the room for Gothon's.",
            "\nIt's dead quiet, too quiet.",

            "\n\nYou stand up and run to the far side of the room and find the neutron bomb.",
            "\nThe bomb is inside it's container, which is locked with a keypad."

            "\n\nYou need to enter a code to unlock the container.",

            "\n\nIf you enter the code wrong 10 times the container will seal itself permanently.",

            "\n\nThe code is three digits long."
        )

        code = str("{}{}{}".format(randrange(1, 10),
                                   randrange(1, 10), randrange(1, 10)))
        guess = input("\n[keypad]>")
        guesses = 9

        while guess != code and guesses > 0:
            print("BZZZZEEEEDDD!!")
            print("Guesses left", guesses)
            guesses -= 1
            guess = input("\n[keypad]>")

            if guess == "000":
                guess = code

        if guess == code:
            print(
                "\nThe container clicks open and the seal breaks, letting gas out and revealing the bomb.",
                "\nYou grab the neutron bomb and run as fast as you can to the bridge where you must place it."
            )
            return "the_bridge"

        else:
            print(
                "\nThe lock buzzes one last time and you hear a sickening melting sound as the mechanism fuzes shut.",

                "\n\nYou decide to sit there and contemplate your life, while the Gothons blow up ship and you with it."
            )
            return "death"


class TheBridge(object):

    def enter(self):
        print(
            "\nYou burst onto the Bridge with the bomb in hand, surprising group of five Gothons.",
            "\nEach of them has an even glier clown costume than the last.",

            "\n\nThey haven't pulled their weapons out yet, as they see the bomb and don't want to set it off."
        )

        action = input("\n>")

        if action == "throw the bomb.":
            print(
                "\nIn a panic you throw the bomb at the group of Gothons and make a leap for the door.",
                "\nRight as you drop it a Gothon shoots you right in the throat.",

                "\n\nAs you fell down on the floor gurgling your own blood,",
                "\nyou see another Gothon frantically trying to disarm the bomb.",

                "\n\nYou die knowing you have failed miserably as the Gothon successfully disassembles the bomb."
            )
            return "death"

        elif action == "place the bomb":
            print(
                "\nYou point your blaster at the bomb under your arm and the Gothons put their hands up and start to sweat.",

                "\n\nYou slowly inch backward to the door, open it, and carefully place the bomb on the floor,",
                "\nwhile keeping your blaster pointed at it."

                "\n\nYou then jump back through the door, punch the close button and blast the lock.",
                "\nNow that the bomb is placed and you have sealed the Gothons to the room you run to the escape pod."
            )
            return "escape_pod"

        else:
            print("DOES NOT COMPUTE!")
            return "the_bridge"


class EscapePod(object):

    def enter(self):
        print(
            "\nYou rush through the ship desperately trying to make it to the escape pod before the bomb explodes.",
            "\nIt seems like hardly any Gothons are on the ship, so your run is clear of interference.",

            "\n\nYou get to the chamber with the escape pods, and now need to pick one to take.",
            "\nSome of them could be damaged, but you don't have enough time to inspect them.",

            "\n\nThere's total of five pods, which one do you take?"
        )

        good_pod = randrange(1, 6)
        guess = int(input("\n[pod #]>"))

        if guess != good_pod:
            print(
                "\nYou jump into pod {} and hit the eject button.",
                "\nThe pod escapes out into the void of space,",
                "\nthen implodes as the hull ruptures, crushing your body into jam jelly.".format(
                    guess)
            )
            return "death"

        else:
            print(
                "\nYou jump into pod {} and hit the eject button.",
                "\nThe pod easily slides out into space and starts heading to planet belows"

                "\n\nAs it flies towards the planet, you look back and see your ship implode,",
                "\nand then explode like a bright star, taking out the Gothon ship.".format(
                    guess)
            )
            return "finished"


class Finished(object):

    def enter(self):
        print("You won! Good job!")
        return "finished"


# Määrittää luokan Map
class Map(object):
    # Määrittää sanakirjan scenes
    scenes = {
        "central_corridor": CentralCorridor(),
        "laser_weapon_armory": LaserWeaponArmory(),
        "the_bridge": TheBridge(),
        "escape_pod": EscapePod(),
        "death": Death(),
        "finished": Finished(),
    }

    # määrittää initin, joka ottaa self ja start_scene argumentit.
    def __init__(self, start_scene):
        # määrittää muuttujan self.start_scene arvoksi start_scene argumentin.
        self.start_scene = start_scene

    # määrittää funktion next_scene joka ottaa argumentit self ja scene_name.
    def next_scene(self, scene_name):
        # määrittää muuttujan val arvoksi Map.scenes dictionaryn,
        # jolle on kutsuttu funktio get parametrillä scene_name.
        val = Map.scenes.get(scene_name)
        # määrittää funktion arvoksi muuttujan val.
        return val

    # määrittää funktion opening_scene, joka ottaa argumentin self.
    def opening_scene(self):
        # määrittää funktion arvoksi muuttujan self, jolle on kutsuttu
        # next_scene funktio parametrilä self.start_scene
        return self.next_scene(self.start_scene)


# määrittää luokan Engine.
class Engine(object):
    # määrittää initin, joka ottaa self ja scene_map argumentit.
    def __init__(self, scene_map):
        # määrittää self.scene_map muuttujan arvoksi scene_map argumentin.
        self.scene_map = scene_map

    # määrittää funktion play, joka ottaa argumentin self.
    def play(self):
        # määrittää muuttujan curren_scene arvoksi self.scene_map muuttujan,
        # jolle on kutsuttu funktio opening_scene.
        current_scene = self.scene_map.opening_scene()
        # määrittää muuttujan last_scene arvoks self.scene_map muuttujan, jolle
        # on kutsuttu funktio next_scene parametrillä 'finished'.
        last_scene = self.scene_map.next_scene('finished')

        # määrittää loopin, joka pyörii niin kauan kun curren_scene ja
        # last_scene muuttujilla on eri arvot.
        while current_scene != last_scene:
            # määrittää muuttujan next_scene_name arvoksi muuttujan
            # current_scene jolle on kutsuttu enter funktio.
            next_scene_name = current_scene.enter()
            # määrittää muuttujan current_scene arvoksi self.scene_map
            # muuttujan jolle on kutsuttu funktio next_scene parametrillä
            # next_scene_name.
            current_scene = self.scene_map.next_scene(next_scene_name)

        # kutsuu muuttujalle current_scene funktion enter.
        current_scene.enter()


# Finally I've got my code that runs the game by making a Map,
# then handing that map to an Engine before calling play to make the game work.
a_map = Map('central_corridor')
a_game = Engine(a_map)
a_game.play()
