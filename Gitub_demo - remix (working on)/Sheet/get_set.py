# get_set.py

from access_data.color_reference import *
from colorist import *
import shared
from access_data.Grimoir import *


# Core values
def vLevel(): return shared.db.Core.L
def vPB(): return shared.db.Core.PB
def vRace(): return shared.db.Core.R.replace(" ", "")
def vSubrace(): return shared.db.Core.SR.replace(" ", "")
def vClass(): return shared.db.Core.C.replace(" ", "")
def vSubclass(): return shared.db.Core.SC.replace(" ", "")
def vBackground(): return shared.db.Core.BG.replace(" ", "")

# Core Setters
def set_Level(value):
    shared.db.Core.L = max(1, min(value, 20))
    shared.db.Core.PB = (shared.db.Core.L - 1) // 4 + 2

def set_Class(value): shared.db.Core.C = value
def set_Subclass(value): shared.db.Core.SC = value
def set_Race(value): shared.db.Core.R = value
def set_Subrace(value): shared.db.Core.SR = value
def set_Background(value): shared.db.Core.BG = value

# Core Data get
def dClass(): return shared.db.Class
def dRace(): return shared.db.Race
def dBackground(): return shared.db.Background

# Core Abil get
def aClass(): return shared.db.Class["Abil"]
def aRace(): return shared.db.Race["Abil"]

# Core Skill get
def sClass(): return shared.db.Class["Skill Select"]


def kMilestone(): return shared.db.Milestone
def kProf(): return shared.db.Prof
def kSkill(): return shared.db.Skill
def kAC(): return shared.db.AC
def kSpeed(): return shared.db.Speed
def kVision(): return shared.db.Vision
def kInitiative(): return shared.db.Initiative
def kHP(): return shared.db.HP
def kCondition(): return shared.db.Condition
def kAtr(): return shared.db.Atr
def kSavingthrow(): return shared.db.SavingThrow
def kSpell(): return shared.db.Spell
def kCharacteristic(): return shared.db.Characteristic
def kDescription(): return shared.db.Description
def kBackpack(): return shared.db.Inventory.Backpack
def kEquip(): return shared.db.Inventory.Equip



def pProf(): return shared.pc.Prof
def pSkill(): return shared.pc.Skill
def pSpeed(): return shared.pc.Speed
def pVision(): return shared.pc.Vision
def pInitiative(): return shared.pc.Initiative
def pAtr(): return shared.pc.Atr

def vMod(atr): return shared.db.Atr[atr]["Mod"]

def cMilestone(): return shared.pc.milestone_count

def dSpell(): return shared.pc.spell_data

def Current_Equip(slot): return kEquip()[slot]
def Current_Backpack(): return list(shared.db.Inventory.Backpack.keys())

def dBackpack(): return shared.db.Inventory.Backpack

def bMult_Category(*categories): return shared.pc.Bazaar.Mult_Category(*categories)

def bCategory(category): return shared.pc.Bazaar.Category(category)

def bSlot(slot): return shared.pc.Bazaar.Slot(slot)

def bProf(prof): return shared.pc.Bazaar.Prof(prof)

def bProperty(prop): return shared.pc.Bazaar.Property(prop)

def bItem(item): return shared.pc.Bazaar.Item(item)


def bOffHand(): return shared.pc.Bazaar.OffHand



def Initiative_text():
    mod = kInitiative()["Val"]
    return f"{'+' if mod >= 0 else '-'}{abs(mod)}"


# Spell bullshit
def cantrips_known(): return len(kSpell().Book[0])




def spells_known():
    cdata = kSpell().Book
    num = 0
    for i in [1, 2, 3, 4, 5, 6, 7, 8, 9]:
        num += len(cdata[i])
    return num


def spells_prepared():
    cdata = kSpell().Prepared
    num = 0
    for i in [1, 2, 3, 4, 5, 6, 7, 8, 9]:
        num += len(cdata[i])
    return num


def valid_class():
    class_exception_map = {1: ["Cleric", "Warlock"], 2: ["Wizard"]}
    return vLevel() >= 3 or vClass() in class_exception_map.get(vLevel(), [])

def valid_spellclass(): return vClass() in spellcast_L or vSubclass() in spellcast_L

def valid_s_spellclass(cat):
    if cat == "Class":
        return vClass() in spellcast_L
    elif cat == "Subclass":
        return vSubclass() in spellcast_L





def prof_color( cat, item): return c_item_true if item in pProf()[cat] else c_item_false


def condition_color( item): return c_item_true if kCondition()[item] else c_item_false


def skill_text( skill):
    mod = kSkill()[skill]["Mod"]
    return f"{'+' if mod >= 0 else '-'}{abs(mod)}"


def dc_val( atr):
    return 8 + kAtr()[atr]["Mod"] + vPB()


