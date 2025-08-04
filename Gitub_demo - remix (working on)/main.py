from dearpygui.dearpygui import *
import shared
import json, sys, os
from colorist import *

from manager.components import Milestone_comp, Race_comp, Class_comp, Background_comp


from manager.character import init_pc
from Sheet.UI import init_ui, populate_Start #, resize_window
# resize_state = {"is_resizing": False, "frame_counter": 0, "delay_frames": 10}

def resource_path(relative_path):
    try: base_path = sys._MEIPASS
    except Exception: base_path = os.path.abspath(".")
    return os.path.join(base_path, relative_path)

# def viewport_resize_callback(sender, app_data):
#     resize_state["is_resizing"] = True
#     resize_state["frame_counter"] = 0

def on_exit_callback():
    shared.save_json()
    save_init_file(resource_path("utils/config_save.ini"))
    stop_dearpygui()

create_context()
with font_registry(): font_choice = add_font(resource_path("utils/Helvetica.ttf"), 13)
configure_app(init_file=resource_path("utils/config_save.ini"), docking=True, docking_space=True)
create_viewport(title="rpg", width=1300, height=860)
#set_viewport_resize_callback(viewport_resize_callback)
set_exit_callback(on_exit_callback)
bind_font(font_choice)
setup_dearpygui()


init_pc()
shared.pc.start_configuration()
init_ui()
populate_Start()
show_viewport()
start_dearpygui()


destroy_context()
# while is_dearpygui_running():
#     if resize_state["is_resizing"]:
#         resize_state["frame_counter"] += 1
#         if resize_state["frame_counter"] > resize_state["delay_frames"]:
#             resize_window()
#             resize_state["is_resizing"] = False
#             resize_state["frame_counter"] = 0
#     render_dearpygui_frame()
