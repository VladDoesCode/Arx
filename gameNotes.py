# TODO implement monster fighting (Monster Class)
# TODO Inventory system
# TODO Create a question function to pass if command statements through - Done!
# TODO Display stats at the top of terminal.
# TODO Create a game-loop-esc function to call upon when something changes
# TODO Save Functionality (maybe check points?)
# TODO BIG todo: make a Trello board of todos. im losing count and going insane.

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

'''
What I can utilize from my Hero class:
_Health: {mainChar._health}    <\
_Armor: {mainChar._armor}      < \ These mean the same thing
Health: {mainChar.health}      < /
Armor: {mainChar.armor}        </
Mana Pool Max: {mainChar.manaPoolmax}
Stamina Pool Max: {mainChar.staminaPoolmax}
Strength: {mainChar.strength}
Agility: {mainChar.agility}
Intelligence: {mainChar.intelligence}
Charisma: {mainChar.charisma}
'''