def input_rasi(sender, data, user_data):
    key = user_data[0]
    if key == "Clear":
        dRace().Rasi = ["", ""]
    else:
        dRace().Rasi[key] = data


def use_race(sender, data, user_data):
    key = user_data[0]
    index = user_data[1]
    aRace()[key]["Use"][index] = data


def use_race_spell(sender, data, user_data):
    key = user_data[0]
    spell = user_data[1]
    aRace()[key][spell]["Use"] = data


def select_race_spell(sender, data, user_data):
    key = user_data[0]
    aRace()[key]["Select"][0] = data


def input_base_atr(sender, data, user_data):
    key = user_data[0]
    kAtr()[key].Base = int(data)


def select_prof_background(sender, data, user_data):
    cat = user_data[0]
    index = user_data[1]
    
    if data != "Clear":
        dBackground()()["Prof"][cat]["Select"][index] = data
    else:
        for key in dBackground()()["Prof"]:
            plen = len(dBackground()()["Prof"][key]["Select"])
            dBackground()()["Prof"][key]["Select"] = [""] * plen


def select_prof_player(sender, data, user_data):
    idx = user_data[0]
    cat = idx
    if idx in ["Artisan", "Gaming", "Musical"]:
        cat = "Tool"

    item = user_data[1]
    prof_list = kProf()[cat]["Player"]
    


def clear_level_select_milestone(sender, data, user_data):
    index = user_data[0]
    if kMilestone()["Feat"][index]:
        prefeat = kMilestone()["Feat"][index]
        for key in list(kMilestone()["Data"].keys()):
            if prefeat == key:
                kMilestone()["Data"].pop(key)
                        
    kMilestone()["Select"][index] = ""
    kMilestone()["Feat"][index] = ""
    kMilestone()["Asi"][index] = ["", ""]


def select_level_milestone(sender, data, user_data):
    index = user_data[0]
    kMilestone()["Select"][index] = data
    
    kMilestone()["Feat"][index] = ""
    kMilestone()["Asi"][index] = ["", ""]


def select_feat_milestone(sender, data, user_data):
    index = user_data[0]
    if data not in kMilestone()["Feat"]:
        kMilestone()["Feat"][index] = data
    
        if data in Feat_Select_L:
            kMilestone()["Data"][data] = {"Select": [""]}
        elif data == "Weapon Master":
            kMilestone()["Data"][data] = {"Select": ["", "", "", ""]}
        else: 
            kMilestone()["Data"][data] = {}


def choice_feat_milestone(sender, data, user_data):
    feat = user_data[0]
    index = user_data[1]
    if data == "Clear":
        output = ""
    else:
        output = data
    
    if feat in list(kMilestone()["Data"].keys()):
        kMilestone()["Data"][feat]["Select"][index] = output


def use_feat_milestone(sender, data, user_data):
    feat = user_data[0]
    index = user_data[1]
    
    if feat in list(kMilestone()["Data"].keys()):
        kMilestone()["Data"][feat]["Use"][index] = data


def select_asi_milestone(sender, data, user_data):
    key = user_data[0]
    index = user_data[1]
    kMilestone()["Asi"][key][index] = data


def use_class(sender, data, user_data):
    key = user_data[0]
    index = user_data[1]
    aClass()[key]["Use"][index] = data


def select_skill_class(sender, data, user_data):
    cat = user_data[0]
    if cat != "Clear":
        sClass()[cat] = data
    else: 
        for idx, val in enumerate(sClass()):
            sClass()[idx] = ""


def select_class(sender, data, user_data):
    key = user_data[0]
    index = user_data[1]
    aClass()[key]["Select"][index] = data


def learn_spell(sender, data, user_data):
    spell = user_data[0]
    level = user_data[1]
    cspell = kSpell()["Book"]
    sdata = dSpell()
    if level == 0:
        max_known = sdata['cantrips_available']
        current_known = cantrips_known()
        if spell not in cspell[level]:  # add spell
            if current_known < max_known:
                cspell[level].append(spell)
        elif spell in cspell[level]:   # remove spell
            cspell[level].remove(spell)
    else:
        max_known = sdata['spells_available']
        current_known = spells_known()
        if spell not in cspell[level]:  # add spell
            if current_known < max_known:
                cspell[level].append(spell)
        elif spell in cspell[level]:   # remove spell
            cspell[level].remove(spell)


def prepare_spell(sender, data, user_data):
    spell = user_data[0]
    level = user_data[1]
    
    cspell = kSpell()["Prepared"]
    sdata = dSpell()

    max_prep = sdata['prepared_available']
    current_prep = spells_prepared()

    if spell not in cspell[level]:  # add spell
        if current_prep < max_prep:
            cspell[level].append(spell)
    elif spell in cspell[level]:   # remove spell
        cspell[level].remove(spell)


