import begin
import time as t
import consolemanager
from universalFunctions import printSlow, scroll_text_up, clear_screen
from colored import fg

console_info = ""
PADDING = consolemanager.Rectangle(0, 6, 12, 0)
PADDINGNONE = consolemanager.Rectangle(0, 0, 1, 0)
PADDINGART = consolemanager.Rectangle(0, 23, 1, 0)

PADDINGMIDDLE = consolemanager.Rectangle(0, 14, 1, 2)
PADDINGBATTLE = consolemanager.Rectangle(0, 14, 29, 2)
PADDINGWIPEART = consolemanager.Rectangle(0, 0, 1, 16)


def titleScreen():
    # Function to create Ascii Art Main Menu.
    global console_info
    console = begin.console
    console_info = console.get_console_info()
    image = [
        "      _____        _____",
        "  ___|\    \   ___|\    \  _____      _____",
        " /    /\    \ |    |\    \ \    \    /    /",
        "|    |  |    ||    | |    | \    \  /    /",
        "|    |__|    ||    |/____/   \____\/____/",
        "|    .--.    ||    |\    \   /    /\    \ ",
        "|    |  |    ||    | |    | /    /  \    \ ",
        "|____|  |____||____| |____|/____/ /\ \____\ ",
        "|    |  |    ||    | |    ||    |/  \|    |",
        "|____|  |____||____| |____||____|    |____|",
        "  \(      )/    \(     )/    \(        )/",
        "   '      '      '     '      '        '",
    ]
    for line in image:
        console.set_cursor_pos(35, console_info.window_rectangle.bottom - 1)
        printSlow(line, 0.05, True, 0, PADDINGNONE)

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

    introChoice = input(
        printSlow("Whats your choice, Adventurer? > ", 0, False))
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
            introChoice = input(
                printSlow("I didn't catch that, Huh? > ", 0, False))

    t.sleep(0.5)
    clear_screen(PADDINGNONE, 0.05)
    createGameArea()


# █=►─═─═━═─═─◄=█
def createGameArea():
    console = begin.console
    console.set_cursor_pos(0, 13)
    printSlow(
        "█=►─═─═" +
        ("=" * (console_info.window_rectangle.right - 14)) + "═─═─◄=█",
        0,
        False,
        0.01,
    )
    console.set_cursor_pos(0, console_info.window_rectangle.bottom - 2)
    printSlow(
        "█=►─═─═" +
        ("=" * (console_info.window_rectangle.right - 14)) + "═─═─◄=█",
        0,
        False,
        0.01,
    )
    mountains()


def mountains():
    console = begin.console
    image = [
        "                                                           ,",
        "                                                          ƒ'▐▄",
        "                                                        ▄▀   ███▄",
        "                                                      ⌐'  ,   ▀███▄",
        "                                                    ,'   ▐█▀    ████▄                 ____ _____ __  __",
        "                                           ,═▄     ,   ▄██▀ ,▌   █████▄,   ,         / () \| () )\ \/ /",
        "                                         ¿'  ▀███▄▄   '▀-  ╒█      ▀▀████▄' ▀█▄     /__/\__\_|\_\/_/\_\ ",
        "            ,∞▄                         ╛ ╓█▌ `▀███▄    ▀▀ ▐▀¥       █████    ███▄                       ╛V▄",
        "          ¿`   ▀█▄▄▄,,                ,'  █▀▀    ▀██▌   ▄████▄      ██████r    ████▄                   Æ   ██▄",
        "        ,' ▀▀   ███████▄▄  .─`  ██▄═^`    '▀        '  █▀▄██▀       ▐██████▄ ,    ▐██▄              ,═ ╓▀╓ '▀██▄",
        "      ⌐'  ▀ ▀▀    ████▀████▄      █▄          ▄▄█▀'   ╙  `           ▐██████ ▀     ████▄          ═   ▀▌▄'   ▄▄▀█▄",
        "   ,.^   , █▀  ,     ▀  ▄██████      ╘▄     4▀`             ,▄▄         ██████`J▄     ███████▄⌐══^`    ██▌ █    ▀██▄",
        ",.^    ▀▀ ,              ▀█▌▀ ▀═       `                  ▄█▀▀  ███▄    ▐▀███' ▄ `    ██████▌          █▀ █'     ▀▀▀█▄▄",
    ]
    yPos = 0
    for line in image:
        console.set_cursor_pos(0, yPos)
        printSlow(line, 0, False, 0.004)
        yPos += 1


