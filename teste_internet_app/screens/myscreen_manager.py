#from kivy.uix.screenmanager import ScreenManager, Screen
from kivymd.uix.screenmanager import MDScreenManager
import os
from kivy_reloader.utils import load_kv_path
from teste_internet_app.screens.main_screen import MainScreen
from teste_internet_app.screens.historico_screen import HistoricoScreen
from teste_internet_app.screens.network_screen import NetworkScreen
from teste_internet_app.controller.main_controller import MainController
from teste_internet_app.screens.topbar import TopBar
#myscreen_manager_kv = os.path.join("teste_internet_app", "screens", "myscreen_manager.kv")
#load_kv_path(myscreen_manager_kv)


class MyScreenManager(MDScreenManager):
    
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
 
        self.add_widget(MainScreen(name='main_screen'))
        self.add_widget(HistoricoScreen(name='historico_screen'))
        self.add_widget(NetworkScreen(name='network_screen'))
    def switch_to_screen(self, screen_name): 
        self.current = screen_name
        #print("Instancia de MyScreenManager")
        #self.add_widget(TopBar(name='topbar'))
   
    
    """def __init__(self,controller, **kwargs):
        super().__init__(**kwargs)

        self.controller = controller  
        self.add_widget(MainScreen(name='main_screen',controller=self.controller))
        self.add_widget(HistoricoScreen(name='historico_screen',controller=self.controller))
        self.add_widget(TopBar(name='topbar'))"""
   