def cast_spell(sender, data, user_data):
    level = user_data[0]
    slots = kSpell()["Slot"][level]
    for i in range(len(slots)):
        if not slots[i]:
            slots[i] = True
            break


def long_rest(sender, data, user_data):
    if valid_spellclass():
        for level in [1, 2, 3, 4, 5, 6, 7, 8, 9]:
            kSpell()["Slot"][level] = [False] * len(kSpell()["Slot"][level])


def mod_health(sender, data, user_data):
    place, delta = user_data
    hp = kHP()
    
    if place == "Temp":
        if delta > 0 or hp["Temp"] > 0:
            hp["Temp"] += delta
            
    elif place == "HP":
        if delta < 0:
            if hp["Temp"] >= 1 and hp["Temp"] > 0:
                hp["Temp"] -= 1
            else:
                hp["Current"] -= 1
        else:
            hp["Current"] = min(hp["Current"] + 1, hp["Sum"])


def mod_hp_player(sender, data, user_data):
    kHP()["Player"] = int(data)


def mod_arcane_ward(sender, data, user_data):
    num = user_data[0]
    max_hp = aClass()["Arcane Ward"]["HP"]["Max"]
    current_hp = aClass()["Arcane Ward"]["HP"]["Current"]
    new_hp = current_hp + num
    new_hp = max(0, min(new_hp, max_hp))
    aClass()["Arcane Ward"]["HP"]["Current"] = new_hp


def select_player_condition(sender, data, user_data):
    index = user_data[0]
    kCondition()[index] = data


def input_characteristic(sender, data, user_data):
    name = user_data[0]
    kCharacteristic()[name] = data


def input_description(sender, data, user_data):
    name = user_data[0]
    kDescription()[name] = data


def add_item_bazaar(sender, data, user_data):
    backpack = kBackpack()
    cat = user_data[0]
    item = user_data[1]
    if item in kBackpack().keys():
        backpack[item][1] += 1
    else:
        backpack[item] = [cat, 1]


def mod_item_backpack(sender, data, user_data):
    item = user_data[0]
    delta = user_data[1]
    backpack = kBackpack()
    if delta == "Clear":
        backpack.pop(item, None)
        return 0
    if item not in backpack: backpack[item] = [None, delta]
    else: backpack[item][1] += delta
    if backpack[item][1] <= 0:
        backpack.pop(item, None)
        return 0
    return backpack[item][1]


def Equip_Item(sender, data, user_data):
    cat = user_data[0]
    equips = kEquip()
    backpack = dBackpack()

    print(f"cat {cat}")
    if data == "Empty":
        equips[cat] = ""
        return
    
    if data in bSlot("Weapon"):
        owned = backpack[data][1]
        if weapon_versatile():
            equips[cat] = data
            return
            

        elif cat == "Main Hand":
            if data in bProperty("Two-handed"): 
                equips[cat] = data
                equips["Off Hand"] = ""
                return
            if same_weapon():
                if owned > 1:
                    equips[cat] = data
                    return
                elif owned == 1:
                    equips[cat] = ""
                    return
            else: 
                equips[cat] = data
                return 

        elif cat == "Off Hand":
            if equips["Main Hand"] in bProperty("Two-handed"):return
            if same_weapon():
                if owned > 1:
                    equips[cat] = data
                    return
                elif owned == 1:
                    equips[cat] = ""
                    return
            else: 
                equips[cat] = data
                return 



    equips[cat] = data



def same_weapon():
    if Current_Equip("Main Hand") == Current_Equip("Off Hand"): return True
    else: return False
def weapon_versatile():
    main_hand = Current_Equip("Main Hand")
    off_hand = Current_Equip("Off Hand")

    if main_hand == off_hand:
        if main_hand in bProperty("Versatile"): return True
        else: return False
    else: return False



