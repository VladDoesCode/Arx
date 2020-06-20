import sys
import time as t
import consolemanager

# Text format block things
big = '--<======================>--'
small = '-<===============>-'

with consolemanager.ConsoleManager(consolemanager.ConsoleStandardHandle.STD_OUTPUT_HANDLE) as console:
    console_info = console.get_console_info()
    PADDING = consolemanager.Rectangle(0, 6, 12, 0)
    PADDINGNONE = consolemanager.Rectangle(0, 0, 1, 0)

    # Function to Type out Printed strings
    def printSlow(fstr, waitTime=0, nextLine=True, typeSpeed=0.03):
        for char in fstr:
            print(char, end='', flush=True)
            t.sleep(typeSpeed)
        t.sleep(waitTime)
        if nextLine == True:
            scroll_text_up(PADDING)
            console.set_cursor_pos(0, console_info.window_rectangle.bottom - 1)
            console.clear_line(
                console.get_console_info().window_rectangle.bottom - 1)
        return ''

    # Function to move text up
    def scroll_text_up(rectangle: consolemanager.Rectangle, clear_rows=1, waitTime=0):
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
                t.sleep(waitTime)

    # Function to clear the screen WITH padding
    def clear_screen(PADDING=PADDING, waitTime=0.015):
        for row in range(console.get_console_info().window_rectangle.bottom - PADDING.top):
            scroll_text_up(PADDING)
            console.clear_line(
                console.get_console_info().window_rectangle.bottom - 1)
            t.sleep(waitTime)
        console.set_cursor_pos(0, console_info.window_rectangle.bottom - 1)

    # Function when I want user to press "Enter" as confirmation.
    def confirm(keep=0):
        input(printSlow("Press Enter to continue..."))
        printSlow("")
        if keep == 0:
            for row in range(console.get_console_info().window_rectangle.bottom - PADDING.top):
                scroll_text_up(PADDING)
                t.sleep(0.015)
        console.set_cursor_pos(0, console_info.window_rectangle.bottom - 1)

    # Question function to utilize all over and to check for command usage
    def qAnswer(question, safeZone=False):
        printSlow(f"{question}")
        console.clear_line(
            console.get_console_info().window_rectangle.bottom - 1)
        # print('> ', end='', flush=True)
        printSlow('> ', 0, False)
        answer = input()
        if answer.lower() == "!stats" and safeZone == True:
            clear_screen()
            printSlow(big)
            printSlow(
                "Remember you can view a list of commands in any safezone with !commands", .5)
            playerStats()
            clear_screen()
        elif answer.lower() == "!statsmeaning" and safeZone == True:
            clear_screen()
            printSlow(big)
            printSlow(
                "Remember you can view a list of commands in any safezone with !commands", .5)
            printSlow(big)
            statMeaning()
        elif answer.lower() == "!commands" and safeZone == True:
            clear_screen()
            commands()
        else:
            scroll_text_up(PADDING)
            printSlow('')
            console.clear_line(
                console.get_console_info().window_rectangle.bottom - 2)
            return answer

