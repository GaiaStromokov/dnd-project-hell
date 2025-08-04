import shared
from Sheet.get_set import *


def Fgen(name): aRace().setdefault(name, {})

    
def Fuse_1(name, num):
    aRace().setdefault(name, {})
    past = aRace().get(name, {}).get("Use", [False])
    aRace()[name] = {"Use": (past + [False] * num)[:num]}

def Fuse_2(index, name, num):
    aRace()[index].setdefault(name, {})
    past = aRace().get(index, {}).get(name, {}).get("Use", [False])
    aRace()[index][name] = {"Use": (past + [False] * num)[:num]}
    
    
def fSelect_1(name, num):
    aRace().setdefault(name, {})
    past = aRace().get(name, {}).get("Select", [])
    aRace()[name]["Select"] = (past + [""] * num)[:num]



class bRace():
    def __init__(self):
        self.Speed = {"Walk": 0, "Climb": 0, "Swim": 0, "Fly": 0, "Burrow": 0}
        self.Vision = {"Dark": 0, "Blind": 0, "Tremor": 0, "Tru": 0}
        self.Skill = []
        self.Weapon = []
        self.Armor = []
        self.Tool = []
        self.Lang = []
        self.Initiative = 0
        self.HP = 0
        self.SavingThrow = []
        
        if vRace(): self.cRace = globals()[vRace()](self)
        if vSubrace(): self.cSubrace = globals()[f"{vRace()}_{vSubrace()}"](self)
    
    def pre_Upd(self):
        self.cRace.pre_Upd()
        if vSubrace(): self.cSubrace.pre_Upd()
        
    def Upd(self):
        self.cRace.Upd()
        if vSubrace(): self.cSubrace.Upd()

    def __repr__(self):
        return str(self.__dict__)



class Empty():
    def __init__(self, p):
        self.p = p
        self.p.Speed["Walk"] = 30
    
    def pre_Upd(self):
        pass
    
    def Upd(self):
        pass
        
class Human():
    def __init__(self, p):
        self.p = p
        self.p.Lang.extend(["Common"])



    def pre_Upd(self):
        pass
    
    def Upd(self):
        pass

class Human_Standard():
    def __init__(self, p):
        self.p = p
        self.p.Speed["Walk"] = 30

    def pre_Upd(self):
        pass
    
    def Upd(self):
        pass

class Human_Variant():
    def __init__(self, p):
        self.p = p
        pass

    def pre_Upd(self):
        pass
    
    def Upd(self):
        pass

class Elf():
    def __init__(self, p):
        self.p = p
        
        self.p.Vision["Dark"] = 60
        self.p.Speed["Walk"] = 30
        self.p.Skill.extend(["Perception"])
        self.p.Lang.extend( ["Common", "Elvish"])


    def pre_Upd(self):
        pass
    
    def Upd(self):
        pass

class Elf_High():
    def __init__(self, p):
        self.p = p
        self.p.Weapon.extend(["Longsword", "Shortsword", "Shortbow", "Longbow"])

    def pre_Upd(self):
        pass
    
    def Upd(self):
        fSelect_1("Cantrip", 1)

class Elf_Wood():
    def __init__(self, p):
        self.p = p
        self.p.Speed["Walk"] = 35
        self.p.Weapon.extend(["Shortbow", "Longsword", "Shortsword", "Longbow"]) 

    def pre_Upd(self):
        pass
    
    def Upd(self):
        pass

class Elf_Drow():
    def __init__(self, p):
        self.p = p
        self.p.Vision["Dark"] = 120
        self.p.Weapon.extend(["Rapier", "Shortsword", "Hand Crossbow"])

    def pre_Upd(self):
        pass
    
    def Upd(self):
        level = vLevel()
        Fgen("Drow Magic")
        if level >= 1: Fuse_2("Drow Magic", "Dancing Lights", 1)
        if level >= 3: Fuse_2("Drow Magic", "Faerie Fire", 1)


class Elf_ShadarKai():
    def __init__(self, p):
        self.p = p

    def pre_Upd(self):
        pass
    
    def Upd(self): 
        Fuse_1("Blessing of the Raven Queen", vPB())

class Dwarf():
    def __init__(self, p):
        self.p = p
        self.p.Vision["Dark"] = 60
        self.p.Speed["Walk"] = 30
        self.p.Weapon.extend(["Battleaxe", "Handaxe", "Light Hammer", "Warhammer"])
        self.p.Lang.extend(["Common", "Dwarvish"])


    def pre_Upd(self):
        pass
    
    def Upd(self):
        pass

class Dwarf_Hill():
    def __init__(self, p):
        self.p = p

    def pre_Upd(self):
        pass
    
    def Upd(self): 
        self.p.HP = vLevel()

