from kivy_reloader.app import App
from kivymd.app import MDApp
from kivy.clock import Clock
from kivy.properties import StringProperty, ColorProperty
from teste_internet_app.screens.main_screen import MainScreen
from teste_internet_app.screens.myscreen_manager import MyScreenManager
from kivymd.uix.screenmanager import MDScreenManager
from teste_internet_app.controller.main_controller import MainController
from teste_internet_app.model.database import Database
from kivymd.theming import ThemeManager

 
class MainApp(App,MDApp):
    #bg_color = ColorProperty()
    
    def build(self):
        self.configure_theme()
        self.controller = MainController(None)
        #self.view = MainScreen(self.controller)
        self.view = MyScreenManager(self.controller)#(self.controller)
        self.controller.view = self.view
        #self.myscreen_manager = self.controller.view
        #self.myscreen_manager.main_screen = getattr(MainScreen)
        #self.theme_cls.dynamic_color = True
        #self.theme_cls.theme_style = "Dark"
        #self.theme_cls.primary_palette = "Purple"
        #self.configure_theme()
        #self.controller = MainController(self.view)
        self.db = Database('my_database.db')
        #print(self.controller.data)
        self.db.create_table()
 
        return self.view
    
    def configure_theme(self): 
        self.theme_cls.theme_style = "Dark" # Você pode mudar para "Dark" 
        self.theme_cls.primary_palette = "Purple" # Altere para a paleta desejada 
        self.theme_cls.primary_hue = "500" # Opcional, para definir a tonalidade principal 
        self.theme_cls.accent_palette = "Red" # Opcional, para definir a cor de destaque # Definindo cores personalizadas para botões 
        #self.theme_cls.primary_dark = "#1976D2" # Azul escuro, por exemplo 
        #self.theme_cls.primary_light = "#BBDEFB" # Azul claro, por exemplo 
        #self.theme_cls.text_color = "#FFFFFF" # Cor do texto do botão
