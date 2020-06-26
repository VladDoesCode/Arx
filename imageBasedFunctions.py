import begin
import time as t
import consolemanager
from universalFunctions import printSlow, scroll_text_up, clear_screen

console_info = ""
PADDING = consolemanager.Rectangle(0, 6, 12, 0)
PADDINGNONE = consolemanager.Rectangle(0, 0, 1, 0)
PADDINGART = consolemanager.Rectangle(0, 23, 1, 0)

PADDINGMIDDLE = consolemanager.Rectangle(0, 14, 1, 2)
PADDINGBATTLE = consolemanager.Rectangle(0, 14, 28, 2)

"""
   _____   __________ ____  ___
  /  _  \  \______   \\   \/  /
 /  /_\  \  |       _/ \     /
/    |    \ |    |   \ /     \ 
\____|__  / |____|_  //___/\  \ 
        \/         \/       \_/
"""


def setArx():
    console = begin.console
    console.set_cursor_pos(console.get_console_info().window_rectangle.right - 30, 0)
    printSlow("   _____  __________ ____  ___ ", 0, False, 0.012)
    console.set_cursor_pos(console.get_console_info().window_rectangle.right - 30, 1)
    printSlow("  /  _  \ \______   \\\   \/  /", 0, False, 0.012)
    console.set_cursor_pos(console.get_console_info().window_rectangle.right - 30, 2)
    printSlow(" /  /_\  \ |       _/ \     /  ", 0, False, 0.012)
    console.set_cursor_pos(console.get_console_info().window_rectangle.right - 30, 3)
    printSlow("/    |    \|    |   \ /     \  ", 0, False, 0.012)
    console.set_cursor_pos(console.get_console_info().window_rectangle.right - 30, 4)
    printSlow("\____|__  /|____|_  //___/\  \ ", 0, False, 0.012)
    console.set_cursor_pos(console.get_console_info().window_rectangle.right - 30, 5)
    printSlow("        \/        \/       \_/ ", 0, False, 0.012)


"""
      _____        _____
  ___|\    \   ___|\    \  _____      _____
 /    /\    \ |    |\    \ \    \    /    /
|    |  |    ||    | |    | \    \  /    /
|    |__|    ||    |/____/   \____\/____/
|    .--.    ||    |\    \   /    /\    \
|    |  |    ||    | |    | /    /  \    \
|____|  |____||____| |____|/____/ /\ \____\
|    |  |    ||    | |    ||    |/  \|    |
|____|  |____||____| |____||____|    |____|
  \(      )/    \(     )/    \(        )/
   '      '      '     '      '        '
"""


