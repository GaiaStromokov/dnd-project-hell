from box import Box


levelL = [str(i) for i in range(1, 21)]
atrL = ["STR", "DEX", "CON", "INT", "WIS", "CHA"]

skillL = [
    "Acrobatics","Animal Handling","Arcana","Athletics","Deception","History","Insight",
    "Intimidation","Investigation","Medicine","Nature","Perception","Performance","Persuasion",
    "Religion","Sleight of Hand","Stealth","Survival"
]
profL=["ARMOR","TOOL","SIMPLE","MARTIAL","LANG"]

featL=["Alert", "Athlete", "Actor", "Charger", "Crossbow Expert"]

dcore = Box({
    "R": {
        "Human": ["Standard", "Variant"],
        "Elf": ["High", "Wood", "Drow"],
        "Dwarf": ["Hill", "Mountain"],
        "Halfling": ["Lightfoot", "Stout"],
        "Dragonborn": ["Black", "Blue", "Green"]
    },
    "C": {
        "Fighter": ["Champion", "Battle Master", "Eldritch Knight"],
        "Rogue": ["Thief", "Assassin", "Arcane Trickster"],
        "Wizard": ["Evocation", "Illusion"],
        "Cleric": ["Life", "Light", "Nature"]
    },
    "BG": ["Acolyte", "Charlatan", "Criminal"]
})


dprof = Box({
    "ARMOR":[
        "Light", "Medium", "Heavy", "Shield"
    ],
    "TOOL": [
        "Alchemist", "Brewer", "Calligrapher", "Carpenter", "Cartographer",
        "Cobbler", "Cook", "Glassblower", "Jeweler", "Leatherworker",
        "Mason", "Painter", "Potter", "Smith", "Tinker", "Weaver", "Thief",
        "Woodworker", "Disguise", "Forgery", "Dice", "Dragonchess", "Cards", "Three-Dragon Ante",
        "Bagpipes", "Drum", "Dulcimer", "Flute", "Lute", "Lyre", "Horn", "Pan Flute", "Shawm", "Viol"
    ],
    "SIMPLE":[
        "Club", "Dagger", "Greatclub", "Handaxe", "Javelin", "Light Hammer", "Mace", "Quarterstaff", "Sickle", "Spear",
        "Light Crossbow", "Dart", "Shortbow", "Sling"
    ],
    "MARTIAL":[
        "Battleaxe", "Flail", "Glaive", "Greataxe", "Greatsword", "Halberd", "Lance", "Longsword", "Maul", "Morningstar",
        "Pike", "Rapier", "Scimitar", "Shortsword", "Trident", "War Pick", "Warhammer", "Whip", "Blowgun", "Hand Crossbow",
        "Heavy Crossbow", "Longbow", "Net"
    ],
    "LANG":[
        "Common", "Dwarvish", "Elvish", "Giant", "Gnomish", "Goblin", "Halfling", "Orc",
        "Abyssal", "Celestial", "Draconic", "Deep Speech", "Infernal", "Primordial", "Sylvan", "Undercommon"
    ]
})
