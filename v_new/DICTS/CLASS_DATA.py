from config.gen_import import *

dclass= Box({
    "Fighter": {
        "HD": 10,
        "SKILL_LIST": ["Acrobatics", "Animal Handling", "Athletics", "History", "Insight", "Intimidation", "Perception", "Survival"],
        "SAVES": ["STR", "CON"],
        "PROF": {
            "ARMOR": ["ALL"],
            "TOOL": [],
            "SIMPLE": ["ALL"],
            "MARTIAL": ["ALL"],
            "LANG": []
        }
    },
    "Rogue": {
        "HD": 8,
        "SKILL_LIST": ["Acrobatics", "Athletics", "Deception", "Insight", "Intimidation", "Investigation", "Perception", "Performance", "Persuasion", "Sleight of Hand", "Stealth"],
        "SAVES": ["DEX", "INT"],
        "PROF": {
            "ARMOR": ["Light"],
            "TOOL": ["Thief"],
            "SIMPLE": ["ALL"],
            "MARTIAL": ["Hand Crossbow", "Longsword", "Rapier", "Shortsword"],
            "LANG": []
        }
    },
    "Cleric": {
        "HD": 8,
        "SKILL_LIST": ["History", "Insight", "Medicine", "Persuasion", "Religion"],
        "SAVES": ["WIS", "CHA"],
        "PROF": {
            "ARMOR": ["Light", "Medium", "Shields"],
            "TOOL": [],
            "SIMPLE": ["ALL"],
            "MARTIAL": [],
            "LANG": []
        }
    },
    "Wizard": {
        "HD": 6,
            "SKILL_LIST": ["Arcana", "History", "Insight", "Investigation", "Medicine", "Religion"],
            "SAVES": ["INT", "WIS"],
            "PROF": {
                "ARMOR": [],
                "TOOL": [],
                "SIMPLE": ["Dagger", "Dart", "Sling", "Quarterstaff", "Light Crossbow"],
                "MARTIAL": [],
                "LANG": []
            }
    }
})