#from kivy.uix.screenmanager import ScreenManager, Screen
from kivymd.uix.screenmanager import MDScreenManager
from teste_internet_app.screens.main_screen import MainScreen
from teste_internet_app.screens.historico_screen import HistoricoScreen
from teste_internet_app.controller.main_controller import MainController
#from screens.screen_two import ScreenTwo

#class MyScreenManager(ScreenManager):
class MyScreenManager(MDScreenManager):
    def __init__(self,controller, **kwargs):
        super().__init__(**kwargs)
        self.controller = controller
        self.add_widget(MainScreen(name='main_screen',controller=self.controller))
        self.add_widget(HistoricoScreen(name='historico_screen',controller=self.controller))