import os
from kivymd.uix.screen import MDScreen
from kivy_reloader.utils import load_kv_path
from teste_internet_app.controller.main_controller import MainController
topbar_screen_kv = os.path.join("teste_internet_app", "screens", "topbar.kv")
load_kv_path(topbar_screen_kv)
class TopBar(MDScreen):
    #controller = MainController()
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
    