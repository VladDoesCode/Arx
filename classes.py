class Hero():
    def __init__(self, health, armor, charClass):
        self._health = health
        self._armor = armor
        if charClass.lower() == "commoner":
            self.strength = 8
            self.agility = 8
            self.intelligence = 8
            self.charisma = 8
        elif charClass.lower() == "warrior":
            self.strength = 16
            self.agility = 6
            self.intelligence = 6
            self.charisma = 12
        elif charClass.lower() == "mage":
            self.strength = 6
            self.agility = 5
            self.intelligence = 16
            self.charisma = 13
        elif charClass.lower() == "thief":
            self.strength = 9
            self.agility = 16
            self.intelligence = 6
            self.charisma = 9
        elif charClass.lower() == "paladin":
            self.strength = 12
            self.agility = 2
            self.intelligence = 10
            self.charisma = 16
        self.staminaPoolmax = self.agility * 5
        self.manaPoolmax = self.intelligence * 5

    @property
    def health(self):
        return self._health

    @property
    def armor(self):
        return self._armor

    @health.setter
    def health(self, value):
        # Here I want to make it delete old health display and display new.
        self._health = value

    @armor.setter
    def armor(self, value):
        # Here I want to make it delete old armor display and display new.
        self._armor = value
