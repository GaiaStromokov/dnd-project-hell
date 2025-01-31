from config.gen_import import *

def get_mod(score): return int((score - 10) // 2)
def get_pb(level): return (level - 1) // 4 + 2
class Player:
    def __init__(self, db):
        self.db = db
        self.uix = None
        
    def __getattr__(self, name):
            if name in self.db:
                return self.db[name]
            raise AttributeError(f"'Player' object has no attribute '{name}'")
        


    def set_uix(self, uix):
        self.uix = uix
        
    
    def upd_ui(self, sender):
        for item in sender:
            if item == "ATR":
                self.uix.ui_ATR()
            elif item == "SAVE":
                self.uix.ui_SAVE()
            elif item == "PB":
                self.uix.ui_PB()
            elif item == "SKILL":
                self.uix.ui_SKILL()
            elif item == "PROF":
                self.uix.ui_PROF()
            elif item == "SRACE":
                self.uix.ui_SRACE()
            elif item == "SPEED":
                self.uix.ui_SPEED()
            elif item == "VISION":
                self.uix.ui_VISION()
            elif item == "TRAIT":
                self.uix.ui_TRAIT()
            elif item == "CLASS_SLIST":
                self.uix.ui_CLASS_SLIST()
            elif item == "ASI":
                self.uix.ui_ASI()
            elif item == "ASIC":
                self.uix.ui_ASIC()
            

    def upd_data(self, sender, data):
        name=sender.split('_')[0]
        if name == "L":
            print("L\n")
            self.upd_level(data)
        elif name == "C":
            print("C")
            self.upd_class(data)
        elif name == "R":
            print("R\n")
            self.upd_race(data)
        elif name == "SR":
            print("SR\n")
            self.upd_subrace(data)
        elif name == "BG":
            print("BG\n")
            self.upd_background(data)
        elif name == "CSKILL":
            print("CSKILL\n")
            self.upd_SKILL(sender, data)
        elif name == "PROF":
            print("PROF\n")
            self.upd_P_PROF(sender, data)
        elif name == "PASI":
            self.upd_ATR(sender,data)
        elif name == "RASI":
            self.upd_ATR(sender,data)
        elif name == "ASIC":
            self.upd_ASIC(sender,data)
        elif name == "ASIV":
            self.upd_ASIV(sender,data)

    def upd_P_PROF(self,sender, data):
        category=sender.split('_')[1]
        item=sender.split('_')[2]
        
        self.PROF[category][item][0] = data
        self.config_PROF()
    
    def upd_ATR(self,sender,data):
        parent=sender.split('_')[0]
        if parent == 'PASI':
            stat=sender.split('_')[1]
            self.ATR[stat].data[0] = int(data)
        if parent == 'RASI':
            self.clear_data("RASI")
            place=int(sender.split('_')[1])
            self.DATA.R.ASI[place]=data
            
            if self.DATA.R.ASI[0] != "":
                self.ATR[self.DATA.R.ASI[0]].data[1] += 1
            if self.DATA.R.ASI[1] != "":
                self.ATR[self.DATA.R.ASI[1]].data[1] += 2
                


        self.config_ATR()
    
    def upd_SKILL(self,sender,data):
        parent=sender.split('_')[0]
        if parent=="CSKILL":
            self.clear_data("CSKILL_data")
            place=int(sender.split('_')[1]) 
            self.DATA.C.SKILL.choice[place]=data
            if self.DATA.C.SKILL.choice[0] != "":
                self.SKILL[self.DATA.C.SKILL.choice[0]].data[2]=True
            if self.DATA.C.SKILL.choice[1] != "":
                self.SKILL[self.DATA.C.SKILL.choice[1]].data[3]=True
        self.upd_ui(["SKILL"])
        
    def upd_level(self, data):
        self.CORE.L = int(data)
        self.config_LEVEL()
        
    def upd_race(self, data):
        self.CORE.R = data
        self.config_RACE()
    
    def upd_subrace(self, data):
        self.CORE.SR = data
        self.config_SRACE()
        
    def upd_class(self, data):
        self.CORE.C = data
        self.config_CLASS()
        
        
    
        
    
        
    def upd_background(self, data):
        self.CORE.BG = data
        self.config_BG()

    def upd_ASIC(self,sender,data):
        place=int(sender.split('_')[1])
        self.DATA.C.ASI.choice[place]=data
        self.upd_ui(["ASIC"])
    
    def upd_ASIV(self,sender,data):
        parent= sender.split('_')[1]
        idx = int(sender.split('_')[2])
        
        if parent == "A":
            place=int(sender.split('_')[3])
            self.DATA.C.ASI.feat[idx]=""
            self.DATA.C.ASI.asi[idx][place]=data
        if parent == "F":
            self.DATA.C.ASI.asi[idx]=""
            self.DATA.C.ASI.feat[idx]=data
            self.config_FEAT()
            
        self.clear_data("CASI_data")
        for stat in atrL:
            self.ATR[stat].data[2]=sum(row.count(stat) for row in self.DATA.C.ASI.asi)
            
        
        self.config_ATR()
        
        # place=int(sender.split('_')[1])
        # self.DATA.C.ASI.choice[place]=data
        # self.upd_ui(["ASIC"])
    # #-------------------------------------

    
    def config_LEVEL(self):
        self.calc_class()
        self.CORE.PB=get_pb(self.CORE.L)
        self.upd_ui(["PB"])
        self.config_SAVE()
        self.config_ASI()



            
    def config_ATR(self):
        for stat in atrL:
            self.ATR[stat].v = sum(self.ATR[stat].data)
            self.ATR[stat].m = get_mod(self.ATR[stat].v)
        self.upd_ui(["ATR","SKILL"])
        self.config_SAVE()
        
    def config_SAVE(self):
        for stat in atrL:
            self.ATR[stat].pbm[0]=self.ATR[stat].m
            self.ATR[stat].pbm[1]=self.ATR[stat].m+self.CORE.PB
        self.upd_ui(["SAVE","SKILL"])
    



    def config_RACE(self):
        self.CORE.SR=""
        self.upd_ui(["SRACE"])
        self.to_dict_RACE("R")
        
    def config_SRACE(self):
        self.to_dict_RACE("SR")



    def config_SPEED(self):
        self.SHEET.SPEED.v = sum(self.SHEET.SPEED.data)
        self.upd_ui(["SPEED"])

    def config_VISION(self):
        self.upd_ui(["VISION"])
        
        
        
    def config_BG(self):
        self.to_dict_BG()
        
    def config_CLASS(self):
        self.calc_class()
        self.to_dict_CLASS()

    def config_ASI(self):
        for index, i in enumerate(dclass[self.CORE.C].ASI):
            if self.CORE.L >= i:
                self.DATA.C.ASI.active[index] = True
            else:
                self.DATA.C.ASI.active[index] = False
        self.upd_ui(["ASI"])


        
    def to_dict_BG(self):
        self.clear_data("BG_data")
        path=dbg[self.CORE.BG]
        self.DATA.BG.Equipment=path.Equipment
        self.SHEET.Feature=path.FEATURE
        for prof in profL:
            for item in path.PROF[prof]:
                self.PROF[prof][item][3]=True
        for skill in path.SKILL:
            self.SKILL[skill].data[4]=True
        self.upd_ui(["SKILL","PROF"])

    def to_dict_RACE(self,sender):
        self.clear_data("RACE_data")
        rpath=drace[self.CORE.R]
        
        
        if sender =="R":
            self.SHEET.SPEED.data[0]=rpath.SPEED
            self.SHEET.VISION=rpath.VISION
            
            rtrait = rpath.TRAIT
            rskill = rpath.SKILL
            rprof = rpath.PROF
        elif sender == "SR":
            srpath=dsrace[self.CORE.R][self.CORE.SR]
            self.SHEET.SPEED.data[0]=srpath.SPEED
            self.SHEET.VISION=srpath.VISION
            
            rtrait=rpath.TRAIT+srpath.TRAIT
            rskill=rpath.SKILL+srpath.SKILL
            rprof = {key: rpath.PROF[key] + srpath.PROF[key] for key in rpath.PROF}
        
        
        
        for trait in rtrait:
            self.SHEET.TRAIT[trait] = dTrait[trait]
            
        for skill in rskill:
            self.SKILL[skill].data[1]=True
        
        for prof in profL:
            for item in rprof[prof]:
                self.PROF[prof][item][1]=True
                
                
        self.config_SPEED()
        self.config_VISION()
        self.upd_ui(["PROF","SKILL","TRAIT"])





    
    def to_dict_CLASS(self):
        self.clear_data("CLASS_data")
        path =  dclass[self.CORE.C]
        
        self.SHEET.HD.die=path.HD
        self.DATA.C.SKILL.list=path.SKILLL
        
        self.ATR[path.SAVE[0]].s=True
        self.ATR[path.SAVE[1]].s=True

        for prof in profL:
            if path.PROF[prof] == ["ALL"]:
                for item in dprof[prof]:
                    self.PROF[prof][item][2] = True
            else:
                for item in path.PROF[prof]:
                    self.PROF[prof][item][2]=True

        self.config_ASI()


        self.upd_ui(["PROF","SKILL","SAVE","CLASS_SLIST","SPEED"])
    #     # parent.ABIL=dcabil[self.CORE.C].ABIL
    #     for index in dclass[self.CORE.C].ABIL:
    #         self.cCLASS.DATA.ABIL[index]=dcabil[self.CORE.C].ABIL[index].DESC
        

    def calc_class(self):
        if self.CORE.L < 3 and self.CORE.C not in ["Cleric", "Warlock"]:
            self.CORE.SC = ""
            items = []
        else:
            items=dcore.C[self.CORE.C]
        self.uix.ui_SCLASS(items)

    def clear_data(self,sender):    
        if sender == "RACE_data":
            self.SHEET.VISION = 0
            self.SHEET.SPEED.data[0] = 0
            self.SHEET.TRAIT = {}
            for skill in skillL:
                self.SKILL[skill].data[1]=False
    
            for prof in profL:
                for item in dprof[prof]:
                    self.PROF[prof][item][1]=False
        elif sender == "RASI":
            for stat in atrL:
                self.ATR[stat].data[1]=0
        elif sender == "CLASS_data":
            self.DATA.C.SKILL.choice=["",""]
            for skill in skillL:
                self.SKILL[skill].data[2]=False
                self.SKILL[skill].data[3]=False
            for prof in profL:
                for item in dprof[prof]:
                    self.PROF[prof][item][2] = False
            for stat in atrL:
                self.ATR[stat].s=False
            self.DATA.C.ASI.active= [False,False,False,False,False,False,False]
            self.DATA.C.ASI.choice=["","","","","","",""]
            self.DATA.C.ASI.feat=["","","","","","","",]
            self.DATA.C.ASI.asi=[["", ""],["", ""],["", ""],["", ""],["", ""],["", ""],["", ""]]
        elif sender == "CSKILL_data":
            for skill in skillL:
                self.SKILL[skill].data[2]=False
                self.SKILL[skill].data[3]=False
        elif sender == "BG_data":
            for skill in skillL:
                self.SKILL[skill].data[4]=False
            for prof in profL:
                for item in dprof[prof]:
                    self.PROF[prof][item][3]=False
            self.DATA.BG.Equipment=[]
            self.SHEET.FEATURE={}
        elif sender == "CASI_data":
            for stat in atrL:
                self.ATR[stat].data[2]=0


