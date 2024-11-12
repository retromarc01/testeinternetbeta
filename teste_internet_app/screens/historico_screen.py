from teste_internet_app.controller.controller_speedtest import ControllerSpeedTest
import os
from kivymd.uix.screen import MDScreen
from kivymd.uix.label import MDLabel
from kivy_reloader.utils import load_kv_path
from kivy.clock import Clock
from kivymd.uix.list import OneLineListItem
from datetime import datetime
from kivy.app import App

historico_screen_kv = os.path.join("teste_internet_app", "screens", "historico_screen.kv")
load_kv_path(historico_screen_kv)

class HistoricoScreen(MDScreen):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        self.get_history()

    def get_history(self):
        """Obtém o histórico de testes de internet e o armazena em `self.history`."""
        try:
            # Instancia o ControllerSpeedTest e chama o método get_history
            controller = ControllerSpeedTest()
            raw_history = controller.get_history()  # Chamada correta do método

            # Verifica se raw_history contém dados válidos
            if raw_history is None:
                print(type(raw_history))
                print("Nenhum dado retornado pela consulta.")
                return
            
            # Processa cada entrada no histórico e armazena em uma lista de dicionários
            self.history = []
            for entry in raw_history:
                id, data_hora, ping, ip, operadora, upload, download, lon, lat, pais = entry[0:]
                self.history.append({
                    "id": id,
                    "data_hora": data_hora,
                    "ping": ping,
                    "ip": ip,
                    "operadora": operadora,
                    "upload": upload,
                    "download": download,
                    "lon": lon,
                    "lat": lat,
                    "pais": pais
                })

            if self.history:
                print(f"Histórico carregado com sucesso: {len(self.history)} registros encontrados.")
                for item in self.history:
                    print(item)
                    datetime_obj = datetime.fromisoformat(item["data_hora"].replace('Z', '+00:00'))
                    formatted_date = datetime_obj.strftime('%d/%m/%Y - %H:%M')
                    item["data_hora"] = formatted_date
                    list_item = OneLineListItem(
                        text=f"{item['id']} - {item['data_hora']} - {item['upload']} - {item['download']}",
                        text_color=App.get_running_app().get_text_color(),
                        on_release=lambda instance, item_id=item['id']: self.item_lista_screen(item_id)
                    )
                    self.ids.container.add_widget(list_item)
            else:
                print("Nenhum histórico encontrado.")
               
        except Exception as e:
            print(f"Erro ao obter histórico: {e}")

    def refresh_callback(self, *args):
        '''A method that updates the state of your application
        while the spinner remains on the screen.'''

        def refresh_callback(interval):
            self.ids.container.clear_widgets()
            self.get_history()
            self.ids.refresh_layout.refresh_done()

        Clock.schedule_once(refresh_callback, 1)
        
    def listar_historico(self):
        self.get_history()
        print("Listando histórico")
        print(self.history)
        print("Fim da listagem")
        return self.history

    def item_lista_screen(self, item_id): 
        app = App.get_running_app() 
        screen_manager = app.view 
        print("item_lista_screen") 
        print(f"ID do item clicado: {item_id}") 
        print(screen_manager.current) 

        # Encontre o item no histórico pelo ID
        item = next((x for x in self.history if x["id"] == item_id), None)
        if not item:
            print("Item não encontrado.")
            return

        # Criar uma nova tela com o ID do item clicado
        screen_list = MDScreen(name=str(item_id)) 

        # Criar e adicionar MDLabels à nova tela 
        label_ip = MDLabel(
            text_color=App.get_running_app().get_text_color(),
            theme_text_color="Custom",
            text=f"data: {item['data_hora']} " + 
                 f"ip: {item['ip']} " + 
                 f"download: {item['download']} " + 
                 f"upload: {item['upload']}",
            halign="center"
        ) 
        screen_list.add_widget(label_ip) 

        # Adicionar a nova tela ao screen_manager e definir como a tela atual 
        screen_manager.add_widget(screen_list) 
        screen_manager.current = str(item_id)
