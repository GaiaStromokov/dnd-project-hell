#ui_upd.py
from dearpygui.dearpygui import *
from Sheet.get_set import *

from access_data.color_reference import *
import math as math
from Sheet.sizing import *
from colorist import *


        
#ANCHOR - Backend Import
from Sheet.backend import (
    stage_Level, 
    
    stage_Race, stage_Subrace, 
    stage_Race_Asi, stage_Race_Use,
    stage_Race_Spell_Use, stage_Race_Spell_Select,
    
    stage_Class, stage_Subclass,
    stage_Class_Use, stage_Class_Skill_Select,
    stage_Class_select,
    
    stage_Background, 
    stage_Background_Prof_Select,
    
    stage_Milestone_Level_Select, 
    stage_Milestone_Feat_Select, stage_Milestone_Feat_Choice, stage_Milestone_Feat_Use,
    stage_Milestone_Asi_Select,
    
    stage_Atr_Base,

    stage_Spell_Learn,
    stage_Spell_Prepare, stage_Spell_Cast, 
    
    stage_Long_Rest, stage_Health_Mod, stage_Player_HP_Mod,
    
    stage_Arcane_Ward,
    
    stage_Player_Prof_Select, stage_Player_Condition,
    
    stage_Characteristic_Input, stage_Description_Input,
    
    
    stage_Bazaar_Add_Item, stage_Backpack_Mod_Item,
    
    stage_Equip_Item
)
import shared


        
#ANCHOR - Call Back Handler
def cbh(sender, data, user_data):
    func_dict = {
        
        "Level Input":                  stage_Level,
        "Core Race":                    stage_Race,
        "Core Subrace":                 stage_Subrace,
        "Core Class":                   stage_Class,
        "Core Subclass":                stage_Subclass,
        "Core Background":              stage_Background,

        "Base Atr":                     stage_Atr_Base,

        "Race Asi":                     stage_Race_Asi,
        "Race Use":                     stage_Race_Use,
        "Race Spell Use":               stage_Race_Spell_Use,
        "Race Spell Select":            stage_Race_Spell_Select,

        
        "Milestone Level Select":       stage_Milestone_Level_Select,
        "Milestone Feat Select":        stage_Milestone_Feat_Select,
        "Milestone Feat Choice":        stage_Milestone_Feat_Choice,
        "Milestone Feat Use":           stage_Milestone_Feat_Use,
        "Milestone Asi Select":         stage_Milestone_Asi_Select,


        "Class Use":                    stage_Class_Use,
        "Class Skill Select":           stage_Class_Skill_Select,
        "Class Select":                 stage_Class_select,
        
        "Spell Learn":                  stage_Spell_Learn,
        "Spell Prepare":                stage_Spell_Prepare,
        "Spell Cast":                   stage_Spell_Cast,
        
        "Background Prof Select":       stage_Background_Prof_Select,
        
        "Long Rest":                    stage_Long_Rest,

        
        "HP":                           stage_Health_Mod,
        "Player HP Mod":                stage_Player_HP_Mod,
        
        "Arcane Ward":                  stage_Arcane_Ward,
        
        "Player Prof Input":            stage_Player_Prof_Select,
        
        "Condition":                    stage_Player_Condition,
        
        "Characteristic":               stage_Characteristic_Input,
        "Description":                  stage_Description_Input,
        
        "Bazaar Add Item":              stage_Bazaar_Add_Item,
        "Backpack Mod Item":            stage_Backpack_Mod_Item,
        
        "Equip Item":                   stage_Equip_Item
    }
    key = user_data[0]
    user_data=user_data[1:]
    print(f"{key} updating {func_dict[key].__name__}, data={data}, user_data={user_data}")
    func_dict[key](sender, data, user_data, populate_Fields)
    
    



#





# =============================================================================
# 2. UI HELPER FUNCTIONS
# =============================================================================

def check_del(tag):
    if does_item_exist(tag): delete_item(item=tag, children_only=False)

def check_con(tag):
    if does_item_exist(tag): delete_item(item=tag, children_only=True)


    
def create_attribute_row(stat: str):
    label_width=40
    value_width=30
    with group(horizontal=True):
        add_button(label=stat, enabled=False, width=label_width)
        add_button(label="", enabled=False, width=value_width, tag=f"atr_sum_{stat}")
        add_button(label="", enabled=False, width=value_width, tag=f"atr_mod_{stat}")
    with popup(f"atr_sum_{stat}", mousebutton=mvMouseButton_Left):
        with group(horizontal=True):
            add_button(label="Base", enabled=False, width=label_width)
            add_combo(items=Base_Atr_L, default_value="", width=value_width, no_arrow_button=True, user_data=["Base Atr", stat], callback=cbh, tag=f"input_atr_base_{stat}")
    with tooltip(f"atr_sum_{stat}"):
        for source in ["Base", "Race", "Feat"]:
            with group(horizontal=True):
                add_button(label=source, enabled=False, width=label_width)
                add_button(label="", enabled=False, width=25, tag=f"atr_{source}_{stat}")


def create_skill_row(skill: str):
    label_width = 100
    mod_width = 30
    with group(horizontal=True): 
        add_button(label=skill, enabled=False, width=label_width, tag=f"skill_label_{skill}")
        add_checkbox(default_value=False, enabled=False, user_data=[], callback=cbh, tag=f"input_skill_{skill}")
        add_button(label="", enabled=False, width=mod_width, tag=f"skill_mod_{skill}")
    with tooltip(f"skill_label_{skill}"):
        add_text(dict_Skill[skill]["Desc"])
        
    with tooltip(f"input_skill_{skill}"):
        for source in ["Player", "Race", "Class", "BG", "Feat"]:
            with group(horizontal=True):
                add_button(label=source, enabled=False, width=50)
                add_checkbox(default_value=False, enabled=False, user_data=[], callback=cbh, tag=f"skill_{source}_{skill}")


        
        
def create_proficiency_popup(button_tag: str, proficiency_map: dict):
    with popup(button_tag, mousebutton=mvMouseButton_Left):
        with group(horizontal=True):
            for category, items in proficiency_map.items():
                with child_window(auto_resize_x=True, auto_resize_y=True, border=True):
                    add_text(category)
                    add_separator()
                    for item in items:
                        if category == "Armor" or category == "Simple" or category == "Martial":
                            item = iName(item)
                        print(f"create prof popup: {item}")
                        add_selectable(label=item, default_value=False,  user_data=["Player Prof Input", category, item], callback=cbh, tag=f"input_prof_{category}_{item}")

    with tooltip(button_tag):
        with group(horizontal=True):
            for category, items in proficiency_map.items():
                with child_window(auto_resize_x=True, auto_resize_y=True, border=True):
                    add_text(category)
                    add_separator()
                    for item in items:
                        add_text(item, color=(0, 0, 0), tag=f"dtext_prof_{category}_{item}")




def create_ideals(name: str):
    button_tag = f"characteristic_{name}"
    with popup(button_tag, mousebutton=mvMouseButton_Left, tag=f"popup_characteristic_{name}"):
        add_input_text(default_value="", on_enter=True, user_data=["Characteristic", name], callback=cbh, tag=f"input_characteristic_{name}")
    with tooltip(button_tag, tag=f"tooltip_characteristic_{name}"):
        add_text("",tag=f"dtext_characteristic_{name}", wrap=400)

def create_description():
    with popup("characteristic_main", mousebutton=mvMouseButton_Left, tag="popup_description"):
        for item in Description_L: 
            with group(horizontal=True):
                add_button(label=item, enabled=False, width=btn_lw)
                add_input_text(default_value="", on_enter=True, width = 70, user_data=["Description", item], callback=cbh, tag=f"input_description_{item}")
    with tooltip("characteristic_main", tag="tooltip_description"):
        for item in Description_L: 
            with group(horizontal=True):
                add_button(label=item, enabled=False, width=btn_lw)
                add_text("", tag=f"dtext_description_{item}", color=c_h2, wrap=400)

        
    
    

# =============================================================================
# 3. UI COMPONENT FUNCTIONS
# =============================================================================

#ANCHOR - Window Skeleton
def W_Skeleton():
    with window(no_title_bar=True, no_close=True, autosize=True, tag="win_main"):
        with group(horizontal=True):
            with group(horizontal=False): ## Main Group
                with group(horizontal=True): 
                    with group(horizontal=False):
                        add_child_window(tag="t1 core", width=t1core_w, height=t1core_h, border=True, no_scrollbar=True)
                        add_child_window(tag="t1 health", width=t1health_w, height=t1health_h, border=True)
                        add_child_window(tag="t1 proficiency", width=t1prof_w, height=t1prof_h, border=True)
                        add_child_window(tag="t1 characteristic", width=t1char_w, height=t1char_h, border=True)
                        add_child_window(tag="t1 buffer 2", width=t1buffer2_w, height=t1buffer2_h, border=True, no_scrollbar=True)
                    with group(horizontal=False):
                        add_child_window(tag="t1 atr", width=t1atr_w, height=t1atr_h, border=True)
                        with group(horizontal=True):
                            add_child_window(tag="t1 initiative", width=t1initiative_w, height=t1initiative_h, border=True)
                            add_child_window(tag="t1 armor class", width=t1armorclass_w, height=t1armorclass_h, border=True)
                        with group(horizontal=True):
                            add_child_window(tag="t1 vision", width=t1vision_w, height=t1vision_h, border=True)
                            add_child_window(tag="t1 speed", width=t1speed_w, height=t1speed_h, border=True)
                        add_child_window(tag="t1 condition", width=t1condition_w, height=t1condition_h, border=True)
                        add_child_window(tag="t1 rest", width=t1rest_w, height=t1rest_h, border=True)
                        add_child_window(tag="t1 buffer 1", width=t1buffer1_w, height=t1buffer1_h, border=True, no_scrollbar=True)
                    with group(horizontal=False):
                        add_child_window(tag="t1 skill", width=t1skill_w, height=t1skill_h, border=True, no_scrollbar=True)
                with group(horizontal=False):
                    add_child_window(tag="t1 inventory", width=t1inventory_w, height=t1inventory_h+12, border=True, no_scrollbar=True)
            with group(horizontal=False):
                add_child_window(tag="t1 block", width=wBlockw, height=hBlockw, border=True, no_scrollbar=True)
                add_child_window(tag="t1 Wallet", width=t1wallet_w, height=t1wallet_h, border=True, no_scrollbar=True)


def t1_Wallet():
    with group(parent="t1 Wallet"):
        with group(horizontal=True):
            for i in coin_L:
                with group(horizontal=True):
                    add_button(label=i)
                    add_text(f"0", color=c_h9, tag=f"coin_{i}")
def t1_Core():
    max_w=t1core_w-16
    max_h=t1core_h-15
    with group(parent="t1 core"):
        add_button(label="Character info", enabled=False, width=max_w, height = header_h)
        with group(horizontal=True):
            add_button(label="Level", enabled=False, width=50)
            add_button(label="<", user_data=["Level Input", -1], callback=cbh, tag="input_level_decrease")
            add_button(label="12", width=25, tag="Level_val")
            add_button(label=">", user_data=["Level Input", 1], callback=cbh, tag="input_level_increase")
            add_button(label="", enabled=False, width=55, tag="pb_val")
        for source in ["Race","Subrace","Class","Subclass","Background"] :
            with group(horizontal=True):
                add_button(label=source, enabled=False, width=80)
                add_combo(width=max_w-88, no_arrow_button=True, user_data=[f"Core {source}"], callback = cbh, tag=f'input_core_{source}')
        

def t1_Atr():
    with group(parent="t1 atr"):
        max_w=t1atr_w-16
        add_button(label="Attributes", enabled=False, width=max_w, height=header_h)
        for stat in Atr_L:
            create_attribute_row(stat)


    
def t1_HP():
    with group(parent="t1 health"):
        max_w=t1health_w-16
        max_h=t1health_h-15
        add_button(label="Health", enabled=False, width=max_w, height=header_h)
        with group(horizontal=False):
            with group(horizontal=True):
                add_button(label="+", width=btn_sw, user_data=["HP","HP", 1], callback=cbh)
                add_button(label="CUR / MAX", enabled=False, width=max_w-108, tag="HP_Manager")
                add_button(label="TEMP", enabled=False, width=max_w-150)
                add_button(label="+", width=btn_sw, user_data=["HP","Temp", 1], callback=cbh)
            with group(horizontal=True):
                add_button(label="-", width=btn_sw, user_data=["HP","HP", -1], callback=cbh)
                add_button(label="", enabled=False, width=max_w-108, tag="hp_val")
                add_button(label="", enabled=False, width=max_w-150, tag="hp_temp")
                add_button(label="-", width=btn_sw, user_data=["HP","Temp", -1], callback=cbh)
    
    with popup("HP_Manager", mousebutton=mvMouseButton_Left):
        add_button(label="Max", width=btn_lw)
        add_input_int(default_value=0, width=90, user_data=["Player HP Mod"], callback=cbh, tag="input_HP_Max")

def t1_Skill():
    max_w=t1skill_w-16
    max_h=t1skill_h-15
    with group(parent="t1 skill"):
        add_button(label="Skills", enabled=False, width=max_w, height=header_h)
        for skill in Skill_L:
            create_skill_row(skill)

def t1_Init():
    with group(parent="t1 initiative"):
        add_button(label="Init", enabled=False, width=btn_mw)
        add_button(label="", enabled=False, width=btn_mw, tag="initiative_val")
    with tooltip("initiative_val"):
        for source in ["Dex", "Race", "Class"]:
            with group(horizontal=True):
                add_button(label=source, enabled=False, width=40)
                add_button(label="", enabled=False, width=25, tag=f"initiative_{source}")

def t1_AC():
    with group(parent="t1 armor class"):
        add_button(label="AC", enabled=False, width=btn_mw, tag="AC_title")
        add_button(label="", enabled=False, width=btn_mw, tag="AC_Val")

        with tooltip("AC_Val"):
            with group(horizontal=True):
                add_button(label="Base", enabled=False, width=50)
                add_button(label="", enabled=False, width=40, tag=f"AC_Base")
            with group(horizontal=True):
                add_button(label="Dex", enabled=False, width=50)
                add_button(label="", enabled=False, width=40, tag=f"AC_Dex")


def t1_Vision():
    with group(parent="t1 vision"):
        add_button(label="Vision", enabled=False, width=btn_mw)
        add_button(label="", enabled=False, width=btn_mw, tag="Dark")
    with tooltip("Dark"):
        for i in Vision_L:
            with group(horizontal=True):
                add_button(label=i, enabled=False, width=50)
                add_button(label="", enabled=False, width=40, tag=f"vision_{i}")

def t1_Speed():
    with group(parent="t1 speed"):
        add_button(label="Speed", enabled=False, width=btn_mw)
        add_button(label="", enabled=False, width=btn_mw, tag="Walk")
    with tooltip("Walk"):
        for i in Speed_L:
            with group(horizontal=True):
                add_button(label=i, enabled=False, width=50)
                add_button(label="", enabled=False, width=40, tag=f"speed_{i}")
                
        
        
