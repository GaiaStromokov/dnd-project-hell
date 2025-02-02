from box import Box
dfeat= Box({
    "Alert": {
        "Type": "Passive",
        "Desc": "you can't be surprised, and creatures you don't see don't gain advantage on attack roll against you.",
        "Data": {
            "init": 5
        }    
    }, 
    "Athlete": {
        "Type": "Passive",
        "Desc": "you stand up and climb more quickly, and you can jump with only a 5-ft run.",
        "Data": {
            "ATR": {
                "choice": ["STR","DEX"]
            }
        }
    }, 
    "Actor": {
        "Type": "Passive",
        "Desc": "",
        "Data": {
            "ATR": {
                "stat": "CHA"
            },
            "SKILL": ["Deception","Performance"]
        }
    }, 
    "Charger": {
        "Type": "Action",
        "Desc": "As part of the Dash action you can make a melee attack with a +5 bonus if you move at least 10 ft before.",
        "Data": {}
    }, 
    "Crossbow Expert": {
        "Type": "Passive",
        "Desc": "You ignore the loading property of crossbows and don't have disadvantage for being in contact with a creature when you shoot.",
        "Data": {}
    }
})