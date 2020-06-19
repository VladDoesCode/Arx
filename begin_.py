import sys
import time as t

import consolemanager
import universalFunctions
from classes import Hero
from universalFunctions import printSlow
from universalFunctions import qAnswer

with consolemanager.ConsoleManager(consolemanager.ConsoleStandardHandle.STD_OUTPUT_HANDLE) as console:

    console_info = console.get_console_info()
    console.set_title("Arx")
    console.set_cursor_info(size=1, visibility=False)
    console.clear_screen()

#   Beggining of the game!
    def beginGame():
        global mainChar
        safeZone = 0
        showStats = True
        console.set_cursor_pos(0, console_info.window_rectangle.bottom - 1)

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
    name = qAnswer("Hello Adventurer, what is your name?")
    while len(name) > 18 or len(name) < 3:
        if len(name) > 18:
            universalFunctions.clear_screen()
            name = qAnswer(
                "I rather not waste breath on such a long name, what else do you go by?")
        elif len(name) < 3 and len(name) > 0:
            universalFunctions.clear_screen()
            name = qAnswer(
                "Ive never met an Adventurer with such a short name, what else do you go by?")
        elif len(name) == 0:
            universalFunctions.clear_screen()
            name = qAnswer(
                "What, are you just going to sit there any say nothing? Give me your name.")

    printSlow(f"Welcome {name}, to the world of Arx!")
    printSlow('A text based adventure created by Vladimir!')
    printSlow('With help from friends! (credits to come.)')
    universalFunctions.confirm()


def askClass():
    global classSelect
    classSelect = qAnswer(
        "What class would you like to play, [Commoner], [Warrior], [Mage], [Thief], or [Paladin]?")
    while classSelect.lower() not in ["commoner", "warrior", "mage", "thief", "paladin"]:
        universalFunctions.clear_screen()
        classSelect = qAnswer(
            "Come again, which class? [Commoner], [Warrior], [Mage], [Thief], or [Paladin].")


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