class Dwarf_Mountain():
    def __init__(self, p):
        self.p = p
        self.p.Armor.extend(["Light", "Medium"])

    def pre_Upd(self):
        pass
    
    def Upd(self):
        pass

class Halfling():
    def __init__(self, p):
        self.p = p
        self.p.Speed["Walk"] = 25
        self.p.Skill.extend(["Stealth"])
        self.p.Lang.extend(["Common", "Halfling"])

    def pre_Upd(self):
        pass
    
    def Upd(self):
        pass

class Halfling_Lightfoot():
    def __init__(self, p):
        self.p = p
        
    def pre_Upd(self):
        pass
    
    def Upd(self):
        pass

class Halfling_Stout():
    def __init__(self, p):
        self.p = p

    def pre_Upd(self):
        pass
    
    def Upd(self):
        pass

class Gnome():
    def __init__(self, p):
        self.p = p
        self.p.Speed["Walk"] = 25
        self.p.Vision["Dark"] = 60
        self.p.Lang.extend(["Common", "Gnomish"])

    def pre_Upd(self):
        pass
    
    def Upd(self):
        pass

class Gnome_Forest():
    def __init__(self, p):
        self.p = p

    def pre_Upd(self):
        pass
    
    def Upd(self):
        pass

class Gnome_Rock():
    def __init__(self, p):
        self.p = p
        self.p.Tool.extend("Tinker")

    def pre_Upd(self):
        pass
    
    def Upd(self):
        pass

class Dragonborn():
    def __init__(self, p):
        self.p = p
        self.p.Speed["Walk"] = 30
        self.p.Lang.extend(["Common", "Draconic"])

    def pre_Upd(self):
        pass
    
    def Upd(self):
        pass

class Dragonborn_Black():
    def __init__(self, p):
        self.p = p

    def pre_Upd(self):
        pass
    
    def Upd(self):
        Fuse_1("Breath Weapon", 1)

class Dragonborn_Blue():
    def __init__(self, p):
        self.p = p

    def pre_Upd(self):
        pass
    
    def Upd(self):
        Fuse_1("Breath Weapon", 1)

class Dragonborn_Brass():
    def __init__(self, p):
        self.p = p
        Fuse_1("Breath Weapon", 1)

class Dragonborn_Bronze():
    def __init__(self, p):
        self.p = p

    def Select(self):
        Fuse_1("Breath Weapon", 1)

class Dragonborn_Copper():
    def __init__(self, p):
        self.p = p

    def Select(self):
        Fuse_1("Breath Weapon", 1)

class Dragonborn_Gold():
    def __init__(self, p):
        self.p = p
        
        Fuse_1("Breath Weapon", 1)

class Dragonborn_Green():
    def __init__(self, p):
        self.p = p

    def Select(self):
        Fuse_1("Breath Weapon", 1)

class Dragonborn_Red():
    def __init__(self, p):
        self.p = p

    def Select(self):
        Fuse_1("Breath Weapon", 1)

class Dragonborn_Silver():
    def __init__(self, p):
        self.p = p

    def Select(self):
        Fuse_1("Breath Weapon", 1)

class Dragonborn_White():
    def __init__(self, p):
        self.p = p

    def Select(self):
        Fuse_1("Breath Weapon", 1)

class HalfOrc():
    def __init__(self, p):
        self.p = p
        self.p.Vision["Dark"] = 60
        self.p.Speed["Walk"] = 30
        self.p.Skill.extend(["Intimidation"])
        self.p.Lang.extend(["Common", "Orc"])
        



    def pre_Upd(self):
        pass
    
    def Upd(self):
        Fgen("Relentless Endurance")
        Fuse_1("Relentless Endurance", 1)
        Fgen("Savage Attacks")

class HalfOrc_Standard():
    def __init__(self, p):
        self.p = p

    def pre_Upd(self):
        pass
    
    def Upd(self):
        pass

class Tiefling():
    def __init__(self, p):
        self.p = p
        self.p.Vision["Dark"] = 60
        self.p.Speed["Walk"] = 30
        self.p.Lang.extend(["Common", "Infernal"]) 


    def pre_Upd(self):
        pass
    
    def Upd(self):
        pass

class Tiefling_Asmodeus():
    def __init__(self, p):
        self.p = p

    def pre_Upd(self):
        pass
    
    def Upd(self):
        Fgen("Infernal Legacy")
        level = vLevel()
        if level >= 1: Fuse_2("Infernal Legacy", "Thaumaturgy", 1)
        if level >= 3: Fuse_2("Infernal Legacy", "Hellish Rebuke", 1)
        if level >= 5: Fuse_2("Infernal Legacy", "Darkness", 1)

