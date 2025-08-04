
import shared
from manager.components.Background_comp import bBackground
from manager.components.Class_comp import bClass
from manager.components.Milestone_comp import bMilestone
from manager.components.Race_comp import bRace
from manager.components.Equipment_comp import Bazaar
from Sheet.get_set import *
from colorist import *

class Character():
    def __init__(self):
        pass
    def start_configuration(self):
        self.init_schema()
        self.Race.pre_Upd()
        self.Class.pre_Upd()
        self.Race.Upd()
        self.Class.Upd()
        
        self.recalculate_stats()
        self.init_spells()
        self.update_spells()

    def new_Level(self):
        self.Race.Upd()
        self.Class.Upd()
        self.Milestone.Upd()
        self.recalculate_stats()
        self.update_spells()

    def init_schema(self):
        self.Bazaar = Bazaar()
        self.Race = bRace()
        self.Class = bClass()
        self.Background = bBackground()
        self.Milestone = bMilestone()
        
        
    @property
    def Atr(self):
        cdata = kAtr()
        Class = self.Class.Atr
        Milestone = self.Milestone.Atr
        return {"STR":cdata["STR"]["Base"]+cdata["STR"]["Rasi"]+Class["STR"]+Milestone["STR"],"DEX":cdata["DEX"]["Base"]+cdata["DEX"]["Rasi"]+Class["DEX"]+Milestone["DEX"],"CON":cdata["CON"]["Base"]+cdata["CON"]["Rasi"]+Class["CON"]+Milestone["CON"],"INT":cdata["INT"]["Base"]+cdata["INT"]["Rasi"]+Class["INT"]+Milestone["INT"],"WIS":cdata["WIS"]["Base"]+cdata["WIS"]["Rasi"]+Class["WIS"]+Milestone["WIS"],"CHA":cdata["CHA"]["Base"]+cdata["CHA"]["Rasi"]+Class["CHA"]+Milestone["STR"]}

    @property
    def Prof(self):
        k_prof = kProf()
        Race = self.Race
        Class = self.Class
        Background = self.Background
        Milestone = self.Milestone
        return {"Weapon":Race.Weapon+k_prof["Weapon"]["Race"]+Class.Weapon+k_prof["Weapon"]["Class"]+Background.Weapon+k_prof["Weapon"]["Background"]+Milestone.Weapon+k_prof["Weapon"]["Feat"]+k_prof["Weapon"]["Player"],"Armor":Race.Armor+k_prof["Armor"]["Race"]+Class.Armor+k_prof["Armor"]["Class"]+Background.Armor+k_prof["Armor"]["Background"]+Milestone.Armor+k_prof["Armor"]["Feat"]+k_prof["Armor"]["Player"],"Tool":Race.Tool+k_prof["Tool"]["Race"]+Class.Tool+k_prof["Tool"]["Class"]+Background.Tool+k_prof["Tool"]["Background"]+Milestone.Tool+k_prof["Tool"]["Feat"]+k_prof["Tool"]["Player"],"Lang":Race.Lang+k_prof["Lang"]["Race"]+Class.Lang+k_prof["Lang"]["Class"]+Background.Lang+k_prof["Lang"]["Background"]+Milestone.Lang+k_prof["Lang"]["Feat"]+k_prof["Lang"]["Player"]}


    @property
    def Skill(self):
        proficient_skills = set(self.Race.Skill) | set(self.Class.Skill+[skill for skill in sClass() if skill]) | set(self.Background.Skill) | set(self.Milestone.Skill)
        return {skill: skill in proficient_skills for skill in Skill_L}

    @property
    def Speed(self):
        Race = self.Race
        Milestone = self.Milestone
        return {speed: Race.Speed[speed] + Milestone.Speed[speed] for speed in Speed_L}

    @property
    def Vision(self):
        Race = self.Race
        Milestone = self.Milestone
        return {vision: Race.Vision[vision] + Milestone.Vision[vision] for vision in Vision_L}

    @property
    def Initiative(self):
        return vMod("DEX") + self.Race.Initiative + self.Class.Initiative + self.MIlestone.Initiative

    @property
    def HP(self):
        return kHP()["Player"] + self.Race.HP + self.Class.HP


    def new_Race(self):
        self.wipe_data("Race Abil")
        self.Race = bRace()
        self.Race.pre_Upd()
        self.Race.Upd()
        self.Milestone.Upd()
        self.recalculate_stats()

    def new_Class(self):
        self.wipe_data("Class Abil")
        self.wipe_data("Class Spell")
        self.Class = bClass()
        self.Class.pre_Upd()
        self.Class.Upd()
        self.Milestone.Upd()
        self.recalculate_stats()
        self.init_spells()
        self.update_spells()
    
    def new_Background(self):
        self.wipe_data("Background Data")
        self.Background = bBackground()
        self.recalculate_stats()
        

    def update_Atr(self):
        self.wipe_data("Atr")
        self.Milestone.Upd()
        self.recalculate_stats()
        self.update_spells()

    def update_Class_Select(self):
        self.Class.pre_Upd()
        self.Class.Upd()
        self.Milestone.Upd()
        self.recalculate_stats()

    def update_Spell_Learn(self): pass

    def update_Spell_Prepare(self): pass

    def update_Spell_Cast(self): pass

    def update_Background_Prof(self):
        self.Background = bBackground()
        self.recalculate_stats()
        

    def init_spells(self):
        if valid_spellclass(): self.spell_data = spell_data_default

    def update_Milestone_Feat(self):
        self.update_Atr()
        

    def update_spells(self):
        if valid_spellclass(): self.Class.Spell_config()


    def wipe_data(self, source):
        if source == "Race Abil": shared.db.Race.Abil={}
        if source == "Class Abil": shared.db.Class.Abil={}
        if source == "Class Spell": shared.db.Spell=spell_default
        if source == "Background Data": shared.db.Background={"Prof": {}, "Equipment": {}}

    def recalculate_stats(self):
        self.pull_atr_data()
        self.sum_Proficiency()
        self.sum_Skill()
        self.sum_Speed()
        self.sum_Vision()
        self.sum_Initiative()
        self.sum_HP()
        self.sum_AC()

    def pull_atr_data(self):
        cdata = dRace().Rasi
        for atr in Atr_L:
            kAtr()[atr]["Rasi"] = 0
            for i, rasi_list in enumerate(cdata):
                if atr in rasi_list:
                    kAtr()[atr]["Rasi"] = i + 1
                    break
        
        for atr in Atr_L:
            val = self.Atr[atr]
            mod = (val- 10) // 2
            kAtr()[atr]["Val"] = val
            kAtr()[atr]["Mod"] = mod


    def sum_Proficiency(self): pass

    def sum_Skill(self):
        Skill = self.Skill
        for skill in Skill_L:
            kSkill()[skill]["Mod"] = kAtr()[dict_Skill[skill]["Atr"]]["Mod"]
            if Skill[skill]: kSkill()[skill]["Mod"] += vPB()


    
    def sum_Speed(self):pass
    def sum_Vision(self): pass
    def sum_Initiative(self): pass


    def sum_HP(self):
        sum = self.HP
        kHP()["Sum"] = sum
        kHP()["Current"] = sum
    
    
    def sum_AC(self):
        dex_modifier = vMod("DEX")

        base_ac = 10
        dex_for_ac = dex_modifier

        armor_id = Current_Equip("Armor")
        if armor_id:
            item = bItem(armor_id)
            
            is_proficient = item.Cat[0] in kProf()["Armor"]
            
            if is_proficient:
                base_ac = item.AC
                dex_for_ac = min(dex_modifier, item.Dex_Max)

        shared.db.AC.Base = base_ac
        shared.db.AC.Dex = dex_for_ac
        shared.db.AC.Sum = base_ac + dex_for_ac
            
        



def init_pc():
    if shared.db is None:
        red("[init_pc] ERROR : Not loaded")
        return
    shared.pc = Character()
    green("[init_pc] - player now exists")