#   This is the ascii art logo.
def titleScreen():
    global console_info
    console = begin.console
    console_info = console.get_console_info()
    console.set_cursor_pos(35, console_info.window_rectangle.bottom - 1)
    printSlow("      _____        _____                   ", 0.05, True, 0, PADDINGNONE)
    console.set_cursor_pos(35, console_info.window_rectangle.bottom - 1)
    printSlow("  ___|\    \   ___|\    \  _____      _____", 0.05, True, 0, PADDINGNONE)
    console.set_cursor_pos(35, console_info.window_rectangle.bottom - 1)
    printSlow(" /    /\    \ |    |\    \ \    \    /    /", 0.05, True, 0, PADDINGNONE)
    console.set_cursor_pos(35, console_info.window_rectangle.bottom - 1)
    printSlow("|    |  |    ||    | |    | \    \  /    / ", 0.05, True, 0, PADDINGNONE)
    console.set_cursor_pos(35, console_info.window_rectangle.bottom - 1)
    printSlow("|    |__|    ||    |/____/   \____\/____/  ", 0.05, True, 0, PADDINGNONE)
    console.set_cursor_pos(35, console_info.window_rectangle.bottom - 1)
    printSlow("|    .--.    ||    |\    \   /    /\    \  ", 0.05, True, 0, PADDINGNONE)
    console.set_cursor_pos(35, console_info.window_rectangle.bottom - 1)
    printSlow("|    |  |    ||    | |    | /    /  \    \ ", 0.05, True, 0, PADDINGNONE)
    console.set_cursor_pos(35, console_info.window_rectangle.bottom - 1)
    printSlow(
        "|____|  |____||____| |____|/____/ /\ \____\ ", 0.05, True, 0, PADDINGNONE
    )
    console.set_cursor_pos(35, console_info.window_rectangle.bottom - 1)
    printSlow("|    |  |    ||    | |    ||    |/  \|    |", 0.05, True, 0, PADDINGNONE)
    console.set_cursor_pos(35, console_info.window_rectangle.bottom - 1)
    printSlow("|____|  |____||____| |____||____|    |____|", 0.05, True, 0, PADDINGNONE)
    console.set_cursor_pos(35, console_info.window_rectangle.bottom - 1)
    printSlow("  \(      )/    \(     )/    \(        )/  ", 0.05, True, 0, PADDINGNONE)
    console.set_cursor_pos(35, console_info.window_rectangle.bottom - 1)
    printSlow("   '      '      '     '      '        '   ", 0.05, True, 0, PADDINGNONE)
    console.set_cursor_pos(23, console_info.window_rectangle.bottom - 1)
    printSlow(
        "A text based adventure game made by Vladimir with help from friends.",
        0.05,
        True,
        0,
        PADDINGNONE,
    )
    console.set_cursor_pos(29, console_info.window_rectangle.bottom - 1)
    printSlow(
        "- Inspired by Choose Your Own Adventure Books and D&D -",
        0.05,
        True,
        0,
        PADDINGNONE,
    )
    for row in range(8):
        t.sleep(0.05)
        scroll_text_up(PADDINGNONE)
    console.set_cursor_pos(31, 22)
    printSlow("[1. Start New Game] [2. Load Game] [3. Game Credit]", 0, False)
    console.set_cursor_pos(40, 23)

    introChoice = input(printSlow("Whats your choice, Adventurer? > ", 0, False))
    while introChoice != "1":
        console.set_cursor_pos(40, 23)
        if introChoice == "1":
            break
        elif introChoice == "2" or introChoice == "3":
            console.set_cursor_pos(25, 25)
            printSlow(
                "That part of Arx isn't ready yet, try again in the next release!",
                1,
                False,
            )
            console.clear_line(25)
            console.clear_line(23)
            console.set_cursor_pos(40, 23)
            introChoice = input(
                printSlow("Whats your choice, Adventurer? > ", 0, False)
            )
        else:
            console.clear_line(23)
            console.set_cursor_pos(42, 23)
            introChoice = input(printSlow("I didn't catch that, Huh? > ", 0, False))

    t.sleep(0.5)
    clear_screen(PADDINGNONE, 0.05)
    createGameArea()


# █=►─═─═━═─═─◄=█
def createGameArea():
    console = begin.console
    console.set_cursor_pos(0, 13)
    printSlow(
        "█=►─═─═" + ("=" * (console_info.window_rectangle.right - 14)) + "═─═─◄=█",
        0,
        False,
        0.01,
    )
    console.set_cursor_pos(0, console_info.window_rectangle.bottom - 2)
    printSlow(
        "█=►─═─═" + ("=" * (console_info.window_rectangle.right - 14)) + "═─═─◄=█",
        0,
        False,
        0.01,
    )
    mountains()


