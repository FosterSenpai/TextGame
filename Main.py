from Creatures.Creature import Creature

def check_dependencies(body_part):
    print([str(parts) for parts in body_part.dependent_body_parts])

def check_health(body_part):
    print(f"{body_part.name}: HP = {body_part.health}, Efficiency = {body_part.efficiency}, is_crippled = {body_part.is_crippled}, is_destroyed = {body_part.is_destroyed}")


Foster = Creature("Foster", 100, 1)
Foster.alive_check()
Foster.print_alive_status()
print(Foster)
print("Left Shoulder dependencies:")
check_dependencies(Foster.body_parts[Foster.part("Left Shoulder")])
#Take damage to left shoulder twice
print("Left Shoulder before damage:")
check_health(Foster.body_parts[Foster.part("Left Shoulder")])
print("Left Shoulder dependencies before damage:")
for part in Foster.body_parts[Foster.part("Left Shoulder")].dependent_body_parts:
    check_health(part)
print("Left Shoulder after damage:")
Foster.body_parts[Foster.part("Left Shoulder")].take_damage(100, Foster)
check_health(Foster.body_parts[Foster.part("Left Shoulder")])
print("Left Shoulder dependencies after damage:")
for part in Foster.body_parts[Foster.part("Left Shoulder")].dependent_body_parts:
    check_health(part)

print("Left Shoulder after damage:")
Foster.body_parts[Foster.part("Left Shoulder")].take_damage(100, Foster)
check_health(Foster.body_parts[Foster.part("Left Shoulder")])
print("Left Shoulder dependencies after damage:")
for part in Foster.body_parts[Foster.part("Left Shoulder")].dependent_body_parts:
    check_health(part)

Foster.alive_check()
Foster.print_alive_status()

# Deal fatal damage to head
print("Head before damage:")
check_health(Foster.body_parts[Foster.part("Head")])
print("Head after damage:")
Foster.body_parts[Foster.part("Head")].take_damage(100, Foster)
Foster.body_parts[Foster.part("Head")].take_damage(100, Foster)
check_health(Foster.body_parts[Foster.part("Head")])
Foster.alive_check()
Foster.print_alive_status()
