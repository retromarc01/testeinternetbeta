import os
from kivymd.uix.screen import MDScreen
from kivy_reloader.utils import load_kv_path
from teste_internet_app.controller.main_controller import MainController
from kivy.properties import ObjectProperty
from kivymd.uix.menu import MDDropdownMenu
from kivy.lang import Builder
from kivy.app import App 
from kivy.clock import Clock
from kivy.metrics import dp

#topbar_screen_kv = os.path.join("teste_internet_app", "screens", "topbar.kv")
#load_kv_path(topbar_screen_kv)
Builder.load_file("teste_internet_app/screens/topbar.kv")
class TopBar(MDScreen):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        #load_kv_path(topbar_screen_kv)
        
        # Itens do menu e seus rótulos
        print("Nova instância de TopBar criada!")
        Clock.schedule_once(self.check_ids, 0.1)
        self.labels = ["historico", "network", "voltar"]

    
    def menu_callback(self, text_item):
        """
        Callback executado ao selecionar um item do menu.
        """
        print(f"Item selecionado: {text_item}")
        app = App.get_running_app() 
        screen_manager = app.view
        
        # Define ações baseadas no item selecionado
        if text_item == "historico":
            print("Ir para histórico")  # Altere conforme necessário
            screen_manager.switch_to_screen("historico_screen")
            #print(screen_manager.current)
            #screen_manager.current = "historico_screen"
            #App.get_running_app().root.current = "historico_screen"
        elif text_item == "voltar":
            print("Voltar para tela principal")  # Altere conforme necessário
            screen_manager.switch_to_screen("main_screen")# App.get_running_app().root.current = "main"
        elif text_item == "network":
            print("Ir para tela de rede")  # Altere conforme necessário
            # App.get_running_app().root.current = "network"
        
        # Fecha o menu após a seleção
        self.menu.dismiss()
        
    def show_menu(self, button):
        """
        Abre o menu dropdown com itens atualizados e cor de texto dinâmica.
        """
        # Obtenha a cor de texto atualizada
        color_text = self.get_text_color()
        
        
        
        # Cria itens do menu com a cor de texto atualizada
        menu_items = [
            {
                "text": label,
                "viewclass": "OneLineListItem",
                "text_color": color_text,
                "on_release": lambda x=label: self.menu_callback(x),
            } for label in self.labels
        ]
        total_height = len(menu_items) * dp(56)
        # Recria o menu dropdown com os itens atualizados e define o botão de chamada
        self.menu = MDDropdownMenu(
            items=menu_items,
            max_height=total_height,
            width_mult=1.6,
            caller=button
        )
        
        # Abre o menu
        self.menu.open()
        
    def callback(self, button):
        """
        Callback genérico para abrir o menu.
        """
        self.show_menu(button)
        
    def get_text_color(self):
        """
        Obtém a cor do texto da aplicação.
        """
        # Acessa a cor de texto da aplicação, ou define um padrão
        color_text = App.get_running_app().get_text_color() if App.get_running_app() else [0, 0, 0, 1]
        return color_text
    
    def check_ids(self, *args):
        print("IDs disponíveis em TopBar:", self.ids)
        