def get_Fighting_Style( Style):
    item_map = {
        "Archery": "You gain a +2 bonus to attack rolls you make with ranged weapons.",
        "Defense": "While you are wearing armor, you gain a +1 bonus to AC.",
        "Dueling": "When you are wielding a melee weapon in one hand and no other weapons, you gain a +2 bonus to damage rolls with that weapon.",
        "Great Weapon Fighting": "When you roll a 1 or 2 on a damage die for an attack you make with a melee weapon that you are wielding with two hands, you can reroll the die and must use the new roll. The weapon must have the two-handed or versatile property for you to gain this benefit.",
        "Protection": "When a creature you can see attacks a target other than you that is within 5 feet of you, you can use your reaction to impose disadvantage on the attack roll. You must be wielding a shield.",
        "Two Weapon Fighting": "When you engage in two-weapon fighting, you can add your ability modifier to the damage of the second attack.",
        "Blind Fighting": "You have blindsight with a range of 10 feet. Within that range, you can effectively see anything that isn't behind total cover.",
        "Interception": f"When a creature you can see hits a target, other than you, within 5 feet of you with an attack, you can use your reaction to reduce the damage the target takes by 1d10 + {vPB()}. You must be wielding a shield or a simple or martial weapon to use this reaction.",
        "Thrown Weapon Fighting": "You can draw a weapon that has the thrown property as part of the attack you make with the weapon. In addition, when you hit with a ranged attack using a thrown weapon, you gain a +2 bonus to the damage roll.",
        "Unarmed Fighting": f"Your unarmed strikes can deal bludgeoning damage equal to 1d6 + {vMod("STR")}. If you aren't wielding any weapons or a shield when you make the attack roll, the d6 becomes a d8. At the start of each of your turns, you can deal 1d4 bludgeoning damage to one creature grappled by you."
    }
    return item_map[Style]


def get_Maneuver( Maneuver):
    item_map = {
        "Ambush": "When you make a Stealth check or roll initiative, Use 1 SD and add too roll, Not available when incapacitated.",
        "Bait and Switch": "on turn, if withen 5 ft of a willing creature with more then 5t of movement, Use 1SD too switch places with the creature, this doesn't provoke OA, until the start of your next turn, you and the creature gains AC equal too roll.",
        "Brace": "When creature moves into melee reach, use reaction and 1 SD too make attack, add SD too damage.",
        "Commander's Strike": "Replace one attack with bonus action, ally you can see makes weapon attack and adds SD too damage.",
        "Commanding Presence": "Use 1 SD on Intimidation, Performance, or Persuasion checks, add too roll.",
        "Disarming Attack": "On hit, use 1 SD, add too damage, target makes STR save or drops item.",
        "Distracting Strike": "On hit, use 1 SD, add too damage, next ally attack has advantage.",
        "Evasive Footwork": "When moving, use 1 SD and add too AC until you stop.",
        "Feinting Attack": "Bonus action, use 1 SD too gain advantage on next attack, add SD too damage if hit.",
        "Goading Attack": "On hit, use 1 SD, add too damage, target makes WIS save or has disadvantage attacking others.",
        "Grappling Strike": "After melee hit, use 1 SD and bonus action too grapple, add SD too Athletics check.",
        "Lunging Attack": "Use 1 SD too increase melee reach by 5 ft, add too damage if hit.",
        "Maneuvering Attack": "On hit, use 1 SD, add too damage, ally moves half speed without provoking OA from target.",
        "Menacing Attack": "On hit, use 1 SD, add too damage, target makes WIS save or frightened until next turn.",
        "Parry": "When hit by melee attack, use reaction and 1 SD too reduce damage by roll + DEX mod.",
        "Precision Attack": "Use 1 SD too add too attack roll before or after rolling.",
        "Pushing Attack": "On hit, use 1 SD, add too damage, Large or smaller makes STR save or pushed 15 ft.",
        "Quick Toss": "Bonus action, use 1 SD too make thrown weapon attack, add too damage if hit.",
        "Rally": "Bonus action, use 1 SD, ally gains temp HP equal too roll + CHA mod.",
        "Riposte": "When enemy misses melee attack, use reaction and 1 SD too attack back, add too damage.",
        "Sweeping Attack": "On melee hit, use 1 SD, second creature within 5 ft takes SD damage if original roll hits.",
        "Tactical Assessment": "Use 1 SD on Investigation, History, or Insight checks, add too roll.",
        "Trip Attack": "On hit, use 1 SD, add too damage, Large or smaller makes STR save or knocked prone."
    }
    return item_map[Maneuver]

    

class sHand():
    def __init__(self, item):
        cdata = bItem(item)
        Tier = cdata.Tier
        
        self.Name = iName(item)
        self.Range = " : ".join(f"{v} ft" for v in (cdata.get("Reach"), cdata.get("Range")) if v)
        
        if item in bCategory("Melee"): Mod = vMod("STR")
        elif item in bCategory("Ranged"): Mod = vMod("DEX")
        elif item in bProperty("Finesse"): Mod = max(vMod("STR"), vMod("DEX"))
        else: Mod = 0
        
        hNum = Mod + vPB() if item in kProf()["Weapon"] else Mod
        self.hNum = hNum + Tier
        self.hSign = "+" if self.hNum >= 0 else "-"
        self.hColor = c_weapon_hit(self.hNum)
        
        if weapon_versatile(): self.dDice = cdata.vDamage
        else: self.dDice = cdata.Damage
        self.dNum = Mod + Tier
        self.dSign = "+" if self.dNum >= 0 else "-"
        self.dColor = c_weapon_dmg(self.dNum)
        self.dType = cdata.Type
        
        

        self.Prop = cdata.Prop
        
