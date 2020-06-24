import time, begin, consolemanager

from begin import console

console_info = console.get_console_info()

def printSlow(fstr, waitTime=0, nextLine=True, typeSpeed=0.03, PADDINGAREA=0):
    console = begin.console
    for char in fstr:
        print(char, end='', flush=True)
        time.sleep(typeSpeed)
    time.sleep(waitTime)
    if nextLine == True:
        scroll_text_up(PADDINGAREA)
        console.set_cursor_pos(0, console_info.window_rectangle.bottom - 1)
        console.clear_line(
            console.get_console_info().window_rectangle.bottom - 1)
    return ''

def scroll_text_up(rectangle: consolemanager.Rectangle, clear_rows=1, waitTime=0):
    console = begin.console
    ci = console.get_console_info()
    for row in range(rectangle.top + 1, ci.window_rectangle.bottom + 1 - rectangle.bottom - clear_rows):
        for clear_row in range(clear_rows):
            console.clear_line_until(ci.window_rectangle.right - rectangle.right - rectangle.left,
                                     row - 1 + clear_row, x_start=rectangle.left)
            line = console.read_console_line(
                row + clear_row)[rectangle.left:-rectangle.right]
            console.set_cursor_pos(
                rectangle.left, row - 1 + clear_row)
            print(line, end='', flush=True)
            time.sleep(waitTime)

contributors = {
    "VladimirBienvenue": [
        "Creator"
    ],
    "Vortetty": [
        "Credits system",
        "Saving system"
    ]
}

def rollCredits():
    """
    Plays the credits, name is a nod to cinemasins on youtube since im watching them while making this code
    :return:
    """
    console.set_cursor_pos(35, console_info.window_rectangle.bottom - 1)
    printSlow("      _____        _____                   ", 0.05, True, 0)
    console.set_cursor_pos(35, console_info.window_rectangle.bottom - 1)
    printSlow("  ___|\    \   ___|\    \  _____      _____", 0.05, True, 0)
    console.set_cursor_pos(35, console_info.window_rectangle.bottom - 1)
    printSlow(" /    /\    \ |    |\    \ \    \    /    /", 0.05, True, 0)
    console.set_cursor_pos(35, console_info.window_rectangle.bottom - 1)
    printSlow("|    |  |    ||    | |    | \    \  /    / ", 0.05, True, 0)
    console.set_cursor_pos(35, console_info.window_rectangle.bottom - 1)
    printSlow("|    |__|    ||    |/____/   \____\/____/  ", 0.05, True, 0)
    console.set_cursor_pos(35, console_info.window_rectangle.bottom - 1)
    printSlow("|    .--.    ||    |\    \   /    /\    \  ", 0.05, True, 0)
    console.set_cursor_pos(35, console_info.window_rectangle.bottom - 1)
    printSlow("|    |  |    ||    | |    | /    /  \    \ ", 0.05, True, 0)
    console.set_cursor_pos(35, console_info.window_rectangle.bottom - 1)
    printSlow("|____|  |____||____| |____|/____/ /\ \____\ ", 0.05, True, 0)
    console.set_cursor_pos(35, console_info.window_rectangle.bottom - 1)
    printSlow("|    |  |    ||    | |    ||    |/  \|    |", 0.05, True, 0)
    console.set_cursor_pos(35, console_info.window_rectangle.bottom - 1)
    printSlow("|____|  |____||____| |____||____|    |____|", 0.05, True, 0)
    console.set_cursor_pos(35, console_info.window_rectangle.bottom - 1)
    printSlow("  \(      )/    \(     )/    \(        )/  ", 0.05, True, 0)
    console.set_cursor_pos(35, console_info.window_rectangle.bottom - 1)
    printSlow("   '      '      '     '      '        '   ", 0.05, True, 0)

    for i in range(len(contributors)):
        contributorName = contributors.keys()[i]
        contributorRoles = contributors[contributorName]
        console.center_text(contributorName + "'s contributions:")
        printSlow(contributorName + "'s contributions:", 0.05, True, 0)
        time.sleep(0.5)
        for i in contributorRoles:
            console.center_text(" - " + i)
            printSlow(" - " + i, 0.05, True, 0)
            time.sleep(0.5)