def drawWarrior():
    console = begin.console
    i = fg("#ff0077")

    Warrior = [
        "\x1b[38;5;15m  \x1b[38;5;15m  \x1b[38;5;15m  \x1b[38;5;15m  \x1b[38;5;247m██\x1b[38;5;247m██\x1b[38;5;247m██\x1b[38;5;247m██\x1b[38;5;243m██\x1b[38;5;243m██\x1b[38;5;15m  \x1b[38;5;15m  \x1b[38;5;15m  \x1b[38;5;15m  \x1b[38;5;247m██\x1b[38;5;247m██\x1b[0m",
        "\x1b[38;5;15m  \x1b[38;5;15m  \x1b[38;5;15m  \x1b[38;5;15m  \x1b[38;5;247m██\x1b[38;5;247m██\x1b[38;5;247m██\x1b[38;5;247m██\x1b[38;5;243m██\x1b[38;5;243m██\x1b[38;5;15m  \x1b[38;5;15m  \x1b[38;5;15m  \x1b[38;5;15m  \x1b[38;5;247m██\x1b[38;5;247m██\x1b[0m",
        "\x1b[38;5;15m  \x1b[38;5;15m  \x1b[38;5;243m██\x1b[38;5;243m██\x1b[38;5;247m██\x1b[38;5;247m██\x1b[38;5;247m██\x1b[38;5;247m██\x1b[38;5;243m██\x1b[38;5;243m██\x1b[38;5;243m██\x1b[38;5;243m██\x1b[38;5;15m  \x1b[38;5;15m  \x1b[38;5;247m██\x1b[38;5;247m██\x1b[0m",
        "\x1b[38;5;15m  \x1b[38;5;15m  \x1b[38;5;243m██\x1b[38;5;243m██\x1b[38;5;247m██\x1b[38;5;247m██\x1b[38;5;247m██\x1b[38;5;247m██\x1b[38;5;243m██\x1b[38;5;243m██\x1b[38;5;243m██\x1b[38;5;243m██\x1b[38;5;15m  \x1b[38;5;15m  \x1b[38;5;247m██\x1b[38;5;247m██\x1b[0m",
        "\x1b[38;5;15m  \x1b[38;5;15m  \x1b[38;5;243m██\x1b[38;5;243m██\x1b[38;5;221m██\x1b[38;5;221m██\x1b[38;5;0m██\x1b[38;5;0m██\x1b[38;5;221m██\x1b[38;5;221m██\x1b[38;5;0m██\x1b[38;5;0m██\x1b[38;5;15m  \x1b[38;5;15m  \x1b[38;5;247m██\x1b[38;5;247m██\x1b[0m",
        "\x1b[38;5;15m  \x1b[38;5;15m  \x1b[38;5;243m██\x1b[38;5;243m██\x1b[38;5;221m██\x1b[38;5;221m██\x1b[38;5;0m██\x1b[38;5;0m██\x1b[38;5;221m██\x1b[38;5;221m██\x1b[38;5;0m██\x1b[38;5;0m██\x1b[38;5;15m  \x1b[38;5;15m  \x1b[38;5;247m██\x1b[38;5;247m██\x1b[0m",
        "\x1b[38;5;15m  \x1b[38;5;15m  \x1b[38;5;137m██\x1b[38;5;137m██\x1b[38;5;221m██\x1b[38;5;221m██\x1b[38;5;221m██\x1b[38;5;221m██\x1b[38;5;221m██\x1b[38;5;221m██\x1b[38;5;221m██\x1b[38;5;221m██\x1b[38;5;15m  \x1b[38;5;15m  \x1b[38;5;247m██\x1b[38;5;247m██\x1b[0m",
        "\x1b[38;5;15m  \x1b[38;5;15m  \x1b[38;5;137m██\x1b[38;5;137m██\x1b[38;5;221m██\x1b[38;5;221m██\x1b[38;5;221m██\x1b[38;5;221m██\x1b[38;5;221m██\x1b[38;5;221m██\x1b[38;5;221m██\x1b[38;5;221m██\x1b[38;5;15m  \x1b[38;5;15m  \x1b[38;5;247m██\x1b[38;5;247m██\x1b[0m",
        "\x1b[38;5;243m██\x1b[38;5;243m██\x1b[38;5;243m██\x1b[38;5;243m██\x1b[38;5;247m██\x1b[38;5;247m██\x1b[38;5;247m██\x1b[38;5;247m██\x1b[38;5;247m██\x1b[38;5;247m██\x1b[38;5;243m██\x1b[38;5;243m██\x1b[38;5;243m██\x1b[38;5;243m██\x1b[38;5;221m██\x1b[38;5;221m██\x1b[0m",
        "\x1b[38;5;243m██\x1b[38;5;243m██\x1b[38;5;243m██\x1b[38;5;243m██\x1b[38;5;247m██\x1b[38;5;247m██\x1b[38;5;247m██\x1b[38;5;247m██\x1b[38;5;247m██\x1b[38;5;247m██\x1b[38;5;243m██\x1b[38;5;243m██\x1b[38;5;243m██\x1b[38;5;243m██\x1b[38;5;221m██\x1b[38;5;221m██\x1b[0m",
        "\x1b[38;5;221m██\x1b[38;5;221m██\x1b[38;5;58m██\x1b[38;5;58m██\x1b[38;5;130m██\x1b[38;5;130m██\x1b[38;5;130m██\x1b[38;5;130m██\x1b[38;5;247m██\x1b[38;5;247m██\x1b[38;5;58m██\x1b[38;5;58m██\x1b[38;5;94m  \x1b[38;5;15m  \x1b[38;5;15m  \x1b[38;5;15m  \x1b[0m",
        "\x1b[38;5;221m██\x1b[38;5;221m██\x1b[38;5;58m██\x1b[38;5;58m██\x1b[38;5;130m██\x1b[38;5;130m██\x1b[38;5;130m██\x1b[38;5;130m██\x1b[38;5;247m██\x1b[38;5;247m██\x1b[38;5;58m██\x1b[38;5;58m██\x1b[38;5;94m  \x1b[38;5;15m  \x1b[38;5;15m  \x1b[38;5;15m  \x1b[0m",
        "\x1b[38;5;15m  \x1b[38;5;15m  \x1b[38;5;243m██\x1b[38;5;243m██\x1b[38;5;243m██\x1b[38;5;243m██\x1b[38;5;243m██\x1b[38;5;243m██\x1b[38;5;243m██\x1b[38;5;243m██\x1b[38;5;243m██\x1b[38;5;243m██\x1b[38;5;94m  \x1b[38;5;15m  \x1b[38;5;15m  \x1b[38;5;15m  \x1b[0m",
        "\x1b[38;5;15m  \x1b[38;5;15m  \x1b[38;5;243m██\x1b[38;5;243m██\x1b[38;5;243m██\x1b[38;5;243m██\x1b[38;5;243m██\x1b[38;5;243m██\x1b[38;5;243m██\x1b[38;5;243m██\x1b[38;5;243m██\x1b[38;5;243m██\x1b[38;5;94m  \x1b[38;5;15m  \x1b[38;5;15m  \x1b[38;5;15m  \x1b[0m",
        "\x1b[38;5;15m  \x1b[38;5;15m  \x1b[38;5;58m██\x1b[38;5;58m██\x1b[38;5;94m  \x1b[38;5;15m  \x1b[38;5;15m  \x1b[38;5;15m  \x1b[38;5;15m  \x1b[38;5;15m  \x1b[38;5;58m██\x1b[38;5;58m██\x1b[38;5;94m  \x1b[38;5;15m  \x1b[38;5;15m  \x1b[38;5;15m  \x1b[0m",
        "\x1b[38;5;15m  \x1b[38;5;15m  \x1b[38;5;58m██\x1b[38;5;58m██\x1b[38;5;94m  \x1b[38;5;15m  \x1b[38;5;15m  \x1b[38;5;15m  \x1b[38;5;15m  \x1b[38;5;15m  \x1b[38;5;58m██\x1b[38;5;58m██\x1b[38;5;94m  \x1b[38;5;15m  \x1b[38;5;15m  \x1b[38;5;15m  \x1b[0m",
    ]

    yPos = 1
    for i in range(len(Warrior)):
        console.set_cursor_pos(30, yPos)
        print(Warrior[i])
        # printSlow(Warrior[i], 0, False, 0.01)
        yPos += 1
