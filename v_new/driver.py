from config.gen_import import *
from config.sub_import import *


class Game:
    def __init__(self):
        self.init_player()
        self.init_uix()

    def init_player(self):
        with open('pandas.json', 'r') as f:
            db = Box(json.load(f))
        self.p = Player(db)

    def init_uix(self):
        self.uix = UIX(self.p)
        self.p.set_uix(self.uix) 
        self.uix.init_ui()

    def save_db(self):
        with open('pandas.json', 'w') as f:
            json.dump(self.p.db.to_dict(), f, indent=4)



create_context()
with font_registry():
    font_choice = add_font("config/Helvetica.ttf", 13)
configure_app(init_file="config/config_save.ini", docking=True, docking_space=True)
create_viewport(title="rpg", width=1400, height=800)
bind_font(font_choice)
setup_dearpygui()

g = Game()

set_exit_callback(g.save_db)
show_viewport()
start_dearpygui()
destroy_context()
save_init_file("config/config_save.ini")