class s_item:
    def __init__(self, item_name):
        pass
    #     item_data = shared.items.get(item_name)
    #     self.Name = item_name
    #     for key, value in item_data.items():setattr(self, key, value)
    # def __repr__(self):return f"s_item({', '.join(f'{k}={repr(v)}' for k, v in self.__dict__.items())})"
    # def get(self, key, default=None):return getattr(self, key, default)
    
Rarity_nL = [0,1,2,3,4]
Rarity_L = ["Common", "Uncommon", "Rare", "Very Rare", "Legendary"]
def item_rarity(tier):
    return Rarity_L[tier]

def isName(item):
    return item.replace('_', ' ').replace('PPP1', '').replace('PPP2', '').replace('PPP3', '')

def iName(item):
    return item.replace('_', ' ').replace('PPP', ' + ')


def Lprof(parent, cat):
    return False #shared.pc[parent][cat] + kProf()[cat][parent]

# ANCHOR - DB Getters

def gCore(): return shared.db.Core


# ----------------
# SECTION - SET 
# ----------------


# ----------------
# SECTION - Resize
# ----------------


#     width = dpg.get_viewport_client_width()
#     height = dpg.get_viewport_client_height()
#     dpg.set_item_width("main_window", width)
#     dpg.set_item_height("main_window", height)
#     dpg.set_item_width("button1", int(width * 0.3))
#     dpg.set_item_height("button1", int(height * 0.05))


#-----------------------------------------------------------
#ANCHOR - BOOK
Race_Options = {
    "Empty": ["Empty"],
    "Human": ["Standard", "Variant"],
    "Elf": ["High", "Drow", "Wood", "Shadar Kai"],
    "Dwarf": ["Hill", "Mountain"],
    "Halfling": ["Lightfoot", "Stout"],
    "Gnome": ["Forest", "Rock"],
    "Dragonborn": ["Black", "Blue", "Brass", "Bronze", "Copper", "Gold","Green","Red","Silver","White"],
    "Half Orc": ["Standard"],
    "Tiefling": ["Asmodeus","Baalzebul", "Dispater", "Fierna", "Glasya", "Levistus", "Mammon", "Mephistopheles", "Zariel"],
    "Harengon": ["Standard"]
}

Class_Options = {
    "Empty": ["Empty"],
    "Fighter": ["Champion", "Battle Master", "Eldrich Knight", "Samuri"],
    "Wizard": ["Abjuration", "Conjuration",] # "Enchantment", "Evocation", "Illusion", "Necromancy" 
}

Race_L = list(Race_Options.keys())
Class_L = list(Class_Options.keys())
Background_L = ["Empty", "Charlatan","Criminal","Entertainer","Folk Hero","Guild Artisan","Hermit","Noble","Outlander","Sage","Sailor","Soldier","Urchin"]
spellcast_L = ["Wizard", "Eldrich Knight"]


Feat_L = ["Actor", "Alert", "Athlete", "Charger", "Crossbow Expert", "Defensive Duelist", "Dual Wielder", "Dungeon Delver", "Durable", "Elemental Adept", "Grappler", "Great Weapon Master", "Healer", "Heavily Armored", "Heavy Armor Master", "Inspiring Leader", "Keen Mind", "Lightly Armored", "Lucky", "Mage Slayer", "Martial Adept", "Medium Armor Master", "Mobile", "Moderately Armored", "Mounted Combatant", "Polearm Master", "Resilient", "Savage Attacker", "Sentinel", "Sharpshooter", "Shield Master", "Skulker", "Tavern Brawler", "Tough", "War Caster", "Weapon Master"]
Feat_Select_L = ["Moderately Armored","Lightly Armored","Elemental Adept","Athlete"]

Prof_L = ["Armor","Weapon","Tool","Lang"]



Level_L = [i for i in range(1, 21)]
Base_Atr_L = [i for i in range(1,19)]

Atr_L = ["STR", "DEX", "CON", "INT", "WIS", "CHA"]

Description_L = ["Gender", "Almnt", "Faith", "Size", "Age", "Hair", "Skin", "Eyes", "Height", "Weight"]

ideals_L = ["Traits", "Ideals", "Bonds", "Flaws"]
Condition_L = ["Blinded", "Charmed", "Deafened", "Frightened", "Grappled", "Incapacitated", "Invisible", "Paralyzed", "Petrified", "Poisoned", "Prone", "Restrained", "Stunned", "Unconscious", "Exhaustion"]


Spell_Desc_L = ["Level","Casting Time", "Duration", "School", "Ritual","Range","Components","Desc", "At Higher Levels"]


#-------
## LINK - #! Spells
#-------

