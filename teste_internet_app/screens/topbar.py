import os
from kivymd.uix.screen import MDScreen
from kivy_reloader.utils import load_kv_path
from teste_internet_app.controller.main_controller import MainController
from kivy.properties import ObjectProperty
from kivymd.uix.menu import MDDropdownMenu
from kivy.app import App 

topbar_screen_kv = os.path.join("teste_internet_app", "screens", "topbar.kv")
load_kv_path(topbar_screen_kv)

class TopBar(MDScreen):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        
        # Itens do menu e seus rótulos
        self.labels = ["historico", "network", "voltar"]
    
    def menu_callback(self, text_item):
        """
        Callback executado ao selecionar um item do menu.
        """
        print(f"Item selecionado: {text_item}")
        
        # Define ações baseadas no item selecionado
        if text_item == "historico":
            print("Ir para histórico")  # Altere conforme necessário
            # App.get_running_app().root.current = "historico"
        elif text_item == "voltar":
            print("Voltar para tela principal")  # Altere conforme necessário
            # App.get_running_app().root.current = "main"
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
        
        # Recria o menu dropdown com os itens atualizados e define o botão de chamada
        self.menu = MDDropdownMenu(
            items=menu_items,
            width_mult=4,
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