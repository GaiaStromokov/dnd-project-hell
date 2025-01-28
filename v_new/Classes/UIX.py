from config.gen_import import *

class UIX:
    def __init__(self, p):
        self.p = p

    @property
    def CORE(self):
        return self.p.db.CORE

    @property
    def ATR(self):
        return self.p.db.ATR
    
    @property
    def SKILL(self):
        return self.p.db.SKILL
    
    @property
    def PROF(self):
        return self.p.db.PROF
    
    @property
    def SHEET(self):
        return self.p.db.SHEET
    
    @property
    def cRACE(self):
        return self.p.db.RACE_data

    @property
    def cCLASS(self):
        return self.p.db.CLASS_data

    @property
    def cBG(self):
        return self.db.BACKGROUND_data
    
    def init_ui(self):
        self.init_Character_Window()
        self.init_ATR_Window()
        self.init_SKILL_Window()
        self.init_ABILITIES_Window()
        self.init_PROF_Window()

    def init_Character_Window(self):
        with window(label="Character Info", no_close=True, autosize=True, tag="CI_Window"):
            with group(horizontal=True):
                add_button(label="Level", enabled=False, width=55)
                add_combo(items=levelval_LST, default_value=self.CORE.L, width=30, no_arrow_button=True, callback=self.p.upd_data, tag='L_ui')
                add_button(label="PB", enabled=False, width=45)
                add_button(label=self.CORE.PB, enabled=False, width=34, tag="PB_ui")
            with group(horizontal=True):
                add_button(label="Race", enabled=False, width=80)
                add_combo(items=list(dcore.R.keys()), default_value=self.CORE.R, width=100, no_arrow_button=True, callback=self.p.upd_data, tag='R_ui')
            with group(horizontal=True):
                add_button(label="Sub Race", enabled=False, width=80)
                add_combo(items=dcore.R[self.CORE.R], default_value=self.CORE.SR, width=100, no_arrow_button=True, callback=self.p.upd_data, tag='SR_ui')
            with group(horizontal=True):
                add_button(label="Class", enabled=False, width=80)
                add_combo(items=list(dcore.C.keys()), default_value=self.CORE.C, width=100, no_arrow_button=True, callback=self.p.upd_data, tag='C_ui')
            with group(horizontal=True):
                add_button(label="Sub Class", enabled=False, width=80)
                add_combo(items=[], default_value=self.CORE.SC, width=100, no_arrow_button=True, tag='SC_ui')
            self.p.calc_class()
            with group(horizontal=True):
                add_button(label="Background", enabled=False, width=80)
                add_combo(items=dcore.BG, default_value=self.CORE.BG, width=100, no_arrow_button=True, callback=self.p.upd_data, tag='BG_ui')
    def init_ATR_Window(self):
        with window(label="Attributes", no_close=True, autosize=True):
            for stat in atr_LST:
                with group(horizontal=True):
                    add_color_button(default_value=[255, 0, 0], enabled=False, width=10, tag=f"{stat}_ST")
                    add_button(label=stat, enabled=False, width=40, tag=f"{stat}_ui")
                    add_button(label=self.ATR[stat].V, enabled=False, width=30, tag=f"{stat}_val")
                    add_button(label=self.ATR[stat].M, enabled=False, width=30,  tag=f"{stat}_mod")
                with popup(f"{stat}_ui", mousebutton=mvMouseButton_Left):
                    add_input_int(default_value=self.ATR[stat].P, step=1, min_value=1, max_value=18, min_clamped=True, max_clamped=True, width=80, callback=self.p.upd_ATR, tag=f"p_{stat}")
    def init_SKILL_Window(self):
        with window(label="Skills", no_close=True, autosize=True):
            for skill in skill_LST:
                with group(horizontal=True):
                    toggled = any([self.SKILL[skill].P, self.SKILL[skill].C[0],self.SKILL[skill].C[1], self.SKILL[skill].R, self.SKILL[skill].BG])
                    add_button(label=skill, enabled=False, width=100)
                    add_checkbox(default_value=toggled, enabled=False, tag=f"{skill}_tog")
                    add_button(label=self.SKILL[skill].V, enabled=False, width=20, tag=f"{skill}_val")
    def init_ABILITIES_Window(self):
        with window(label="Abilities", no_close=True, autosize=True):
            with child_window(auto_resize_y=True,auto_resize_x=True, border=True):
                add_button(label="Racial Abilities", enabled=False)
                with child_window(auto_resize_y=True,auto_resize_x=True, border=True, tag="Race_ac"):
                    with group(horizontal=True):
                        add_button(label="Darkvision", enabled=False, height=30)
                        add_button(label=self.SHEET.VISION.V, enabled=False, height=30, tag="VISION_ui")
                        with child_window(auto_resize_y=True,auto_resize_x=True, border=True, tag="Race_asi_child"):
                            add_button(label="Race ASI", enabled=False, tag="Race_asi_label")
                            with popup("Race_asi_label", mousebutton=mvMouseButton_Left):
                                with group(horizontal=True):
                                    add_button(label="+1", enabled=False)
                                    add_combo(items=atr_LST, default_value=self.cRACE.ASI[0], width=60, tag="RASI_0", callback=self.p.upd_ATR)
                                with group(horizontal=True):
                                    add_button(label="+2", enabled=False)
                                    add_combo(items=atr_LST, default_value=self.cRACE.ASI[1], width=60, tag="RASI_1", callback=self.p.upd_ATR)
                with child_window(auto_resize_y=True,width=300, border=True, tag="Race_Feature_child"):
                    with group(parent="Race_Feature_child"):
                        for trait in self.cRACE.DATA.TRAITS.COMBINE:
                            add_button(label=trait, enabled=False)
                            add_text(self.cRACE.DATA.TRAITS.COMBINE[trait].Desc, wrap=250)
            with child_window(auto_resize_y=True,auto_resize_x=True, border=True):
                add_button(label="Class Abilities", enabled=False)
                with child_window(auto_resize_y=True,auto_resize_x=True, border=True, tag="Class_ac"):
                    with child_window(auto_resize_y=True,auto_resize_x=True, border=True, tag="Class_skill_child"):
                        add_button(label="Class Skill", enabled=False, tag="Class_skill_label")
                        with popup("Class_skill_label", mousebutton=mvMouseButton_Left):
                            with group(horizontal=True):
                                add_button(label="Skill 1", enabled=False)
                                add_combo(items=self.cCLASS.DATA.SKILL_LIST, default_value=self.cCLASS.SKILL[0], width=100, tag="CSKILL_0", callback=self.p.upd_data)
                            with group(horizontal=True):
                                add_button(label="Skill 2", enabled=False)
                                add_combo(items=self.cCLASS.DATA.SKILL_LIST, default_value=self.cCLASS.SKILL[1], width=100, tag="CSKILL_1", callback=self.p.upd_data)
    def init_PROF_Window(self):
        with window(label="Proficiency", no_close=True, autosize=True):
            for prof in dprof.keys():
                with menu(label=f"{prof}"):
                    for item in dprof[prof]:
                        toggled = any(self.PROF[prof][item])
                        ptoggled = any(self.PROF[prof][item][1:4]) 
                        add_selectable(label=item, default_value=toggled, enabled=not ptoggled, callback=self.p.upd_data, tag=f"PROF_{prof}_{item}")


    def upd_PROF_ui(self):
        for prof in dprof.keys():
            for item in dprof[prof]:
                toggled = any(self.PROF[prof][item])
                ptoggled = any(self.PROF[prof][item][1:4]) 
                configure_item(f"PROF_{prof}_{item}", default_value=toggled, enabled=not ptoggled)
                
    def upd_TRAIT_ui(self):
        delete_item("Race_Feature_child", children_only=True)
        with group(parent="Race_Feature_child"):
            for trait in self.cRACE.DATA.TRAITS.COMBINE:
                add_button(label=trait, enabled=False)
                add_text(self.cRACE.DATA.TRAITS.COMBINE[trait].Desc, wrap=250)
                    
    def upd_SPEED_ui(self):
        pass
    
    def upd_VISION_ui(self):
        configure_item("VISION_ui", label=self.SHEET.VISION.V)
        
    def upd_PB_ui(self):
        configure_item("PB_ui", label=self.CORE.PB)
        
    def upd_ATR_ui(self):
        for stat in atr_LST:
            configure_item(f"{stat}_val", label=self.ATR[stat].V) 
            configure_item(f"{stat}_mod", label=self.ATR[stat].M)
            
    def upd_SKILL_ui(self):
        for skill in skill_LST:
            toggled = any([self.SKILL[skill].P, any(self.SKILL[skill].C), self.SKILL[skill].R, self.SKILL[skill].BG])
            configure_item(f"{skill}_tog", default_value=toggled)
            configure_item(f"{skill}_val", label=self.SKILL[skill].V)
        
    def upd_SRACE_ui(self):
        configure_item("SR_ui", items=dcore.R[self.CORE.R], default_value=self.CORE.SR)
    
    
    
    def upd_subclass_ui(self,items):
        configure_item("SC_ui", items=items, default_value=self.CORE.SC)
    
    def upd_class_skill_list(self):
        configure_item("CSKILL_0", items=self.cCLASS.DATA.SKILL_LIST, default_value=self.cCLASS.SKILL[0])
        configure_item("CSKILL_1", items=self.cCLASS.DATA.SKILL_LIST, default_value=self.cCLASS.SKILL[1])
        
