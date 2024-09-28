from Creatures.BodyParts import Hand, BodyPart
from Items import Object


class Creature:
    """
    Base class for every creature in the game
    :param name: Name of the creature
    :param health: Health of the creature
    :param level: Level of the creature
    :var body_parts: Body parts of the creature, list of BodyPart objects
    :var right_pocket: Right pocket of the creature, Object.Container object
    :var left_pocket: Left pocket of the creature, Object.Container object
    """
    def __init__(self, name, health, level):
        self.name = name
        self.health = health
        self.level = level
        self.body_parts = [                                          # Index
            Hand("Left Hand"),                                       # 0 - left hand
            Hand("Right Hand"),                                      # 1 - right hand
            BodyPart("Head", is_critical_to_survival=True),    # 2 - head
            BodyPart("Neck", is_critical_to_survival=True),    # 3 - neck
            BodyPart("Chest", is_critical_to_survival=True),   # 4 - chest
            BodyPart("Left Shoulder"),                               # 5 - left shoulder
            BodyPart("Right Shoulder"),                              # 6 - right shoulder
            BodyPart("Left Arm"),                                    # 7 - left arm
            BodyPart("Right Arm"),                                   # 8 - right arm
            BodyPart("Left Leg"),                                    # 9 - left leg
            BodyPart("Right Leg"),                                   # 10 - right leg
            BodyPart("Left Foot"),                                   # 11 - left foot
            BodyPart("Right Foot")                                   # 12 - right foot
        ]

        # Set dependent body parts
        # Left Shoulder, Hand + Arm dependent
        self.body_parts[self.get_part("Left Shoulder")].set_dependent_body_parts(self.body_parts[self.get_part("Left Hand")])
        self.body_parts[self.get_part("Left Shoulder")].set_dependent_body_parts(self.body_parts[self.get_part("Left Arm")])
        # Right Shoulder, Hand + Arm dependent
        self.body_parts[self.get_part("Right Shoulder")].set_dependent_body_parts(self.body_parts[self.get_part("Right Hand")])
        self.body_parts[self.get_part("Right Shoulder")].set_dependent_body_parts(self.body_parts[self.get_part("Right Arm")])
        # Left Arm, Hand dependent
        self.body_parts[self.get_part("Left Arm")].set_dependent_body_parts(self.body_parts[self.get_part("Left Hand")])
        # Right Arm, Hand dependent
        self.body_parts[self.get_part("Right Arm")].set_dependent_body_parts(self.body_parts[self.get_part("Right Hand")])
        # Left Leg, Foot dependent
        self.body_parts[self.get_part("Left Leg")].set_dependent_body_parts(self.body_parts[self.get_part("Left Foot")])
        # Right Leg, Foot dependent
        self.body_parts[self.get_part("Right Leg")].set_dependent_body_parts(self.body_parts[self.get_part("Right Foot")])

        # Pocket containers, use for loot
        self.right_pocket = Object.Container(10, 0)
        self.left_pocket = Object.Container(10, 0)

    def __str__(self):
        return f"{self.name} - Level: {self.level} - Health: {self.health}"

    @staticmethod # This is how you make a static method in Python
    def get_part(body_part_name):
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


    def deal_damage(self, hand, enemy):
        """
        TODO:
        Take in hand of attacking creature as parameter to get weapon damage
        Take in enemy as parameter to deal damage to enemy body part
            Choose random body part to deal damage to
        use enemy body part take_damage method to deal damage to body part
        enemy_body_part.take_damage(self.hand.weapon_slot.damage)
        """
        pass

class Player(Creature):
    #TODO: Implement player class, add inventory, money, experience, race?, class?
    # skills(could add skills to base class for enemies to use)?, what else would be unique to a player?
    # tiredness, hunger, thirst, sanity, temperature, weight, height, age ? maybe not that far
    pass

class Enemy(Creature):
    #TODO: Implement enemy class, add loot table, AI, faction, what else would be unique to an enemy?
    # type/element, rarity, xp(given to player), money(given to player)
    pass
