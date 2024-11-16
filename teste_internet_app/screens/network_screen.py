#from teste_internet_app.controller.wifi_scanner_controller import WifiScannerController
import os
from kivy.clock import Clock
from kivymd.uix.list import OneLineListItem
from kivymd.uix.screen import MDScreen
from kivy_reloader.utils import load_kv_path
network_screen_kv = os.path.join("teste_internet_app", "screens", "network_screen.kv")
load_kv_path(network_screen_kv)

class NetworkScreen(MDScreen):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        #self.wifi_scanner = WifiScannerController()
        print("Nova instância de NetworkScreen criada!")
        print(self.ids)
        #Clock.schedule_once(self.display_networks, 1)  # Executa após a inicialização da tela

    def display_networks(self, *args):
        # Escaneia as redes disponíveis
        networks = self.wifi_scanner.scan_networks()
        
        if not networks:
            self.ids.container.add_widget(OneLineListItem(text="Nenhuma rede Wi-Fi encontrada"))
        else:
            # Adiciona cada rede como um item de lista
            for network in networks:
                network_info = f"{network['ssid']} - Sinal: {network['signal_level']}dBm"
                self.ids.container.add_widget(OneLineListItem(text=network_info))