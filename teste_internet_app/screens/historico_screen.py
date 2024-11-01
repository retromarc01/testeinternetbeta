#from teste_internet_app.screens.myscreen_manager import MyScreenManager
from kivymd.uix.screen import MDScreen
from kivymd.uix.screenmanager import MDScreenManager

class HistoricoScreen(MDScreen):
    def __init__(self, controller, **kwargs):
        super().__init__(**kwargs)
        self.controller = controller