def t1_Condition():
    with group(parent="t1 condition"):
        add_button(label="Conditions", enabled=False, width=h2_width, height=26, tag="condition_select")
    with popup("condition_select", mousebutton=mvMouseButton_Left):
        with child_window(auto_resize_x=True, auto_resize_y=True, border=True):
            for i in Condition_L:
                add_selectable(label=i, default_value=False, user_data=["Condition", i], callback=cbh, tag=f"input_condition_{i}")
    with tooltip("condition_select"):
        with child_window(auto_resize_x=True, auto_resize_y=True, border=True):
            for i in Condition_L:
                add_text(i, color=(0, 0, 0), tag=f"dtext_condition_{i}")

def t1_Rest():
    with group(parent="t1 rest"):
        add_button(label="Short Rest", width=h2_width, height=30, user_data=["Short Rest"], callback=cbh, tag="short_rest")
        add_button(label="Long Rest", width=h2_width, height=30, user_data=["Long Rest"], callback=cbh, tag="long_rest")


def t1_Buffer():
    pass


def t1_Prof():
    max_w=t1prof_w-16
    max_h=t1prof_h-15
    btn_w = max_w-101
    with group(parent="t1 proficiency"):
        add_button(label="Proficiencies", enabled=False, width=max_w, height=header_h)
        with group(horizontal=True):
            add_button(label="Weapons", width=btn_w, tag="prof_weapon")
            add_button(label="Armor", width=btn_w, tag="prof_armor")
        with group(horizontal=True):
            add_button(label="Tools", width=btn_w, tag="prof_tool")
            add_button(label="Languages", width=btn_w, tag="prof_lang")

    # Create popups using the helper
    create_proficiency_popup("prof_weapon", {k: set(bProf("Weapon")) & set(bCategory(k)) for k in ["Simple", "Martial"]})
    create_proficiency_popup("prof_armor", {"Armor": bProf("Armor")})
    create_proficiency_popup("prof_tool", {"Artisan": Job_L, "Gaming": Game_L, "Musical": Music_L})
    create_proficiency_popup("prof_lang", {"Languages": Lang_L})


def t1_Player_Desc():
    max_w=t1char_w-16
    max_h=t1char_h-15
    btn_w = max_w-101
    with group(parent="t1 characteristic"):
        add_button(label="Characteristics", enabled=False, width=max_w, height=header_h, tag="characteristic_main")
        with group(horizontal=True):
            add_button(label="Traits", width=btn_w, tag="characteristic_Traits")
            add_button(label="Ideals", width=btn_w, tag="characteristic_Ideals")
        with group(horizontal=True):
            add_button(label="Bonds", width=btn_w, tag="characteristic_Bonds")
            add_button(label="Flaws", width=btn_w, tag="characteristic_Flaws")
    
    # Create popups/tooltips using helpers
    for i in ideals_L:
        create_ideals(i)
    
    create_description()
    







def t1_Block():
    w1 = wBlockw - 16
    w2 = w1 - 16

    h1 = hBlockw - 40
    h2 = h1 - 15
    with group(parent="t1 block"):
        with tab_bar(tag="tabbar_block"):
            with tab(label="Features/Traits", tag="block_tab_F"):
                with child_window(width=w1, height=h1, border=True):
                    add_separator(label="Race")
                    with child_window(auto_resize_y=True, width=w2, border=True, tag="F_race_b1"):pass
                    with child_window(auto_resize_y=True, width=w2, border=True, tag="F_race_b2"):pass
                    add_separator(label="Class")
                    with child_window(auto_resize_y=True, width=w2, border=True, tag="F_class_b1"):pass
                    with child_window(auto_resize_y=True, width=w2, border=True, tag="F_class_b2"):pass
                    add_separator(label="Feat")
                    with child_window(auto_resize_y=True, width=w2, border=False):
                        with collapsing_header(label="Milestones"):
                            with child_window(auto_resize_y=True, width=w2, border=True, tag="F_milestone_b1"):
                                pass
                    with child_window(auto_resize_y=True, width=w2, border=True, tag="F_milestone_b2"):
                        pass
                    add_separator(label="Background")
                    with child_window(auto_resize_y=True, width=w2, border=True, tag="F_background_b1"):
                        pass
                    with child_window(auto_resize_y=True, width=w2, border=True, tag="F_background_b2"):
                        pass
            with tab(label="Actions", tag="block_tab_A"):
                with child_window(auto_resize_x=True, auto_resize_y=True, border=True):
                    with child_window(auto_resize_y=True, width=w2, border=True):
                        add_separator(label="Weapons")
                        add_child_window(auto_resize_y=True, width=w2, border=True, tag="cw_weapons")

def t2_Block_Weapons():
    with group(parent="cw_weapons"):
        with table(header_row=True, row_background=False, borders_innerH=True, borders_outerH=True, borders_innerV=True, resizable=True,borders_outerV=True):


            add_table_column(label="Weapon", width_stretch=True, init_width_or_weight=0)
            add_table_column(label="Range", width_stretch=True, init_width_or_weight=0)
            add_table_column(label="Hit", width_stretch=True, init_width_or_weight=0)
            add_table_column(label="Damage", width_stretch=True, init_width_or_weight=0)
            add_table_column(label="Type", width_stretch=True, init_width_or_weight=0)
            add_table_column(label="Notes", width_stretch=True, init_width_or_weight=0)
            
            for i in range(2):
                with table_row():
                    for j in weapon_atr_list:
                        add_table_cell(tag=f"wcell_{j}_{i}")


def t1_Inventory():
    with group(parent="t1 inventory"):
        with tab_bar(tag="tabbar_inventory"):
            with tab(label="Equip", tag="tab_inv_Equip"):
                add_child_window(height=t1inventory_h-25, border=True, tag="cw_inv_equip")
            with tab(label="Backpack", tag="tab_inv_backpack"):
                add_child_window(height=t1inventory_h-80, border=True, no_scrollbar=True, tag="cw_inv_backpack")
                add_child_window(height=50, border=True, tag="cw_inv_totals")
            with tab(label="Bazaar", tag="tab_inv_bazaar"):
                add_child_window(height=t1inventory_h-25, border=True, no_scrollbar=True,  tag="cw_inv_bazaar")



def t2_Inventory_Bazaar():
    with group(parent="cw_inv_bazaar"):
        with tab_bar(tag="tabbar_Bazaar"):
            for equipment_type in equipment_type_L:
                with tab(label=equipment_type, tag=f"tab_bazaar_{equipment_type}"):
                    with tab_bar(tag=f"tabbar_Bazaar_{equipment_type}"):
                        for rank in range(5):
                            rarity = item_rarity(rank)
                            with tab(label=rarity, tag=f"tab_bazaar_rarity_{equipment_type}_{rarity}"):
                                add_child_window(height=t1inventory_h - 85, border=True, no_scrollbar=True, tag=f"bazaar_rarity_{equipment_type}_{rarity}")
def load_icons():
    figure_w, figure_h, figure_channel, figure_data = load_image("image/Figure_Icon.png")
    armor_w, armor_h, armor_channel, armor_data = load_image("image/Armor_Icon.png")
    arms_w, arms_h, arms_channel, arms_data = load_image("image/Arms_Icon.png")
    body_w, body_h, body_channel, body_data = load_image("image/Body_Icon.png")
    face_w, face_h, face_channel, face_data = load_image("image/Face_Icon.png")
    hands_w, hands_h, hands_channel, hands_data = load_image("image/Hands_Icon.png")
    head_w, head_h, head_channel, head_data = load_image("image/Head_Icon.png")
    mainhand_w, mainhand_h, mainhand_channel, mainhand_data = load_image("image/MainHand_Icon.png")
    offhand_w, offhand_h, offhand_channel, offhand_data = load_image("image/OffHand_Icon.png")
    ring_w, ring_h, ring_channel, ring_data = load_image("image/Ring_Icon.png")
    shoulders_w, shoulders_h, shoulders_channel, shoulders_data = load_image("image/Shoulders_Icon.png")
    throat_w, throat_h, throat_channel, throat_data = load_image("image/Throat_Icon.png")
    waist_w, waist_h, waist_channel, waist_data = load_image("image/Waist_Icon.png")
    feet_w, feet_h, feet_channel, feet_data = load_image("image/Feet_Icon.png")

    with texture_registry(show=False):
        add_static_texture(width=figure_w, height=figure_h, default_value=figure_data, tag="figure_icon_t")
        add_static_texture(width=armor_w, height=armor_h, default_value=armor_data, tag="armor_icon_t")
        add_static_texture(width=arms_w, height=arms_h, default_value=arms_data, tag="arms_icon_t")
        add_static_texture(width=body_w, height=body_h, default_value=body_data, tag="body_icon_t")
        add_static_texture(width=face_w, height=face_h, default_value=face_data, tag="face_icon_t")
        add_static_texture(width=hands_w, height=hands_h, default_value=hands_data, tag="hands_icon_t")
        add_static_texture(width=head_w, height=head_h, default_value=head_data, tag="head_icon_t")
        add_static_texture(width=mainhand_w, height=mainhand_h, default_value=mainhand_data, tag="mainhand_icon_t")
        add_static_texture(width=offhand_w, height=offhand_h, default_value=offhand_data, tag="offhand_icon_t")
        add_static_texture(width=ring_w, height=ring_h, default_value=ring_data, tag="ring_icon_t")
        add_static_texture(width=shoulders_w, height=shoulders_h, default_value=shoulders_data, tag="shoulders_icon_t")
        add_static_texture(width=throat_w, height=throat_h, default_value=throat_data, tag="throat_icon_t")
        add_static_texture(width=waist_w, height=waist_h, default_value=waist_data, tag="waist_icon_t")
        add_static_texture(width=feet_w, height=feet_h, default_value=feet_data, tag="feet_icon_t")

def t2_Inventory_Equip():
    ebtn_w = 98
    with group(parent="cw_inv_equip"):
        with group(horizontal=False):
            with group(horizontal=True):
                with group(horizontal=False):
                    with group(horizontal=True):
                        add_image("face_icon_t")
                        with child_window(auto_resize_x=True, height=35, border=True, no_scrollbar=True):
                            add_combo(width=ebtn_w, no_arrow_button=True, user_data=["Equip Item", "Face"], callback = cbh, tag=f'input_equip_Face')  
                    with group(horizontal=True):
                        add_image("throat_icon_t")
                        with child_window(auto_resize_x=True, auto_resize_y=True, border=True, no_scrollbar=True):
                            add_combo(width=ebtn_w, no_arrow_button=True, user_data=["Equip Item", "Throat"], callback = cbh, tag=f'input_equip_Throat')
                    with group(horizontal=True):
                        add_image("body_icon_t")
                        with child_window(auto_resize_x=True, auto_resize_y=True, border=True, no_scrollbar=True):
                            add_combo(width=ebtn_w, no_arrow_button=True, user_data=["Equip Item", "Body"], callback = cbh, tag=f'input_equip_Body')
                    with group(horizontal=True):
                        add_image("hands_icon_t")
                        with child_window(auto_resize_x=True, auto_resize_y=True, border=True, no_scrollbar=True):
                            add_combo(width=ebtn_w, no_arrow_button=True, user_data=["Equip Item", "Hands"], callback = cbh, tag=f'input_equip_Hands')
                    with group(horizontal=True):
                        add_image("waist_icon_t")
                        with child_window(auto_resize_x=True, auto_resize_y=True, border=True, no_scrollbar=True):
                            add_combo(width=ebtn_w, no_arrow_button=True, user_data=["Equip Item", "Waist"], callback = cbh, tag=f'input_equip_Waist')
                    with group(horizontal=True):
                        add_image("feet_icon_t")
                        with child_window(auto_resize_x=True, auto_resize_y=True, border=True, no_scrollbar=True):
                            add_combo(width=ebtn_w, no_arrow_button=True, user_data=["Equip Item", "Feet"], callback = cbh, tag=f'input_equip_Feet')
                    with group(horizontal=True):
                        add_image("mainhand_icon_t")
                        with child_window(auto_resize_x=True, auto_resize_y=True, border=True, no_scrollbar=True):
                            add_combo(width=ebtn_w, no_arrow_button=True, user_data=["Equip Item", "Main Hand"], callback = cbh, tag=f'input_equip_MainHand')
                add_image("figure_icon_t")
                with group(horizontal=False):
                    with group(horizontal=True):
                        with child_window(auto_resize_x=True, auto_resize_y=True, border=True, no_scrollbar=True):
                            add_combo(width=ebtn_w, no_arrow_button=True, user_data=["Equip Item", "Head"], callback = cbh, tag=f'input_equip_Head')
                        add_image("head_icon_t")
                    with group(horizontal=True):
                        with child_window(auto_resize_x=True, auto_resize_y=True, border=True, no_scrollbar=True):
                            add_combo(width=ebtn_w, no_arrow_button=True, user_data=["Equip Item", "Shoulders"], callback = cbh, tag=f'input_equip_Shoulders')
                        add_image("shoulders_icon_t")
                    with group(horizontal=True):
                        with child_window(auto_resize_x=True, auto_resize_y=True, border=True, no_scrollbar=True):
                            add_combo(width=ebtn_w, no_arrow_button=True, user_data=["Equip Item", "Armor"], callback = cbh, tag=f'input_equip_Armor')
                        add_image("armor_icon_t")
                    with group(horizontal=True):
                        with child_window(auto_resize_x=True, auto_resize_y=True, border=True, no_scrollbar=True):
                            add_combo(width=ebtn_w, no_arrow_button=True, user_data=["Equip Item", "Arms"], callback = cbh, tag=f'input_equip_Arms')
                        add_image("arms_icon_t")
                    with group(horizontal=True):
                        with child_window(auto_resize_x=True, auto_resize_y=True, border=True, no_scrollbar=True):
                            add_combo(width=ebtn_w, no_arrow_button=True, user_data=["Equip Item", "Ring 1"], callback = cbh, tag=f'input_equip_Ring1')
                        add_image("ring_icon_t")
                    with group(horizontal=True):
                        with child_window(auto_resize_x=True, auto_resize_y=True, border=True, no_scrollbar=True):
                            add_combo(width=ebtn_w, no_arrow_button=True, user_data=["Equip Item", "Ring 2"], callback = cbh, tag=f'input_equip_Ring2')
                        add_image("ring_icon_t")
                    with group(horizontal=True):
                        with child_window(auto_resize_x=True, auto_resize_y=True, border=True, no_scrollbar=True):
                            add_combo(width=ebtn_w, no_arrow_button=True, user_data=["Equip Item", "Off Hand"], callback = cbh, tag=f'input_equip_OffHand')
                        add_image("offhand_icon_t")


#ANCHOR - Initiative the UI
def init_ui():
    init_ui_W()
    init_ui_t1()
    init_ui_t2()
    init_ui_t3()

def init_ui_W():
    load_icons()
    W_Skeleton()
    
def init_ui_t1():
    t1_Core()
    t1_HP()
    t1_Prof()
    t1_Player_Desc()
    t1_Buffer()
    t1_Atr()
    t1_Init()
    t1_AC()
    t1_Vision()
    t1_Speed()
    t1_Condition()
    t1_Rest()
    t1_Skill()
    t1_Block()
    t1_Inventory()
    t1_Wallet()
def init_ui_t2():
    t2_Block_Weapons()
    t2_Inventory_Bazaar()
    t2_Inventory_Equip()
    
def init_ui_t3():
    pass

#ANCHOR - Populate Start
def populate_Start():
    populate_Fields("All")