def spell_not_cantrip(spell_name):
    return Grimoir[spell_name]["Level"] != 0


def get_spell_list(Class, level):
    return [spell for spell, v in Grimoir.items() if v['Level'] == level and Class in v['List']]


#-------
## LINK - #! Class based shit
#-------



spell_default = {
    "Slot": [[],[],[],[],[],[],[],[],[],[]],
    "Book": [[],[],[],[],[],[],[],[],[],[]],
    "Prepared": [[],[],[],[],[],[],[],[],[],[]]
}


spell_data_default = {
    "Caster": "",
    "max_spell_level": [0,0,0,0,0,0,0,0,0,0],
    "cantrips_available": 0,
    "spells_available": 0,
    "slots": [[],[],[],[],[],[],[],[],[],[]],
    "abil": "",
    "mod": 0,
    "atk": "",
    "prepared_available": 0
    
}

dict_Feat_Count = {
    'Fighter': [0, 0, 0, 0, 1, 1, 2, 2, 3, 3, 3, 3, 4, 4, 5, 5, 6, 6, 6, 7, 7],
    'Rogue': [0, 0, 0, 0, 1, 1, 1, 1, 2, 2, 3, 3, 4, 4, 4, 4, 5, 5, 5, 6, 6],
    'Wizard': [0, 0, 0, 0, 1, 1, 1, 1, 2, 2, 2, 2, 3, 3, 3, 3, 4, 4, 4, 5, 5],
    'Ranger': [0, 0, 0, 0, 1, 1, 1, 1, 2, 2, 2, 2, 3, 3, 3, 3, 4, 4, 4, 5, 5],
    'Paladin': [0, 0, 0, 0, 1, 1, 1, 1, 2, 2, 2, 2, 3, 3, 3, 3, 4, 4, 4, 5, 5]
}



#ANCHOR - Speed Dict
dict_Skill = {
    "Acrobatics": {"Atr": "DEX", "Desc": "Balance, flips, and avoiding being knocked down."},
    "Animal Handling": {"Atr": "WIS", "Desc": "Control and calm animals or read their behavior."},
    "Arcana": {"Atr": "INT", "Desc": "Knowledge of magic, spells, and magical traditions."},
    "Athletics": {"Atr": "STR", "Desc": "Climbing, jumping, swimming, and grappling."},
    "Deception": {"Atr": "CHA", "Desc": "Lying, bluffing, and misleading others."},
    "History": {"Atr": "INT", "Desc": "Recall historical facts, people, and events."},
    "Insight": {"Atr": "WIS", "Desc": "Detecting lies, motives, and emotions."},
    "Intimidation": {"Atr": "CHA", "Desc": "Threatening or coercing others into compliance."},
    "Investigation": {"Atr": "INT", "Desc": "Finding hidden clues or analyzing scenes."},
    "Medicine": {"Atr": "WIS", "Desc": "Stabilize the dying and diagnose illnesses."},
    "Nature": {"Atr": "INT", "Desc": "Knowledge of plants, animals, and the environment."},
    "Perception": {"Atr": "WIS", "Desc": "Noticing hidden things or sudden changes."},
    "Performance": {"Atr": "CHA", "Desc": "Acting, singing, dancing, and entertaining."},
    "Persuasion": {"Atr": "CHA", "Desc": "Convincing others with logic or charm."},
    "Religion": {"Atr": "INT", "Desc": "Understanding deities, rites, and dogma."},
    "Sleight of Hand": {"Atr": "DEX", "Desc": "Pickpocketing or manipulating objects subtly."},
    "Stealth": {"Atr": "DEX", "Desc": "Sneaking, hiding, and moving silently."},
    "Survival": {"Atr": "WIS", "Desc": "Tracking, finding food, and navigating the wild."}
}



#SECTION - Prof Tool
dict_Tool = {
    "Alchemist": {"Tag": "Job"}, "Brewer": {"Tag": "Job"}, "Calligrapher": {"Tag": "Job"}, "Carpenter": {"Tag": "Job"}, "Cartographer": {"Tag": "Job"}, "Cobbler": {"Tag": "Job"}, "Cook": {"Tag": "Job"}, "Glassblower": {"Tag": "Job"}, "Jeweler": {"Tag": "Job"}, "Leatherworker": {"Tag": "Job"}, "Mason": {"Tag": "Job"}, "Painter": {"Tag": "Job"}, "Potter": {"Tag": "Job"}, "Smith": {"Tag": "Job"}, "Tinker": {"Tag": "Job"}, "Weaver": {"Tag": "Job"}, "Thief": {"Tag": "Job"}, "Woodworker": {"Tag": "Job"}, "Navigator": {"Tag": "Job"}, "Disguise": {"Tag": "Job"}, "Forgery": {"Tag": "Job"},
    "Dice": {"Tag": "Game"}, "Dragonchess": {"Tag": "Game"}, "Cards": {"Tag": "Game"}, "Three-Dragon Ante": {"Tag": "Game"},
    "Bagpipes": {"Tag": "Music"}, "Drum": {"Tag": "Music"}, "Dulcimer": {"Tag": "Music"}, "Flute": {"Tag": "Music"}, "Lute": {"Tag": "Music"}, "Lyre": {"Tag": "Music"}, "Horn": {"Tag": "Music"}, "Pan Flute": {"Tag": "Music"}, "Shawm": {"Tag": "Music"}, "Viol": {"Tag": "Music"}
}