# ------------------------------------------
# Stat Bar Setting and Icon Functions below:
# ------------------------------------------

    '''
       _____   __________ ____  ___
      /  _  \  \______   \\   \/  /
     /  /_\  \  |       _/ \     /
    /    |    \ |    |   \ /     \
    \____|__  / |____|_  //___/\  \
            \/         \/       \_/
    '''

    def setArx():
        console.set_cursor_pos(
            console.get_console_info().window_rectangle.right - 32, 0)
        printSlow("   _____   __________ ____  ___ ", 0, False, 0.012)
        console.set_cursor_pos(
            console.get_console_info().window_rectangle.right - 32, 1)
        printSlow("  /  _  \  \______   \\\   \/  /", 0, False, 0.012)
        console.set_cursor_pos(
            console.get_console_info().window_rectangle.right - 32, 2)
        printSlow(" /  /_\  \  |       _/ \     /  ", 0, False, 0.012)
        console.set_cursor_pos(
            console.get_console_info().window_rectangle.right - 32, 3)
        printSlow("/    |    \ |    |   \ /     \  ", 0, False, 0.012)
        console.set_cursor_pos(
            console.get_console_info().window_rectangle.right - 32, 4)
        printSlow("\____|__  / |____|_  //___/\  \ ", 0, False, 0.012)
        console.set_cursor_pos(
            console.get_console_info().window_rectangle.right - 32, 5)
        printSlow("        \/         \/       \_/ ", 0, False, 0.012)

    def setHP(current_hp, showStats, mainChar, max_hp=100, initialize=False):
        mainChar.health = current_hp
        console.set_cursor_pos(8, 0)
        printSlow("Hero's Stats:")
        if showStats == True and initialize == False:
            console.set_cursor_pos(0, 1)

            console.set_text_color('bright white', 'black')
            print(f"[Health  {current_hp: >3}/{max_hp}:".ljust(14),
                  end='', flush=True)
            health_percentage_current = int(
                ((current_hp / max_hp) * 100) // 10)

            console.set_text_color('bright white', 'light red')
            print(' ' * health_percentage_current, end='', flush=True)

            console.set_text_color('bright white', 'red')
            print(' ' * (10 - health_percentage_current), end='', flush=True)

            console.set_text_color('bright white', 'black')
            printSlow(']', 0, False)
            console.set_default_text_color()
        elif showStats == True and initialize == True:
            console.set_cursor_pos(0, 1)

            console.set_text_color('bright white', 'black')
            printSlow(
                f"[Health  {current_hp: >3}/{max_hp}:".ljust(14), 0, False)
            health_percentage_current = int(
                ((current_hp / max_hp) * 100) // 10)

            console.set_text_color('bright white', 'light red')
            printSlow(' ' * health_percentage_current, 0, False)

            console.set_text_color('bright white', 'red')
            printSlow(' ' * (10 - health_percentage_current), 0, False)

            console.set_text_color('bright white', 'black')
            printSlow(']', 0, False)
            console.set_default_text_color()

    def setMana(current_mana, showStats, mainChar, max_mana=None, initialize=False):
        mainChar.mana = current_mana
        if showStats == True and initialize == False:
            if max_mana is None:
                max_mana = mainChar.manaPoolMax
            console.set_cursor_pos(0, 2)
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
            printSlow(']', 0, False)
            console.set_default_text_color()
        elif showStats == True and initialize == True:
            if max_mana is None:
                max_mana = mainChar.manaPoolmax
            console.set_cursor_pos(0, 2)
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
            printSlow(']', 0, False)
            console.set_default_text_color()

    def setStamina(current_stamina, showStats, mainChar, max_stamina=None, initialize=False):
        mainChar.stamina = current_stamina
        if showStats == True and initialize == False:
            if max_stamina is None:
                max_stamina = mainChar.staminaPoolmax
            console.set_cursor_pos(0, 3)
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
            printSlow(']', 0, False)
            console.set_default_text_color()
        elif showStats == True and initialize == True:
            if max_stamina is None:
                max_stamina = mainChar.staminaPoolmax
            console.set_cursor_pos(0, 3)
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
            printSlow(']', 0, False)
            console.set_default_text_color()

    def setArmor(current_armor, showStats, mainChar, max_armor=10, initialize=False):
        mainChar.armor = current_armor
        if showStats == True and initialize == False:
            console.set_cursor_pos(0, 4)
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
            printSlow(']', 0, False)
            console.set_default_text_color()
        elif showStats == True and initialize == True:
            console.set_cursor_pos(0, 4)
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

    '''
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
    '''

    #   This is the ascii art logo.
    def titleScreen():
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
        printSlow("   '      '      '     '      '        '   ",
                  0.05, True, 0)
        console.set_cursor_pos(23, console_info.window_rectangle.bottom - 1)
        printSlow(
            "A text based adventure game made by Vladimir with help from friends.", 0.05, True, 0)
        console.set_cursor_pos(27, console_info.window_rectangle.bottom - 1)
        printSlow(
            "Use !credits in a safe zone to view the help of my friends!",  0.05, True, 0)
        for row in range(8):
            t.sleep(0.05)
            scroll_text_up(PADDINGNONE)
        console.set_cursor_pos(31, 22)
        printSlow(
            "[1. Start New Game] [2. Load Game] [3. Game Credit]", 0.5, False)
        console.set_cursor_pos(40, 23)

        introChoice = input(
            printSlow("Whats your choice, Adventurer? > ", 0, False))
        while introChoice != "1":
            console.clear_line(23)
            console.set_cursor_pos(40, 23)
            introChoice = input("Whats your choice, Adventurer? > ")
            if introChoice == "1":
                break
            elif introChoice == "2" or introChoice == "3":
                console.set_cursor_pos(25, 25)
                printSlow(
                    "That part of Arx isn't ready yet, try again in the next release!", 1, False)
                console.clear_line(25)

        t.sleep(.5)
        clear_screen(PADDINGNONE, 0.05)
