from config.gen_import import *

drace=Box({
    "Human": {
            "SPEED": 30,
            "VISION": 0,
            "TRAITS": [],
            "SKILL": [],
            "PROF": {
                "ARMOR": [],
                "TOOL": [],
                "SIMPLE": [],
                "MARTIAL": [],
                "LANG": ["Common"]
            }
    },
    "Elf": {
            "SPEED": 30,
            "VISION": 60,
            "TRAITS": ["Fey Ancestry", "Trance"],
            "SKILL": ["Perception"],
            "PROF": {
                "ARMOR": [],
                "TOOL": [],
                "SIMPLE": [],
                "MARTIAL": [],
                "LANG": ["Common", "Elvish"]
            }
    },
    "Dwarf": {
            "SPEED": 30,
            "VISION": 60,
            "TRAITS": ["Dwarven Resilience", "Stonecunning"],
            "SKILL": [],
            "PROF": {
                "ARMOR": [],
                "TOOL": [],
                "SIMPLE": ["Handaxe", "Light Hammer"],
                "MARTIAL": ["Battleaxe", "Warhammer"],
                "LANG": ["Common", "Dwarvish"]
            }
    },
    "Dragonborn": {
            "SPEED": 30,
            "VISION": 0,
            "TRAITS": [],
            "SKILL": [],
            "PROF": {
                "ARMOR": [],
                "TOOL": [],
                "SIMPLE": [],
                "MARTIAL": [],
                "LANG": ["Common", "Draconic"]
            }
    },
    "Halfling": {
            "SPEED": 25,
            "VISION": 0,
            "TRAITS": ["Lucky", "Brave", "Nimble"],
            "SKILL": ["Stealth"],
            "PROF": {
                "ARMOR": [],
                "TOOL": [],
                "SIMPLE": [],
                "MARTIAL": [],
                "LANG": ["Common", "Halfling"]
            }
    }
})


dsrace=Box({
    "Human": {
        "Standard": {
            "SPEED": 30,
            "VISION": 0,
            "TRAITS": [],
            "SKILL": [],
            "PROF": {
                "ARMOR": [],
                "TOOL": [],
                "SIMPLE": [],
                "MARTIAL": [],
                "LANG": []
            }
        },
        "Variant": {
            "SPEED": 30,
            "VISION": 0,
            "TRAITS": ["Feat"],
            "SKILL": [],
            "PROF": {
                "ARMOR": [],
                "TOOL": [],
                "SIMPLE": [],
                "MARTIAL": [],
                "LANG": []
            }
        },
    },
    "Elf": {
        "High": {
            "SPEED": 30,
            "VISION": 60,
            "TRAITS": ["Cantrip"],
            "SKILL": [],
            "PROF": {
                "ARMOR": [],
                "TOOL": [],
                "SIMPLE": ["Shortbow"],
                "MARTIAL": ["Longsword", "Shortsword", "Longbow"],
                "LANG": []
            }
        },
        "Wood": {
            "SPEED": 35,
            "VISION": 60,
            "TRAITS": ["Mask of the Wild"],
            "SKILL": ["Stealth"],
            "PROF": {
                "ARMOR": [],
                "TOOL": [],
                "SIMPLE": ["Shortbow"],
                "MARTIAL": ["Longsword", "Shortsword", "Longbow"],
                "LANG": []
            }
        },
        "Drow": {
            "SPEED": 30,
            "VISION": 120,
            "TRAITS": ["Sunlight Sensitivity", "Drow Magic"],
            "SKILL": [],
            "PROF": {
                "ARMOR": [],
                "TOOL": [],
                "SIMPLE": [],
                "MARTIAL": ["Rapier", "Shortsword", "Hand Crossbow"],
                "LANG": []
            }
        }
    },
    "Dwarf": {
        "Hill": {
            "SPEED": 30,
            "VISION": 60,
            "TRAITS": ["Dwarven Toughness"],
            "SKILL": [],
            "PROF": {
                "ARMOR": [],
                "TOOL": [],
                "SIMPLE": [],
                "MARTIAL": [],
                "LANG": []
            }
        },
        "Mountain": {
            "SPEED": 30,
            "VISION": 60,
            "TRAITS": [],
            "SKILL": [],
            "PROF": {
                "ARMOR": ["Light", "Medium"],
                "TOOL": [],
                "SIMPLE": [],
                "MARTIAL": [],
                "LANG": []
            }
        }
    },
    "Dragonborn": {
        "Black": {
            "SPEED": 30,
            "VISION": 0,
            "TRAITS": ["Draconic Ancestry Black", "Breath Weapon Acid"],
            "SKILL": [],
            "PROF": {
                "ARMOR": [],
                "TOOL": [],
                "SIMPLE": [],
                "MARTIAL": [],
                "LANG": []
            }
        },
        "Blue": {
            "SPEED": 30,
            "VISION": 0,
            "TRAITS": ["Draconic Ancestry Blue", "Breath Weapon Lightning"],
            "SKILL": [],
            "PROF": {
                "ARMOR": [],
                "TOOL": [],
                "SIMPLE": [],
                "MARTIAL": [],
                "LANG": []
            }
        },
        "Green": {
            "SPEED": 30,
            "VISION": 0,
            "TRAITS": ["Draconic Ancestry Green", "Breath Weapon Poison"],
            "SKILL": [],
            "PROF": {
                "ARMOR": [],
                "TOOL": [],
                "SIMPLE": [],
                "MARTIAL": [],
                "LANG": []
            }
        }
    },
    "Halfling": {
        "Lightfoot": {
            "SPEED": 25,
            "VISION": 0,
            "TRAITS": ["Naturally Stealthy"],
            "SKILL": [],
            "PROF": {
                "ARMOR": [],
                "TOOL": [],
                "SIMPLE": [],
                "MARTIAL": [],
                "LANG": []
            }
        },
        "Stout": {
            "SPEED": 25,
            "VISION": 0,
            "TRAITS": ["Stout Resilience"],
            "SKILL": [],
            "PROF": {
                "ARMOR": [],
                "TOOL": [],
                "SIMPLE": [],
                "MARTIAL": [],
                "LANG": []
            }
        }
    },
})