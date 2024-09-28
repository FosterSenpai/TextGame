import random

#TODO: Fix up methods, probs just delete them and remake. pull item names out into their own file .
weapon_prefixes = [
    "Ancient", "Arcane", "Blazing", "Bloodthirsty", "Brutal", "Cursed", "Dark", "Deadly", "Divine", "Dragon's",
    "Dreadful", "Enchanted", "Eternal", "Exalted", "Fiery", "Forsaken", "Frost", "Ghostly", "Glorious", "Golden",
    "Grim", "Hallowed", "Haunted", "Infernal", "Iron", "Legendary", "Light", "Mighty", "Mystic", "Night",
    "Phantom", "Poisonous", "Primal", "Radiant", "Savage", "Shadow", "Shimmering", "Silver", "Sinister", "Sorrowful",
    "Spectral", "Storm", "Thunder", "Unholy", "Vengeful", "Vicious", "War", "Wicked", "Wind", "Wrathful"
]

weapon_middle_words = [
    "Blade", "Edge", "Fang", "Claw", "Strike", "Slash", "Bite", "Fury", "Wrath", "Doom",
    "Scourge", "Reaper", "Slicer", "Cleaver", "Crusher", "Destroyer", "Annihilator", "Ravager", "Maul", "Hammer",
    "Spear", "Lance", "Pike", "Halberd", "Axe", "Mace", "Flail", "Scimitar", "Saber", "Katana",
    "Rapier", "Dagger", "Dirk", "Knife", "Bow", "Crossbow", "Arrow", "Bolt", "Staff", "Wand",
    "Rod", "Scepter", "Orb", "Shield", "Buckler", "Gauntlet", "Glove", "Whip", "Chain", "Trident"
]

weapon_suffixes = [
    "of Power", "of Fury", "of the Phoenix", "of Shadows", "of the Dragon", "of the Wolf", "of the Bear",
    "of the Tiger", "of the Lion", "of the Eagle",
    "of the Serpent", "of the Kraken", "of the Leviathan", "of the Hydra", "of the Basilisk", "of the Chimera",
    "of the Griffin", "of the Minotaur", "of the Cyclops", "of the Gorgon",
    "of the Titan", "of the Giant", "of the Colossus", "of the Behemoth", "of the Juggernaut", "of the Warlord",
    "of the Conqueror", "of the Gladiator", "of the Champion", "of the Hero",
    "of the Paladin", "of the Knight", "of the Crusader", "of the Templar", "of the Samurai", "of the Ninja",
    "of the Assassin", "of the Rogue", "of the Thief", "of the Hunter",
    "of the Ranger", "of the Druid", "of the Shaman", "of the Sorcerer", "of the Wizard", "of the Warlock",
    "of the Necromancer", "of the Lich", "of the Vampire", "of the Werewolf"
]


def generate_weapon_name():
    return f"{random.choice(weapon_prefixes)} {random.choice(weapon_middle_words)} {random.choice(weapon_suffixes)}"


armor_prefixes = [
    "Ancient", "Arcane", "Blazing", "Bloodthirsty", "Brutal", "Cursed", "Dark", "Deadly", "Divine", "Dragon's",
    "Dreadful", "Enchanted", "Eternal", "Exalted", "Fiery", "Forsaken", "Frost", "Ghostly", "Glorious", "Golden",
    "Grim", "Hallowed", "Haunted", "Infernal", "Iron", "Legendary", "Light", "Mighty", "Mystic", "Night",
    "Phantom", "Poisonous", "Primal", "Radiant", "Savage", "Shadow", "Shimmering", "Silver", "Sinister", "Sorrowful",
    "Spectral", "Storm", "Thunder", "Unholy", "Vengeful", "Vicious", "War", "Wicked", "Wind", "Wrathful"
]

armor_middle_words = [
    "Plate", "Mail", "Guard", "Shield", "Helm", "Cuirass", "Greaves", "Gauntlets", "Bracers", "Boots",
    "Pauldrons", "Vambraces", "Sabatons", "Breastplate", "Hauberk", "Tassets", "Gorget", "Visor", "Mask", "Mantle",
    "Coif", "Aegis", "Harness", "Plackart", "Fauld", "Cuisses", "Rerebrace", "Spaulders", "Bevor", "Cuisse",
    "Tunic", "Jerkin", "Tabard", "Doublet", "Gambeson", "Brigandine", "Jack", "Surcoat", "Haubergeon", "Armet",
    "Bascinet", "Barbute", "Sallet", "Kettle", "Morion", "Burgonet", "Cervelliere", "Close", "Great", "Zischagge"
]

armor_suffixes = [
    "of Protection", "of Fortitude", "of the Guardian", "of the Sentinel", "of the Defender", "of the Protector",
    "of the Warden", "of the Keeper", "of the Shield", "of the Bulwark",
    "of the Bastion", "of the Fortress", "of the Citadel", "of the Rampart", "of the Stronghold", "of the Aegis",
    "of the Barrier", "of the Wall", "of the Palisade", "of the Redoubt",
    "of the Bastille", "of the Keep", "of the Tower", "of the Castle", "of the Garrison", "of the Barricade",
    "of the Blockade", "of the Outpost", "of the Watch", "of the Guard",
    "of the Sentinel", "of the Vigil", "of the Lookout", "of the Scout", "of the Patrol", "of the Sentry",
    "of the Watchman", "of the Observer", "of the Overseer", "of the Surveyor",
    "of the Inspector", "of the Examiner", "of the Monitor", "of the Watcher", "of the Protectorate",
    "of the Safeguard", "of the Custodian", "of the Steward", "of the Caretaker", "of the Conservator"
]


def generate_armor_name():
    return f"{random.choice(armor_prefixes)} {random.choice(armor_middle_words)} {random.choice(armor_suffixes)}"


goblin_names = [
    "Grub", "Snag", "Grit", "Mug", "Zog", "Ruk", "Bog", "Grog", "Snarl", "Gash",
    "Thug", "Rag", "Skulk", "Brak", "Snort", "Gib", "Nash", "Grim", "Ruk", "Snub",
    "Grot", "Murk", "Zug", "Rag", "Snaggle", "Grizzle", "Mugwort", "Zogwort", "Ruknar", "Bogrot",
    "Grogmar", "Snarlgash", "Gashnark", "Thuggrim", "Ragzog", "Skulkrag", "Brakgrot", "Snortgib", "Gibnash", "Nashgrim",
    "Grimruk", "Snubgrot", "Grotmug", "Murkzog", "Zugrag", "Ragsnag", "Snagglegrit", "Grizzlethug", "Mugwortgash",
    "Zogwortsnarl"
]

goblin_professions = [
    "Warrior", "Shaman", "Thief", "Assassin", "Hunter",
    "Scout", "Berserker", "Sorcerer", "Alchemist", "Rogue",
    "Archer", "Mage", "Warlock", "Necromancer", "Bard",
    "Priest", "Druid", "Monk", "Paladin", "Ranger"
]


def generate_goblin_name():
    name = f"{goblin_names[random.randrange(len(goblin_names))]} the {goblin_professions[random.randrange(len(goblin_professions))]}"
    return name

