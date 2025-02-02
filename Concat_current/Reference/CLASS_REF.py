from box import Box
dclass= Box({
    "Fighter": {
        "HD": 10,
        "SKILLL": ["Acrobatics", "Animal Handling", "Athletics", "History", "Insight", "Intimidation", "Perception", "Survival"],
        "SAVE": ["STR", "CON"],
        "PROF": {
            "ARMOR": ["ALL"],
            "TOOL": [],
            "SIMPLE": ["ALL"],
            "MARTIAL": ["ALL"],
            "LANG": []
        },
        "ABIL": ["Fighting Style", "Second Wind", "Action Surge", "Extra Attack", "Indomitable" ],
        "ASI": [4,6,8,12,14,16,19]
    },
    "Rogue": {
        "HD": 8,
        "SKILLL": ["Acrobatics", "Athletics", "Deception", "Insight", "Intimidation", "Investigation", "Perception", "Performance", "Persuasion", "Sleight of Hand", "Stealth"],
        "SAVE": ["DEX", "INT"],
        "PROF": {
            "ARMOR": ["Light"],
            "TOOL": ["Thief"],
            "SIMPLE": ["ALL"],
            "MARTIAL": ["Hand Crossbow", "Longsword", "Rapier", "Shortsword"],
            "LANG": []
        },
        "ABIL": {},
        "ASI": [4,8,10,12,16,19]
    },
    "Cleric": {
        "HD": 8,
        "SKILLL": ["History", "Insight", "Medicine", "Persuasion", "Religion"],
        "SAVE": ["WIS", "CHA"],
        "PROF": {
            "ARMOR": ["Light", "Medium", "Shield"],
            "TOOL": [],
            "SIMPLE": ["ALL"],
            "MARTIAL": [],
            "LANG": []
        },
        "ABIL": {},
        "ASI": [4,8,12,16,19]
    },
    "Wizard": {
        "HD": 6,
            "SKILLL": ["Arcana", "History", "Insight", "Investigation", "Medicine", "Religion"],
            "SAVE": ["INT", "WIS"],
            "PROF": {
                "ARMOR": [],
                "TOOL": [],
                "SIMPLE": ["Dagger", "Dart", "Sling", "Quarterstaff", "Light Crossbow"],
                "MARTIAL": [],
                "LANG": []
            },
            "ABIL": {},
            "ASI": [4,8,12,16,19]
    }
})