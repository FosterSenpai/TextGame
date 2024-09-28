from BodyParts import Hand, BodyPart
import Object

class Creature:
    def __init__(self, name, health, level):
        self.name = name
        self.health = health
        self.level = level
        self.body_parts = [
            Hand("Left Hand"),
            Hand("Right Hand"),
            BodyPart("Head"),
            BodyPart("Neck"),
            BodyPart("Chest"),
            BodyPart("Left Shoulder"),
            BodyPart("Right Shoulder"),
            BodyPart("Left Arm"),
            BodyPart("Right Arm"),
            BodyPart("Left Leg"),
            BodyPart("Right Leg"),
            BodyPart("Left Foot"),
            BodyPart("Right Foot")
        ]
        self.right_pocket = Object.Container(10, 0)
        self.left_pocket = Object.Container(10, 0)

    def __str__(self):
        return f"{self.name} is level {self.level} with {self.health} health."

class Player(Creature):
    pass

class Enemy(Creature):
    pass