#ANCHOR - Populate Fields Handler
def populate_Fields(source):
    field_map = {
        "All": populate_All,
        "Level": populate_All,
        "Long Rest": populate_All,
        
        "Race": populate_Race,
        "Class": populate_Class,
        "Background": populate_Background,
        "Atr": populate_Atr,
        
        "Spell": populate_Spell,
        
        "Arcane Ward": populate_Arcane_Ward,
        
        "Milestone": populate_Milestone,
        
        "Background Prof Select": populate_Background,
        
        "Generic": populate_generic,
        
        
        "HP": populate_HP,
        
        "Condition": populate_Condition,
        
        "Characteristic": populate_characteristics,
        "Description": populate_characteristics,
        
        "Bazaar Add Item": populate_Inventory,
        
        "Reset Backpack": populate_Inventory,
        
        "Mod Backpack": populate_Backpack,
        
        "Mod Equip": populate_Equip,

        
        "Mod Armor": populate_Armor
        
    }
    field_map[source]()

def populate_All():
    fields_static()
    fields_dynamic()

def populate_Race():
    populate_generic()
    dyn_F_race()
    dyn_F_milestone()
    
def populate_Class():
    populate_generic()
    dyn_F_class()
    dyn_block_spells()


def populate_Background():
    populate_generic()
    dyn_F_background()



def populate_Atr():
    st_atr()
    st_skill()
    st_initiative()
    dyn_block_A()
    dyn_F_race()
    dyn_F_class()
    dyn_F_milestone()
    dyn_block_spells()

def populate_Spell():
    spell_learn_ammounts()
    spell_learn_check()
    
    spell_prepare_ammounts()
    spell_prepare_cells()

    spell_cast_ammounts()
    spell_cast_cells()
    dyn_F_class()

def populate_generic():
    st_core()
    st_skill()
    st_HP()
    st_initiative()
    st_vision()
    st_speed()
    st_prof()

def populate_HP():
    st_HP()
    
def populate_Arcane_Ward():
    configure_item("Arcane_Ward_HP", label=f"{aClass()["Arcane Ward"]["HP"]["Current"]} / {aClass()["Arcane Ward"]["HP"]["Max"]}")

def populate_Milestone():
    populate_Atr()

def populate_Condition():
    st_condition()

def fields_static():
    st_core()
    st_atr()
    st_skill()
    st_HP()
    st_armor()
    st_initiative()
    st_vision()
    st_speed()
    st_condition()
    st_prof()
    st_characteristics()
    st_Inventory_Bazaar()

def fields_dynamic():
    dyn_block()
    dyn_Inventory()

def populate_characteristics():
    st_characteristics()

def populate_Inventory():
    dyn_Inventory()

def populate_Backpack():
    ensure_Backpack()

def populate_Equip():
    dyn_block_A()
    dyn_Inventory_Equip()
    


def populate_Armor():
    st_armor()

# #--------------------------------------------------------------------



#ANCHOR - Static Functions

def st_core():
    configure_item("Level_val", label=vLevel())
    configure_item("pb_val", label = f"PB: +{vPB()}")
    configure_item("input_core_Race", items=Race_L, default_value=vRace())
    configure_item("input_core_Subrace", items=Race_Options[vRace()], default_value=vSubrace())
    configure_item("input_core_Class", items=Class_L, default_value=vClass())
    configure_item("input_core_Subclass", items=Class_Options[vClass()] if valid_class() else [], default_value=vSubclass())
    configure_item("input_core_Background", items=Background_L, default_value=vBackground())



def st_atr():
    data=kAtr()
    for atr in Atr_L:
        cdata=data[atr]
        configure_item(f"atr_sum_{atr}", label = cdata.Val)
        configure_item(f"atr_mod_{atr}", label = cdata.Mod)
        configure_item(f"input_atr_base_{atr}", default_value = cdata.Base)
        configure_item(f"atr_Base_{atr}", label = cdata.Base)
        configure_item(f"atr_Race_{atr}", label = cdata.Rasi)
        configure_item(f"atr_Feat_{atr}", label = cdata.Milestone)


def st_skill():
    for skill in Skill_L:
        cdata=pSkill()[skill]
        configure_item(f"input_skill_{skill}", default_value=cdata)
        configure_item(f"skill_mod_{skill}", label=skill_text(skill))
        # configure_item(f"skill_Player_{skill}", default_value=skill in cdata["Player"])
        # configure_item(f"skill_Race_{skill}", default_value=skill in cdata["Race"])
        # configure_item(f"skill_Class_{skill}", default_value=skill in cdata["Class"])
        # configure_item(f"skill_BG_{skill}", default_value=skill in cdata["Background"])
        # configure_item(f"skill_Feat_{skill}", default_value=skill in cdata["Feat"])
        

def st_HP():

    configure_item("hp_val", label = f"{kHP()["Current"]} / {kHP()["Sum"]}")
    configure_item("hp_temp", label = kHP()["Temp"])
    set_value("input_HP_Max", kHP()["Player"])
    

    
def st_initiative():
    configure_item("initiative_val", label = Initiative_text())
    configure_item("initiative_Dex", label = kAtr()["DEX"]["Mod"])
    configure_item("initiative_Race", label = kInitiative()["Race"])
    configure_item("initiative_Class", label = kInitiative()["Class"])
    
def st_vision():
    cdata=pVision()
    configure_item("Dark",label = cdata["Dark"])
    # for i in Vision_L:
    #     configure_item(f"vision_{i}",label = cdata[i]["Val"])

def st_speed():
    cdata=pSpeed()
    configure_item("Walk",label = cdata["Walk"])
    # for i in Speed_L: configure_item(f"speed_{i}",label = cdata[i]["Val"])

def st_armor():
    configure_item("AC_Val", label = kAC().Sum)
    configure_item("AC_Base", label = kAC().Base)
    configure_item("AC_Dex", label = kAC().Dex)

def t1_AC():
    with group(parent="t1 armor class"):
        add_button(label="AC", enabled=False, width=btn_mw, tag="AC_title")
        add_button(label="", enabled=False, width=btn_mw, tag="AC_Val")

        with tooltip("AC_Val"):
            with group(horizontal=True):
                add_button(label="Base", enabled=False, width=50)
                add_button(label="", enabled=False, width=40, tag=f"AC_Base")
            with group(horizontal=True):
                add_button(label="Dex", enabled=False, width=50)
                add_button(label="", enabled=False, width=40, tag=f"AC_Dex")
    
        
def st_condition():
    for i in Condition_L:
        configure_item(f"input_condition_{i}",default_value = kCondition()[i])
        configure_item(f"dtext_condition_{i}", color = condition_color(i))

def st_characteristics():
    cdata=kCharacteristic()
    for i in ideals_L:
        configure_item(f"input_characteristic_{i}", default_value=cdata[i])
        configure_item(f"dtext_characteristic_{i}", default_value=cdata[i])
    
    cdata=kDescription()
    for i in Description_L:
        configure_item(f"input_description_{i}", default_value=cdata[i])
        configure_item(f"dtext_description_{i}", default_value=cdata[i])


def st_prof():
    cdata = pProf()
    print(f"cdata: {cdata}")
    print(f"set {set(bProf("Weapon")) & set(bCategory("Simple"))}")
    for i in set(bProf("Weapon")) & set(bCategory("Simple")):
        i = iName(i)
        print(f"st prof: {i}")
        configure_item(f"input_prof_Simple_{i}", default_value=i in cdata["Weapon"])
        configure_item(f"dtext_prof_Simple_{i}", color=prof_color("Weapon", i))
    for i in set(bProf("Weapon")) & set(bCategory("Martial")):
        i = iName(i)
        configure_item(f"input_prof_Martial_{i}", default_value=i in cdata["Weapon"])
        configure_item(f"dtext_prof_Martial_{i}", color=prof_color("Weapon", i))
    for i in bProf("Armor"):
        i = iName(i)
        configure_item(f"input_prof_Armor_{i}", default_value=i in cdata["Armor"])
        configure_item(f"dtext_prof_Armor_{i}", color=prof_color("Armor", i))
    for i in Job_L:
        configure_item(f"input_prof_Artisan_{i}", default_value=i in cdata["Tool"])
        configure_item(f"dtext_prof_Artisan_{i}", color=prof_color("Tool", i))
    for i in Game_L:
        configure_item(f"input_prof_Gaming_{i}", default_value=i in cdata["Tool"])
        configure_item(f"dtext_prof_Gaming_{i}", color=prof_color("Tool", i))
    for i in Music_L:
        configure_item(f"input_prof_Musical_{i}", default_value=i in cdata["Tool"])
        configure_item(f"dtext_prof_Musical_{i}", color=prof_color("Tool", i))
    for i in Lang_L:
        configure_item(f"input_prof_Languages_{i}", default_value=i in cdata["Lang"])
        configure_item(f"dtext_prof_Languages_{i}", color=prof_color("Lang", i))





def dyn_block():
    dyn_block_A()
    dyn_block_F()
    dyn_block_spells()




#ANCHOR - Spell Functions




def dyn_block_A():
    clear_block_A()
    Versatile = weapon_versatile()
    for hand, idx in [("Main Hand", 0), ("Off Hand", 1)]:
        if hand == "Off Hand" and Versatile: continue
        item = Current_Equip(hand)
        if not item: continue
        cdata = sHand(item)
        with group(parent=f"wcell_Name_{idx}"): add_text(cdata.Name)
        with group(parent=f"wcell_Range_{idx}"): add_text(cdata.Range)
        with group(parent=f"wcell_Hit_{idx}"): 
            with group(horizontal=True):
                add_text(cdata.hSign)
                add_text(cdata.hNum, color=cdata.hColor)
        with group(parent=f"wcell_Damage_{idx}"): 
            with group(horizontal=True):
                add_text(cdata.dDice)
                add_text(cdata.dSign)
                add_text(cdata.dNum, color=cdata.dColor)
        with group(parent=f"wcell_Type_{idx}"): 
            add_text(cdata.dType, tag=f"wdtype_{idx}")
            check_del(f"tooltip_dtype_{idx}")
            with tooltip(f"wdtype_{idx}", tag=f"tooltip_dtype_{idx}"):
                add_text(weapon_dtype_d[cdata.dType])

        with group(parent=f"wcell_Notes_{idx}"):
            with group(horizontal=True):
                for i in cdata.Prop: 
                    add_text(weapon_prop_sc[i], tag=f"wprop_{idx}_{i}")
                    check_del(f"tooltip_type_{i}_{idx}")
                    with tooltip(f"wprop_{idx}_{i}", tag=f"tooltip_type_{i}_{idx}"):
                        add_text(i, color=c_h1)
                        add_text(weapon_prop_d[i], wrap=240)

                    

def clear_block_A():
    for atr in weapon_atr_list:
        delete_item(f"wcell_{atr}_0", children_only=True)
        delete_item(f"wcell_{atr}_1", children_only=True)

        


def dyn_block_spells():
    if valid_spellclass():
        if not does_item_exist("block_tab_spells"):
            with tab(label="Spell", tag="block_tab_spells", parent="tabbar_block"):
                with child_window(auto_resize_y=True, width=415, border=True):
                    with tab_bar(tag="tab_Spell"):
                        with tab(label="Cast", tag="tab_cast"):
                            add_child_window(auto_resize_y=True, width=400, border=True, tag="cw_cast")
                        with tab(label="Learn", tag="tab_learn"):
                            add_child_window(auto_resize_y=True, width=400, border=True, tag="cw_learn")
                        with tab(label="Prepare", tag="tab_prepare"):
                            add_child_window(auto_resize_y=True, width=400, border=True, tag="cw_prepare")
        block_post_spells()
    else:
        check_del("block_tab_spells")

def block_post_spells():
    spell_learn()
    spell_prepare()
    spell_cast()

def spell_cast():
    delete_item("cw_cast", children_only=True)
    with group(parent="cw_cast"):
        add_child_window(auto_resize_y=True, width=380, no_scrollbar=True, border=True, tag="cast_ammounts")
        add_child_window(auto_resize_y=True, width=380, no_scrollbar=True, border=True, tag="cast_cells")
    spell_cast_ammounts()
    spell_cast_cells()
    
def spell_cast_ammounts():
    delete_item("cast_ammounts", children_only=True)
    with group(parent="cast_ammounts"):
            with group(horizontal=True):
                add_button(label="Abil", enabled=False, width=40)
                add_text(dSpell()["abil"], color=c_h2, tag="cast_Abil")
                add_button(label="Atk", enabled=False, width=40)
                add_text(dSpell()["atk"], color=c_h2, tag="cast_Atk")
                add_button(label="DC", enabled=False, width=40)
                add_text(dSpell()["dc"], color=c_h2, tag="cast_DC")
                
def spell_cast_cells():
    delete_item("cast_cells", children_only=True)
    with group(parent="cast_cells"):
        for level in range(0,dSpell()["max_spell_level"]+1):
            if kSpell()["Book"][level]:
                with group(horizontal=False):
                    with group(horizontal=True):
                        add_text(f"Level {level}" if level != 0 else "Cantrip", color=c_h1)
                        if level != 0:
                            for idx,val in enumerate(kSpell().Slot[level]):
                                add_checkbox(default_value=val, enabled=False)
                    if level == 0:
                        for spell in kSpell()["Book"][0]:
                            with group(horizontal=True):
                                add_button(label="Will", user_data=["Spell Cast", 0], callback=cbh, tag=f"input_SSpell_data_{0}_{spell}")
                                add_text(spell, color=c_h2, tag=f"spell_cast_{spell}")
                                check_del(f"tooltip_spell_cast_{spell}")
                                with tooltip(f"spell_cast_{spell}", tag=f"tooltip_spell_cast_{spell}"):
                                    spell_detail(spell)
                    else:
                        for spell in kSpell()["Prepared"][level]:
                            with group(horizontal=True):
                                add_button(label="Cast", user_data=["Spell Cast", level], callback=cbh, tag=f"input_SSpell_data_{level}_{spell}")
                                add_text(spell, color=c_h2, tag=f"spell_cast_{spell}")
                                check_del(f"tooltip_spell_cast_{spell}")
                                with tooltip(f"spell_cast_{spell}", tag=f"tooltip_spell_cast_{spell}"):
                                    spell_detail(spell)

def spell_learn():
    delete_item("cw_learn", children_only=True)
    with group(parent="cw_learn"):
        add_child_window(auto_resize_y=True, width=380, no_scrollbar=True, border=True, tag="learn_ammounts")
        add_child_window(auto_resize_y=True, width=380, no_scrollbar=True, border=True, tag="learn_cells")
    spell_learn_ammounts()
    spell_learn_cells()

def spell_learn_ammounts():
    delete_item("learn_ammounts", children_only=True)
    with group(parent="learn_ammounts"):
        with group(horizontal=True):
            add_text("Cantrips", color=c_h1)
            add_text(cantrips_known(), color=c_text, tag="Cantrip Known")
            add_text("/", color=c_text)
            add_text(dSpell()["cantrips_available"], color=c_text, tag="Cantrip num")
            add_text("Spells", color=c_h1)
            add_text(spells_known(), color=c_text, tag="Spell Known")
            add_text("/", color=c_text)
            add_text(dSpell()["spells_available"], color=c_text, tag="Spell num")
        
