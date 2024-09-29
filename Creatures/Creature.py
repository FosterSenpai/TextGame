from random import randrange

from Creatures.BodyParts import Hand, BodyPart
from Items import Object


class Creature:
    """
    Base class for every creature in the game
    :param name: Name for the creature
    :param health: Initial health for the creature
    :param level: Initial Level of the creature
    :var name: Name of the creature
    :var health: Health of the creature
    :var level: Level of the creature
    :var is_alive: If the creature is alive or dead (bool, default is True)
    :var body_parts: Body parts of the creature, list of BodyPart objects
    :var right_pocket: Right pocket of the creature, Object.Container object
    :var left_pocket: Left pocket of the creature, Object.Container object
    """
    def __init__(self, name, health, level):
        self.name = name
        self.health = health
        self.level = level
        self.is_alive = True
        self.body_parts = [                                                            # Index
            Hand("Left Hand", owner=self),                                       # 0 - left hand
            Hand("Right Hand", owner=self),                                      # 1 - right hand
            BodyPart("Head", is_critical_to_survival=True, owner=self),          # 2 - head
            BodyPart("Neck", is_critical_to_survival=True, owner=self),          # 3 - neck
            BodyPart("Chest", is_critical_to_survival=True, owner=self),         # 4 - chest
            BodyPart("Left Shoulder", owner=self),                               # 5 - left shoulder
            BodyPart("Right Shoulder", owner=self),                              # 6 - right shoulder
            BodyPart("Left Arm", owner=self),                                    # 7 - left arm
            BodyPart("Right Arm", owner=self),                                   # 8 - right arm
            BodyPart("Left Leg", owner=self),                                    # 9 - left leg
            BodyPart("Right Leg", owner=self),                                   # 10 - right leg
            BodyPart("Left Foot", owner=self),                                   # 11 - left foot
            BodyPart("Right Foot", owner=self)                                   # 12 - right foot
        ]

        # Set dependent body parts
        # Left Shoulder, Hand + Arm dependent
        self.body_parts[self.part("Left Shoulder")].set_dependent_body_parts(self.body_parts[self.part("Left Hand")])
        self.body_parts[self.part("Left Shoulder")].set_dependent_body_parts(self.body_parts[self.part("Left Arm")])
        # Right Shoulder, Hand + Arm dependent
        self.body_parts[self.part("Right Shoulder")].set_dependent_body_parts(self.body_parts[self.part("Right Hand")])
        self.body_parts[self.part("Right Shoulder")].set_dependent_body_parts(self.body_parts[self.part("Right Arm")])
        # Left Arm, Hand dependent
        self.body_parts[self.part("Left Arm")].set_dependent_body_parts(self.body_parts[self.part("Left Hand")])
        # Right Arm, Hand dependent
        self.body_parts[self.part("Right Arm")].set_dependent_body_parts(self.body_parts[self.part("Right Hand")])
        # Left Leg, Foot dependent
        self.body_parts[self.part("Left Leg")].set_dependent_body_parts(self.body_parts[self.part("Left Foot")])
        # Right Leg, Foot dependent
        self.body_parts[self.part("Right Leg")].set_dependent_body_parts(self.body_parts[self.part("Right Foot")])

        # Pocket containers, use for loot
        self.right_pocket = Object.Container(10, 0)
        self.left_pocket = Object.Container(10, 0)

    def __str__(self):
        return f"{self.name} - Level: {self.level} - Health: {self.health}"

    @staticmethod # This is how you make a static method in Python
    def part(body_part_name):
        """
        #TODO: there has to be a better way to do this, end up typing way too much
        Converts body part name string to its index in the body_parts list
        :param body_part_name: Name of body part as a string
        .. note:: Names are capitalized words
        :return: Index of body part in body_parts list as an int
        """
        if body_part_name == "Left Hand":
            return 0
        elif body_part_name == "Right Hand":
            return 1
        elif body_part_name == "Head":
            return 2
        elif body_part_name == "Neck":
            return 3
        elif body_part_name == "Chest":
            return 4
        elif body_part_name == "Left Shoulder":
            return 5
        elif body_part_name == "Right Shoulder":
            return 6
        elif body_part_name == "Left Arm":
            return 7
        elif body_part_name == "Right Arm":
            return 8
        elif body_part_name == "Left Leg":
            return 9
        elif body_part_name == "Right Leg":
            return 10
        elif body_part_name == "Left Foot":
            return 11
        elif body_part_name == "Right Foot":
            return 12

    def alive_check(self):
        """
        Check if creature is alive, updates is_alive attribute
        :return: True if creature is alive, False if creature is dead
        """
        # Check if health is 0 or iterates through body parts to check if any are critical to survival and destroyed
        if self.health <= 0:
            self.is_alive = False
            return False
        return True

    def print_alive_status(self) -> None:
        """
        Print description of creature's alive status
        """
        if self.is_alive:
            print(f"{self.name} is alive")
        else:
            print(f"{self.name} is dead")

    def deal_damage(self, hand, enemy) -> None:
        """
        Deal damage to enemy creature
        :param hand: Hand object of the creature dealing damage
        :param enemy: Enemy object that is taking damage
        """
        damage = hand.weapon_slot.damage
        # Choose random body part to deal damage to
        enemy_body_part = enemy.body_parts[randrange(0, len(enemy.body_parts))]
        enemy_body_part.take_damage(damage, enemy)

class Player(Creature):
    #TODO: Implement player class, add inventory, money, experience, race?, class?
    # skills(could add skills to base class for enemies to use)?, what else would be unique to a player?
    # tiredness, hunger, thirst, sanity, temperature, weight, height, age ? maybe not that far
    pass

class Enemy(Creature):
    #TODO: Implement enemy class, add loot table, AI, faction, what else would be unique to an enemy?
    # type/element, rarity, xp(given to player), money(given to player)
    pass
