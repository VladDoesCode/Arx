import sys
import time as t

import consoleManager
import universalFunctions
from classes import Hero
from universalFunctions import printSlow

# PADDING = consoleManager.Rectangle(0, 5, 12, 0)


def beginGame():
    global mainChar
    # with consoleManager.ConsoleManager(consoleManager.ConsoleStandardHandle.STD_OUTPUT_HANDLE) as console:
    showStats = True
    askName()
    askClass()
    mainChar = Hero(100, 10, classSelect)
    universalFunctions.set_hp(100, showStats, mainChar, 100, True)
    universalFunctions.set_mana(
        mainChar.manaPoolmax, showStats, mainChar, mainChar.manaPoolmax, True)
    universalFunctions.set_stamina(
        mainChar.staminaPoolmax, showStats, mainChar, mainChar.staminaPoolmax, True)
    universalFunctions.set_armor(10, showStats, mainChar, 10, True)
    dialogue1()


# ------------------------------------------
# Break to indicate all the functions below:
# ------------------------------------------


def askName():
    printSlow("Hello Adventurer, what is your name?")
    name = input("> ")
    while len(name) > 18 or len(name) < 3:
        if len(name) > 18:
            printSlow(
                "Ive never met an Adventurer with such a long name, what else do you go by?")
        elif len(name) < 3:
            printSlow(
                "Ive never met an Adventurer with such a short name, what else do you go by?")
        name = input("> ")
    printSlow("Welcome, %s" % name.capitalize() + " to the city of Arx!")


def askClass():
    global classSelect
    printSlow(
        "What class would you like to play, [Commoner], [Warrior], [Mage], [Thief], or [Paladin]?")
    classSelect = input("> ")
    while classSelect.lower() not in ["commoner", "warrior", "mage", "thief", "paladin"]:
        printSlow(
            "Come again, which class? [Commoner], [Warrior], [Mage], [Thief], or [Paladin].")
        classSelect = input("> ")


def dialogue1():
    printSlow(f"Agility: {mainChar.agility}")
    printSlow(f"Charisma: {mainChar.charisma}")
    printSlow(f"Intelligence: {mainChar.intelligence}")
    printSlow(f"Mana Pool Max: {mainChar.manaPoolmax}")
    printSlow(f"Stamina Pool Max: {mainChar.staminaPoolmax}")
    printSlow(f"Strength: {mainChar.strength}")
    printSlow(f"_Health: {mainChar._health}")
    printSlow(f"_Armor: {mainChar._armor}")
    printSlow(f"Health: {mainChar.health}")
    printSlow(f"Armor: {mainChar.armor}")
