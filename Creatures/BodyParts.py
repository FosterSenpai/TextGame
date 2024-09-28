from Items.Object import Armor, Weapon
from typing import Optional


class BodyPart:
    """
    Class for a body part of a creature
    :param name: Name of the body part
    :param is_critical_to_survival: If body part is destroyed, creature dies. (optional, default is False)
    :var health: Health of the body part, if health reaches 0, body part is destroyed
    :var armor: Armor value of the body part, will take armor from defense value of armor in gear slot.
    :var efficiency: Efficiency of the body part, 0 - 1 range (0.5 = 50% efficiency)
    :var gear_slot: Gear slot for body part
    :var is_crippled: When health reaches 0, body part has a 75% chance of being crippled, can be fixed.
    :var is_destroyed: When health reaches 0, body part is destroyed, cannot be fixed.
    :var is_critical_to_survival: If body part is destroyed, creature dies.
    :var dependent_body_parts: List of body parts that are dependent on this body part, if this part is destroyed,
        dependent parts are also destroyed.
    """

    def __init__(self, name, is_critical_to_survival=False):
        self.name = name
        self.health = 100
        self.armor = 0
        self.efficiency = 1
        self.gear_slot: Optional[Armor] = None
        self.is_crippled = False
        self.is_destroyed = False
        self.is_critical_to_survival = is_critical_to_survival
        self.dependent_body_parts = []

    def __str__(self):
        return f"{self.name} - Health: {self.health} - Armor: {self.armor} - Efficiency: {self.efficiency}"

    def set_dependent_body_parts(self, dependent_body_part):
        """
        Append body parts that are dependent on this body part to the dependent_body_parts list
        :param dependent_body_part: Body part object that is dependent on this body part
        .. note:: When a body part with dependent body parts is destroyed, dependent body parts are also destroyed
        :return: none
        """
        self.dependent_body_parts.append(dependent_body_part)

    def calculate_efficiency(self):
        """
        TODO:
        Take in level of creature as parameter
        Calculate efficiency based on level of creature and health of body part
        if crippled, efficiency is 0.25
        if destroyed, efficiency is 0
        :return: The efficiency of the body part as a float
        """
        pass

    def equip_armor(self,armor: Armor):
        """
        Equip armor to body part
        :param armor: Armor item object to equip
        :return: none
        """
        self.gear_slot = armor
        self.armor = self.gear_slot.defense

    def take_damage(self,damage):
        """
        TODO:
        Take in damage as parameter
        Calculate damage taken based on pure damage taken, armor value and subtract from health
        if health hits 0 roll for crippled or destroyed
            check if body part is critical to survival
            check if parts are dependent on this part
        :return: The damage taken as an int (use for combat log)
        """
        pass


class Hand(BodyPart):
    """
    Class for a hand derived from BodyPart
    :param name: Name of the hand
    :var weapon_slot: Gear slot for weapon
    :var ring_slot: Gear slot for ring (TODO: Implement rings)
    """

    def __init__(self, name):
        super().__init__(name)
        self.weapon_slot: Optional[Weapon] = None  # Weapon slot for hand
        self.ring_slot: Optional[Armor] = None  # Ring slot for hand