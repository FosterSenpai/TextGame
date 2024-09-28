from Creatures.Creature import Creature

def check_dependencies(body_part):
    print([str(part) for part in body_part.dependent_body_parts])

Foster = Creature("Foster", 100, 1)
print(Foster)
check_dependencies(Foster.body_parts[Foster.get_part("Left Shoulder")])
check_dependencies(Foster.body_parts[Foster.get_part("Right Shoulder")])
check_dependencies(Foster.body_parts[Foster.get_part("Left Arm")])
check_dependencies(Foster.body_parts[Foster.get_part("Right Arm")])
check_dependencies(Foster.body_parts[Foster.get_part("Left Leg")])
check_dependencies(Foster.body_parts[Foster.get_part("Right Leg")])
