import sys
import time as t
import consolemanager
import begin
import random

# Text format block things
big = '--<======================>--'
small = '-<===============>-'

console_info = ""
PADDING = consolemanager.Rectangle(0, 6, 12, 0)
PADDINGNONE = consolemanager.Rectangle(0, 0, 1, 0)
PADDINGART = consolemanager.Rectangle(0, 23, 1, 0)
PADDINGMIDDLE = consolemanager.Rectangle(0, 14, 1, 2)


# Function to Type out Printed strings
def printSlow(fstr, waitTime=0, nextLine=True, typeSpeed=0.02, PADDINGAREA=PADDINGMIDDLE):
    global console_info
    console = begin.console
    console_info = console.get_console_info()
    for char in fstr:
        print(char, end='', flush=True)
        t.sleep(typeSpeed)
    t.sleep(waitTime)
    if nextLine == True:
        scroll_text_up(PADDINGAREA)
        console.set_cursor_pos(0, console_info.window_rectangle.bottom - 1)
        console.clear_line(
            console.get_console_info().window_rectangle.bottom - 1)
    return ''


# Function to move text up
def scroll_text_up(rectangle: consolemanager.Rectangle, clear_rows=1, waitTime=0, scroll="all"):
    console = begin.console
    ci = console.get_console_info()
    if scroll == "all":
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
    elif scroll == "mid":
        console = begin.console
        ci = console.get_console_info()
        for line in range(console.get_console_info().window_rectangle.bottom + 1 - 15 - 3):
            text = console.read_console_line(line + 15)
            console.clear_line(line + 15)
            console.set_cursor_pos(0, line + 14)
            print(text)
        console.clear_line(ci.window_rectangle.bottom - 1)


# Function to clear the screen WITH padding
def clear_screen(Padding=PADDING, waitTime=0.015):
    console = begin.console
    for row in range(console.get_console_info().window_rectangle.bottom - Padding.top):
        scroll_text_up(Padding)
        console.clear_line(
            console.get_console_info().window_rectangle.bottom - 1)
        t.sleep(waitTime)
    console.set_cursor_pos(0, console_info.window_rectangle.bottom - 1)

# Function when I want user to press "Enter" as confirmation.
def confirm(keep=0):
    console = begin.console
    input(printSlow("Press Enter to continue..."))
    printSlow("")
    if keep == 0:
        for row in range(console.get_console_info().window_rectangle.bottom - PADDING.top):
            scroll_text_up(PADDING)
            t.sleep(0.015)
    console.set_cursor_pos(0, console_info.window_rectangle.bottom - 1)

# Question function to utilize all over and to check for command usage
def qAnswer(question, safeZone=False, PADDINGAREA=PADDINGMIDDLE):
    console = begin.console
    scroll_text_up(PADDINGNONE, scroll="mid")
    console.set_cursor_pos(0, console_info.window_rectangle.bottom - 3)
    printSlow(f"{question}", 0, False, 0.03, PADDINGAREA)
    console.set_cursor_pos(0, console_info.window_rectangle.bottom-1)
    answer = input(printSlow('> ', 0, False, 0.03, PADDINGAREA))
    console.clear_line(console_info.window_rectangle.bottom, 2)
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
        scroll_text_up(PADDINGAREA)
        return answer


