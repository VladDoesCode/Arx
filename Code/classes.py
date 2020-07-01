import random
from universalFunctions import (
    setEnemyArmor,
    setEnemyHP,
    setEnemyMana,
    setEnemyStamina,
    clearEnemyStats,
    setHP,
    setMana,
    setArmor,
    setStamina,
    clear_screen,
    PADDINGNONE,
)


class Hero:
    def __init__(self, health, armor, charClass):
        self._health = health
        self.healthPoolmax = self.health
        self._armor = armor
        self.armorPoolmax = self.armor
        if charClass.lower() == "commoner":
            self.strength = 8
            self.agility = 8
            self.intelligence = 8
            self.charisma = 8
            self.charClass = "commoner"
        elif charClass.lower() == "warrior":
            self.strength = 16
            self.agility = 6
            self.intelligence = 6
            self.charisma = 12
            self.charClass = "warrior"
        elif charClass.lower() == "mage":
            self.strength = 6
            self.agility = 5
            self.intelligence = 16
            self.charisma = 13
            self.charClass = "mage"
        elif charClass.lower() == "thief":
            self.strength = 9
            self.agility = 16
            self.intelligence = 6
            self.charisma = 9
            self.charClass = "thief"
        elif charClass.lower() == "paladin":
            self.strength = 12
            self.agility = 2
            self.intelligence = 10
            self.charisma = 16
            self.charClass = "paladin"
        self.staminaPoolmax = self.agility * 5
        self._stamina = self.staminaPoolmax
        self.manaPoolmax = self.intelligence * 5
        self._mana = self.manaPoolmax

    @property
    def health(self):
        return self._health

    @property
    def mana(self):
        return self._mana

    @property
    def stamina(self):
        return self._stamina

    @property
    def armor(self):
        return self._armor

    @health.setter
    def health(self, value):
        self._health = value
        if self._health > 0:
            setHP(self._health, True, self, self.healthPoolmax)
        else:
            clear_screen(PADDINGNONE)

    @mana.setter
    def mana(self, value):
        self._mana = value
        setMana(self._mana, True, self, self.manaPoolmax)

    @stamina.setter
    def stamina(self, value):
        self._stamina = value
        setStamina(self._stamina, True, self, self.staminaPoolmax)

    @armor.setter
    def armor(self, value):
        self._armor = value
        setArmor(self._armor, True, self, self.armorPoolmax)


class Monster:
    def __init__(self, monsterType, mainChar):
        if monsterType == "skeleton":

            self.name = "Skeleton"

            self.healthPoolmax = int(
                mainChar.healthPoolmax * (random.randint(2, 3) / 5)
            )
            self._health = self.healthPoolmax

            self.manaPoolmax = random.randint(5, 20)
            self._mana = self.manaPoolmax

            self.staminaPoolmax = random.randint(20, 45)
            self._stamina = self.staminaPoolmax

            self.armorPoolmax = random.randint(5, 9)
            self._armor = self.armorPoolmax

            self.strength = random.randint(16, 19)
            self.agility = random.randint(6, 10)
            self.intelligence = random.randint(3, 10)
            self.charisma = random.randint(3, 10)

        # setEnemyHP(self, self.health, True)
        # setEnemyMana(self, True)
        # setEnemyStamina(self, True)
        # setEnemyArmor(self, self.armor, True)

    @property
    def health(self):
        return self._health

    @property
    def mana(self):
        return self._mana

    @property
    def stamina(self):
        return self._stamina

    @property
    def armor(self):
        return self._armor

    @health.setter
    def health(self, value):
        self._health = value
        if self._health > 0:
            setEnemyHP(self, self.healthPoolmax)
        else:
            clearEnemyStats()

    @mana.setter
    def mana(self, value):
        self._mana = value
        setEnemyMana(self)

    @stamina.setter
    def stamina(self, value):
        self._stamina = value
        setEnemyStamina(self)

    @armor.setter
    def armor(self, value):
        self._armor = value
        setEnemyArmor(self, self.armorPoolmax)
