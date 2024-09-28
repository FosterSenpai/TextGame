from Object import Armor, Weapon
from typing import Optional

class BodyPart:
    def __init__(self, name):
        self.name = name
        self.health = 100
        self.armor = 0
        self.gear_slot: Optional[Armor] = None  # Gear slot for body part

class Hand(BodyPart):
    def __init__(self, name):
        super().__init__(name)
        self.weapon_slot: Optional[Weapon] = None  # Weapon slot for hand