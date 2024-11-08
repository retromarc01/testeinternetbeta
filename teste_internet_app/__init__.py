from teste_internet_app.controller.controller_speedtest import ControllerSpeedTest
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
from kivymd.uix.label import MDLabel
from teste_internet_app.screens.topbar import TopBar
from kivymd.uix.card import MDCard
from kivy.core.window import Window
#Window.size = (360, 640)

 
class MainApp(App,MDApp):
    #bg_color = ColorProperty()
    def build(self):
        self.configure_theme()
        self.controller = MainController(None)
        #self.view = MainScreen(self.controller)
        self.view = MyScreenManager(self.controller)#(self.controller)
        self.controller.view = self.view
<<<<<<< HEAD
=======
        #self.main_screen = MainScreen(self.controller)
        #self.theme_cls.theme_style_switch_animation = True
        #self.theme_cls.theme_style_switch_animation_duration = 0.8
        #self.theme_cls.theme_style = "Dark"
        #self.theme_cls.primary_hue = "600"
        #self.theme_cls.primary_palette = "Purple"
        #self.myscreen_manager = self.controller.view
        #self.myscreen_manager.main_screen = getattr(MainScreen)
        #self.theme_cls.dynamic_color = True
        #self.theme_cls.theme_style = "Dark"
        #self.theme_cls.primary_palette = "Purple"
        #self.configure_theme()

        #self.controller = MainController(self.view)
>>>>>>> testing
        self.db = Database('my_database.db')
        self.main_screen = MainScreen(self.controller)
        print(self.main_screen.ids)
    
        #print(self.controller.data)
        self.db.create_table()
 
        return self.view
    
    def get_card_bg_color(self): 
        return [1, 1, 1, 1] if self.theme_cls.theme_style == "Light" else [0.2, 0.2, 0.2, 1]
    
    
    def get_icon(self): # Define o ícone com base no tema atual 
        return "moon-waning-crescent" if self.theme_cls.theme_style == "Light" else "white-balance-sunny"
    
    def configure_theme(self): 
        self.theme_cls.theme_style = "Light" # Você pode mudar para "Dark" 
        self.theme_cls.primary_palette = "Blue" # Altere para a paleta desejada 
        self.theme_cls.primary_hue = "500" # Opcional, para definir a tonalidade principal 
        self.theme_cls.accent_palette = "Red" # Opcional, para definir a cor de destaque # Definindo cores personalizadas para botões 
        #self.theme_cls.text_color = [0, 0, 0, 1]
        #self.theme_cls.primary_dark = "#1976D2" # Azul escuro, por exemplo 
        #self.theme_cls.primary_light = "#BBDEFB" # Azul claro, por exemplo 
        #self.theme_cls.text_color = "#FFFFFF" # Cor do texto do botão
        
    
        
    def switch_theme(self): # Troca entre "Light" e "Dark" 
        self.topbar = TopBar()
        print(self.topbar.ids.topbar.right_action_items)
        
        if self.theme_cls.theme_style == "Light" : 
            self.theme_cls.theme_style = "Dark" 
           
        else: self.theme_cls.theme_style = "Light"
        #self.topbar.ids.topbar.right_action_items = [[self.get_icon(), lambda x: self.switch_theme()]]
        for widget in self.root.walk(): 
            if isinstance(widget, MDLabel): widget.text_color = self.get_text_color()
            if isinstance(widget, MDCard): widget.md_bg_color = self.get_card_bg_color()
            
                
        self.topbar.ids.topbar.right_action_items = [[self.get_icon(), lambda x: self.switch_theme()]]
            
        
        
    def get_text_color(self): 
<<<<<<< HEAD
        return (0, 0, 0, 1)if self.theme_cls.theme_style == "Light"  else (1, 1, 1, 1)
=======
        return (0, 0, 0, 1)if self.theme_cls.theme_style == "Light"  else (1, 1, 1, 1)
    
    
    
    """def get_ping(self):
        print("ping")
        ping = ControllerSpeedTest().ping()
        print(ping)
        print(ControllerSpeedTest().ping())
        ping = str(ping)
        self.update_label_ping(ping)
        return str(ping)
    
    def update_label_ping(self,ping):
        ping = str(ping)
        print(ping) 
        return ping"""
>>>>>>> testing
