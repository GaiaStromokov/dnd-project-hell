from config.gen_import import *
from DICTS.DICT_IMPORT import *


def get_mod(score): return int((score - 10) // 2)
def get_pb(level): return (level - 1) // 4 + 2
class Player:
    def __init__(self, db):
        self.db = db
        self.uix = None
        
    @property
    def ATR(self):
        return self.db.ATR

    @property
    def CORE(self):
        return self.db.CORE
    
    @property
    def SKILL(self):
        return self.db.SKILL
    
    @property
    def PROF(self):
        return self.db.PROF
    
    @property
    def SHEET(self):
        return self.db.SHEET
    
    @property
    def cRACE(self):
        return self.db.RACE_data
    @property
    def cCLASS(self):
        return self.db.CLASS_data
    
    @property
    def cBG(self):
        return self.db.BACKGROUND_data

    def set_uix(self, uix):
        self.uix = uix
        
    
    def upd_data(self, sender, data):
        name=sender.split('_')[0]
        if name == "L":
            self.upd_level(data)
        elif name == "C":
            self.upd_class(data)
        elif name == "R":
            self.upd_race(data)
        elif name == "SR":
            self.upd_subrace(data)
        elif name == "BG":
            self.upd_background(data)
        elif name == "CSKILL":
            self.upd_SKILL(sender, data)
        elif name == "PROF":
            self.upd_P_PROF(sender, data)

    def upd_P_PROF(self,sender, data):
        category=sender.split('_')[1]
        item=sender.split('_')[2]
        
        self.PROF[category][item][0] = data
        self.onchange_PROF()
    
    def upd_ATR(self,sender,data):
        parent=sender.split('_')[0]
        if parent == 'p':
            stat=sender.split('_')[1]
            self.ATR[stat].P = int(data)
        if parent == 'RASI':
            place=int(sender.split('_')[1])
            self.cRACE.ASI[place]=data
            self.clear_data("Race_ATR")
            self.ATR[self.cRACE.ASI[0]].R[0]=1
            self.ATR[self.cRACE.ASI[1]].R[1]=2
                
        self.onchange_ATR()
    
    def upd_SKILL(self,sender,data):
        parent=sender.split('_')[0]
        if parent=="CSKILL":
            place=int(sender.split('_')[1]) 
            self.clear_data("Skill_CLASS")
            self.cCLASS.SKILL[place]=data
            if self.cCLASS.SKILL[0] != "":
                self.SKILL[self.cCLASS.SKILL[0]].C[0]=True
            if self.cCLASS.SKILL[1] != "":
                self.SKILL[self.cCLASS.SKILL[1]].C[1]=True
        self.onchange_SKILL()
        
    def upd_level(self, data):
        self.CORE.L = int(data)
        self.onchange_LEVEL()
        
    def upd_class(self, data):
        self.CORE.C = data
        
        self.onchange_CLASS()
    def upd_race(self, data):
        self.CORE.R = data
        self.onchange_RACE()
        
    def upd_subrace(self, data):
        self.CORE.SR = data
        self.onchange_SRACE()
        
    def upd_background(self, data):
        self.CORE.BG = data
        self.onchange_BG()
        
    #-------------------------------------
    
    def onchange_PROF(self):
        self.uix.upd_PROF_ui()
    
    def onchange_LEVEL(self):
        self.confirm_class()
        self.CORE.PB=get_pb(self.CORE.L)
        self.uix.upd_PB_ui()
        self.onchange_SKILL()

    def onchange_ATR(self):
        for stat in self.ATR:
            self.ATR[stat].V = self.ATR[stat].P + sum(self.ATR[stat].C.ASI_a) + sum(self.ATR[stat].C.ASI_b) + sum(self.ATR[stat].R)
            self.ATR[stat].M = get_mod(self.ATR[stat].V)
        self.uix.upd_ATR_ui()
        self.onchange_SKILL()

    def onchange_SKILL(self):
        for skill in skill_LST:
            toggled = any([self.SKILL[skill].P, any(self.SKILL[skill].C), self.SKILL[skill].R, self.SKILL[skill].BG])
            if toggled:
                value = self.ATR[self.SKILL[skill].ATR].M + self.CORE.PB
            else:
                value = self.ATR[self.SKILL[skill].ATR].M
            self.SKILL[skill].V = value
        self.uix.upd_SKILL_ui()

    def onchange_RACE(self):
        self.CORE.SR=""
        self.uix.upd_SRACE_ui()
        self.to_dict_RACE()
        
    def onchange_SRACE(self):
        self.to_dict_SRACE()

    def onchange_speed(self):
        self.SHEET.SPEED.V = self.cRACE.DATA.SPEED + self.SHEET.SPEED.CLASS
        self.uix.upd_SPEED_ui()
    
    def onchange_vision(self):
        self.SHEET.VISION.V = self.cRACE.DATA.VISION
        self.uix.upd_VISION_ui()
        
    def onchange_BG(self):
        self.to_dict_BG()
        
    def onchange_CLASS(self):
        self.calc_class()
        self.clear_data("CLASS_data")
        self.to_dict_CLASS()
        self.uix.upd_class_skill_list()
        self.uix.upd_SPEED_ui
        self.uix.upd_VISION_ui
        
    def to_dict_BG(self):
        self.clear_data("BG_data")
        path=dbg[self.CORE.BG]
        parent=self.cBG.DATA
        
        parent.PROF=path.PROF
        parent.SKILL=path.SKILL
           
        parent.Equipment=path.Equipment
        parent.Feature=path.Feature
        for prof in dprof.keys():
            for item in parent.PROF[prof]:
                self.PROF[prof][item][3]=True
        
        for skill in parent.SKILL:
            self.SKILL[skill].BG=True
            
        self.onchange_SKILL()
        self.onchange_PROF()
        
        
    def to_dict_RACE(self):
        self.clear_data("RACE_data")
        self.clear_data("SUBRACE_data")
        path=drace[self.CORE.R]
        parent=self.cRACE.DATA
        
        parent.SPEED = path.SPEED
        parent.VISION = path.VISION
        parent.SKILL.RACE = path.SKILL
        parent.PROF.RACE = path.PROF
        
        for trait in path.TRAITS:
            parent.TRAITS.RACE[trait] = dTrait[trait]

        self.combine_race_data()
        

    def to_dict_SRACE(self):
        self.clear_data("SUBRACE_data")
        path=dsrace[self.CORE.R][self.CORE.SR]
        parent=self.cRACE.DATA
        parent.SPEED = path.SPEED
        parent.VISION = path.VISION
        parent.SKILL.SRACE = path.SKILL

        parent.PROF.SRACE=path.PROF
        
        for trait in path.TRAITS:
            parent.TRAITS.SRACE[trait] = dTrait[trait]

        self.combine_race_data()
        
    def combine_race_data(self):
        self.clear_data("RACE_COMBINE_data")
        path = self.cRACE.DATA
        path.SKILL.COMBINE = path.SKILL.RACE + path.SKILL.SRACE
        path.TRAITS.COMBINE = {**path.TRAITS.RACE, **path.TRAITS.SRACE}
        

        for prof in dprof.keys():
            path.PROF.COMBINE[prof] = path.PROF.RACE[prof] + path.PROF.SRACE[prof]
            for item in path.PROF.COMBINE[prof]:
                self.PROF[prof][item][2]=True
        
        for skill in path.SKILL.COMBINE:
            self.SKILL[skill].R=True
        
        
        
        self.onchange_speed()
        self.onchange_vision()
        self.onchange_SKILL()
        self.onchange_PROF()
        self.uix.upd_TRAIT_ui()

    
    def to_dict_CLASS(self):
        path = self.cCLASS.DATA
        path.HD=dclass[self.CORE.C].HD
        path.SKILL_LIST=dclass[self.CORE.C].SKILL_LIST
        path.SAVES=dclass[self.CORE.C].SAVES
        for prof in dprof.keys():
            path.PROF[prof]=dclass[self.CORE.C].PROF[prof]
            if path.PROF[prof] == ["ALL"]:
                for item in dprof[prof]:
                    self.PROF[prof][item][1] = True
            else:
                for item in path.PROF[prof]:
                    self.PROF[prof][item][1]=True
        self.onchange_PROF()
        
        
            
        
        

    def calc_class(self):
        if self.CORE.L < 3 and self.CORE.C not in ["Cleric", "Warlock"]:
            self.CORE.SC = ""
            items = []
        else:
            items=dcore.C[self.CORE.C]
        self.uix.upd_subclass_ui(items)

    def clear_data(self,sender):
        if sender == "Race_ATR":
            for stat in atr_LST:
                self.ATR[stat].R=[0,0]
        elif sender == "CLASS_data":
            self.cCLASS.SKILL[0]=""
            self.cCLASS.SKILL[1]=""
            for skill in skill_LST:
                self.SKILL[skill].C[0]=False
                self.SKILL[skill].C[1]=False
            for prof in dprof.keys():
                for item in dprof[prof]:
                    self.PROF[prof][item][1] = False
        elif sender == "RACE_data":
            self.cRACE.DATA.SPEED = 0
            self.cRACE.DATA.VISION = 0
            self.cRACE.DATA.TRAITS.RACE = {}
            self.cRACE.DATA.SKILL.RACE = []
            for prof in list(dprof.keys()):
                self.cRACE.DATA.PROF.RACE[prof] = []
        elif sender == "SUBRACE_data":
            self.cRACE.DATA.SPEED = 0
            self.cRACE.DATA.VISION = 0
            self.cRACE.DATA.TRAITS.SRACE = {}
            self.cRACE.DATA.SKILL.SRACE = []
            for prof in list(dprof.keys()):
                self.cRACE.DATA.PROF.SRACE[prof] = []
        
        elif sender == "RACE_COMBINE_data":
            self.cRACE.DATA.SPEED = 0
            self.cRACE.DATA.VISION = 0
            self.cRACE.DATA.TRAITS.COMBINE = {}
            self.cRACE.DATA.SKILL.COMBINE = []
            for prof in list(dprof.keys()):
                self.cRACE.DATA.PROF.COMBINE[prof] = []
                for item in dprof[prof]:
                    self.PROF[prof][item][2]=False
                
            for skill in skill_LST:
                self.SKILL[skill].R = False
                
        elif sender == "BG_data":
            self.cBG.DATA.SKILL=[]
            for skill in skill_LST:
                self.SKILL[skill].BG=False
            for prof in list(dprof.keys()):
                self.cBG.DATA.PROF[prof] = []
                for item in dprof[prof]:
                    self.PROF[prof][item][3]=False
            self.cBG.DATA.Equipment=[]
            self.cBG.DATA.Feature={}

