from config.gen_import import *



dcabil = Box({
    "Fighter":{
        "ABIL": {
            "Fighting Style":{
                "DATA": {
                    "ACCESS": 1, 
                    "UPG": [],
                    "ACTIVE": False
                },
                "C1": "",
                "DESC": "You adopt a particular style of fighting as your specialty"
                
            }, 
            "Second Wind":{
                "DATA": {
                    "ACCESS": 1,
                    "UPG": [],
                    "ACTIVE": False
                },
                "DESC": "You have a limited well of stamina that you can draw on to protect yourself from harm."
            }, 
            "Action Surge":{
                "DATA": {
                    "ACCESS": 2,
                    "UPG": {17:2},
                    "ACTIVE": False
                },
                "DESC": "you can push yourself beyond your normal limits for a moment."
            }, 
            "Extra Attack":{
                "DATA": {
                    "ACCESS": 5,
                    "UPG": {11:2},
                    "ACTIVE": False
                },
                "DESC": "you can attack again, whenever you take the Attack action on your turn.",
                "NUM": 1
            }, 
            "Indomitable":{
                "DATA": {
                    "ACCESS": 9,
                    "UPG": {13:2,17:3}
                    
                },
                "PUBLIC": {
                    "ACTIVE": False,
                    "DESC": "you can reroll a saving throw that you fail.",
                    "USE": {"M":1,"V":1}
                }
            }
        },
    },
    
    "Rogue":{
        "ABIL": {}
    },
    "Cleric":{
        "ABIL": {}
    },
    "Wizard":{
        "ABIL": {}
    }
})


dscabil = Box({})