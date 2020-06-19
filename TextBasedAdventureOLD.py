# TODO implement monster fighting AI
# TODO Inventory system
# TODO Create a question function to pass if command statements through - Done!
# TODO Display stats at the top of terminal.
# TODO Create a game-loop-esc function to call upon when something changes
# TODO Save Functionality (maybe check points?)
# TODO Implement Mana?
# TODO BIG todo: make a Trello board of todos. im losing count and going insane.


# Imports
import consolemanager
import os
import random
import sys
import time
from random import randint

PADDING = consolemanager.Rectangle(0, 5, 12, 0)
safeZone = 0

# Text format block things
# big = "░▒▓█►-━════════════════━-◄█▓▒░"
# small = "█►-━═══════════━-◄█"
big = ''
small = ''


def set_hp(console, current_hp,  max_hp=100, initialize=False):
    my_player.stats.health = current_hp
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
        print_slow(f"[Health  {current_hp: >3}/{max_hp}:".ljust(14), 0, False)
        health_percentage_current = int(((current_hp / max_hp) * 100) // 10)

        console.set_text_color('bright white', 'light red')
        print_slow(' ' * health_percentage_current, 0, False)

        console.set_text_color('bright white', 'red')
        print_slow(' ' * (10 - health_percentage_current), 0, False)

        console.set_text_color('bright white', 'black')
        print_slow(']')
        console.set_default_text_color()


def set_mana(console, current_mana, max_mana=None, initialize=False):
    my_player.stats.mana = current_mana
    if showStats == True and initialize == False:
        if max_mana is None:
            max_mana = my_player.stats.manaPoolMax
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
            max_mana = my_player.stats.manaPoolmax
        console.set_cursor_pos(0, 1)
        console.set_text_color('bright white', 'black')
        print_slow(
            f"[Mana      {current_mana: >2}/{max_mana}:".ljust(14), 0, False)
        mana_percent_current = int(
            ((current_mana / max_mana) * 100) // 10)

        console.set_text_color('bright white', 'light aqua')
        print_slow(' ' * mana_percent_current, 0, False)

        console.set_text_color('bright white', 'aqua')
        print_slow(' ' * (10 - mana_percent_current), 0, False)

        console.set_text_color('bright white', 'black')
        print_slow(']')
        console.set_default_text_color()


def set_stamina(console, current_stamina, max_stamina=None, initialize=False):
    my_player.stats.stamina = current_stamina
    if showStats == True and initialize == False:
        if max_stamina is None:
            max_stamina = my_player.stats.staminaPoolmax
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
            max_stamina = my_player.stats.staminaPoolmax
        console.set_cursor_pos(0, 2)
        console.set_text_color('bright white', 'black')
        print_slow(
            f"[Stamina   {current_stamina: >2}/{max_stamina}:".ljust(14), 0, False)
        stamina_percent_current = int(
            ((current_stamina / max_stamina) * 100) // 10)

        console.set_text_color('bright white', 'light green')
        print_slow(' ' * stamina_percent_current, 0, False)

        console.set_text_color('bright white', 'green')
        print_slow(' ' * (10 - stamina_percent_current), 0, False)

        console.set_text_color('bright white', 'black')
        print_slow(']')
        console.set_default_text_color()


def set_armor(console, current_armor, max_armor=10, initialize=False):
    my_player.stats.armor = current_armor
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
        print_slow(
            f"[Armor     {current_armor: >2}/{max_armor}:".ljust(14), 0, False)
        armor_percentage_current = int(
            ((current_armor / max_armor) * 100) // 10)

        console.set_text_color('bright white', 'light yellow')
        print_slow(' ' * armor_percentage_current, 0, False)

        console.set_text_color('bright white', 'yellow')
        print_slow(' ' * (10 - armor_percentage_current), 0, False)

        console.set_text_color('bright white', 'black')
        print_slow(']')
        console.set_default_text_color()


# Prints text slowly
def print_slow(fstr, waitTime=0, nextLine=True):
    for letter in fstr:
        print(letter, end='', flush=True)
        time.sleep(0.03)
    time.sleep(waitTime)
    if nextLine == True:
        scroll_text_up(PADDING)
        console.set_cursor_pos(0, console_info.window_rectangle.bottom - 1)
        console.clear_line(
            console.get_console_info().window_rectangle.bottom - 1)
    return ''


# Shows player what each player stat does
def statMeaning():
    print_slow(big)
    print_slow('Stats in Arx')
    print_slow(small)
    print_slow('Strength:', .5)
    print_slow('Primary benefit(s): Weapon Damage')
    print_slow('Additional benefit(s): Increases Inventory', .5)
    print_slow('')
    print_slow('Agility:', .5)
    print_slow('Primary benefit(s): Increased Stamina pool')
    print_slow('Additional benefit(s): Crit chance and Dodge chance', .5)
    print_slow('')
    print_slow('Intelligence:', .5)
    print_slow('Primary benfit(s): Increased Mana pool')
    print_slow('Additional benefit(s): Spell Damage and Heal Amount', .5)
    print_slow('')
    print_slow('Charisma:', .5)
    print_slow('Primary benefit(s): Trade prices')
    print_slow('Additional benefit(s): Chance to prevent negative effects', .5)
    print_slow(big)
    confirm()


# Shows player their stats
def playerStats():
    print_slow(big)
    print_slow(
        "Lets look at your characters stats! (They are dependent on what class you pick!)", .5)
    print_slow(small)
    # print_slow(f"► Your Mana is {my_player.mana}")
    print_slow(f"► Your Strength is: {my_player.stats.strength}", .5)
    print_slow(f"► Your Agility is: {my_player.stats.agility}", .5)
    print_slow(f"► Your Intelligence is: {my_player.stats.intelligence}", .5)
    print_slow(f"► Your Charisma is: {my_player.stats.charisma}", .5)
    print_slow(small)
    confirm(1)


# Shows player all the commands and their uses
def commands():
    print_slow(big)
    print_slow("Let's see what you can do in safezones.....", 1)
    print_slow("Ahh yes, here they are, the 'commands'!")
    print_slow("► '!stats' displats a list of your players stats")
    print_slow(
        "► '!statsmeaning' shows how each character stat effects gameplay.")
    print_slow(
        "► '!commands' displays this screen but I assume you already knew that!", .5)
    print_slow(big)
    confirm()


def clear_screen():
    for row in range(console.get_console_info().window_rectangle.bottom - PADDING.top):
        scroll_text_up(PADDING)
        console.clear_line(
            console.get_console_info().window_rectangle.bottom - 1)


# Question function to utilize all over and to check for command usage
def qAnswer(question):
    print_slow(f"{question}")
    console.clear_line(console.get_console_info().window_rectangle.bottom - 1)
    print('► ', end='', flush=True)
    answer = input()
    if answer.lower() == "!stats" and safeZone == 1:
        clear_screen()
        print_slow(big)
        print_slow(
            "Remember you can view a list of commands in any safezone with !commands", .5)
        playerStats()
        clear_screen()
    elif answer.lower() == "!statsmeaning" and safeZone == 1:
        clear_screen()
        print_slow(big)
        print_slow(
            "Remember you can view a list of commands in any safezone with !commands", .5)
        print_slow(big)
        statMeaning()
    elif answer.lower() == "!commands" and safeZone == 1:
        clear_screen()
        commands()
    else:
        return answer


def confirm(keep=0):
    input(print_slow("Press Enter to continue..."))
    if keep == 0:
        for row in range(console.get_console_info().window_rectangle.bottom - PADDING.top):
            scroll_text_up(PADDING)
            time.sleep(0.002)


def scroll_text_up(rectangle: consolemanager.Rectangle, clear_rows=1):
    ci = console.get_console_info()
    for row in range(rectangle.top + 1, ci.window_rectangle.bottom + 1 - rectangle.bottom - clear_rows):
        for clear_row in range(clear_rows):
            console.clear_line_until(ci.window_rectangle.right - rectangle.right - rectangle.left,
                                     row - 1 + clear_row, x_start=rectangle.left)
            line = console.read_console_line(
                row + clear_row)[rectangle.left:-rectangle.right]
            console.set_cursor_pos(rectangle.left, row - 1 + clear_row)
            print(line, end='', flush=True)


# TODO - I use this as marker for when my game starts
# ¸,ø¤º°`°º¤ø,¸¸,ø¤º° ━ °º¤ø,¸¸,ø¤º°`°º¤ø,¸¸,ø¤º°`°º¤ø,¸¸,ø¤º° ━ °º¤ø,¸¸,ø¤º°`°º¤ø,¸
# Start of the game
with consolemanager.ConsoleManager(consolemanager.ConsoleStandardHandle.STD_OUTPUT_HANDLE) as console:
    console.set_title("Arx")
    console.set_cursor_info(size=1, visibility=False)
    console.clear_screen()
    console_info = console.get_console_info()
    safeZone = 0
    showStats = True
    console.set_cursor_pos(0, console_info.window_rectangle.bottom - 1)

    # Get Characters name
    while True:
        print_slow(big)
        playerName = qAnswer("Hello Adventurer, what is your name?")
    # If character name is 18 or more characters, don't allow it.
        if len(playerName) <= 18 and len(playerName) > 0:
            break
        elif len(playerName) == 0:
            print_slow(small)
            print_slow('Are you just going to sit there and not talk?')
            print_slow(small)
        else:
            print_slow(small)
            print_slow(
                'Thats a mighty long name, do you go by something shorter?')
            print_slow(small)

    # Set the name to capital
    playerName = playerName.capitalize()
    print_slow(small)
    print_slow(f'{playerName}, welcome to the world of Arx!')
    print_slow('A text based adventure created by Vladimir!')
    print_slow('With help from friends! (credits to come.)')
    print_slow(big)
    confirm()

    # Pick a class
    while True:
        console.set_cursor_pos(0, console_info.window_rectangle.bottom - 1)
        print_slow(small)
        playerClass = qAnswer(
            'What class would you like to play? [Commoner], [Warrior], [Mage], [Thief], or [Paladin]?')
        clear_screen()
        console.set_cursor_pos(
            0, console.get_console_info().window_rectangle.bottom - 1)
        # if playerClass.lower() in ['commoner', 'warrior', 'mage', 'thief', 'paladin']:
        #     # This is where I init my char class.
        #     my_player = Player(100, 0, playerClass.lower())
        # break
        if playerClass.lower() == "commoner":
            stats = PlayerClassCommoner(100, 0)
            my_player = Player(stats)
            break

        elif playerClass.lower() == "warrior":
            stats = PlayerClassWarrior(100, 0)
            my_player = Player(stats)
            break

        elif playerClass.lower() == "mage":
            stats = PlayerClassMage(100, 0)
            my_player = Player(stats)
            break

        elif playerClass.lower() == "thief":
            stats = PlayerClassThief(100, 0)
            my_player = Player(stats)
            break

        elif playerClass.lower() == "paladin":
            stats = PlayerClassPaladin(100, 0)
            my_player = Player(stats)
            break

    # Setting player stats bars and info.
    my_player.stats.manaPoolMax = my_player.stats.intelligence * 5
    my_player.stats.staminaPoolMax = my_player.stats.agility * 5
    set_hp(console, 100, 100, True)
    set_mana(console, my_player.stats.manaPoolmax, None, True)
    set_stamina(console, my_player.stats.staminaPoolmax, None, True)
    set_armor(console, 10, 10, True)
    console.set_cursor_pos(
        35, console.get_console_info().window_rectangle.top + 1)
    print_slow(f"[Name:  {playerName.capitalize()}]")
    console.set_cursor_pos(
        35, console.get_console_info().window_rectangle.top + 2)
    print_slow(f"[Class:  {playerClass.capitalize()}]")
    time.sleep(1)
    console.set_cursor_pos(
        0, console.get_console_info().window_rectangle.top + 8)
    print_slow(
        '^ These are your stat bars, they update in real time when events occur in Arx.')
    console.set_cursor_pos(
        0, console.get_console_info().window_rectangle.top + 8)
    print_slow('Make sure to keep an eye out on them!')
    console.set_cursor_pos(
        0, console.get_console_info().window_rectangle.top + 8)
    confirm()

    # Display character's stats and what they mean.
    playerStats()
    statMeaning()

    # First choice
    safeZone = 1
    while True:
        print_slow(big)
        print_slow("Now that you're situated with your stats, would you like to:")
        print_slow("[1] visit the town or [2] fight a monster?")
        answer = qAnswer("Type in the number you choose.")
        scroll_text_up(PADDING)
        console.set_cursor_pos(
            0, console.get_console_info().window_rectangle.bottom - 1)
        if answer == '1':
            print_slow("The town isn't avaliable yet, try again later ;)")
            # break
        elif answer == '2':
            print_slow(
                'Alright lets climb this hill, I think I see some monsters on top!')
            # Monster Encounter goes here
            break
        else:
            print_slow("I didn't catch your answer, come again?")
    print_slow('This is as far as the game goes so far!')
    ''' --------------------------------------- '''
