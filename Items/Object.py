from enum import Enum

#TODO: Delete or redo this file. Build stronger foundation for items and containers, will need to redo loot table file.
class ItemType(Enum):
    WEAPON = "weapon"
    ARMOR = "armor"
    CONSUMABLE = "consumable"
    MISC = "misc"


class ItemRarity(Enum):
    COMMON = "common"
    UNCOMMON = "uncommon"
    RARE = "rare"
    EPIC = "epic"
    LEGENDARY = "legendary"


class Container:
    def __init__(self, capacity_limit, current_capacity):
        self.capacity_limit = capacity_limit
        self.current_capacity = current_capacity

    items = []  # List for items in container.

    def calculate_current_capacity(self):
        for item in self.items:
            self.current_capacity += item.weight
            return self.current_capacity

    def is_full(self):
        return self.current_capacity >= self.capacity_limit

    def add_item(self, item):
        if not self.is_full():
            if self.calculate_current_capacity() + item.weight > self.capacity_limit:
                print("Item is too heavy.")
                return
            else:
                self.items.append(item)
                print(f"{item.name} added to container.")

    def remove_item(self, item):
        if item in self.items:
            self.current_capacity -= item.weight
            self.items.remove(item)
            print(f"{item.name} removed from container.")
        else:
            print(f"{item.name} not in container.")


class Item:
    """Base class for all items.
    Stats every item should have
    should be defined here.

    :param name: Name of the item.
    :param weight: Weight of the item.
    :param item_rarity: Rarity of the item.
    """

    def __init__(self, name, weight, item_rarity):
        self.name = name
        self.weight = weight
        self.item_rarity = item_rarity
        self.item_type = None
        self.value = None
        self.description = None


class Equipment(Item):
    """Base class for all equipment.
    Additional stats for equipment should be defined here.
    Currently only durability is added here.

    :param name: Name of the equipment.
    :param weight: Weight of the equipment.
    :param item_rarity: Rarity of the equipment."""

    def __init__(self, name, weight, item_rarity):
        super().__init__(name, weight, item_rarity)
        self.durability = 100


class Weapon(Equipment):
    """Base class for all weapons.
    Additional stats for weapons should be defined here.
    Damage is added here.
    Value is added here, based on damage and rarity.

    :param name: Name of the weapon.
    :param weight: Weight of the weapon.
    :param item_rarity: Rarity of the weapon.
    :param damage: Damage of the weapon."""

    def __init__(self, name, weight, item_rarity, damage):
        super().__init__(name, weight, item_rarity)
        self.item_type = ItemType.WEAPON
        self.damage = damage
        self.value = self.calculate_value()

    def calculate_value(self):
        """Calculates the value of the weapon based on damage and rarity.

        Formula: damage * rarity multiplier."""

        if self.item_rarity == ItemRarity.COMMON:
            self.value = self.damage * 2
        elif self.item_rarity == ItemRarity.UNCOMMON:
            self.value = self.damage * 3
        elif self.item_rarity == ItemRarity.RARE:
            self.value = self.damage * 4
        elif self.item_rarity == ItemRarity.EPIC:
            self.value = self.damage * 5
        elif self.item_rarity == ItemRarity.LEGENDARY:
            self.value = self.damage * 6
        return self.value


class Armor(Equipment):
    """Base class for all armor.
    Additional stats for armor should be defined here.
    Armor is added here.
    Value is added here, based on armor and rarity.

    :param name: Name of the armor.
    :param weight: Weight of the armor.
    :param item_rarity: Rarity of the armor.
    :param defense: Defense of the armor."""

    def __init__(self, name, weight, item_rarity, defense):
        super().__init__(name, weight, item_rarity)
        self.item_type = ItemType.ARMOR
        self.defense = defense
        self.value = self.calculate_value()

    def calculate_value(self):
        """Calculates the value of the armor based on defense and rarity.

        Formula: armor * rarity multiplier."""

        if self.item_rarity == ItemRarity.COMMON:
            self.value = self.defense * 2
        elif self.item_rarity == ItemRarity.UNCOMMON:
            self.value = self.defense * 3
        elif self.item_rarity == ItemRarity.RARE:
            self.value = self.defense * 4
        elif self.item_rarity == ItemRarity.EPIC:
            self.value = self.defense * 5
        elif self.item_rarity == ItemRarity.LEGENDARY:
            self.value = self.defense * 6
        return self.value


class Consumable(Item):
    pass


class Potion(Consumable):
    pass


class Food(Consumable):
    pass