def spell_learn_cells():
    delete_item("learn_cells", children_only=True)
    with group(parent="learn_cells"):
        for i in range(0,dSpell()["max_spell_level"]+1):
            with collapsing_header(label=f"Level {i}", tag = f"ch_learn_cells_{i}"):
                for spell in get_spell_list(dSpell()["Caster"], i):
                    add_selectable(label=spell, default_value=spell in kSpell()["Book"][i],width=370, user_data=["Spell Learn", spell, i], callback=cbh, tag=f"input_Slearn_{spell}")
                    check_del(f"tooltip_Learn_{spell}")
                    with tooltip(f"input_Slearn_{spell}", tag=f"tooltip_Learn_{spell}"):
                        spell_detail(spell)


def spell_learn_check():
    for level in range(0,dSpell()["max_spell_level"]+1):
        for spell in get_spell_list(vClass(), level): configure_item(f"input_Slearn_{spell}", default_value=spell in kSpell()["Book"][level])

                
                
def spell_prepare():
    delete_item("cw_prepare", children_only=True)
    with group(parent="cw_prepare"):
        add_child_window(auto_resize_y=True, width=380, no_scrollbar=True, border=True, tag="prepare_ammounts")
        add_child_window(auto_resize_y=True, width=380, no_scrollbar=True, border=True, tag="prepare_cells")
    spell_prepare_ammounts()
    spell_prepare_cells()
    

            
def spell_prepare_ammounts():
    delete_item("prepare_ammounts", children_only=True)
    with group(parent="prepare_ammounts"):
        with group(horizontal=True):
            add_text("Prepared", color=c_h1)
            add_text(spells_prepared(), color=c_text, tag="Prepared current")
            add_text("/", color=c_text)
            add_text(dSpell()["prepared_available"], color=c_text, tag="Prepared Num")
            
            


def spell_prepare_cells():
    delete_item("prepare_cells", children_only=True)
    with group(parent="prepare_cells"):
        for i in range(1,dSpell()["max_spell_level"]+1):
            add_separator(label=f"Level {i}")
            with child_window(height=100,width=370, no_scrollbar=True, border=True):
                for spell in kSpell()["Book"][i]:
                    add_selectable(label=spell, default_value=spell in kSpell()["Prepared"][i],width=370, user_data=["Spell Prepare", spell, i], callback=cbh, tag=f"input_Sprepare_{spell}")
                    check_del(f"tooltip_Prepared_{spell}")
                    with tooltip(f"input_Sprepare_{spell}", tag=f"tooltip_Prepared_{spell}"): spell_detail(spell)



#ANCHOR - Features and traits
def dyn_block_F():
    dyn_F_milestone()
    dyn_F_race()
    dyn_F_class()
    dyn_F_background()
    

#ANCHOR - FT RACE
def dyn_F_race():
    
    dyn_F_race_asi()
    delete_item(item="F_race_b2", children_only=True)
    globals()[f"{vRace()}_window"]()


def dyn_F_race_asi():
    delete_item(item="F_race_b1", children_only=True)
    with group(parent="F_race_b1"):
        with group(horizontal=True):
            add_text("Ability Score Increase: +1/+2", color=c_h1)
            add_combo(items=Atr_L, default_value=dRace().Rasi[0],  width=50, no_arrow_button=True, user_data=["Race Asi", 0], callback=cbh, tag="input_Rasi_1")
            add_combo(items=Atr_L, default_value=dRace().Rasi[1],  width=50, no_arrow_button=True, user_data=["Race Asi", 1], callback=cbh,  tag="input_Rasi_2")
            add_button(label="Clear", enabled=True, width=50, user_data=["Race Asi","Clear"], callback=cbh, tag="input_Rasi_clear")




#ANCHOR - FT CLASS

def dyn_F_class():
    dyn_F_class_Skill_Select()
    delete_item(item="F_class_b2", children_only=True)
    globals()[f"{vClass()}_window"]()


def dyn_F_class_Skill_Select():
    delete_item("F_class_b1", children_only=True)
    with group(parent="F_class_b1"):
        with group(horizontal=True):
            add_text("Skill Select", color=c_h1)
            for idx,key in enumerate(sClass()):
                add_combo(items=dl[f"{vClass()} Skills"], default_value=key,  width=100, no_arrow_button=True, user_data=["Class Skill Select",idx], callback=cbh, tag=f"input_Cskillselect_{idx}")
            add_button(label = "Clear", user_data=["Class Skill Select", "Clear"], callback=cbh, tag=f"input_Cskillselect_Clear")

#ANCHOR - FT FEAT 

def dyn_F_milestone():
    
    dyn_F_Level_Select()
    delete_item(item="F_milestone_b2", children_only=True)
    for feat in kMilestone()["Feat"]:
        if feat: 
            func = f"{feat.replace(' ', '')}_window"
            if func in globals(): globals()[func]()




def dyn_F_Level_Select():
    delete_item(item="F_milestone_b1", children_only=True)
    with group(parent="F_milestone_b1"):
        for i in range(cMilestone()):
            with group(horizontal=True):
                add_text(f"Milestone {i}: ", color=c_h1)
                data = kMilestone()["Select"][i]
                add_combo(items=["Feat", "Asi", "Clear"], default_value=data,  width=50, no_arrow_button=True, user_data=["Milestone Level Select", i], callback=cbh, tag=f"input_Milestone_Level_Select_{i}")
                if data == "Feat":
                    cdata = kMilestone()["Feat"][i]
                    add_combo(items=Feat_L, default_value=cdata,  width=150, no_arrow_button=True, user_data=["Milestone Feat Select", i], callback=cbh, tag=f"input_Milestone_Feat_Select_{i}")
                elif data == "Asi":
                    cdata = kMilestone()["Asi"][i]
                    add_combo(items=Atr_L, default_value=cdata[0],  width=50, no_arrow_button=True, user_data=["Milestone Asi Select", i, 0], callback=cbh, tag=f"input_Milestone_Asi_Select_{i}_0")
                    add_combo(items=Atr_L, default_value=cdata[1],  width=50, no_arrow_button=True, user_data=["Milestone Asi Select", i, 1], callback=cbh, tag=f"input_Milestone_Asi_select_{i}_1")


#ANCHOR - FT Background

def dyn_F_background():
    
    dyn_F_background_Prof_Select()
    delete_item(item="F_background_b2", children_only=True)
    Background_window()



def dyn_F_background_Prof_Select():
    delete_item("F_background_b1", children_only=True)
    data = dBackground()["Prof"]
    with group(parent="F_background_b1"):
        with group(horizontal=True):
            add_text("Skill Select", color=c_h1)
            for key in data:
                for idx, val in enumerate(data[key]["Select"]):
                    add_combo(items = ["Clear"] + dl[vBackground()][key], default_value=val, width=100, no_arrow_button=True, user_data=["Background Prof Select", key, idx], callback=cbh, tag=f"input_Background_Prof_Select_{key}_{idx}")

def Background_window():
    Background_Feature_Map = {
        "Empty": ["No Feature", "You have no special feature from your background."],
        "Acolyte": [
            "Shelter of the Faithful",
            "As an acolyte, you command the respect of those who share your faith, and you can perform the religious ceremonies of your deity. You and your adventuring companions can expect to receive free healing and care at a temple, shrine, or other established presence of your faith, though you must provide any material components needed for spells. Those who share your religion will support you (but only you) at a modest lifestyle. You might also have ties to a specific temple dedicated to your chosen deity or pantheon, and you have a residence there. This could be the temple where you used to serve, if you remain on good terms with it, or a temple where you have found a new home. While near your temple, you can call upon the priests for assistance, provided the assistance you ask for is not hazardous and you remain in good standing with your temple."
        ],
        "Charlatan": [
            "False Identity",
            "You have created a second identity that includes documentation, established acquaintances, and disguises that allow you to assume that persona. Additionally, you can forge documents including official papers and personal letters, as long as you have seen an example of the kind of document or the handwriting you are trying to copy"
        ],
        "Criminal": [
            "Criminal Contact",
            "You have a reliable and trustworthy contact who acts as your liaison to a network of other criminals. You know how to get messages to and from your contact, even over great distances; specifically, you know the local messengers, corrupt caravan masters, and seedy sailors who can deliver messages for you."
        ],
        "Entertainer": [
            "By Popular Demand",
            "You can always find a place to perform, usually in an inn or tavern but possibly with a circus, at a theater, or even in a noble's court. At such a place, you receive free lodging and food of a modest or comfortable standard (depending on the quality of the establishment), as long as you perform each night. In addition, your performance makes you something of a local figure. When strangers recognize you in a town where you have performed, they typically take a liking to you."
        ],
        "FolkHero": [
            "Rustic Hospitality",
            "Since you come from the ranks of the common folk, you fit in among them with ease. You can find a place to hide, rest, or recuperate among other commoners, unless you have shown yourself to be a danger to them. They will shield you from the law or anyone else searching for you, though they will not risk their lives for you."
        ],
        "GuildArtisan": [
            "Guild Membership",
            "As an established and respected member of a guild, you can rely on certain benefits that membership provides. Your fellow guild members will provide you with lodging and food if necessary, and pay for your funeral if needed. In some cities and towns, a guildhall offers a central place to meet other members of your profession, which can be a good place to meet potential patrons, allies, or hirelings. Guilds often wield tremendous political power. If you are accused of a crime, your guild will support you if a good case can be made for your innocence or the crime is justifiable. You can also gain access to powerful political figures through the guild, if you are a member in good standing. Such connections might require the donation of money or magic items to the guild's coffers. You must pay dues of 5 gp per month to the guild. If you miss payments, you must make up back dues to remain in the guild's good graces."
        ],
        "Hermit": [
            "Discovery",
            "The quiet seclusion of your extended hermitage gave you access to a unique and powerful discovery. The exact nature of this revelation depends on the nature of your seclusion. It might be a great truth about the cosmos, the deities, the powerful beings of the outer planes, or the forces of nature. It could be a site that no one else has ever seen. You might have uncovered a fact that has long been forgotten, or unearthed some relic of the past that could rewrite history. It might be information that would be damaging to the people who or consigned you to exile, and hence the reason for your return to society."
        ],
        "Noble": [
            "Position of Privilege",
            "Thanks to your noble birth, people are inclined to think the best of you. You are welcome in high society, and people assume you have the right to be wherever you are. The common folk make every effort to accommodate you and avoid your displeasure, and other people of high birth treat you as a member of the same social sphere. You can secure an audience with a local noble if you need to."
        ],
        "Outlander": [
            "Wanderer",
            "You have an excellent memory for maps and geography, and you can always recall the general layout of terrain, settlements, and other features around you. In addition, you can find food and fresh water for yourself and up to five other people each day, provided that the land offers berries, small game, water, and so forth."
        ],
        "Sage": [
            "Researcher",
            "When you attempt to learn or recall a piece of lore, if you do not know that information, you often know where and from whom you can obtain it. Usually, this information comes from a library, scriptorium, university, or a sage or other learned person or creature. Your DM might rule that the knowledge you seek is secreted away in an almost inaccessible place, or that it simply cannot be found. Unearthing the deepest secrets of the multiverse can require an adventure or even a whole campaign."
        ],
        "Sailor": [
            "Ship's Passage",
            "When you need to, you can secure free passage on a sailing ship for yourself and your adventuring companions. You might sail on the ship you served on, or another ship you have good relations with (perhaps one captained by a former crewmate). Because you're calling in a favor, you can't be certain of a schedule or route that will meet your every need. Your Dungeon Master will determine how long it takes to get where you need to go. In return for your free passage, you and your companions are expected to assist the crew during the voyage."
        ],
        "Soldier": [
            "Military Rank",
            "You have a military rank from your career as a soldier. Soldiers loyal to your former military organization still recognize your authority and influence, and they defer to you if they are of a lower rank. You can invoke your rank to exert influence over other soldiers and requisition simple equipment or horses for temporary use. You can also usually gain access to friendly military encampments and fortresses where your rank is recognized."
        ],
        "Urchin": [
            "City Secrets",
            "You know the secret patterns and flow to cities and can find passages through the urban sprawl that others would miss. When you are not in combat, you (and companions you lead) can travel between any two locations in the city twice as fast as your speed would normally allow."
        ]
    }
    data = Background_Feature_Map[vBackground()]
    Name = data[0]
    Desc = data[1]
    
    delete_item("F_background_b2", children_only=True)
    with group(parent="F_background_b2"):
        add_text(Name, color=c_h1, tag=Name)
        check_del(f"tooltip_Background_{Name}")
        with tooltip(Name, tag=f"tooltip_Background_{Name}"): add_text(Desc, color=c_text, wrap=avg_wrap)
        






#------------------------------------------------


#ANCHOR - FEATS

def Actor_window():
    d1 = "Gain advantage on Deception and Performance checks when trying to pass yourself off as a different person."
    d2 = f"You can mimic the speech of another person or the sounds made by other creatures. You must have heard the person speaking, or heard the creature make the sound, for at least 1 minute. A successful Wisdom Insight check contested by your {kSkill()["Deception"]["Mod"]:+d} Deception check allows a listener to determine that the effect is faked."

    with group(parent="F_milestone_b2"):
        add_text("Actor", color=c_h1, tag="Actor")
        add_text(d1, color=c_text, wrap=avg_wrap)
        add_text(d2, color=c_text, wrap=avg_wrap)


def Alert_window():
    d1 = "You can't be surprised while you are conscious."
    d2 = "Other creatures don't gain advantage on attack rolls against you as a result of being unseen by you."
    
    with group(parent="F_milestone_b2"):
        add_text("Alert", color=c_h1, tag="Alert")
        add_text(d1, color=c_text, wrap=avg_wrap)
        add_text(d2, color=c_text, wrap=avg_wrap)

def Athlete_window():
    feat = "Athlete"
    d1 = "When you are prone, standing up uses only 5 feet of your movement."
    d2 = "Climbing doesn't cost you extra movement."
    d3 = "You can make a running long jump or a running high jump after moving only 5 feet on foot, rather than 10 feet."
    
    with group(parent="F_milestone_b2"):
        
        add_text(feat, color=c_h1, tag=feat)
        add_text(d1, color=c_text, wrap=avg_wrap)
        add_text(d2, color=c_text, wrap=avg_wrap)
        add_text(d3, color=c_text, wrap=avg_wrap)
        check_del(f"popup_{feat}")
        with popup(feat, mousebutton=mvMouseButton_Left, max_size=[500,400], tag=f"popup_{feat}"):
            with group(horizontal=False):
                add_combo(items=["Clear"]+dl[feat], default_value=kMilestone()()["Data"][feat]["Select"][0], width=50, no_arrow_button=True, user_data=["Milestone Feat Choice",feat, 0], callback=cbh, tag=f"input_Feat_Choice_{feat}")

def Charger_window():
    d1 = "When you use your action to Dash, you can use a bonus action to make one melee weapon attack or shove a creature, and if you moved at least 10 feet in a straight line immediately before taking this bonus action, you gain a +5 bonus to the attack's damage roll or push the target with extra force."
    d2 = "When you use the Attack action and attack with a melee weapon on your turn, you can use a bonus action to try to shove a creature within 5 feet of you. If you moved at least 10 feet in a straight line immediately before this shove, you get a +5 bonus to the check."
    
    with group(parent="F_milestone_b2"):
        add_text("Charger", color=c_h1, tag="Charger")
        add_text(d1, color=c_text, wrap=avg_wrap)
        add_text(d2, color=c_text, wrap=avg_wrap)

