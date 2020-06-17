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


'''
------------------------------
How I define the stats in Arx.
------------------------------
Strength:
Description: Measures physical power and carrying capacity
Primary benefit(s): Weapon Damage
Additional benefit(s): Increases Inventory

Agility:
Description: 
Primary benefit(s): Increased Stamina pool
Additional benefit(s): Crit chance and Dodge chance

Intelligence:
Description:
Primary benefit(s): Increased Mana pool
Additional benefit(s): Spell Damage and Heal Amount

Charisma:
Description:
Primary benefit(s): Trade prices
Additional benefit(s): Chance to prevent negative effects

--------------------------
Class specific info in Arx
--------------------------

Assume 10 is a base value for every stat, where anything above 10 is
a stat that class specializes in and vice vera. (0 - 20)
Total of 40 for every class (except Commoner)

Commoner:
Description: Base class with equal across the board stats. They are all lowered for balance.
Strength: 8
Agility: 8
Intelligence: 8
Charisma: 8

Warrior:
Description: Strength based class that hits hard, lifts more, and has higher Charisma
Strength: 16
Agility: 6
Intelligence: 6
Charisma: 12

Mage:
Description: Intelligence based class with higher Charisma
Strength: 6
Agility: 5
Intelligence: 16
Charisma: 13

Thief:
Description: Agility based class with good Strength and Charisma
Strength: 9
Agility: 16
Intelligence: 6
Charisma: 9

Paladin:
Description: Charisma based class with better strength and good heals.
Strength: 12
Agility: 2
Intelligence: 10
Charisma: 16
'''


# Setting up players stats
class Player:
    def __init__(self, health, armor):
        self._health = health
        self._armor = armor
        if playerClass.lower() == "commoner":
            self.strength = 8
            self.agility = 8
            self.intelligence = 8
            self.charisma = 8
        elif playerClass.lower() == "warrior":
            self.strength = 16
            self.agility = 6
            self.intelligence = 6
            self.charisma = 12
        elif playerClass.lower() == "mage":
            self.strength = 6
            self.agility = 5
            self.intelligence = 16
            self.charisma = 13
        elif playerClass.lower() == "thief":
            self.strength = 9
            self.agility = 16
            self.intelligence = 6
            self.charisma = 9
        elif playerClass.lower() == "paladin":
            self.strength = 12
            self.agility = 2
            self.intelligence = 10
            self.charisma = 16

    def __str__(self):
        return f'-◄[Health: {self.health}, Armor: {self.armor}]►-'

    @property
    def health(self):
        return self._health

    @property
    def armor(self):
        return self._armor

    @health.setter
    def health(self, value):
        # Here I want to make it delete old health display and display new.
        self.health = value

    @armor.setter
    def armor(self, value):
        # Here I want to make it delete old armor display and display new.
        self.armor = value


def set_hp(console, max_hp, current_hp):
    if showStats == 1:
        console.set_cursor_pos(0, 0)
        console.set_text_color('bright white', 'black')
        print(f"[Health {current_hp: >3}/{max_hp}:".ljust(14),
              end='', flush=True)
        health_percentage_current = int(((current_hp / max_hp) * 100) // 10)

        console.set_text_color('bright white', 'light red')
        print(' ' * health_percentage_current, end='', flush=True)

        console.set_text_color('bright white', 'red')
        print(' ' * (10 - health_percentage_current), end='', flush=True)

        console.set_text_color('bright white', 'black')
        print(']')
        console.set_default_text_color()


def set_armor(console, max_armor, current_armor):
    if showStats == 1:
        console.set_cursor_pos(0, 1)
        console.set_text_color('bright white', 'black')
        print(f"[Armor    {current_armor: >2}/{max_armor}:".ljust(14),
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


def set_mana(console, max_mana, current_mana):
    if showStats == 1:
        console.set_cursor_pos(0, 2)
        console.set_text_color('bright white', 'black')
        print(f"[Mana     {current_mana: >2}/{max_mana}:".ljust(14),
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


def set_stamina(console, max_stamina, current_stamina):
    if showStats == 1:
        console.set_cursor_pos(0, 3)
        console.set_text_color('bright white', 'black')
        print(f"[Stamina  {current_stamina: >2}/{max_stamina}:".ljust(14),
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


# Prints text slowly
def print_slow(fstr, waitTime=0):
    for letter in fstr:
        print(letter, end='', flush=True)
        time.sleep(0.03)
    time.sleep(waitTime)
    scroll_text_up(PADDING)
    console.set_cursor_pos(0, console_info.window_rectangle.bottom - 1)
    console.clear_line(console.get_console_info().window_rectangle.bottom - 1)
    return ''


# Shows player what each player stat does
def statMeaning():
    print_slow(big)
    print_slow('Stats in Arx')
    print_slow(small)
    print_slow('Strength:')
    print_slow('Primary benefit(s): Weapon Damage')
    print_slow('Additional benefit(s): Increases Inventory', .5)
    print_slow('')
    print_slow('Agility:')
    print_slow('Primary benefit(s): Increased Stamina pool')
    print_slow('Additional benefit(s): Crit chance and Dodge chance', .5)
    print_slow('')
    print_slow('Intelligence:')
    print_slow('Primary benfit(s): Increased Mana pool')
    print_slow('Additional benefit(s): Spell Damage and Heal Amount', .5)
    print_slow('')
    print_slow('Charisma:')
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
    print_slow(f"► Your Strength is: {my_player.strength}", .5)
    print_slow(f"► Your Agility is: {my_player.agility}", .5)
    print_slow(f"► Your Intelligence is: {my_player.intelligence}", .5)
    print_slow(f"► Your Charisma is: {my_player.charisma}", .5)
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
    showStats = 1
    set_hp(console, 100, 100)
    set_armor(console, 10, 10)
    set_mana(console, 50, 50)
    set_stamina(console, 50, 50)
    console.set_cursor_pos(0, console_info.window_rectangle.bottom - 1)

    # Infinite (until it breaks) loop to get characters name.
    while True:
        print_slow(big)
        playerName = qAnswer("Hello Adventurer, what is your name?")
    # If character name is 18 or more characters, don't allow it.
        if len(playerName) <= 18:
            break
        print_slow(small)
        print_slow('Thats a mighty long name, do you go by something shorter?')
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
        playerClass = qAnswer(
            'What class would you like to play? [Commoner], [Warrior], [Mage], [Thief], or [Paladin]?')
        clear_screen()
        console.set_cursor_pos(
            0, console.get_console_info().window_rectangle.bottom - 1)
        if playerClass.lower() in ['commoner', 'warrior', 'mage', 'thief', 'paladin']:
            break

    my_player = Player(100, 0)

    # Display character's stats and what they mean.
    playerStats()
    statMeaning()

    # First choice
    showStats = 1
    safeZone = 1
    set_hp(console, 100, 100)
    set_armor(console, 10, 0)
    set_mana(console, 50, 40)
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