dict_Lang = {
    "Common": {},
    "Dwarvish": {},
    "Elvish": {},
    "Giant": {},
    "Gnomish": {},
    "Goblin": {},
    "Halfling": {},
    "Orc": {},
    "Abyssal": {},
    "Celestial": {},
    "Draconic": {},
    "Deep Speech": {},
    "Infernal": {},
    "Primordial": {},
    "Sylvan": {},
    "Undercommon": {}
}



#!SECTION Data List
Armor_L = ["Light","Medium","Heavy","Shield"]

Job_L = [k for k, v in dict_Tool.items() if v["Tag"] == "Job"]
Game_L = [k for k, v in dict_Tool.items() if v["Tag"] == "Game"]
Music_L = [k for k, v in dict_Tool.items() if v["Tag"] == "Music"]
Lang_L = list(dict_Lang.keys())
Skill_L = list(dict_Skill.keys())


Vision_L = ["Dark", "Blind","Tremor","Tru"]
Speed_L = ["Walk","Climb","Swim","Fly", "Burrow"]

dl = {
    "Cantrip": [spell for spell, v in Grimoir.items() if v['Level'] == 0 and 'Wizard' in v['List']],
    
    # Class Skills
    "Empty Skills": [],
    "Fighter Skills": ["Acrobatics", "Animal Handling", "Athletics", "History", "Insight", "Intimidation", "Perception", "Survival"],
    "Wizard Skills":  ["Arcana", "History", "Insight", "Investigation", "Medicine", "Religion"],
    
    # Feats
    
    "Athlete": ["STR", "DEX"],
    "Lightly Armored": ["STR","DEX"],
    "Moderately Armored": ["STR", "DEX"],
    "Elemental Adept": ["Acid", "Cold", "Fire", "Lightning", "Thunder"],
    "Resiliant": Atr_L,
    "Weapon Master": [], #s_cat("Simple"),
    
    
    
    # Backgrounds
    "Empty": {},
    "Acolyte": {"Lang": Lang_L},
    "Charlatan": {},
    "Criminal": {"Game": Game_L},
    "Entertainer": {"Music": Music_L},
    "FolkHero": {"Job": Job_L},
    "GuildArtisan": {"Job": Job_L, "Lang": Lang_L},
    "Hermit": {"Lang": Lang_L},
    "Noble": {"Game": Game_L, "Lang": Lang_L},
    "Outlander": {"Music": Music_L, "Lang": Lang_L},
    "Sage": {"Lang": Lang_L},
    "Sailor": {},
    "Soldier": {"Game": Game_L},
    "Urchin": {},

    "Fighting Styles": ["Archery", "Defense", "Great Weapon Fighting", "Protection", "Two Weapon Fighting", "Blind Fighting", "Interception", "Thrown Weapon Fighting", "Unarmed Fighting"],
    "Maneuvers": ["Ambush", "Bait and Switch", "Brace", "Commander's Strike", "Commanding Presence", "Disarming Attack", "Distracting Strike", "Evasive Footwork", "Feinting Attack", "Goading Attack", "Grappling Strike", "Lunging Attack", "Maneuvering Attack", "Menacing Attack", "Parry", "Precision Attack", "Pushing Attack", "Quick Toss", "Rally", "Riposte", "Sweeping Attack", "Tactical Assessment", "Trip Attack"],
    "Student of War": {"Job": Job_L}
}

coin_L = ["CP", "SP", "GP", "PP"]
weapon_atr_list = ["Name", "Range", "Hit", "Damage", "Type", "Notes"]
equipment_type_L = ["Weapon", "Armor","Wand", "Staff", "Rod", "Potion", "Scroll", "Ring", "Wonderous", "Other"]
Fighter_Second_Wind_Use = [0,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1]
Fighter_Action_Surge_Use = [0,0,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,2,2,2,2]
Fighter_Indomitable_Use = [0,0,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,2,2,2,2]

Fighter_Combat_Superiority_Use = [0,0,0,4,4,4,4,5,5,5,5,5,5,5,5,6,6,6,6,6,6]
Fighter_Combat_Superiority_Select = [0,0,0,3,3,3,3,5,5,5,7,7,7,7,7,9,9,9,9,9,9]