def CrossbowExpert_window():
    d1 = "You ignore the loading quality of crossbows with which you are proficient."
    d2 = "Being within 5 feet of a hostile creature doesn't impose disadvantage on your ranged attack rolls."
    d3 = "When you use the Attack action and attack with a one-handed weapon, you can use a bonus action to fire a hand crossbow you are holding."
    
    with group(parent="F_milestone_b2"):
        add_text("Crossbow Expert", color=c_h1, tag="CrossbowExpert")
        add_text(d1, color=c_text, wrap=avg_wrap)
        add_text(d2, color=c_text, wrap=avg_wrap)
        add_text(d3, color=c_text, wrap=avg_wrap)

def DefensiveDuelist_window():
    d1 = "When you are wielding a finesse weapon with which you are proficient and another creature hits you with a melee attack, you can use your reaction to add your proficiency bonus to your AC for that attack, potentially causing the attack to miss you."
    
    with group(parent="F_milestone_b2"):
        add_text("Defensive Duelist", color=c_h1, tag="DefensiveDuelist")
        add_text(d1, color=c_text, wrap=avg_wrap)

def DualWielder_window():
    d1 = "You gain a +1 bonus to AC while you are wielding a separate melee weapon in each hand."
    d2 = "You can use two-weapon fighting even when the one-handed melee weapons you are wielding aren't light."
    d3 = "You can draw or stow two one-handed weapons when you would normally be able to draw or stow only one."
    
    with group(parent="F_milestone_b2"):
        add_text("Dual Wielder", color=c_h1, tag="DualWielder")
        add_text(d1, color=c_text, wrap=avg_wrap)
        add_text(d2, color=c_text, wrap=avg_wrap)
        add_text(d3, color=c_text, wrap=avg_wrap)

def DungeonDelver_window():
    d1 = "You have advantage on Wisdom (Perception) and Intelligence (Investigation) checks made to detect the presence of secret doors."
    d2 = "You have advantage on saving throws made to avoid or resist traps, as well as on Intelligence checks to find or disable them."
    d3 = "Even when you are engaged in another activity while traveling, you remain alert to danger."
    
    with group(parent="F_milestone_b2"):
        add_text("Dungeon Delver", color=c_h1, tag="DungeonDelver")
        add_text(d1, color=c_text, wrap=avg_wrap)
        add_text(d2, color=c_text, wrap=avg_wrap)
        add_text(d3, color=c_text, wrap=avg_wrap)

def Durable_window():
    d1 = "When you roll a Hit Die to regain hit points, the minimum number of hit points you regain from the roll equals {self.mod['CON'] * 2}."
    
    with group(parent="F_milestone_b2"):
        add_text("Durable", color=c_h1, tag="Durable")
        add_text(d1, color=c_text, wrap=avg_wrap)

def ElementalAdept_window():
    feat="ElementalAdept"
    value = kMilestone()()["Data"][feat]["Select"][0]
    d1 = "Spells you cast ignore resistance to {value}"
    d2 = "When you roll damage for a spell you cast that deals {value} damage, you treat any 1 on a damage die as a 2."
    
    with group(parent="F_milestone_b2"):
        add_text("Elemental Adept", color=c_h1, tag="ElementalAdept")
        add_text(d1, color=c_text, wrap=avg_wrap)
        add_text(d2, color=c_text, wrap=avg_wrap)
        check_del("popup_ElementalAdept")
        with popup(feat, mousebutton=mvMouseButton_Left, max_size=[500,400], tag=f"popup_{feat}"):
            with group(horizontal=False):
                add_combo(items=dl[feat] ,default_value=value, width=50, no_arrow_button=True, user_data=["Milestone Feat Choice", feat,0], callback=cbh, tag=f"input_Feat_Choice_{feat}")

def Grappler_window():
    d1 = "You have advantage on attack rolls against a creature you are grappling."
    d2 = "You can use your action to try to pin a creature grappled by you. To do so, make another grapple check. If you succeed, you and the creature are both restrained until the grapple ends."
    
    with group(parent="F_milestone_b2"):
        add_text("Grappler", color=c_h1, tag="Grappler")
        add_text(d1, color=c_text, wrap=avg_wrap)
        add_text(d2, color=c_text, wrap=avg_wrap)

def GreatWeaponMaster_window():
    d1 = "On your turn, when you score a critical hit with a melee weapon or reduce a creature to 0 hit points with one, you can make one melee weapon attack as a bonus action."
    d2 = "Before you make a melee attack with a heavy weapon you are proficient with, you can choose to take a -5 penalty to the attack roll. If the attack hits, you add +10 to the attack's damage."
    
    with group(parent="F_milestone_b2"):
        add_text("Great Weapon Master", color=c_h1, tag="GreatWeaponMaster")
        add_text(d1, color=c_text, wrap=avg_wrap)
        add_text(d2, color=c_text, wrap=avg_wrap)

def Healer_window():
    d1 = "When you use a healer's kit to stabilize a dying creature, that creature also regains 1 hit point."
    d2 = "As an action, you can spend one use of a healer's kit to tend to a creature that has 1 or more hit points and restore 1d6 + 4 hit points to it, plus additional hit points equal to the creature's maximum number of Hit Dice."
    
    with group(parent="F_milestone_b2"):
        add_text("Healer", color=c_h1, tag="Healer")
        add_text(d1, color=c_text, wrap=avg_wrap)
        add_text(d2, color=c_text, wrap=avg_wrap)

def HeavilyArmored_window():
    with group(parent="F_milestone_b2"):
        add_text("Heavily Armored", color=c_h1, tag="HeavilyArmored")

def HeavyArmorMaster_window():
    d1 = "Prerequisite: Proficiency with heavy armor."
    d2 = "While you are wearing heavy armor, bludgeoning, piercing, and slashing damage that you take from nonmagical weapons is reduced by 3."
    
    with group(parent="F_milestone_b2"):
        add_text("Heavy Armor Master", color=c_h1, tag="HeavyArmorMaster")
        add_text(d1, color=c_text, wrap=avg_wrap)
        add_text(d2, color=c_text, wrap=avg_wrap)

def InspiringLeader_window():
    d1 = "You can spend 10 minutes inspiring your companions, shoring up their resolve to fight. When you do so, choose up to six friendly creatures (which can include yourself) within 30 feet who can hear and understand you and who spend at least 1 hit die. Each creature gains temporary hit points equal to {self.mod['CHA'] + self.level}"
    
    with group(parent="F_milestone_b2"):
        add_text("Inspiring Leader", color=c_h1, tag="InspiringLeader")
        add_text(d1, color=c_text, wrap=avg_wrap)

def KeenMind_window():
    d1 = "You always know which way is north."
    d2 = "You always know the number of hours left before the next sunrise or sunset."
    d3 = "You can accurately recall anything you have seen or heard within the past month."
    
    with group(parent="F_milestone_b2"):
        add_text("Keen Mind", color=c_h1, tag="KeenMind")
        add_text(d1, color=c_text, wrap=avg_wrap)
        add_text(d2, color=c_text, wrap=avg_wrap)
        add_text(d3, color=c_text, wrap=avg_wrap)

def LightlyArmored_window():
    feat = "LightlyArmored"
    with group(parent="F_milestone_b2"):
        add_text("Lightly Armored", color=c_h1, tag=feat)
        check_del(f"popup_{feat}")
        with popup(feat, mousebutton=mvMouseButton_Left, max_size=[500,400], tag=f"popup_{feat}"):
            with group(horizontal=False):
                add_combo(items=dl[feat], default_value=kMilestone()()["Data"][feat]["Select"][0], width=50, no_arrow_button=True, user_data=["Milestone Feat Choice",feat, 0], callback=cbh, tag=f"input_Feat_Choice_{feat}")

def Lucky_window():
    feat = "Lucky"
    use = kMilestone()()["Data"][feat]["Use"]
    d1 = "Whenever you make an attack roll, an ability check, or a saving throw, you can spend one luck point to roll an additional d20. You choose which d20 is used."
    d2 = "You can also spend one luck point when an attack roll is made against you. Roll a d20, and you choose whether the attack uses the attacker's roll or yours."
    
    with group(parent="F_milestone_b2"):
        with group(horizontal=True):
            add_text(feat, color=c_h1, tag=feat)
            for idx, val in enumerate(use):
                add_checkbox(default_value=val, enabled=True, user_data=["Milestone Feat Use", "Lucky", idx], callback=cbh, tag=f"input_Feat_Use_{feat}_{idx}")
        add_text(d1, color=c_text, wrap=avg_wrap)
        add_text(d2, color=c_text, wrap=avg_wrap)
        

def MageSlayer_window():
    d1 = "When a creature within 5 feet of you casts a spell, you can use your reaction to make a melee weapon attack against that creature."
    d2 = "When you damage a creature that is concentrating on a spell, that creature has disadvantage on the saving throw it makes to maintain its concentration."
    d3 = "You have advantage on saving throws against spells cast by creatures within 5 feet of you."
    
    with group(parent="F_milestone_b2"):
        add_text("Mage Slayer", color=c_h1, tag="MageSlayer")
        add_text(d1, color=c_text, wrap=avg_wrap)
        add_text(d2, color=c_text, wrap=avg_wrap)
        add_text(d3, color=c_text, wrap=avg_wrap)

def MediumArmorMaster_window():
    d1 = "Wearing medium armor doesn't impose disadvantage on your Dex (Stealth) checks."
    d2 = "When you are wearing medium armor, you can add 3, rather than 2, to your AC if you have a Dexterity of +2 or higher."
    
    with group(parent="F_milestone_b2"):
        add_text("Medium Armor Master", color=c_h1, tag="MediumArmorMaster")
        add_text(d1, color=c_text, wrap=avg_wrap)
        add_text(d2, color=c_text, wrap=avg_wrap)

def Mobile_window():
    d1 = "When you use the Dash action, difficult terrain doesn't cost you extra movement on that turn."
    d2 = "When you make a melee attack against a creature, you don't provoke opportunity attacks from that creature for the rest of the turn, whether you hit or not."
    
    with group(parent="F_milestone_b2"):
        add_text("Mobile", color=c_h1, tag="Mobile")
        add_text(d1, color=c_text, wrap=avg_wrap)
        add_text(d2, color=c_text, wrap=avg_wrap)

def ModeratelyArmored_window():
    feat = "ModeratelyArmored"
    with group(parent="F_milestone_b2"):
        add_text("Moderately Armored", color = c_h1, tag = feat)
        check_del(f"popup_{feat}")
        with popup(feat, mousebutton=mvMouseButton_Left, max_size=[500,400], tag=f"popup_{feat}"):
            with group(horizontal=False):
                add_combo(items=dl[feat], default_value=kMilestone()()["Data"][feat]["Select"][0], width=50, no_arrow_button=True, user_data=["Milestone Feat Choice",feat, 0], callback=cbh, tag=f"input_Feat_Choice_{feat}")

def MountedCombatant_window():
    d1 = "You have advantage on melee attack rolls against unmounted creatures that are smaller than your mount."
    d2 = "You can force an attack targeted at your mount to target you instead."
    d3 = "If your mount is subjected to an effect that allows you to make a saving throw to negate or reduce the effect, you can make the saving throw for your mount."
    
    with group(parent="F_milestone_b2"):
        add_text("Mounted Combatant", color=c_h1, tag="MountedCombatant")
        add_text(d1, color=c_text, wrap=avg_wrap)
        add_text(d2, color=c_text, wrap=avg_wrap)
        add_text(d3, color=c_text, wrap=avg_wrap)

def PolearmMaster_window():
    d1 = "When you take the Attack action and attack with only a glaive, halberd, quarterstaff, or spear, you can use a bonus action to make a melee attack with the opposite end of the weapon. This attack uses the same ability modifier as the primary attack and deals 1d4 bludgeoning damage."
    d2 = "While you are wielding a glaive, halberd, pike, quarterstaff, or spear, other creatures provoke an opportunity attack from you when they enter your reach."
    
    with group(parent="F_milestone_b2"):
        add_text("Polearm Master", color=c_h1, tag="PolearmMaster")
        add_text(d1, color=c_text, wrap=avg_wrap)
        add_text(d2, color=c_text, wrap=avg_wrap)

def Resilient_window():
    feat = "Resilient"
    with group(parent="F_milestone_b2"):
        add_text(feat, color=c_h1, tag=feat)
        check_del(f"popup_{feat}")
        with popup(feat, mousebutton=mvMouseButton_Left, max_size=[500,400], tag=f"popup_{feat}"):
            with group(horizontal=False):
                add_combo(items=dl[feat] ,default_value=kMilestone()()["Data"][feat]["Select"][0], width=50, no_arrow_button=True, user_data=["Milestone Feat Choice", feat,0], callback=cbh, tag=f"input_Feat_Choice_{feat}")

def SavageAttacker_window():
    d1 = "Once per turn when you roll damage for a melee weapon attack, you can reroll the weapon's damage dice and use either total."
    with group(parent="F_milestone_b2"):
        add_text("Savage Attacker", color=c_h1, tag="SavageAttacker")
        add_text(d1, color=c_text, wrap=avg_wrap)

def Sentinel_window():
    d1 = "When you hit a creature with an opportunity attack, the creature's speed becomes 0 for the rest of the turn."
    d2 = "Creatures within 5 feet of you provoke opportunity attacks even if they take the Disengage action before leaving your reach."
    d3 = "When a creature within 5 feet of you makes an attack against a target other than you (and that target doesn't have this feat), you can use your reaction to make a melee weapon attack against the attacking creature."
    
    with group(parent="F_milestone_b2"):
        add_text("Sentinel", color=c_h1, tag="Sentinel")
        add_text(d1, color=c_text, wrap=avg_wrap)
        add_text(d2, color=c_text, wrap=avg_wrap)
        add_text(d3, color=c_text, wrap=avg_wrap)

def Sharpshooter_window():
    d1 = "Attacking at long range doesn't impose disadvantage on your ranged weapon attack rolls."
    d2 = "Your ranged weapon attacks ignore half cover and three-quarters cover."
    d3 = "Before you make a ranged weapon attack with a weapon that you are proficient with, you can choose to take a -5 penalty to the attack roll. If the attack hits, you add +10 to the attack's damage."
    
    with group(parent="F_milestone_b2"):
        add_text("Sharpshooter", color=c_h1, tag="Sharpshooter")
        add_text(d1, color=c_text, wrap=avg_wrap)
        add_text(d2, color=c_text, wrap=avg_wrap)
        add_text(d3, color=c_text, wrap=avg_wrap)

def ShieldMaster_window():
    d1 = "If you take the Attack action on your turn, you can use a bonus action to try to shove a creature within 5 feet of you with your shield."
    d2 = "If you aren't incapacitated, you can add your shield's AC bonus to any Dexterity saving throw you make against a spell or other harmful effect that targets only you."
    d3 = "If you are subjected to an effect that allows you to make a Dexterity saving throw to take only half damage, you can use your reaction to take no damage if you succeed on the saving throw, interposing your shield between yourself and the source of the effect."
    
    with group(parent="F_milestone_b2"):
        add_text("Shield Master", color=c_h1, tag="ShieldMaster")
        add_text(d1, color=c_text, wrap=avg_wrap)
        add_text(d2, color=c_text, wrap=avg_wrap)
        add_text(d3, color=c_text, wrap=avg_wrap)