# Function to calculate where to place a string in between two points
def spacing(x1, x2, str1, str2):
    console = begin.console
    return ((x1 + ((x2 - x1 + 1) // 2)) - (len(str1) - 1) - ((len(str2) - 1) // 2) + 2)


# Monster encounter function
def monsterFight(monster, mainChar):
    clear_screen(PADDINGART)
    printSlow(f"You encounter a {monster.name}!", 0, True, 0.03, PADDINGART)
    choice = qAnswer(
        "What would you like to do? [1. Attack] [2. Try to Escape!]", False, PADDINGART)
    while monster.health > 0:
        enemyCritChance = monster.agility + 5
        enemyDodgeChance = monster.agility + 5
        heroCritChance = mainChar.agility + 10
        heroDodgeChance = mainChar.agility + 10

        if choice == "1":
            roll = random.randint(1, 100)
            if roll > enemyDodgeChance:

                roll = random.randint(1, 100)
                if roll > heroCritChance:
                    playerAttackMultiplier = 1

                elif roll <= heroCritChance:
                    playerAttackMultiplier = 2

                localMonsterhealth = monster.health - \
                    (3 + (mainChar.strength * playerAttackMultiplier - monster.armor))

                if localMonsterhealth > 0:

                    monster.health = monster.health - \
                        (3 + (mainChar.strength * playerAttackMultiplier - monster.armor))
                    if playerAttackMultiplier == 1:
                        printSlow(
                            f"You strike the {monster.name} with your sword, dealing {3 + (mainChar.strength * playerAttackMultiplier - monster.armor)} damage!", 0, True, 0.03, PADDINGART)
                        printSlow("", 0, True, 0.03, PADDINGART)

                    elif playerAttackMultiplier == 2:
                        printSlow(
                            f"You critically strike the {monster.name} with your sword for {3 + (mainChar.strength * playerAttackMultiplier - monster.armor)} damage; breaking one armor point!", 0, True, 0.03, PADDINGART)
                        printSlow("", 0, True, 0.03, PADDINGART)
                        if monster.armor > 0:
                            monster.armor = monster.armor - 1

                else:

                    monster.health = 0
                    printSlow(
                        f"You decapitate the {monster.name}. It drops to the ground in front of you.", 0, True, 0.03, PADDINGART)
                    printSlow("", 0, True, 0.03, PADDINGART)

            else:
                printSlow(
                    f"You swing your sword and miss the {monster.name}", 0, True, 0.03, PADDINGART)
                printSlow("", 0, True, 0.03, PADDINGART)

        elif choice == "2":

            printSlow(
                "- Escaping isn't possible right now, try again later! -", 0.5, True, 0.03, PADDINGART)
            printSlow("", 0, True, 0.03, PADDINGART)

        else:

            printSlow("Theres no time for other matters, you must fight or run!",
                      0, True, 0.03, PADDINGART)
            printSlow("", 0, True, 0.03, PADDINGART)

        if monster.health > 0:

            roll = random.randint(1, 100)
            if roll > heroDodgeChance:

                roll = random.randint(1, 100)
                if roll > enemyCritChance:
                    enemyAttackMultiplier = 1

                elif roll <= enemyCritChance:
                    enemyAttackMultiplier = 1.5

                localHerohealth = mainChar.health - \
                    (int(monster.strength * enemyAttackMultiplier - mainChar.armor))

                if localHerohealth > 0:

                    mainChar.health = mainChar.health - \
                        (int(monster.strength * enemyAttackMultiplier - mainChar.armor))
                    if enemyAttackMultiplier == 1:
                        printSlow(
                            f"The {monster.name} attacks you, dealing {monster.strength * enemyAttackMultiplier - mainChar.armor} damage!", 0, True, 0.03, PADDINGART)
                        printSlow("", 0, True, 0.03, PADDINGART)

                    elif enemyAttackMultiplier == 1.5:
                        printSlow(
                            f"The {monster.name} critically attacks you for {int(monster.strength * enemyAttackMultiplier - mainChar.armor)} damage; breaking one armor point.", 0, True, 0.03, PADDINGART)
                        printSlow("", 0, True, 0.03, PADDINGART)
                        if mainChar.armor > 0:
                            mainChar.armor = mainChar.armor - 1

                else:

                    mainChar.health = 0
                    printSlow(
                        f"You were defeated by: {monster.name}.", 0, True, 0.03, PADDINGART)
                    t.sleep(1)
                    printSlow(
                        f"Thank you very much for playing ARX!", 0, True, 0.03, PADDINGART)
                    t.sleep(1)
                    exit()

            elif roll <= heroDodgeChance:

                printSlow(
                    f"The {monster.name} tried to attack you and misses", 0, True, 0.03, PADDINGART)
                printSlow("", 0, True, 0.03, PADDINGART)

            choice = qAnswer(
                "Now what? [1. Attack] [2. Try to Escape!]", False, PADDINGART)

    clear_screen()
    printSlow(f"Wow, you defeated the {monster.name}")

# -------------------------
# Dialogue Functions Below:
# -------------------------


# Shows player their stats
def playerStats(mainChar):
    console = begin.console
    printSlow(big)
    printSlow(
        "Lets look at your characters stats! (They are dependent on what class you pick!)", .5)
    printSlow(small)
    printSlow(f"► Your Strength is: {mainChar.strength}")
    printSlow(f"► Your Agility is: {mainChar.agility}")
    printSlow(
        f"► Your Intelligence is: {mainChar.intelligence}")
    printSlow(f"► Your Charisma is: {mainChar.charisma}")
    printSlow(small)
    confirm(1)


# Shows player what each player stat does
def statMeaning():
    console = begin.console
    printSlow(big)
    printSlow('Stats in Arx')
    printSlow(small)
    printSlow('Strength:')
    printSlow('Primary benefit(s): Weapon Damage')
    printSlow('Additional benefit(s): Increases Inventory')
    printSlow('')
    printSlow('Agility:')
    printSlow('Primary benefit(s): Increased Stamina pool')
    printSlow('Additional benefit(s): Crit chance and Dodge chance')
    printSlow('')
    printSlow('Intelligence:')
    printSlow('Primary benfit(s): Increased Mana pool')
    printSlow('Additional benefit(s): Spell Damage and Heal Amount')
    printSlow('')
    printSlow('Charisma:')
    printSlow('Primary benefit(s): Trade prices')
    printSlow('Additional benefit(s): Chance to prevent negative effects')
    printSlow(big)
    confirm()


# ------------------------------------------
# Stat Bar Setting and Icon Functions below:
# ------------------------------------------


def setHP(current_hp, showStats, mainChar, max_hp=100, initialize=False):
    console = begin.console
    mainChar._health = current_hp
    console.set_cursor_pos(8, 0)
    printSlow("Hero's Stats:", 0, False)
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
    console.set_cursor_pos(0, console_info.window_rectangle.bottom - 1)


def setMana(current_mana, showStats, mainChar, max_mana=None, initialize=False):
    console = begin.console
    mainChar._mana = current_mana
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
    console.set_cursor_pos(0, console_info.window_rectangle.bottom - 1)


def setStamina(current_stamina, showStats, mainChar, max_stamina=None, initialize=False):
    console = begin.console
    mainChar._stamina = current_stamina
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
    console.set_cursor_pos(0, console_info.window_rectangle.bottom - 1)


def setArmor(current_armor, showStats, mainChar, max_armor=10, initialize=False):
    console = begin.console
    mainChar._armor = current_armor
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
        printSlow(']', 0, False)
        console.set_default_text_color()
    console.set_cursor_pos(0, console_info.window_rectangle.bottom - 1)


#   ---------------------------
#   ENEMIES SET FUNCTION BELOW:
#   ---------------------------

def setEnemyHP(monster, max_hp, initialize=False):
    console = begin.console
    # TODO Set this to center monster.name relative to the len()
    console.set_cursor_pos(60, 0)
    printSlow(f"{monster.name}'s Stats:", 0, False)
    console.set_cursor_pos(55, 1)
    if initialize == False:

        console.set_text_color('bright white', 'black')
        print(f"[Health  {monster.health: >3}/{max_hp}:".ljust(14),
              end='', flush=True)
        health_percentage_current = int(
            ((monster.health / max_hp) * 100) // 10)

        console.set_text_color('bright white', 'light red')
        print(' ' * health_percentage_current, end='', flush=True)

        console.set_text_color('bright white', 'red')
        print(' ' * (10 - health_percentage_current), end='', flush=True)

        console.set_text_color('bright white', 'black')
        printSlow(']', 0, False)
        console.set_default_text_color()
    else:

        console.set_text_color('bright white', 'black')
        printSlow(
            f"[Health  {monster.health: >3}/{max_hp}:".ljust(14), 0, False)
        health_percentage_current = int(
            ((monster.health / max_hp) * 100) // 10)

        console.set_text_color('bright white', 'light red')
        printSlow(' ' * health_percentage_current, 0, False)

        console.set_text_color('bright white', 'red')
        printSlow(' ' * (10 - health_percentage_current), 0, False)

        console.set_text_color('bright white', 'black')
        printSlow(']', 0, False)
        console.set_default_text_color()
    console.set_cursor_pos(0, console_info.window_rectangle.bottom - 1)


def setEnemyMana(monster, initialize=False):
    console = begin.console
    console.set_cursor_pos(55, 2)

    if len(str(monster.mana)) == 2:
        spaces = "     "
    elif len(str(monster.mana)) < len(str(monster.manaPoolmax)):
        spaces = "     "
    else:
        spaces = "      "

    if initialize == False:

        console.set_text_color('bright white', 'black')
        print(f"[Mana{spaces}{monster.mana: >2}/{monster.manaPoolmax}:".ljust(14),
              end='', flush=True)
        mana_percent_current = int(
            ((monster.mana / monster.manaPoolmax) * 100) // 10)

        console.set_text_color('bright white', 'light aqua')
        print(' ' * mana_percent_current, end='', flush=True)

        console.set_text_color('bright white', 'aqua')
        print(' ' * (10 - mana_percent_current), end='', flush=True)

        console.set_text_color('bright white', 'black')
        printSlow(']', 0, False)
        console.set_default_text_color()
    else:

        console.set_text_color('bright white', 'black')
        printSlow(
            f"[Mana{spaces}{monster.mana: >2}/{monster.manaPoolmax}:".ljust(14), 0, False)
        mana_percent_current = int(
            ((monster.mana / monster.manaPoolmax) * 100) // 10)

        console.set_text_color('bright white', 'light aqua')
        printSlow(' ' * mana_percent_current, 0, False)

        console.set_text_color('bright white', 'aqua')
        printSlow(' ' * (10 - mana_percent_current), 0, False)

        console.set_text_color('bright white', 'black')
        printSlow(']', 0, False)
        console.set_default_text_color()
    console.set_cursor_pos(0, console_info.window_rectangle.bottom - 1)


def setEnemyStamina(monster, initialize=False):
    console = begin.console
    console.set_cursor_pos(55, 3)

    if initialize == False:

        console.set_text_color('bright white', 'black')
        print(f"[Stamina  {monster.stamina: >2}/{monster.staminaPoolmax}:".ljust(14),
              end='', flush=True)
        stamina_percent_current = int(
            ((monster.stamina / monster.staminaPoolmax) * 100) // 10)

        console.set_text_color('bright white', 'light green')
        print(' ' * stamina_percent_current, end='', flush=True)

        console.set_text_color('bright white', 'green')
        print(' ' * (10 - stamina_percent_current), end='', flush=True)

        console.set_text_color('bright white', 'black')
        printSlow(']', 0, False)
        console.set_default_text_color()
    else:

        console.set_text_color('bright white', 'black')
        printSlow(
            f"[Stamina  {monster.stamina: >2}/{monster.staminaPoolmax}:".ljust(14), 0, False)
        stamina_percent_current = int(
            ((monster.stamina / monster.staminaPoolmax) * 100) // 10)

        console.set_text_color('bright white', 'light green')
        printSlow(' ' * stamina_percent_current, 0, False)

        console.set_text_color('bright white', 'green')
        printSlow(' ' * (10 - stamina_percent_current), 0, False)

        console.set_text_color('bright white', 'black')
        printSlow(']', 0, False)
        console.set_default_text_color()
    console.set_cursor_pos(0, console_info.window_rectangle.bottom - 1)


def setEnemyArmor(monster, max_armor, initialize=False):
    console = begin.console
    console.set_cursor_pos(55, 4)

    if initialize == False:

        console.set_text_color('bright white', 'black')
        print(f"[Armor     {monster.armor: >2}/{max_armor}:".ljust(14),
              end='', flush=True)
        armor_percentage_current = int(
            ((monster.armor / max_armor) * 100) // 10)

        console.set_text_color('bright white', 'light yellow')
        print(' ' * armor_percentage_current, end='', flush=True)

        console.set_text_color('bright white', 'yellow')
        print(' ' * (10 - armor_percentage_current), end='', flush=True)

        console.set_text_color('bright white', 'black')
        printSlow(']', 0, False)
        console.set_default_text_color()
    else:

        console.set_text_color('bright white', 'black')
        printSlow(
            f"[Armor     {monster.armor: >2}/{max_armor}:".ljust(14), 0, False)
        armor_percentage_current = int(
            ((monster.armor / max_armor) * 100) // 10)

        console.set_text_color('bright white', 'light yellow')
        printSlow(' ' * armor_percentage_current, 0, False)

        console.set_text_color('bright white', 'yellow')
        printSlow(' ' * (10 - armor_percentage_current), 0, False)

        console.set_text_color('bright white', 'black')
        printSlow(']', 0, False)
        console.set_default_text_color()
    console.set_cursor_pos(0, console_info.window_rectangle.bottom - 1)


def clearEnemyStats():
    console = begin.console
    console.set_cursor_pos(60, 0)
    print("                           ")
    console.set_cursor_pos(55, 1)
    print("                           ")
    console.set_cursor_pos(55, 2)
    print("                           ")
    console.set_cursor_pos(55, 3)
    print("                           ")
    console.set_cursor_pos(55, 4)
    print("                           ")
    console.set_cursor_pos(0, console_info.window_rectangle.bottom - 1)
