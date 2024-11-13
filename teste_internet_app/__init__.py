#from teste_internet_app.controller.wifi_scanner_controller import WifiScannerController
from teste_internet_app.controller.controller_speedtest import ControllerSpeedTest
from teste_internet_app.controller.history_controller import HistoryController
#from kivy_garden.matplotlib.backend_kivyagg import FigureCanvasKivyAgg
from kivy_reloader.app import App
from kivymd.app import MDApp
from kivy.clock import Clock
from kivy.properties import StringProperty, ColorProperty
from teste_internet_app.screens.main_screen import MainScreen
from teste_internet_app.screens.historico_screen import HistoricoScreen
from teste_internet_app.screens.myscreen_manager import MyScreenManager
from kivymd.uix.screenmanager import MDScreenManager
#from teste_internet_app.controller.main_controller import MainController
#from teste_internet_app.model.database import Database
from kivymd.theming import ThemeManager
from kivymd.uix.label import MDLabel
from teste_internet_app.screens.topbar import TopBar
from kivymd.uix.card import MDCard 
from kivymd.uix.menu import MDDropdownMenu
from kivy.uix.boxlayout import BoxLayout
from kivy.core.window import Window
#Window.size = (360, 820) # simulando 1080 x 2460px
#Window.size = (360,640) # simulando 1080 x 1920px 
 
class MainApp(App,MDApp):
   
    def build(self):
        self.configure_theme()
        #self.controller = MainController(None)
        #self.view = MainScreen(self.controller)
        self.view = MyScreenManager()#(self.controller)
        self.topbar = TopBar()
        #self.historico = HistoricoScreen()
        
        # Configure a estrutura do layout principal
        main_layout = BoxLayout(orientation="vertical") 
        main_layout.add_widget(self.topbar)  # Adicione o TopBar ao layout principal
        main_layout.add_widget(self.view)    # 
        #self.topbar_screen = self.view.get_screen('topbar')
        #self.controller.view = self.view
        #self.topbar_screen = self.view.get_screen('topbar')
        #self.db = Database('my_database.db')
        #self.main_screen = MainScreen(self.controller)
        #print(self.main_screen.ids)
    
        #print(self.controller.data)
        #self.db.create_table()
        
        return main_layout
        #return self.view 
    
    def get_dynamic_text_color(self): 
        return [0, 0, 0, 1] if self.theme_cls.theme_style == "Light" else [1, 1, 1, 1]
    
    def get_text_color(self): 
        # Definir a cor do texto com base no tema 
        if self.theme_cls.theme_style == "Light": 
            return [0, 0, 0, 1] # Preto para tema claro 
        else: 
            return [1, 1, 1, 1] # Branco para tema escuro
        #return (0, 0, 0, 1)if self.theme_cls.theme_style == "Light"  else (1, 1, 1, 1)
    
    def get_card_bg_color(self): 
        return [1, 1, 1, 1] if self.theme_cls.theme_style == "Light" else [0.2, 0.2, 0.2, 1]
    
    
    def get_icon(self):
        return "moon-waning-crescent" if self.theme_cls.theme_style == "Light" else "white-balance-sunny"
    
    """def get_icon(self): # Define o ícone com base no tema atual 
        icon = "moon-waning-crescent" 
        if self.theme_cls.theme_style == "Light" : 
            icon = "moon-waning-crescent"
            return icon
        else : 
            icon = "white-balance-sunny"
            return icon"""
        
        #return  #"moon-waning-crescent" if self.theme_cls.theme_style == "Light" else "white-balance-sunny"
    
    def configure_theme(self):
        self.theme_cls.theme_style = "Light"
        self.theme_cls.primary_palette = "Blue"
        self.theme_cls.primary_hue = "500"
        self.theme_cls.accent_palette = "Red"
    
    """def configure_theme(self): 
        self.theme_cls.theme_style = "Light" # Você pode mudar para "Dark" 
        self.theme_cls.primary_palette = "Blue" # Altere para a paleta desejada 
        self.theme_cls.primary_hue = "500" # Opcional, para definir a tonalidade principal 
        self.theme_cls.accent_palette = "Red" # Opcional, para definir a cor de destaque # Definindo cores personalizadas para botões 
        #self.theme_cls.text_color = [0, 0, 0, 1]
        #self.theme_cls.primary_dark = "#1976D2" # Azul escuro, por exemplo 
        #self.theme_cls.primary_light = "#BBDEFB" # Azul claro, por exemplo 
        #self.theme_cls.text_color = "#FFFFFF" # Cor do texto do botão"""
        
    def on_start(self):
        # Aguarda o carregamento do layout e acessa o ID
        #Clock.schedule_once(self.set_topbar_icon, 0.1)
        self.set_topbar_icon()
        #Clock.schedule_once(self.check_connection, 0.1)
        
        
    def set_topbar_icon(self):
        print("set_topbar_icon")
        try:
            if 'topbar' in self.topbar.ids:
                self.topbar.ids.topbar.right_action_items = [[self.get_icon(), lambda x: self.switch_theme()]]
                print("Ícone atualizado:", self.topbar.ids.topbar.right_action_items)
            else:
                print("ID 'topbar' não encontrado em TopBar.")
        except Exception as e:
            print(f"Erro ao acessar topbar: {e}")
        
    """def set_topbar_icon(self):
        print("set_topbar_icon")
        print(self.topbar_screen.ids.topbar.right_action_items)
        try:
            # Atualiza o ícone no TopBar, acessando a instância armazenada
            if 'topbar' in self.topbar_screen.ids:
                self.topbar_screen.ids.topbar.right_action_items = [[self.get_icon(), lambda x: self.switch_theme()]]
                print("Ícone atualizado!")
            else:
                print("ID 'topbar' não encontrado em TopBar.")
        except Exception as e:
            print(f"Erro ao acessar topbar: {e}")"""
        
    def switch_theme(self): # Troca entre "Light" e "Dark" 
        #self.topbar = TopBar()
        #print(self.topbar.ids.topbar.right_action_items)
        print(self.root.ids)
        
        
        if self.theme_cls.theme_style == "Light" : 
            self.theme_cls.theme_style = "Dark"
      
           
        else: 
            self.theme_cls.theme_style = "Light"
            
        self.set_topbar_icon()
            
        
            
        #self.topbar.ids.topbar.right_action_items = [[self.get_icon(), lambda x: self.switch_theme()]]
        for widget in self.root.walk(): 
            if isinstance(widget, MDLabel): 
                widget.text_color = self.get_text_color()
            
            if isinstance(widget, MDCard): 
                widget.md_bg_color = self.get_card_bg_color()
    
    """def check_connection(self, *args): 
        controller = ControllerSpeedTest() 
        if not controller.verificar_conexao(): 
            self.show_error_label()     
                
    def show_error_label(self): # Adiciona uma MDLabel com a mensagem de erro à tela principal 
        main_layout = BoxLayout(orientation="vertical") 
        error_label = MDLabel( text="Não há conexão com a internet.", halign="center", theme_text_color="Error" ) 
        
        main_layout.add_widget(error_label)""" 
            
                