def Skulker_window():
    d1 = "You can try to hide when you are lightly obscured from the creature from which you are hiding."
    d2 = "When you are hidden from a creature and miss it with a ranged weapon attack, making the attack does not reveal your position."
    d3 = "Dim light doesn't impose disadvantage on your Wisdom (Perception) checks that rely on sight."
    
    with group(parent="F_milestone_b2"):
        add_text("Skulker", color=c_h1, tag="Skulker")
        add_text(d1, color=c_text, wrap=avg_wrap)
        add_text(d2, color=c_text, wrap=avg_wrap)
        add_text(d3, color=c_text, wrap=avg_wrap)

def TavernBrawler_window():
    d1 = "You are proficient with improvised weapons and unarmed strikes. When you hit a creature with an unarmed strike or improvised weapon, you deal bludgeoning damage equal to 1d4 + {self.p.Atr[STR][Mod]}"
    d2 = "When you use the Attack action and attack with an unarmed strike or improvised weapon on your turn, you can make one grapple attempt as a bonus action."
    
    with group(parent="F_milestone_b2"):
        add_text("Tavern Brawler", color=c_h1, tag="TavernBrawler")
        add_text(d1, color=c_text, wrap=avg_wrap)
        add_text(d2, color=c_text, wrap=avg_wrap)

def Tough_window():
    d1 = "Gain 2 bonus health per level"
    
    with group(parent="F_milestone_b2"):
        add_text("Tough", color=c_h1, tag="Tough")
        add_text(d1, color=c_text, wrap=avg_wrap)


def WarCaster_window():
    d1 = "You have advantage on Constitution saving throws that you make to maintain your concentration on a spell when you take damage."
    d2 = "You can perform the somatic components of spells even when you have weapons or a shield in one or both hands."
    d3 = "When a hostile creature's movement provokes an opportunity attack from you, you can use your reaction to cast a spell at the creature, rather than making an opportunity attack. The spell must have a casting time of one action and must target only that creature."
    
    with group(parent="F_milestone_b2"):
        add_text("War Spell_dataer", color=c_h1, tag="WarSpell_dataer")
        add_text(d1, color=c_text, wrap=avg_wrap)
        add_text(d2, color=c_text, wrap=avg_wrap)
        add_text(d3, color=c_text, wrap=avg_wrap)

def WeaponMaster_window():
    feat = "WeaponMaster"
    select = kMilestone()()["Data"][feat]["Select"]
    d1 = "You gain proficiency with four weapons of your choice."
    
    with group(parent="F_milestone_b2"):
        add_text("Weapon Master", color=c_h1, tag=feat)
        add_text(d1, color=c_text, wrap=avg_wrap)
        check_del(f"popup_{feat}")
        with popup(feat, mousebutton=mvMouseButton_Left, max_size=[500,400], tag=f"popup_{feat}"):
            with group(horizontal=False):
                for i in [0,1,2,3]:
                    add_combo(items=dl[feat] ,default_value=select[i], width=50, no_arrow_button=True, user_data=["Milestone Feat Choice", feat, i], callback=cbh, tag=f"input_Feat_Choice_{feat}_{i}")


#------------------------------------------------






def spell_detail(spell):
    data = Grimoir[spell]
    with group(horizontal=True):
        add_text("Level", color=c_h1)
        if data["Level"] == 0: add_text("Cantrip", color=c_text)
        else: add_text(data["Level"], color=c_text)
        add_text("School", color=c_h1)
        add_text(data["School"], color=f"{c_spell_school[data["School"]]}")
    with group(horizontal=True):
        add_text("Range", color=c_h1)
        add_text(data["Range"], color=c_text)
        add_text("Components", color=c_h1)
        add_text(data["Components"], color=c_text)
    with group(horizontal=True):
        add_text("Casting Time", color=c_h1)
        add_text(data["Casting Time"], color=c_text)
        add_text("Duration", color=c_h1)
        add_text(data["Duration"], color=c_text)
    with group(horizontal=True):
        if data["Ritual"] == True:
            add_text("Ritual", color=c_h1)
            add_text(data["Ritual"], color=c_text)
        if data["Concentration"] == True:
            add_text("Concentration", color=c_h1)
            add_text(data["Concentration"], color=c_text)
    with group(horizontal=False):
        add_text("Description", color=c_h1)
        add_text(data["Desc"], color=c_text, wrap=420)
    # if data["At Higher Levels"] != "":
    #     with group(horizontal=False):
    #         add_text("At Higher Levels", color=c_h1)
    #         add_text(data["At Higher Levels"], color=c_text, wrap=420)




#----------------------------------------------------

#ANCHOR - RACE

def Empty_window():
    pass

def Human_window():
    pass

def Human_Standard_window():
    pass

def Human_Variant_window():
    pass

def Elf_window():
    Fey_Ancestry = "You have advantage on saving throws against being charmed, and immunity to magical sleep"
    Trance = "you don't need to sleep. Instead meditate deeply for 4 hours a day."
    with group(parent="F_race_b2"):
        add_text("Fey Ancestry", color=c_h1, wrap=avg_wrap)
        add_text(Fey_Ancestry, color=c_text, wrap=avg_wrap)
    
        add_text("Trance", color=c_h1, wrap=avg_wrap)
        add_text(Trance, color=c_text, wrap=avg_wrap)
    if vSubrace(): globals()[f"{vRace()}_{vSubrace()}_window"]()

def Elf_High_window():
    with group(parent="F_race_b2"):
        cdata=aRace()["Cantrip"]
        spell = cdata["Select"][0]
        add_text("Cantrip", color=c_h1, wrap=avg_wrap, tag=f"rabil_Cantrip")
        check_del("tooltip_rabil_Cantrip")
        with popup("rabil_Cantrip", mousebutton=mvMouseButton_Left, tag="tooltip_rabil_Cantrip"):
            add_combo(items=dl["Cantrip"], default_value=spell, width=100, no_arrow_button=True, user_data=["Race Spell Select","Cantrip"], callback=cbh, tag=f"input_Rspellselect_Cantrip")
        if spell != "":
            add_text(spell, color=c_h2, wrap=avg_wrap, tag=f"rspell_Cantrip")
            check_del("tooltip_rspell_Cantrip")
            with tooltip(f"rspell_Cantrip", tag=f"tooltip_rspell_Cantrip"):
                spell_detail(spell)
    
def Elf_Wood_window():
    Mask_of_the_Wild="You can attempt to hide even when you are only lightly obscured."
    with group(parent="F_race_b2"):
        add_text("Mask of the Wild", color=c_h1, wrap=avg_wrap)
        add_text(Mask_of_the_Wild, color=c_text, wrap=avg_wrap)

def Elf_Drow_window():
    with group(parent="F_race_b2"):
        cdata=aRace()["Drow Magic"]
        add_text("Drow Magic", color=c_h1, wrap=300, tag=f"Drow_Magic")
        for spell in cdata.keys():
            with group(horizontal=True):
                add_text(spell, color=c_h2, wrap=300, tag=f"Drow_Magic_{spell}")
                if "Use" in cdata[spell]:
                    add_checkbox(default_value=cdata[spell]["Use"][0], enabled=True, user_data=["Race Spell Use","Drow Magic",spell], callback=cbh, tag=f"input_Rspelluse_Drow_Magic_{spell}")
            check_del(f"tooltip_Drow_Magic_{spell}")
            with tooltip(f"Drow_Magic_{spell}", tag=f"tooltip_Drow_Magic_{spell}"):
                spell_detail(spell)

def Elf_ShadarKai_window():
    if vLevel() < 3: Blessing_of_the_Raven_Queen = "(bonus) teleport up to 30 ft to an unoccupied space you can see"
    else: Blessing_of_the_Raven_Queen = "(bonus) teleport up to 30 ft to an unoccupied space you can see, gain resistance to all damage until the start of your next turn, during that time you appear ghostly/translucent"

    cdata=aRace()["Blessing of the Raven Queen"]
    with group(parent="F_race_b2"):
        with group(horizontal=False):
            with group(horizontal=True):
                add_text("Blessing of the Raven Queen", color=c_h1, wrap=avg_wrap)
                for idx,val in enumerate(cdata["Use"]):
                    add_checkbox(default_value=val, enabled=True, user_data=["Race Use","Blessing of the Raven Queen",idx], callback=cbh, tag=f"input_Ruse_Blessing_of_the_Raven_Queen_{idx}")
            add_text(Blessing_of_the_Raven_Queen, color=c_text, wrap=avg_wrap)

def Dwarf_window():
    Dwarven_Resilience = "Advantage on saving throws against poison, as well as resistance against poison damage."
    Stonecunning = f"+{2*vPB()} on stonework History"
    with group(parent="F_race_b2"):
        add_text("Dwarven Resilience", color=c_h1, wrap=avg_wrap)
        add_text(Dwarven_Resilience, color=c_text, wrap=avg_wrap)
        
        add_text("Stonecunning", color=c_h1, wrap=avg_wrap)
        add_text(Stonecunning, color=c_text, wrap=avg_wrap)
    if vSubrace(): globals()[f"{vRace()}_{vSubrace()}_window"]()

def Dwarf_Hill_window():
    with group(parent="F_race_b2"):
        add_text("Dwarven Toughness", color=c_h1, wrap=avg_wrap)


def Dwarf_Mountain_window():
    pass

def Halfling_window():
    Lucky = "When you roll a 1 on an attack roll, ability check, or saving throw, you can reroll and must use the new roll."
    Brave = "Advantage on saving throws against being frightened."
    Nimble = "You can move through the space of any creature that is a size larger than yours."
    with group(parent="F_race_b2"):
        add_text("Lucky", color=c_h1, wrap=avg_wrap)
        add_text(Lucky, color=c_text, wrap=avg_wrap)
        
        add_text("Brave", color=c_h1, wrap=avg_wrap)
        add_text(Brave, color=c_text, wrap=avg_wrap)
        
        add_text("Nimble", color=c_h1, wrap=avg_wrap)
        add_text(Nimble, color=c_text, wrap=avg_wrap)
    if vSubrace(): globals()[f"{vRace()}_{vSubrace()}_window"]()

def Halfling_Lightfoot_window():
    Naturally_Stealthy = "You can attempt to hide even when obscured only by a creature larger than you."
    with group(parent="F_race_b2"):
        add_text("Naturally Stealthy", color=c_h1, wrap=avg_wrap)
        add_text(Naturally_Stealthy, color=c_text, wrap=avg_wrap)

def Halfling_Stout_window():
    Stout_Resilience = "Advantage on saving throws against poison, Resistance against poison damage."
    with group(parent="F_race_b2"):
        add_text("Stout Resilience", color=c_h1, wrap=avg_wrap)
        add_text(Stout_Resilience, color=c_text, wrap=avg_wrap)

def Gnome_window():
    Gnome_Cunning = "Advantage on Int/Wis/Cha saves against magic"
    with group(parent="F_race_b2"):
        add_text("Gnome Cunning", color=c_h1, wrap=avg_wrap)
        add_text(Gnome_Cunning, color=c_text, wrap=avg_wrap)
    if vSubrace(): globals()[f"{vRace()}_{vSubrace()}_window"]()

def Gnome_Forest_window():
    Speak_with_Small_Beasts = "Through sounds and gestures, you can communicate simple ideas with Small or smaller beasts"
    with group(parent="F_race_b2"):
        add_text("Speak with Small Beasts", color=c_h1, wrap=avg_wrap)
        add_text(Speak_with_Small_Beasts, color=c_text, wrap=avg_wrap)
        
        cdata = aRace()["Natural Illusionist"]
        for spell in cdata.keys():
            with group(horizontal=True):
                add_text(spell, color=c_h2, wrap=300, tag=f"Natural_Illusionist_{spell}")
            check_del(f"tooltip_Natural_Illusionist_{spell}")
            with tooltip(f"Natural_Illusionist_{spell}", tag=f"tooltip_Natural_Illusionist_{spell}"):
                spell_detail(spell)


def Gnome_Rock_window():
    Artificers_Lore = f"History (Magic/Alchemy/Tech) item checks use {2*vPB()+kAtr()["INT"]["Mod"]}"
    Tinker = "Using tinker's tools, you can spend 1 hour and 10 gp worth of materials to construct a Tiny clockwork device (AC 5, 1 hp). The device ceases to function after 24 hours (unless you spend 1 hour repairing it to keep the device functioning), or when you use your action to dismantle it; at that time, you can reclaim the materials used to create it. You can have up to three such devices active at a time. When you create a device, choose one of the following options:"
    Clockwork_Toy = "This toy is a clockwork animal, monster, or person, such as a frog, mouse, bird, dragon, or soldier. When placed on the ground, the toy moves 5 feet across the ground on each of your turns in a random direction. It makes noises as appropriate to the creature it represents.",
    Fire_Starter = "The device produces a miniature flame, which you can use to light a candle, torch, or campfire. Using the device requires your action.",
    Music_Box = "When opened, this music box plays a single song at a moderate volume. The box stops playing when it reaches the song's end or when it is closed."
    with group(parent="F_race_b2"):
        add_text("Tinker", color=c_h1, tag="Tinker")
        check_del("Tooltip_Tinker")
        with tooltip("Tinker", tag="Tooltip_Tinker"):
            with group(horizontal=False):
                add_text("Tinker", color=c_h1)
                add_text(Tinker, color=c_text, wrap=300)
            with group(horizontal=False):
                add_text("Clockwork Toy", color=c_h2)
                add_text(Clockwork_Toy, color=c_text, wrap=300)
            with group(horizontal=False):
                add_text("Fire Starter", color=c_h2)
                add_text(Fire_Starter, color=c_text, wrap=300)
            with group(horizontal=False):
                add_text("Music Box", color=c_h2)
                add_text(Music_Box, color=c_text, wrap=300)
                
        add_text("Artificers Lore", color=c_h1)
        add_text(Artificers_Lore, color=c_text)




def Dragonborn_window():
    if vSubrace(): 
        Dragonborn_subrace_window()


def Dragonborn_subrace_window():
    dnum=[0,2,2,2,2,2,3,3,3,3,3,4,4,4,4,4,5,5,5,5,5][vLevel()]
    
    type_map = {"Black": "Acid", "Blue": "Lightning", "Brass": "Fire", "Bronze": "Lightning", "Copper": "Acid", "Gold": "Fire", "Green": "Poison", "Red": "Fire", "Silver": "Cold", "White": "Cold"}
    save_map = {"Acid": "DEX", "Lightning": "DEX", "Fire": "DEX", "Poison": "CON", "Cold": "CON"}
    type=type_map[vSubrace()]
    save=save_map[type]
    dc = dc_val(save)
    Breath_Weapon = f"(action) Exhale {type} in a 30ft. line: all creatures in range must make a DC {dc} {save} saving throw, taking {dnum}d6 {type} damage on fail, half on success."
    Dragonic_Resistance = f"Gain resistance to {type} damage"
    with group(parent="F_race_b2"):
        add_text("Draconic Resistance", color=c_h1, wrap=avg_wrap)
        add_text(Dragonic_Resistance, color=c_text, wrap=avg_wrap)

        cdata = aRace()["Breath Weapon"]
        with group(horizontal=False):
            with group(horizontal=True):
                add_text("Breath Weapon", color=c_h1, wrap=avg_wrap)
                add_checkbox(default_value=cdata["Use"][0], enabled=True, user_data=["Race Use", "Breath Weapon",0], callback=cbh, tag=f"input_Ruse_Breath_Weapon_0")
            add_text(Breath_Weapon, color=c_text, wrap=avg_wrap)

