# -*- coding: utf-8 -*-

from sys import exit


def game_over():
    print("\nHävisit Pelin!")
    exit(0)


def you_win():
    print("\nHöhhöh höö, kutittaa. \nVoitit pelin!")
    exit(0)


def start():
    print("Sakarin villapaita peli.")
    print("Pue Sakarille villapaita?")
    print("1. Joo.")
    print("2. En.")

    while True:
        wool_shirt = input(">")

        if wool_shirt == "1":
            you_win()
        elif wool_shirt == "2":
            game_over()
        else:
            print("\nValitse 1 tai 2")


start()