"""
                                                                    ,                                                                  1               
                                                                   ƒ'▐▄                                                                2               
                                                                 ▄▀   ███▄                                                             3               
                                                               ⌐'  ,   ▀███▄                                                           4               
                                                            ,'   ▐█▀    ████▄                                                          5               
                                                   ,═▄     ,   ▄██▀ ,▌   █████▄,   ,                                                   6              
                                                 ¿'  ▀███▄▄   '▀-  ╒█      ▀▀████▄' ▀█▄                                                7               
                    ,∞▄                         ╛ ╓█▌ `▀███▄    ▀▀ ▐▀¥       █████    ███▄                       ╛V▄                   8               
                  ¿`   ▀█▄▄▄,,                ,'  █▀▀    ▀██▌   ▄████▄      ██████r    ████▄                   Æ   ██▄                 9               
                ," ▀▀   ███████▄▄  .─`  ██▄═^`    '▀        '  █▀▄██▀       ▐██████▄ ,    ▐██▄              ,═ ╓▀╓ '▀██▄               10               
              ⌐'  ▀ ▀▀    ████▀████▄      █▄          ▄▄█▀"   ╙  `           ▐██████ ▀     ████▄          ═   ▀▌▄"   ▄▄▀█▄             11               
         ,.^   , █▀  ,     ▀  ▄██████      ╘▄     4▀`             ,▄▄         ██████`J▄     ███████▄⌐══^`    ██▌ █    ▀██ ██▄          12               
      ,.^    ▀▀ ,              ▀█▌▀ ▀═       `                  ▄█▀▀  ███▄    ▐▀███' ▄ `    ██████▌          █▀ █'    █▄▀' ▀▀▀▀█▄▄,    13               
"""
"""
   ____ _____ __  __
  / () \| () )\ \/ /
 /__/\__\_|\_\/_/\_\ 
"""


def mountains():
    console = begin.console
    console.set_cursor_pos(0, 0)
    printSlow(
        "                                                             ,",
        0,
        False,
        0.006,
    )
    console.set_cursor_pos(0, 1)
    printSlow(
        "                                                            ƒ'▐▄",
        0,
        False,
        0.006,
    )
    console.set_cursor_pos(0, 2)
    printSlow(
        "                                                          ▄▀   ███▄",
        0,
        False,
        0.006,
    )
    console.set_cursor_pos(0, 3)
    printSlow(
        "                                                        ⌐'  ,   ▀███▄                 ____ _____ __  __",
        0,
        False,
        0.006,
    )
    console.set_cursor_pos(0, 4)
    printSlow(
        "                                                     ,'   ▐█▀    ████▄               / () \| () )\ \/ /",
        0,
        False,
        0.006,
    )
    console.set_cursor_pos(0, 5)
    printSlow(
        "                                            ,═▄     ,   ▄██▀ ,▌   █████▄,   ,       /__/\__\_|\_\/_/\_\ ",
        0,
        False,
        0.006,
    )
    console.set_cursor_pos(0, 6)
    printSlow(
        "                                          ¿'  ▀███▄▄   '▀-  ╒█      ▀▀████▄' ▀█▄",
        0,
        False,
        0.006,
    )
    console.set_cursor_pos(0, 7)
    printSlow(
        "             ,∞▄                         ╛ ╓█▌ `▀███▄    ▀▀ ▐▀¥       █████    ███▄                       ╛V▄",
        0,
        False,
        0.006,
    )
    console.set_cursor_pos(0, 8)
    printSlow(
        "           ¿`   ▀█▄▄▄,,                ,'  █▀▀    ▀██▌   ▄████▄      ██████r    ████▄                   Æ   ██▄",
        0,
        False,
        0.006,
    )
    console.set_cursor_pos(0, 9)
    printSlow(
        "         ,' ▀▀   ███████▄▄  .─`  ██▄═^`    '▀        '  █▀▄██▀       ▐██████▄ ,    ▐██▄              ,═ ╓▀╓ '▀██▄",
        0,
        False,
        0.006,
    )
    console.set_cursor_pos(0, 10)
    printSlow(
        "       ⌐'  ▀ ▀▀    ████▀████▄      █▄          ▄▄█▀'   ╙  `           ▐██████ ▀     ████▄          ═   ▀▌▄'   ▄▄▀█▄",
        0,
        False,
        0.006,
    )
    console.set_cursor_pos(0, 11)
    printSlow(
        "  ,.^   , █▀  ,     ▀  ▄██████      ╘▄     4▀`             ,▄▄         ██████`J▄     ███████▄⌐══^`    ██▌ █    ▀██ ██▄",
        0,
        False,
        0.006,
    )
    console.set_cursor_pos(0, 12)
    printSlow(
        ".^    ▀▀ ,              ▀█▌▀ ▀═       `                  ▄█▀▀  ███▄    ▐▀███' ▄ `    ██████▌          █▀ █'    █▄▀' ▀▀█▄",
        0,
        True,
        0.006,
    )
