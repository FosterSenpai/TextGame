import random

from Items.Object import Armor, Weapon
from typing import Optional

class BodyPart:
    """
    Class for a body part of a creature
    :param name: Name of the body part
    :param owner: Creature object that the body part belongs to
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
    :var owner: Creature object that the body part belongs to
    """

    def __init__(self, name, is_critical_to_survival=False, owner=None):
        self.name = name
        self.health = 100
        self.armor = 0
        self.efficiency = 1
        self.gear_slot: Optional[Armor] = None
        self.is_crippled = False
        self.is_destroyed = False
        self.is_critical_to_survival = is_critical_to_survival
        self.dependent_body_parts = []
        self.owner = owner

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

    def calculate_efficiency(self, creature_level):
        """
        Calculate the efficiency of the body part
        :param creature_level: Level of the creature
        :return: Efficiency of the body part as a float
        .. note:: Linearly scales efficiency based on creature level, makes game easier as player levels up
        Call after every level up and when body part takes damage
        """
        efficiency = self.efficiency #start with base efficiency
        #Check if body part is crippled or destroyed
        if self.is_crippled:
            efficiency *= 0.25 #25% of efficiency when crippled
        if self.is_destroyed:
            efficiency = 0
        #Calculate final efficiency based on creature level
        efficiency *= (self.health / 100) * (creature_level / 10)
        return efficiency


    def equip_armor(self,armor: Armor):
        """
        Equip armor to body part
        :param armor: Armor item object to equip
        :return: none
        Note: Updates armor value of body part with defense value of equipped armor
        """
        self.gear_slot = armor
        self.armor = self.gear_slot.defense # Update body part armor value with defense value of armor

    def take_damage(self, damage, owner):
        """
        Take damage to body part
        :param damage: Damage value to take
        :param owner: Creature object that the body part belongs to
        :return: none

        Notes: Handles efficiency calculation, crippling, destruction and killing of the creature if
        critical body part is destroyed
        """
        damage_taken = damage - self.armor

        # If already crippled, take double damage and if health reaches 0 while crippled, destroy the part
        if self.is_crippled:
            damage_taken *= 2
            if self.health - damage_taken <= 0:
                self.is_destroyed = True
                for part in self.dependent_body_parts:
                    part.is_destroyed = True
                    part.health = 0
                    part.efficiency = 0
                if self.is_critical_to_survival:
                    self.owner.health = 0
                    self.owner.is_alive = False

        # Apply damage to health and calculate efficiency
        self.health -= damage_taken
        self.efficiency = self.calculate_efficiency(self.owner.level)
        if self.efficiency < 0:
            self.efficiency = 0

        # Check if body part is crippled/destroyed
        if self.health <= 0:
            self.health = 0
            if random.random() < 0.75:  # 75% chance of being crippled
                self.is_crippled = True
            else:  # 25% chance of being destroyed
                self.is_destroyed = True
                # destroy dependent body parts
                for part in self.dependent_body_parts:
                    part.is_destroyed = True
                    part.health = 0
                    part.efficiency = 0
                if self.is_critical_to_survival:
                    self.owner.health = 0
                    self.owner.is_alive = False



class Hand(BodyPart):
    """
    Class for a hand derived from BodyPart
    :param name: Name of the hand
    :var weapon_slot: Gear slot for weapon
    :var ring_slot: Gear slot for ring (TODO: Implement rings)
    """

    def __init__(self, name, owner=None):
        super().__init__(name)
        self.weapon_slot: Optional[Weapon] = None  # Weapon slot for hand
        self.ring_slot: Optional[Armor] = None  # Ring slot for hand