class Tiefling_Baalzebul():
    def __init__(self, p):
        self.p = p


    def pre_Upd(self):
        pass
    
    def Upd(self):
        Fgen("Legacy of Maladomini")
        level = vLevel()
        if level >= 1: Fuse_2("Legacy of Maladomini", "Thaumaturgy", 1)
        if level >= 3: Fuse_2("Legacy of Maladomini", "Ray of Sickness", 1)
        if level >= 5: Fuse_2("Legacy of Maladomini", "Crown of Madness", 1)

class Tiefling_Dispater():
    def __init__(self, p):
        self.p = p

    def pre_Upd(self):
        pass
    
    def Upd(self):
        Fgen("Legacy of Dis")
        level = vLevel()
        if level >= 1: Fuse_2("Legacy of Dis", "Thaumaturgy", 1)
        if level >= 3: Fuse_2("Legacy of Dis", "Disguise Self", 1)
        if level >= 5: Fuse_2("Legacy of Dis", "Detect Thoughts", 1)

class Tiefling_Fierna():
    def __init__(self, p):
        self.p = p

    def pre_Upd(self):
        pass
    
    def Upd(self):
        Fgen("Legacy of Minauros")
        level = vLevel()
        if level >= 1: Fuse_2("Legacy of Minauros", "Mage Hand", 1)
        if level >= 3: Fuse_2("Legacy of Minauros", "Tensers Floating Disk", 1)
        if level >= 5: Fuse_2("Legacy of Minauros", "Arcane Lock", 1)

class Tiefling_Glasya():
    def __init__(self, p):
        self.p = p

    def pre_Upd(self):
        pass
    
    def Upd(self):
        Fgen("Legacy of Cania")
        level = vLevel()
        if level >= 1: Fuse_2("Legacy of Cania", "Mage Hand", 1)
        if level >= 3: Fuse_2("Legacy of Cania", "Burning Hands", 1)
        if level >= 5: Fuse_2("Legacy of Cania", "Flame Blade", 1)

class Tiefling_Levistus():
    def __init__(self, p):
        self.p = p

    def pre_Upd(self):
        pass
    
    def Upd(self):
        Fgen("Legacy of Stygia")
        level = vLevel()
        if level >= 1: Fuse_2("Legacy of Stygia", "Ray of Frost", 1)
        if level >= 3: Fuse_2("Legacy of Stygia", "Armor of Agathys", 1)
        if level >= 5: Fuse_2("Legacy of Stygia", "Darkness", 1)

class Tiefling_Mammon():
    def __init__(self, p):
        self.p = p

    def pre_Upd(self):
        pass
    
    def Upd(self):
        Fgen("Legacy of Minauros")
        level = vLevel()
        if level >= 1: Fuse_2("Legacy of Minauros", "Mage Hand", 1)
        if level >= 3: Fuse_2("Legacy of Minauros", "Tensers Floating Disk", 1)
        if level >= 5: Fuse_2("Legacy of Minauros", "Arcane Lock", 1)

class Tiefling_Mephistopheles():
    def __init__(self, p):
        self.p = p

    def pre_Upd(self):
        pass
    
    def Upd(self):
        Fgen("Legacy of Cania")
        level = vLevel()
        if level >= 1: Fuse_2("Legacy of Cania", "Mage Hand", 1)
        if level >= 3: Fuse_2("Legacy of Cania", "Burning Hands", 1)
        if level >= 5: Fuse_2("Legacy of Cania", "Flame Blade", 1)

class Tiefling_Zariel():
    def __init__(self, p):
        self.p = p

    def pre_Upd(self):
        pass
    
    def Upd(self):
        Fgen("Legacy of Avernus")
        level = vLevel()
        if level >= 1: Fuse_2("Legacy of Avernus", "Thaumaturgy", 1)
        if level >= 3: Fuse_2("Legacy of Avernus", "Searing Smite", 1)
        if level >= 5: Fuse_2("Legacy of Avernus", "Branding Smite", 1)
            
class Harengon():
    def __init__(self, p):
        self.p = p
        self.p.Speed["Walk"] = 30
        self.p.Skill.extend(["Perception"])
        self.p.Lang.extend(["Common"])



    def pre_Upd(self):
        pass
    
    def Upd(self):
        Fgen("Rabbit Hop")
        Fuse_1("Rabbit Hop", vPB())
        self.p.Initiative = vPB()

class Harengon_Standard():
    def __init__(self, p):
        self.p = p

    def pre_Upd(self):
        pass
    
    def Upd(self):
        pass
