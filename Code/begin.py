import sys
import time as t

import consolemanager
import universalFunctions
import imageBasedFunctions
import random
from classes import *
from universalFunctions import printSlow, qAnswer, monsterFight

PADDINGNONE = consolemanager.Rectangle(0, 0, 1, 0)
PADDINGMIDDLE = consolemanager.Rectangle(0, 23, 1, 2)
PADDINGWIPEART = consolemanager.Rectangle(0, 0, 1, 18)

console = consolemanager.Console(std_handle=consolemanager.ConsoleStandardHandle.STD_OUTPUT_HANDLE)
console.resize(170, 41)
console_info = console.get_console_info()

console.set_title("ARX")
console.set_cursor_info(size=1, visibility=False)
console.clear_screen()
mainChar = ""
classSelect = ""


def beginGame():
    "Beggining of the game"

    global mainChar
    console.set_cursor_pos(0, console_info.window_rectangle.bottom - 1)

    imageBasedFunctions.titleScreen()
    askName()
    askClass()
    mainChar = Hero(100, 10, classSelect)
    dialogue1()


# ------------------------------------------
# Break to indicate all the functions below:
# ------------------------------------------

name = ""


def askName():
    global name
    name = qAnswer("Hello Adventurer, what is your name?")
    while len(name) > 17 or len(name) < 3:
        if len(name) > 17:
            universalFunctions.clear_screen()
            name = qAnswer("Thats a mighty long name, do you go by something shorter?")
        elif len(name) < 3 and len(name) > 0:
            universalFunctions.clear_screen()
            name = qAnswer(
                "Ive never met an Adventurer with such a short name, what else do you go by?"
            )
        elif len(name) == 0:
            universalFunctions.clear_screen()
            name = qAnswer(
                "What, are you just going to sit there and say nothing? Give me your name."
            )
    console.set_cursor_pos(0, console_info.window_rectangle.bottom - 3)
    printSlow(f"Welcome {name}, to the world of Arx!", 0, True)


def askClass():
    global classSelect
    classSelect = qAnswer(
        "What class would you like to play, [Commoner], [Warrior], [Mage], [Thief], or [Paladin]?"
    )
    while classSelect.lower() not in [
        "commoner",
        "warrior",
        "mage",
        "thief",
        "paladin",
    ]:
        universalFunctions.clear_screen()
        classSelect = qAnswer(
            "Come again, which class? [Commoner], [Warrior], [Mage], [Thief], or [Paladin]."
        )


def class_art():
    if mainChar.charClass == "commoner":
        imageBasedFunctions.drawCommoner()
    if mainChar.charClass == "warrior":
        imageBasedFunctions.drawWarrior()
    if mainChar.charClass == "mage":
        imageBasedFunctions.drawMage()
    if mainChar.charClass == "thief":
        imageBasedFunctions.drawThief()
    if mainChar.charClass == "paladin":
        imageBasedFunctions.drawPaladin()


def monster_art(monster):
    if monster.name == "Skeleton":
        imageBasedFunctions.drawSkeleton()


def dialogue1():
    universalFunctions.playerStats(mainChar)
    universalFunctions.statMeaning()

    # First choice
    printSlow("Now that you're situated with your stats, would you like to:",
              0, True, 0.02, PADDINGMIDDLE)
    answer = qAnswer(
        "[1] Visit the Town or [2] Fight a Monster?", False, PADDINGMIDDLE)
    while answer not in ["2"]:
        if answer == "1":
            printSlow("The town isn't avaliable yet, try again later ;)",
                      1, True, 0.02, PADDINGMIDDLE)
            clear_screen(PADDINGMIDDLE)
            printSlow(
                "Now that you're situated with your stats, would you like to:",
                0, True, 0.02, PADDINGMIDDLE)
            answer = qAnswer(
                "[1] Visit the Town or [2] Fight a Monster?", False, PADDINGMIDDLE)
        else:
            printSlow("I didn't catch your answer, come again?")
            answer = qAnswer(
                "[1] Visit the Town or [2] Fight a Monster?", False, PADDINGMIDDLE)

    if answer == "2":
        universalFunctions.clear_screen(PADDINGMIDDLE)
        printSlow(
            "Alright lets climb this hill, I think I see some monsters on top!", 0, True, 0.02, PADDINGMIDDLE)
        printSlow("", 0, True, 0.02, PADDINGMIDDLE)

    universalFunctions.clear_screen(PADDINGWIPEART)
    monster1 = Monster("skeleton", mainChar)
    monsterFight(monster1, mainChar)

    # ---------------------------------------
    #         THIS IS THE END SO FAR
    # EVERYTHING BELOW THIS IS JUST TEMPORARY
    # ---------------------------------------

    printSlow(
        "This is the end so far! More to come soon, let me know of any ideas you have for Arx!"
    )
    while True:
        answer = qAnswer(
            "For the mean time you can fight another monster! Type [1] to do so."
        )
        if answer == "1":
            monster1 = Monster("skeleton", mainChar)
            monsterFight(monster1, mainChar)
        else:
            clear_screen(PADDINGNONE)
            printSlow(f"Thank you very much for playing Arx! {name}")
            t.sleep(1)
            exit()