max_spell_Level = {
    "Wizard": [0,1,1,1,2,2,3,3,4,4,5,5,6,6,7,7,8,8,9,9,9], 
    "Eldrich Knight": [0,0,0,1,1,1,1,2,2,2,2,2,2,3,3,3,3,3,3,4,4]
}
cantrips_available = {
    "Wizard": [0,3,3,3,4,4,4,4,4,4,5,5,5,5,5,5,5,5,5,5,5],
    "Eldrich Knight": [0,0,0,2,2,2,2,2,2,2,3,3,3,3,3,3,3,3,3,3,3]
}

spells_available = {
    "Wizard": [],
    "Eldrich Knight": [0,0,0,3,4,4,4,5,6,6,7,8,8,9,10,10,11,11,11,12,13]
}

casting_abil = {
    "Wizard": "INT",
    "Eldrich Knight": "INT"
}

casting_class = {
    "Wizard": "Wizard",
    "Eldrich Knight": "Wizard"
}
spell_slots = {
    "Wizard": [[0, 0, 0, 0, 0, 0, 0, 0, 0, 0],[0, 2, 0, 0, 0, 0, 0, 0, 0, 0],[0, 3, 0, 0, 0, 0, 0, 0, 0, 0],[0, 4, 2, 0, 0, 0, 0, 0, 0, 0],[0, 4, 3, 0, 0, 0, 0, 0, 0, 0],[0, 4, 3, 2, 0, 0, 0, 0, 0, 0],[0, 4, 3, 3, 0, 0, 0, 0, 0, 0],[0, 4, 3, 3, 1, 0, 0, 0, 0, 0],[0, 4, 3, 3, 2, 0, 0, 0, 0, 0],[0, 4, 3, 3, 3, 1, 0, 0, 0, 0],[0, 4, 3, 3, 3, 2, 0, 0, 0, 0],[0, 4, 3, 3, 3, 2, 1, 0, 0, 0],[0, 4, 3, 3, 3, 2, 1, 0, 0, 0],[0, 4, 3, 3, 3, 2, 1, 1, 0, 0],[0, 4, 3, 3, 3, 2, 1, 1, 0, 0],[0, 4, 3, 3, 3, 2, 1, 1, 1, 0],[0, 4, 3, 3, 3, 2, 1, 1, 1, 0],[0, 4, 3, 3, 3, 2, 1, 1, 1, 1],[0, 4, 3, 3, 3, 3, 1, 1, 1, 1],[0, 4, 3, 3, 3, 3, 2, 1, 1, 1],[0, 4, 3, 3, 3, 3, 2, 2, 1, 1]],
    "Eldrich Knight": [[0,0,0,0,0],[0,0,0,0,0],[0,0,0,0,0],[0,2,0,0,0],[0,3,0,0,0],[0,3,0,0,0],[0,3,0,0,0],[0,4,2,0,0],[0,4,2,0,0],[0,4,2,0,0],[0,4,3,0,0],[0,4,3,0,0],[0,4,3,0,0],[0,4,3,2,0],[0,4,3,2,0],[0,4,3,2,0],[0,4,3,3,0],[0,4,3,3,0],[0,4,3,3,0],[0,4,3,3,1],[0,4,3,3,1]]
}


inventory_equip_L = ["Face","Throat","Body","Hands","Waist","Feet","Armor","Main Hand","Off Hand","Ring 1","Ring 2"]

weapon_prop_d = {
    "Ammunition": "Requires ammo. One ammo used per attack. Half recoverable after battle.",
    "Finesse": "Use either Strength or Dexterity modifier for attack and damage.",
    "Heavy": "Small creatures have disadvantage due to weapon size.",
    "Light": "Small and easy to handle.",
    "Loading": "Can only fire one shot per action or reaction.",
    "Range": "Has normal and long range. Attacks beyond normal range have disadvantage.",
    "Reach": "Extends melee attack range by 5 feet.",
    "Thrown": "Can be thrown. Uses melee attack modifier.",
    "Two-handed": "Requires two hands to use.",
    "Versatile": "Can be used one or two handed. Damage increases when used with two hands."
}

weapon_prop_sc = {
    "Ammunition": "AMM",
    "Finesse": "FIN",
    "Heavy": "HVY",
    "Light": "LGT",
    "Loading": "LDG",
    "Range": "RNG",
    "Reach": "REH",
    "Thrown": "TRN",
    "Two-handed": "THD",
    "Versatile": "VSL"
}

weapon_dtype_d = {
    "Piercing": "Puncturing and penetrating.",
    "Slashing": "Cutting and severing.",
    "Bludgeoning": "Blunt impact and concussive force."
}


