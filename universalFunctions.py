import sys
import time as t
import consoleManager

console = consoleManager.ConsoleManager(
    consoleManager.ConsoleStandardHandle.STD_OUTPUT_HANDLE)

PADDING = consoleManager.Rectangle(0, 5, 12, 0)


def printSlow(text, typespeed=0.03, sleeptime=0, nextline=True):
    for char in text:
        sys.stdout.write(char)
        sys.stdout.flush()
        t.sleep(typespeed)
    t.sleep(sleeptime)
    if nextline == True:
        print(" ")


def set_hp(current_hp, showStats, mainChar, max_hp=100, initialize=False):
    mainChar.health = current_hp
    if showStats == True and initialize == False:
        console.set_cursor_pos(0, 0)
        console.set_text_color('bright white', 'black')
        print(f"[Health  {current_hp: >3}/{max_hp}:".ljust(14),
              end='', flush=True)
        health_percentage_current = int(((current_hp / max_hp) * 100) // 10)

        console.set_text_color('bright white', 'light red')
        print(' ' * health_percentage_current, end='', flush=True)

        console.set_text_color('bright white', 'red')
        print(' ' * (10 - health_percentage_current), end='', flush=True)

        console.set_text_color('bright white', 'black')
        print(']')
        console.set_default_text_color()
    elif showStats == True and initialize == True:
        console.set_cursor_pos(0, 0)
        console.set_text_color('bright white', 'black')
        printSlow(f"[Health  {current_hp: >3}/{max_hp}:".ljust(14), 0, False)
        health_percentage_current = int(((current_hp / max_hp) * 100) // 10)

        console.set_text_color('bright white', 'light red')
        printSlow(' ' * health_percentage_current, 0, False)

        console.set_text_color('bright white', 'red')
        printSlow(' ' * (10 - health_percentage_current), 0, False)

        console.set_text_color('bright white', 'black')
        printSlow(']')
        console.set_default_text_color()


def set_mana(current_mana, showStats, mainChar, max_mana=None, initialize=False):
    mainChar.mana = current_mana
    if showStats == True and initialize == False:
        if max_mana is None:
            max_mana = mainChar.manaPoolMax
        console.set_cursor_pos(0, 1)
        console.set_text_color('bright white', 'black')
        print(f"[Mana      {current_mana: >2}/{max_mana}:".ljust(14),
              end='', flush=True)
        mana_percent_current = int(
            ((current_mana / max_mana) * 100) // 10)

        console.set_text_color('bright white', 'light aqua')
        print(' ' * mana_percent_current, end='', flush=True)

        console.set_text_color('bright white', 'aqua')
        print(' ' * (10 - mana_percent_current), end='', flush=True)

        console.set_text_color('bright white', 'black')
        print(']')
        console.set_default_text_color()
    elif showStats == True and initialize == True:
        if max_mana is None:
            max_mana = mainChar.manaPoolmax
        console.set_cursor_pos(0, 1)
        console.set_text_color('bright white', 'black')
        printSlow(
            f"[Mana      {current_mana: >2}/{max_mana}:".ljust(14), 0, False)
        mana_percent_current = int(
            ((current_mana / max_mana) * 100) // 10)

        console.set_text_color('bright white', 'light aqua')
        printSlow(' ' * mana_percent_current, 0, False)

        console.set_text_color('bright white', 'aqua')
        printSlow(' ' * (10 - mana_percent_current), 0, False)

        console.set_text_color('bright white', 'black')
        printSlow(']')
        console.set_default_text_color()


def set_stamina(current_stamina, showStats, mainChar, max_stamina=None, initialize=False):
    mainChar.stamina = current_stamina
    if showStats == True and initialize == False:
        if max_stamina is None:
            max_stamina = mainChar.staminaPoolmax
        console.set_cursor_pos(0, 2)
        console.set_text_color('bright white', 'black')
        print(f"[Stamina   {current_stamina: >2}/{max_stamina}:".ljust(14),
              end='', flush=True)
        stamina_percent_current = int(
            ((current_stamina / max_stamina) * 100) // 10)

        console.set_text_color('bright white', 'light green')
        print(' ' * stamina_percent_current, end='', flush=True)

        console.set_text_color('bright white', 'green')
        print(' ' * (10 - stamina_percent_current), end='', flush=True)

        console.set_text_color('bright white', 'black')
        print(']')
        console.set_default_text_color()
    elif showStats == True and initialize == True:
        if max_stamina is None:
            max_stamina = mainChar.staminaPoolmax
        console.set_cursor_pos(0, 2)
        console.set_text_color('bright white', 'black')
        printSlow(
            f"[Stamina   {current_stamina: >2}/{max_stamina}:".ljust(14), 0, False)
        stamina_percent_current = int(
            ((current_stamina / max_stamina) * 100) // 10)

        console.set_text_color('bright white', 'light green')
        printSlow(' ' * stamina_percent_current, 0, False)

        console.set_text_color('bright white', 'green')
        printSlow(' ' * (10 - stamina_percent_current), 0, False)

        console.set_text_color('bright white', 'black')
        printSlow(']')
        console.set_default_text_color()


def set_armor(current_armor, showStats, mainChar, max_armor=10, initialize=False):
    mainChar.armor = current_armor
    if showStats == True and initialize == False:
        console.set_cursor_pos(0, 3)
        console.set_text_color('bright white', 'black')
        print(f"[Armor     {current_armor: >2}/{max_armor}:".ljust(14),
              end='', flush=True)
        armor_percentage_current = int(
            ((current_armor / max_armor) * 100) // 10)

        console.set_text_color('bright white', 'light yellow')
        print(' ' * armor_percentage_current, end='', flush=True)

        console.set_text_color('bright white', 'yellow')
        print(' ' * (10 - armor_percentage_current), end='', flush=True)

        console.set_text_color('bright white', 'black')
        print(']')
        console.set_default_text_color()
    elif showStats == True and initialize == True:
        console.set_cursor_pos(0, 3)
        console.set_text_color('bright white', 'black')
        printSlow(
            f"[Armor     {current_armor: >2}/{max_armor}:".ljust(14), 0, False)
        armor_percentage_current = int(
            ((current_armor / max_armor) * 100) // 10)

        console.set_text_color('bright white', 'light yellow')
        printSlow(' ' * armor_percentage_current, 0, False)

        console.set_text_color('bright white', 'yellow')
        printSlow(' ' * (10 - armor_percentage_current), 0, False)

        console.set_text_color('bright white', 'black')
        printSlow(']')
        console.set_default_text_color()


def scroll_text_up(rectangle: consoleManager.Rectangle, clear_rows=1):
    ci = console.get_console_info()
    for row in range(rectangle.top + 1, ci.window_rectangle.bottom + 1 - rectangle.bottom - clear_rows):
        for clear_row in range(clear_rows):
            console.clear_line_until(ci.window_rectangle.right - rectangle.right - rectangle.left,
                                     row - 1 + clear_row, x_start=rectangle.left)
            line = console.read_console_line(
                row + clear_row)[rectangle.left:-rectangle.right]
            console.set_cursor_pos(rectangle.left, row - 1 + clear_row)
            print(line, end='', flush=True)


def clear_screen(PADDING):
    for row in range(console.get_console_info().window_rectangle.bottom - PADDING.top):
        scroll_text_up(PADDING)
        console.clear_line(
            console.get_console_info().window_rectangle.bottom - 1)