def HalfOrc_window():
    Relentless_Endurance ="When you are reduced to 0 hit points but not killed outright, you can drop to 1 hit point instead"
    Savage_Attacks = "When you score a critical hit with a melee weapon attack, you can roll one of the weapon's damage dice one additional time and add it to the extra damage of the critical hit."
    cdata = aRace()["Relentless Endurance"]
    with group(parent="F_race_b2"):
        with group(horizontal=True):
            add_text("Relentless Endurance", color=c_h1, wrap=avg_wrap)
            add_checkbox(default_value=cdata["Use"][0], enabled=True, user_data=["Race Use", "Relentless Endurance",0], callback=cbh, tag="input_Ruse_Relentless_Endurance_0")
        add_text(Relentless_Endurance, color=c_text, wrap=avg_wrap)
        
        add_text("Savage Attacks", color=c_h1, wrap=avg_wrap)
        add_text(Savage_Attacks, color=c_text, wrap=avg_wrap)
    if vSubrace(): globals()[f"{vRace()}_{vSubrace()}_window"]()

def HalfOrc_Standard_window():
    pass

def Tiefling_window():
    tiefling_map={"Asmodeus": "Infernal Legacy","Baalzebul": "Legacy of Maladomini","Dispater": "Legacy of Dis","Fierna": "Legacy of Minauros","Glasya": "Legacy of Cania","Levistus": "Legacy of Stygia","Mammon": "Legacy of Minauros","Mephistopheles": "Legacy of Cania","Zariel": "Legacy of Avernus",}
    if vSubrace(): 
        legacy = tiefling_map[vSubrace()]
        cdata=aRace()[legacy]
        Tiefling_subrace_window(cdata,legacy)

def Tiefling_subrace_window(cdata,legacy):
    with group(parent="F_race_b2"):
        add_text(legacy, color=c_h1, wrap=300, tag=f"{legacy}")
        for spell in cdata.keys():
            with group(horizontal=True):
                add_text(spell, color=c_h2, wrap=300, tag=f"{legacy}_{spell}")
                if "Use" in cdata[spell]:
                    add_checkbox(default_value=cdata[spell]["Use"][0], enabled=True, user_data=["Race Spell Use",legacy,spell], callback=cbh, tag=f"input_Rspelluse_{legacy}_{spell}")
                check_del(f"tooltip_{legacy}_{spell}")
                with tooltip(f"{legacy}_{spell}", tag=f"tooltip_{legacy}_{spell}"):
                    spell_detail(spell)


def Harengon_window():
    Lucky_Footwork = "(reaction) On failed dex save add 1d4 to save; cannot use if prone or at 0 speed."
    Rabbit_Hop = f"(Bonus) If speed is greater than 0, jump {5*vPB()} ft without provoking opportunity attacks"
    with group(parent="F_race_b2"):
        add_text("Lucky Footwork", color=c_h1, wrap=avg_wrap)
        add_text(Lucky_Footwork, color=c_text, wrap=avg_wrap)
        cdata = aRace()["Rabbit Hop"]
        with group(horizontal=True):
            add_text("Rabbit Hop", color=c_h1, wrap=avg_wrap)
            for idx, val in enumerate(cdata["Use"]):
                add_checkbox(default_value=val, enabled=True, user_data=["Race Use", "Rabbit Hop",idx], callback=cbh, tag=f"input_Ruse_Rabbit_Hop_{idx}")
        add_text(Rabbit_Hop, color=c_text, wrap=avg_wrap)
    if vSubrace(): globals()[f"{vRace()}_{vSubrace()}_window"]()

def Harengon_Standard_window():
    pass

    

#-----------------------------------------------------------

#ANCHOR - Class shit
def Empty_window():
    pass
    
def Fighter_window():
    data = aClass()
    with group(parent="F_class_b2"):
        if "Fighting Style" in data:
            cdata=aClass()["Fighting Style"]
            add_text("Fighting Style", color=c_h1, wrap=avg_wrap, tag="Fighting Style")
            check_del("popup_Fighting_Style")
            with popup("Fighting Style", mousebutton=mvMouseButton_Left, tag="popup_Fighting_Style"):
                for idx,value in enumerate(cdata["Select"]):
                    add_combo(items=dl["Fighting Styles"], default_value=value, width=80, no_arrow_button=True, callback=cbh,  user_data=["Class Select","Fighting Style",idx], tag=f"input_Cselect_Fighting_Style_{idx}")
            for item in cdata["Select"]:
                if item != "":
                    add_text(item, color=c_h2, wrap=avg_wrap)
                    add_text(get_Fighting_Style(item), color=c_text, wrap=avg_wrap)

        if "Second Wind" in data:
            Second_Wind = f"(bonus) regain 1d10+{vLevel()} HP"
            cdata=aClass()["Second Wind"]
            with group(horizontal=False):
                with group(horizontal=True):
                    add_text("Second Wind", color=c_h1, wrap=avg_wrap)
                    add_checkbox(default_value=cdata["Use"][0], enabled=True, callback=cbh, user_data=["Class Use", "Second Wind",idx], tag=f"input_Cuse_Second_Wind_{idx}")
                add_text(Second_Wind, color=c_text, wrap=avg_wrap)
                
        if "Action Surge" in data:
            Action_Surge = "(free) take one additional action."
            #---
            cdata=aClass()["Action Surge"]
            with group(horizontal=False):
                with group(horizontal=True):
                    add_text("Action Surge", color=c_h1, wrap=avg_wrap)
                    for idx,value in enumerate(cdata["Use"]):
                        add_checkbox(default_value=value, enabled=True, callback=cbh, user_data=["Class Use", "Action Surge",idx], tag=f"input_Cuse_Action_Surge_{idx}")
                add_text(Action_Surge, color=c_text, wrap=avg_wrap)

        if "Extra Attack" in data:
            extra_attack_num=[0,0,0,0,0,2,2,2,2,2,2,3,3,3,3,3,3,4,4,4,4][vLevel()]
            Extra_Attack = f"On Attack action, attack {extra_attack_num} times"
            #---
            with group(horizontal=True):
                add_text("Extra Attack", color=c_h1, wrap=avg_wrap)
                add_text(Extra_Attack, color=c_text, wrap=avg_wrap)

        if "Indomitable" in data:
            Indomitable = "You can reroll a saving throw that you fail. If you do so, you must use the new roll"
            cdata=aClass()["Indomitable"]
            #---
            with group(horizontal=False):
                with group(horizontal=True):
                    add_text("Indomitable", color=c_h1, wrap=avg_wrap)
                    for idx,value in enumerate(cdata["Use"]):
                        add_checkbox(default_value=value, enabled=True, callback=cbh, user_data=["Class Use", "Indomitable",idx], tag=f"input_Cuse_Indomitable_{idx}")
                add_text(Indomitable, color=c_text, wrap=avg_wrap)
    if vSubclass(): globals()[f"{vClass()()}_{vSubclass()()}_window"]()

def Fighter_Champion_window():
    data = aClass()
    with group(parent="F_class_b2"):
        if "Improved Critical" in data:
            Improved_Critical = "weapon attacks crit on 18-20." 
            add_text("Improved Critical", color=c_h1)
            add_text(Improved_Critical, color=c_text, wrap=avg_wrap)

        if "Superior Critical" in data:
            Superior_Critical="weapon attacks crit on 19-20."
            add_text("Superior Critical", color=c_h1)
            add_text(Superior_Critical, color=c_text, wrap=avg_wrap)
            
        if "Remarkable Athlete" in data:
            Remarkable_Athlete = f"add +{math.ceil(vPB()/2)} to any non proficient Str/Dex/Con check. On running long jump, increase distance by {vMod("STR")} ft."
            add_text("Remarkable_Athlete", color=c_h1)
            add_text(Remarkable_Athlete, color=c_text, wrap=avg_wrap)

        if "Survivor" in data:
            Survivor = f"At the start of your turn, regain {5+ kAtr()['CON']['Mod']} hp if at less then half HP and above 0 HP"
            add_text("Survivor", color=c_h1)
            add_text(Survivor, color=c_text, wrap=avg_wrap)

def Fighter_BattleMaster_window():
    data = aClass()
    with group(parent="F_class_b2"):
        if "Combat Superiority" in data:
            die = [0,0,0,8,8,8,8,8,8,8,10,10,10,10,10,10,10,10,12,12,12][vLevel()]
            cdata=data["Combat Superiority"]
            with group(horizontal=True):
                add_text(f"Combat Superiority (d{die})", color=c_h1, wrap=avg_wrap, tag="Combat Superiority")
                check_del("popup_Combat_Superiority")
                with popup("Combat Superiority", mousebutton=mvMouseButton_Left, tag="popup_Combat_Superiority"):
                    for idx,value in enumerate(cdata["Select"]): add_combo(items=dl["Maneuvers"], default_value=value, width=80, no_arrow_button=True, callback=cbh,  user_data=["Class Select","Combat Superiority",idx], tag=f"input_Cselect_Combat_Superiority_{idx}")
                for idx,value in enumerate(cdata["Use"]):
                    add_checkbox(default_value=value, enabled=True, callback=cbh, user_data=["Class Use", "Combat Superiority",idx], tag=f"input_Cuse_Combat_Superiority_{idx}")
            for item in cdata["Select"]:
                if item:
                    add_text(item, color=c_h2, wrap=avg_wrap, tag=f"Maneuver_{item}")
                    check_del(f"tooltip_{item}")
                    with tooltip(f"Maneuver_{item}", tag=f"tooltip_{item}"):
                        add_text(get_Maneuver(item), color=c_text, wrap=avg_wrap)
        if "Student of War" in data:
            cdata=data["Student of War"]
            add_text("Student of War", color=c_h1, wrap=avg_wrap, tag="Student of War")
            check_del("popup_Student_of_War")
            with popup("Student of War", mousebutton=mvMouseButton_Left, tag="popup_Student_of_War"):
                add_combo(items=dl["Student of War"], default_value=cdata["Select"][0],  width=80, no_arrow_button=True, callback=cbh,  user_data=["Class Select", "Student of War",0], tag=f"input_Cselect_Student_of_War_{idx}")
        if "Relentless" in data:
            Relentless = "When you roll initiative with 0 SD; gain 1 SD."
            with group(horizontal=True):
                add_text("Relentless", color=c_h1, wrap=avg_wrap)
                add_text(Relentless, color=c_text, wrap=avg_wrap)

def Fighter_EldrichKnight_window():
    data = aClass()
    with group(parent="F_class_b2"):
        if "Weapon Bond" in data:
            Weapon_Bond_1 = "Learn a ritual that creates a magical bond between yourself and one weapon. You perform the ritual over the course of 1 hour, which can be done during a short rest. The weapon must be within your reach throughout the ritual, at the conclusion of which you touch the weapon and forge the bond."
            Weapon_Bond_2 = "Once you have bonded a weapon to yourself, you can't be disarmed of that weapon unless you are incapacitated. If it is on the same plane of existence, you can summon that weapon as a bonus action on your turn, causing it to teleport instantly to your hand."
            Weapon_Bond_3 = "You can have up to two bonded weapons, but can summon only one at a time with your bonus action. If you attempt to bond with a third weapon, you must break the bond with one of the other two."
            add_text("Weapon Bond", color=c_h1, wrap=avg_wrap, tag="Weapon Bond")
            check_del("tooltip_Weapon_Bond")
            with tooltip("Weapon Bond", tag="tooltip_Weapon_Bond"):
                add_text(Weapon_Bond_1, color=c_text, wrap=avg_wrap)
                add_text(Weapon_Bond_2, color=c_text, wrap=avg_wrap)
                add_text(Weapon_Bond_3, color=c_text, wrap=avg_wrap)
                        
                        
        if "War Magic" in data:
            War_Magic = "(action-cantrip) gain (bonus) make one weapon attack."
            add_text("War Magic", color=c_h1, wrap=avg_wrap)
            add_text(War_Magic, color=c_text, wrap=avg_wrap)
        if "Improved War Magic" in data:
            Improved_War_Magic = "(action-spell) gain (bonus) make one weapon attack."
            add_text("Improved War Magic", color=c_h1, wrap=avg_wrap)
            add_text(Improved_War_Magic, color=c_text, wrap=avg_wrap)
        if "Eldrich Strike" in data:
            Eldrich_Strike = "When you hit a creature with a weapon attack, that creature has disadvantage on the next saving throw it makes against a spell you cast before the end of your next turn."
            add_text("Eldrich Strike", color=c_h1, wrap=avg_wrap)
            add_text(Eldrich_Strike, color=c_text, wrap=avg_wrap)
        if "Arcane Charge" in data:
            Arcane_Charge = "(Action Surge) Teleport up to 30 feet to an unoccupied space you can see, teleport before or after extra action"
            add_text("Arcane Charge", color=c_h1, wrap=avg_wrap)
            add_text(Arcane_Charge, color=c_text, wrap=avg_wrap)

def Fighter_Samuri_window():
    data = aClass()
    with group(parent="F_class_b2"):

        
        if "Bonus Proficiency" in data:
            title = "Bonus Proficiency"
            cdata=data[title]
            add_text(title, color=c_h1, wrap=avg_wrap, tag=title)
            check_del("popup_Bonus_Proficiency")
            with popup(title, mousebutton=mvMouseButton_Left, tag="popup_Bonus_Proficiency"):
                add_combo(items=dl[title], default_value=cdata["Select"][0],  width=80, no_arrow_button=True, callback=cbh,  user_data=["Class Select", title,0], tag=f"input_Cselect_Bonus_Proficiency")
        if "Fighting Spirit" in data:
            Fighting_Spirit = ""
            with group(horizontal=True):
                add_text("Fighting Spirit", color=c_h1, wrap=avg_wrap)
                add_text(Fighting_Spirit, color=c_text, wrap=avg_wrap)
                
        if "Elegant Courtier" in data:
            Elegant_Courtier = f"Persuasion checks gain {kAtr()["WIS"]["Mod"]:+d}"
            with group(horizontal=True):
                add_text("Elegant Courtier", color=c_h1, wrap=avg_wrap)
                add_text(Elegant_Courtier, color=c_text, wrap=avg_wrap)
                
        if "Tireless Spirit" in data:
            Tireless_Spirit = "When you roll initiative and have no uses of Fighting Spirit remaining, regain one use."
            with group(horizontal=True):
                add_text("Tireless Spirit", color=c_h1, wrap=avg_wrap)
                add_text(Tireless_Spirit, color=c_text, wrap=avg_wrap)
        if "Rapid Strike" in data:
            Rapid_Strike = "On Attack with advantage, you may remove advantage to gain +1 attack, 1/turn."
            with group(horizontal=True):
                add_text("Rapid Strike", color=c_h1, wrap=avg_wrap)
                add_text(Rapid_Strike, color=c_text, wrap=avg_wrap)
                
        if "Strength before Death" in data:
            Strength_before_Death = ""
            with group(horizontal=True):
                add_text("Strength before Death", color=c_h1, wrap=avg_wrap)
                add_text(Strength_before_Death, color=c_text, wrap=avg_wrap)
                
                
