import os
from kivymd.uix.screen import MDScreen
from kivy_reloader.utils import load_kv_path
historico_screen_kv = os.path.join("teste_internet_app", "screens", "historico_screen.kv")
load_kv_path(historico_screen_kv)
class HistoricoScreen(MDScreen):
    def __init__(self, controller, **kwargs):
        super().__init__(**kwargs)
        self.controller = controller 