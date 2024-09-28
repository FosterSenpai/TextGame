from Creature import Creature, Player, Enemy

Foster = Player("Foster", 100, 1)
print([str(part) for part in Foster.body_parts[Creature.get_part("Left Shoulder")].dependent_body_parts])