def Wizard_window():
    data = aClass()
    with group(parent="F_class_b2"):
        if "Spellcasting" in data:
            Spellcasting_1 = "Must be spell level you can prepare, Costs 50 gp + 2 hours per spell level"
            Spellcasting_2 = "Too backup own spellbook, Costs 10 gp + 1 hour per spell level"
            add_text("Spellcasting", color=c_h1, wrap=avg_wrap, tag="Spellcasting")
            check_del("tooltip_Spellcasting")
            with tooltip("Spellcasting", tag=f"tooltip_Spellcasting"):
                add_text("Copying external spells", color=c_h1, wrap=avg_wrap)
                add_text(Spellcasting_1, color=c_text, wrap=avg_wrap)
                add_text("Copying internal spells", color=c_h1, wrap=avg_wrap)
                add_text(Spellcasting_2, color=c_text, wrap=avg_wrap)
                
        if "Arcane Recovery" in data:
            cdata=data["Arcane Recovery"]
            Arcane_Recovery = f"Regain Spell slots with a combined level of {math.ceil(vLevel()/2)}, None highter then 6th level"
            with group(horizontal=False):
                with group(horizontal=True):
                    add_text("Arcane Recovery", color=c_h1, wrap=avg_wrap)
                    for idx,value in enumerate(cdata["Use"]):
                        add_checkbox(default_value=value, enabled=True, callback=cbh, user_data=["Class Use", "Arcane Recovery",idx], tag=f"input_Cuse_Arcane_Recovery_{idx}")
                add_text(Arcane_Recovery, color=c_text, wrap=avg_wrap)

        if "Spell Mastery" in data:
            cdata=data["Spell Mastery"]
            add_text("Spell Mastery", color=c_h1, wrap=avg_wrap, tag="Spell Mastery")
            check_del("popup_Spell_Mastery")
            with popup("Spell Mastery", mousebutton=mvMouseButton_Left, tag="popup_Spell_Mastery"):
                add_combo(items=kSpell()["Book"][1], default_value=cdata["Select"][0],  width=80, no_arrow_button=True, callback=cbh,  user_data=["Class Select", "Spell Mastery",0], tag=f"input_Cselect_Spell_Mastery_0")
                add_combo(items=kSpell()["Book"][2], default_value=cdata["Select"][1],  width=80, no_arrow_button=True, callback=cbh,  user_data=["Class Select", "Spell Mastery",1], tag=f"input_Cselect_Spell_Mastery_1")
            for idx,spell in enumerate(cdata["Select"]):
                if spell != "":
                    with group(horizontal=True):
                        add_text(spell, color=c_h2, tag=f"Spell Mastery {spell}")
                        add_checkbox(default_value=cdata["Use"][idx], enabled=True, callback=cbh, user_data=["Class Use", "Spell Mastery",idx], tag=f"input_Cuse_Spell_Mastery_{idx}")
                        check_del(f"tooltip_Spell_Mastery_{spell}")
                        with tooltip(f"Spell Mastery {spell}", tag=f"tooltip_Spell_Mastery_{spell}"):
                            spell_detail(spell)
                            
        if "Signature Spells" in data:
            cdata=data["Signature Spells"]
            add_text("Signature Spells", color=c_h1, wrap=avg_wrap, tag="Signature Spells")
            check_del("popup_Signature_Spells")
            with popup("Signature Spells", mousebutton=mvMouseButton_Left, tag="popup_Signature_Spells"):
                add_combo(items=kSpell()["Book"][3], default_value=cdata["Select"][0],  width=80, no_arrow_button=True, callback=cbh,  user_data=["Class Select", "Signature Spells",0], tag=f"input_Cselect_Signature_Spells_0")
                add_combo(items=kSpell()["Book"][3], default_value=cdata["Select"][1],  width=80, no_arrow_button=True, callback=cbh,  user_data=["Class Select", "Signature Spells",1], tag=f"input_Cselect_Signature_Spells_1")
            for idx,spell in enumerate(cdata["Select"]):
                if spell != "":
                    with group(horizontal=True):
                        add_text(spell, color=c_h2, tag=f"Signature Spells {spell}")
                        add_checkbox(default_value=cdata["Use"][idx], enabled=True, callback=cbh, user_data=["Class Use", "Signature Spells",idx], tag=f"input_Cuse_Signature_Spells_{idx}")
                        check_del(f"tooltip_Signature_Spells_{spell}")
                        with tooltip(f"input_Signature_Spells_{spell}", tag=f"tooltip_Signature_Spells_{spell}"):
                            spell_detail(spell)
        if vSubclass(): globals()[f"{vClass()()}_{vSubclass()()}_window"]()



def Wizard_Abjuration_window():
    data = aClass()
    with group(parent="F_class_b2"):
        if "Abjuration Savant" in data:
            Abjuration_Savant = "Abjuration spells cost 25gp and 1 hour per spell level."
            add_text("Abjuration Savant", color=c_h1, wrap=avg_wrap, tag="Abjuration Savant")
            add_text(Abjuration_Savant, color=c_text, wrap=avg_wrap)
        if "Arcane Ward" in data:
            Arcane_Ward = "On casting a 1st-level+ Abjuration spell, create a magical ward that lasts until a long rest. It can regain HP equal to twice the spell level on subsequent Abjuration spell casts."
            cdata=aClass()["Arcane Ward"]
            with group(horizontal=True):
                add_text("Arcane Ward", color=c_h1, wrap=avg_wrap, tag="Arcane Ward")
                add_checkbox(default_value=cdata["Use"][0], enabled=True, callback=cbh, user_data=["Class Use", "Arcane Ward",0], tag="input_Cuse_Arcane_Ward_0")
                add_button(label="Ward HP", enabled=False)
                add_button(label=f"{cdata["HP"]["Current"]} / {cdata["HP"]["Max"]}", enabled=False, tag="Arcane_Ward_HP")
                add_button(label="-", user_data = ["Arcane Ward", -1], callback=cbh)
                add_button(label="+", user_data = ["Arcane Ward", 1], callback=cbh)
            add_text(Arcane_Ward, color=c_text, wrap=avg_wrap)
        
        if "Projected Ward" in data:
            Projected_Ward = "(reaction) When a creature within 30 ft is hit, use your Arcane Ward to absorb the damage."
            add_text("Projected Ward", color=c_h1, wrap=avg_wrap, tag="Projected Ward")
            add_text(Projected_Ward, color=c_text, wrap=avg_wrap)
        if "Improved Abjuration" in data:
            Improved_Abjuration = f"When an Abjuration spell requires you to make an ability check, add your proficiency bonus ({vPB()}) to that check."
            add_text("Improved Abjuration", color=c_h1, wrap=avg_wrap, tag="Improved Abjuration")
            add_text(Improved_Abjuration, color=c_text, wrap=avg_wrap)
        if "Spell Resistance" in data:
            Spell_Resistance = "Gain advantage on saving throws against spells and resistance to spell damage."
            add_text("Improved Abjuration", color=c_h1, wrap=avg_wrap, tag="Improved Abjuration")
            add_text(Spell_Resistance, color=c_text, wrap=avg_wrap)


def Wizard_Conjuration_window():
    data = aClass()
    if "Conjuration Savant" in data:
        Conjuration_Savant = "Conjuration spells cost 25gp and 1 hour per spell level."
        add_text("Conjuration Savant", color=c_h1, wrap=avg_wrap, tag="Conjuration Savant")
        add_text(Conjuration_Savant, color=c_text, wrap=avg_wrap)
    if "Minor Conjuration" in data:
        Minor_Conjuration = "(action) Conjure a non-magical item (up to 3ft, 10 lbs). It lasts for 1 hour or until it takes damage."
        add_text("Minor Conjuration", color=c_h1, wrap=avg_wrap, tag="Minor Conjuration")
        add_text(Minor_Conjuration, color=c_text, wrap=avg_wrap)
    if "Benign Transportation" in data:
        Benign_Transportation = "(action) Teleport up to 30ft or swap places with a willing creature. Usable again after a long rest or casting a Level 1+ conjuration spell."
        add_text("Benign Transportation", color=c_h1, wrap=avg_wrap, tag="Benign Transportation")
        add_text(Benign_Transportation, color=c_text, wrap=avg_wrap)
    if "Focused Conjuration" in data:
        Focused_Conjuration = "Your concentration on conjuration spells can't be broken as a result of taking damage."
        add_text("Focused Conjuration", color=c_h1, wrap=avg_wrap, tag="Focused Conjuration")
        add_text(Focused_Conjuration, color=c_text, wrap=avg_wrap)
    if "Durable Summons" in data:
        Durable_Summons = "Any creature you summon or create with a conjuration spell has 30 temporary hit points."
        add_text("Durable Summons", color=c_h1, wrap=avg_wrap, tag="Durable Summons")
        add_text(Durable_Summons, color=c_text, wrap=avg_wrap)


#ANCHOR - Inventory

def dyn_Inventory():
    dyn_Inventory_Equip()
    dyn_Inventory_Backpack()
    
    
def dyn_Inventory_Backpack():
    delete_item("cw_inv_backpack", children_only=True)
    with group(parent="cw_inv_backpack"):
        with table(header_row=True, row_background=False, borders_innerH=True, borders_outerH=True, borders_innerV=True, borders_outerV=True, resizable=True):
            add_table_column(label="Item", width_stretch=True, init_width_or_weight=0)
            add_table_column(label="Slot", width_stretch=True, init_width_or_weight=0)
            add_table_column(label="QTY", width_stretch=True, init_width_or_weight=0)
            add_table_column(label="Weight", width_stretch=True, init_width_or_weight=0)
            add_table_column(label="Cost", width_stretch=True, init_width_or_weight=0)
            
            for item in Current_Backpack():
                cdata = bItem(item)
                qty = kBackpack()[item][1]
                weight = int(w) if (w := round(float(cdata.Weight)*qty, 2)) == int(w) else w
                cost = int(c) if (c := round(float(cdata.Cost)*qty, 2)) == int(c) else c
                with table_row():
                    with table_cell():
                        add_text(iName(item), tag=f"bp_item_{item}")
                    with table_cell():
                        add_text(cdata.Slot, tag=f"bp_slot_{item}")
                    with table_cell():
                        with group(horizontal=True):
                            add_text(qty, tag = f"bp_qty_{item}")
                            add_button(label="<", small=True, user_data=["Backpack Mod Item", item, -1], callback=cbh)
                            add_button(label=">", small=True, user_data=["Backpack Mod Item", item, 1], callback=cbh)
                            add_button(label="X", small=True, user_data=["Backpack Mod Item", item, "Clear"], callback=cbh)
                    with table_cell():
                        add_text(weight, tag=f"bp_weight_{item}")
                    with table_cell():
                        add_text(cost, tag=f"bp_cost_{item}")

                    check_del(f"bp_tooltip_{item}")
                    with tooltip(f"bp_item_{item}", tag=f"bp_tooltip_{item}"):
                        disp_item_detail(item)
                        
                        
def ensure_Backpack():
    for item in Current_Backpack():
        qty = kBackpack()[item][1]
        cdata = bItem(item)
        slot=cdata.Slot
        weight = int(w) if (w := round(float(cdata.Weight)*qty, 2)) == int(w) else w
        cost = int(c) if (c := round(float(cdata.Cost)*qty, 2)) == int(c) else c
        
        set_value(f"bp_slot_{item}", slot)
        set_value(f"bp_qty_{item}", qty)
        set_value(f"bp_weight_{item}", weight)
        set_value(f"bp_cost_{item}", cost)

def dyn_Inventory_Equip():
    backpack = set(Current_Backpack())
    slots = [("Face","input_equip_Face"),("Throat","input_equip_Throat"),("Body","input_equip_Body"),("Hands","input_equip_Hands"),("Waist","input_equip_Waist"),("Feet","input_equip_Feet"),("Armor","input_equip_Armor"),("Main Hand","input_equip_MainHand"),("Off Hand","input_equip_OffHand"),("Ring 1","input_equip_Ring1"),("Ring 2","input_equip_Ring2")]
    two_handed = set(bProperty("Two-handed"))
    main_hand_item = Current_Equip("Main Hand")
    for slot, tag in slots:
        valid = bSlot("Weapon") if slot == "Main Hand" else bOffHand() if slot == "Off Hand" else bSlot(slot)
        filtered_items = [iName(i) for i in valid if i in backpack]
        items = (["Empty"] + filtered_items) if filtered_items else []
        value = "Weapon Grip" if slot == "Off Hand" and main_hand_item in two_handed else iName(Current_Equip(slot)) or ""
        if slot == "Off Hand" and weapon_versatile(): value = "Verse Grip"

        configure_item(tag, items=items, default_value=value)

        


def st_Inventory_Bazaar():
    cList = {
        "Weapon": [("Simple", "Melee"), ("Simple", "Ranged"), ("Martial", "Melee"), ("Martial", "Ranged")],
        "Armor": ["Light", "Medium", "Heavy"]
    }
    
    for category_type, categories in cList.items():
        for tier in range(5):
            rarity = item_rarity(tier)
            check_con(f"bazaar_rarity_{category_type}_{rarity}")
            
            with group(parent=f"bazaar_rarity_{category_type}_{rarity}"):
                for category_info in categories:
                    if category_type == "Weapon":
                        tag1, tag2 = category_info
                        label = f"{tag1} {tag2}"
                        items = bMult_Category(tier, tag1, tag2)
                    else:
                        label = tag1 = category_info
                        items = bMult_Category(tier, tag1)
                    
                    add_separator(label=label if tier == 0 else f"{label} (+{tier})")
                    
                    for i in range(0, len(items), 4):
                        with group(horizontal=True):
                            for item in items[i:i+4]:
                                button_tag = f"add_{category_type}_{tier}_{item}"
                                tooltip_tag = f"bazaar_tooltip_{tier}_{item}"
                                
                                add_button(label=isName(item), width=sitem_w, user_data=["Bazaar Add Item", category_type, item], callback=cbh, tag=button_tag)
                                check_del(tooltip_tag)
                                with tooltip(button_tag, tag=tooltip_tag): 
                                    disp_item_detail(item)

def disp_item_detail(item):
    data=bItem(item)
    if data.Slot == "Weapon": weapon_detail(data)
    if data.Slot == "Armor": armor_detail(data)

def weapon_detail(data):
    with group(horizontal=True):
        if data.get("Reach"):
            add_text("Reach", color=c_h1)
            add_text(data.Reach, color=c_text)
        if data.get("Range"):
            add_text("Range", color=c_h1)
            add_text(data.Range, color=c_text)
        add_text("Damage", color=c_h1)
        add_text(data.Damage, color=c_h5)
        add_text(data.Type, color=c_damagetype[f"{data.Type}"])
    with group(horizontal=True):
        add_text("Prop", color=c_h1)
        for prop in data.Prop: add_text(f"{prop}", color=c_text)
        add_text("Rarity", color=c_h1)
        add_text(item_rarity(data.Tier), color=c_rarity[f"{item_rarity(data.Tier)}"])
        add_text("Weight", color=c_h1)
        add_text(data.Weight, color=c_text)
        add_text("Cost", color=c_h1)
        add_text(data.Cost, color=c_h9)

def armor_detail(data):
    pass


def resize_window():
    print("resizing_window")


