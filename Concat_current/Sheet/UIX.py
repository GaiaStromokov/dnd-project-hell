from config.gen_import import *
class UIX:
    def __init__(self, p):
        self.p = p

    def __getattr__(self, name):
        if hasattr(self.p.db, name):
            return getattr(self.p.db, name)
        raise AttributeError(f"'UIX' object has no attribute '{name}'")
    
    def init_ui(self):
        self.init_Character_Window()
        self.init_ATR_Window()
        self.init_SKILL_Window()
        self.init_PROF_Window()
        self.init_ABILITIES_Window()
        self.init_ADMIN_Window()
        

    def init_Character_Window(self):
        with window(label="Character Info", no_close=True, autosize=True, tag="CI_Window"):
            with group(horizontal=True):
                add_button(label="Level", enabled=False, width=55)
                add_combo(items=levelL, default_value=self.CORE.L, width=30, no_arrow_button=True, callback=self.p.upd_data, tag='L_ui')
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
            for stat in atrL:
                with group(horizontal=True):
                    add_checkbox(default_value=self.ATR[stat].s, enabled=False, tag=f"{stat}_ST")
                    add_button(label=stat, enabled=False, width=40, tag=f"{stat}_ui")
                    add_button(label=self.ATR[stat].v, enabled=False, width=30, tag=f"{stat}_val")
                    add_button(label=self.ATR[stat].m, enabled=False, width=30,  tag=f"{stat}_mod")
                with tooltip(f"{stat}_ST"):
                    add_button(label=self.ATR[stat].pbm[self.ATR[stat].s], enabled=False, width=30, tag=f"{stat}_ST_val")
                with popup(f"{stat}_ui", mousebutton=mvMouseButton_Left):
                    add_input_int(default_value=self.ATR[stat].data[0], step=1, min_value=1, max_value=18, min_clamped=True, max_clamped=True, width=80, callback=self.p.upd_ATR, tag=f"PASI_{stat}")
    def init_SKILL_Window(self):
        with window(label="Skills", no_close=True, autosize=True):
            for skill in skillL:
                with group(horizontal=True):
                    toggled = any(self.SKILL[skill].data)
                    add_button(label=skill, enabled=False, width=100)
                    add_checkbox(default_value=toggled, enabled=False, tag=f"{skill}_tog")
                    add_button(label=self.ATR[self.SKILL[skill].atr].pbm[toggled], enabled=False, width=20, tag=f"{skill}_val")
    def init_PROF_Window(self):
        with window(label="Proficiency", no_close=True, autosize=True):
            for prof in profL:
                with menu(label=f"{prof}"):
                    for item in dprof[prof]:
                        toggled = any(self.PROF[prof][item])
                        ptoggled = any(self.PROF[prof][item][1:4]) 
                        add_selectable(label=item, default_value=toggled, enabled=not ptoggled, callback=self.p.upd_data, tag=f"PROF_{prof}_{item}")
    def init_ABILITIES_Window(self):
        with window(label="Abilities", no_close=True, autosize=True):
            with child_window(auto_resize_y=True,auto_resize_x=True, border=True):
                with group(horizontal=True):
                        add_button(label="Darkvision", enabled=False, height=30)
                        add_button(label=self.SHEET.VISION, enabled=False, height=30, tag="VISION_ui")
            with child_window(auto_resize_y=True,auto_resize_x=True, border=True):
                add_button(label="Racial Abilities", enabled=False)
                with child_window(auto_resize_y=True,auto_resize_x=True, border=True):
                    with child_window(auto_resize_y=True,width=300, border=True, tag="Race_Feature_child"):
                        with group(parent="Race_Feature_child"):
                            for trait in self.SHEET.TRAIT:
                                add_button(label=trait, enabled=False)
                                add_text(self.SHEET.TRAIT[trait].Desc, wrap=250)
            
            with child_window(auto_resize_y=True,auto_resize_x=True, border=True):
                add_button(label="Class Abilities", enabled=False)
                with child_window(auto_resize_y=True,auto_resize_x=True, border=True):
                    with child_window(auto_resize_y=True,width=300, border=True, tag="Class_Ability_child"):
                        pass
                    
            with child_window(auto_resize_y=True,auto_resize_x=True, border=True):
                add_button(label="Feats", enabled=False)
                with child_window(auto_resize_y=True,auto_resize_x=True, border=True):
                    with child_window(auto_resize_y=True,width=300, border=True, tag="Feat_child"):
                        pass


    def init_ADMIN_Window(self):
        with window(label="Admin", no_close=True, autosize=True):
            with child_window(auto_resize_y=True,auto_resize_x=True, border=True, tag="Rasi_child"):
                add_button(label="Race ASI", enabled=False, tag="Rasi_label")
                with popup("Rasi_label", mousebutton=mvMouseButton_Left):
                    with group(horizontal=True):
                        add_button(label="+1", enabled=False)
                        add_combo(items=atrL, default_value=self.DATA.R.ASI[0], width=60, tag="RASI_0", callback=self.p.upd_ATR)
                    with group(horizontal=True):
                        add_button(label="+2", enabled=False)
                        add_combo(items=atrL, default_value=self.DATA.R.ASI[1], width=60, tag="RASI_1", callback=self.p.upd_ATR)
            with child_window(auto_resize_y=True,auto_resize_x=True, border=True, tag="Class_skill_child"):
                add_button(label="Class Skill", enabled=False, tag="Cskill_label")
                with popup("Cskill_label", mousebutton=mvMouseButton_Left):
                    with group(horizontal=True):
                        add_button(label="Skill 1", enabled=False)
                        add_combo(items=self.DATA.C.SKILL.list, default_value=self.DATA.C.SKILL.choice[0], width=100, tag="CSKILL_0", callback=self.p.upd_data)
                    with group(horizontal=True):
                        add_button(label="Skill 2", enabled=False)
                        add_combo(items=self.DATA.C.SKILL.list, default_value=self.DATA.C.SKILL.choice[1], width=100, tag="CSKILL_1", callback=self.p.upd_data)
            with child_window(auto_resize_y=True, width=300, border=True, tag="ASI_child"):
                for index, active in enumerate(self.DATA.C.ASI.active):
                    if active:
                        with group(horizontal=True):
                            with child_window(auto_resize_y=True, auto_resize_x=True, border=True):
                                with group(horizontal=True):
                                    add_button(label=f"ASI {index}", enabled=False)
                                    add_combo(items=["ASI","FEAT"],default_value=self.DATA.C.ASI.choice[index], width=60, no_arrow_button=True,tag=f"ASIC_{index}", callback=self.p.upd_data)
                            with child_window(auto_resize_y=True, auto_resize_x=True, border=True, tag=f"ASIV_{index}"):
                                if self.DATA.C.ASI.choice[index] == "ASI":
                                    with group(horizontal=True):
                                        add_combo(items=atrL,default_value=self.DATA.C.ASI.asi[index][0],width=60, no_arrow_button=True, tag=f"ASIV_A_{index}_0", callback=self.p.upd_data)
                                        add_combo(items=atrL,default_value=self.DATA.C.ASI.asi[index][1],width=60, no_arrow_button=True, tag=f"ASIV_A_{index}_1", callback=self.p.upd_data)
                                if self.DATA.C.ASI.choice[index] == "FEAT":
                                    with group(horizontal=True):
                                        add_combo(items=featL,default_value=self.DATA.C.ASI.feat[index],width=60, no_arrow_button=True, tag=f"ASIV_F_{index}", callback=self.p.upd_data)

    def ui_ASI(self):
        delete_item("ASI_child", children_only=True)
        with group(parent="ASI_child"):
            for index, active in enumerate(self.DATA.C.ASI.active):
                if active:
                    with group(horizontal=True):
                        with child_window(auto_resize_y=True, auto_resize_x=True, border=True):
                            with group(horizontal=True):
                                add_button(label=f"ASI {index}", enabled=False)
                                add_combo(items=["ASI","FEAT"],default_value=self.DATA.C.ASI.choice[index],width=60, no_arrow_button=True, tag=f"ASIC_{index}", callback=self.p.upd_data)
                        with child_window(auto_resize_y=True, auto_resize_x=True, border=True, tag=f"ASIV_{index}"):
                            pass
    def ui_ASIC(self):
        for index, active in enumerate(self.DATA.C.ASI.active):
            if active:
                delete_item(f"ASIV_{index}", children_only=True)
                with group(parent=f"ASIV_{index}"):
                    if self.DATA.C.ASI.choice[index] == "ASI":
                        with group(horizontal=True):
                            add_combo(items=atrL,default_value=self.DATA.C.ASI.asi[index][0],width=60, no_arrow_button=True, tag=f"ASIV_A_{index}_0", callback=self.p.upd_data)
                            add_combo(items=atrL,default_value=self.DATA.C.ASI.asi[index][1],width=60, no_arrow_button=True, tag=f"ASIV_A_{index}_1", callback=self.p.upd_data)
                    if self.DATA.C.ASI.choice[index] == "FEAT":
                        with group(horizontal=True):
                            add_combo(items=featL,default_value=self.DATA.C.ASI.feat[index],width=60, no_arrow_button=True, tag=f"ASIV_F_{index}", callback=self.p.upd_data)

        
    def ui_TRAIT(self):
        delete_item("Race_Feature_child", children_only=True)
        with group(parent="Race_Feature_child"):
            for trait in self.SHEET.TRAIT:
                add_button(label=trait, enabled=False)
                add_text(self.SHEET.TRAIT[trait].Desc, wrap=250)
                    
    def ui_SPEED(self):
        pass
    
    def ui_VISION(self):
        configure_item("VISION_ui", label=self.SHEET.VISION)
        
    def ui_PB(self):
        configure_item("PB_ui", label=self.CORE.PB)
        
    def ui_ATR(self):
        for stat in atrL:
            configure_item(f"{stat}_val", label=self.ATR[stat].v) 
            configure_item(f"{stat}_mod", label=self.ATR[stat].m)
    
    def ui_SAVE(self):
        for stat in atrL:
            configure_item(f"{stat}_ST", default_value=self.ATR[stat].s)
            configure_item(f"{stat}_ST_val", label=self.ATR[stat].pbm[self.ATR[stat].s])
            

    def ui_SKILL(self):
        for skill in skillL:
            toggled = any(self.SKILL[skill].data)
            configure_item(f"{skill}_tog", default_value=toggled)
            configure_item(f"{skill}_val", label=self.ATR[self.SKILL[skill].atr].pbm[toggled])

    def ui_PROF(self):
        for prof in profL:
            for item in dprof[prof]:
                toggled = any(self.PROF[prof][item])
                ptoggled = any(self.PROF[prof][item][1:4]) 
                configure_item(f"PROF_{prof}_{item}", default_value=toggled, enabled=not ptoggled)
                
    def ui_SRACE(self):
        configure_item("SR_ui", items=dcore.R[self.CORE.R], default_value=self.CORE.SR)
    
    def ui_SCLASS(self,items):
        configure_item("SC_ui", items=items, default_value=self.CORE.SC)
    
    def ui_CLASS_SLIST(self):
        configure_item("CSKILL_0", items=self.DATA.C.SKILL.list, default_value=self.DATA.C.SKILL.choice[0])
        configure_item("CSKILL_1", items=self.DATA.C.SKILL.list, default_value=self.DATA.C.SKILL.choice[1])
        
