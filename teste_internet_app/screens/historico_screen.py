#from teste_internet_app.controller.controller_speedtest import ControllerSpeedTest
from teste_internet_app.controller.history_controller import HistoryController
import os
from kivymd.uix.screen import MDScreen
from kivymd.uix.label import MDLabel
from kivy_reloader.utils import load_kv_path
from kivy.clock import Clock
from kivymd.uix.list import OneLineListItem
from datetime import datetime
from kivy.app import App
import matplotlib.pyplot as plt
from kivy_garden.matplotlib.backend_kivyagg import FigureCanvasKivyAgg

historico_screen_kv = os.path.join("teste_internet_app", "screens", "historico_screen.kv")
load_kv_path(historico_screen_kv)

class HistoricoScreen(MDScreen):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        self.get_history()

    def get_history(self):
        """Obtém o histórico de testes de internet e o armazena em `self.history`."""
        try:
            print("Obtendo histórico... instanciando HistoryController")
            controller = HistoryController()
            raw_history = controller.get_history()

            if raw_history is None:
                print("Nenhum dado retornado pela consulta.")
                return

            self.history = []
            for entry in raw_history:
                id, data_hora, ping, ip, operadora, upload, download, lon, lat, pais = entry[0:]
                self.history.append({
                    "id": id,
                    "data_hora": data_hora,
                    "ping": ping,
                    "ip": ip,
                    "operadora": operadora,
                    "upload": float(upload.replace(' MB', '')),
                    "download": float(download.replace(' MB', '')),
                    "lon": lon,
                    "lat": lat,
                    "pais": pais
                })

            if self.history:
                for item in self.history:
                    datetime_obj = datetime.fromisoformat(item["data_hora"].replace('Z', '+00:00'))
                    formatted_date = datetime_obj.strftime('%d/%m/%Y - %H:%M')
                    item["data_hora"] = formatted_date
                    list_item = OneLineListItem(
                        text=f"{item['id']} - {item['data_hora']} - upload:  {item['upload']} MB - download: {item['download']} MB",
                        text_color=App.get_running_app().get_text_color(),
                        on_release=lambda instance, item_id=item['id']: self.item_lista_screen(item_id)
                    )
                    self.ids.container.add_widget(list_item)
            else:
                print("Nenhum histórico encontrado.")
               
        except Exception as e:
            print(f"Erro ao obter histórico: {e}")

    def refresh_callback(self, *args):
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
        print(f"ID do item clicado: {item_id}") 

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
            text=f"Data: {item['data_hora']} " + 
                 f"IP: {item['ip']} " + 
                 f"Download: {item['download']} MB " + 
                 f"Upload: {item['upload']} MB",
            halign="center"
        ) 
        screen_list.add_widget(label_ip)

        # Adicionar o gráfico como um widget abaixo do label
        grafico_widget = self.plotar_grafico(item_id)
        screen_list.add_widget(grafico_widget)

        # Adicionar a nova tela ao screen_manager e definir como a tela atual 
        screen_manager.add_widget(screen_list) 
        screen_manager.current = str(item_id)
    
    def plotar_grafico(self, item_id):
        # Verifica o tema atual do aplicativo
        app = App.get_running_app()
        tema_escuro = app.theme_cls.theme_style == "Dark" # Define cores baseadas no tema atual 
        cor_fundo_figura = 'black' if tema_escuro else 'white' 
        cor_fundo_grafico = 'black' if tema_escuro else 'lightgray' 
        cor_download = 'blue' 
        cor_upload = 'green' 
        cor_titulo = 'white' if tema_escuro else 'black'

        # Obtém as três últimas entradas a partir do item atual
        item_index = next((index for (index, d) in enumerate(self.history) if d["id"] == item_id), None)
        if item_index is None:
            print("Item não encontrado para plotagem.")
            return
        
        ultimos_tres = self.history[max(0, item_index-2):item_index+1]

        # Extrair dados para o gráfico
        datas = [item['data_hora'] for item in ultimos_tres]
        downloads = [item['download'] for item in ultimos_tres]
        uploads = [item['upload'] for item in ultimos_tres]

        # Configurar e exibir o gráfico com as cores do tema
        fig, ax = plt.subplots(facecolor=cor_fundo_figura) 
        ax.set_facecolor(cor_fundo_grafico)
        bar_width = 0.35

        # Barras de download e upload
        ax.bar(range(len(datas)), downloads, width=bar_width, color=cor_download, label='Download')
        ax.bar([i + bar_width for i in range(len(datas))], uploads, width=bar_width, color=cor_upload, label='Upload')

        # Configuração dos rótulos e título
        ax.set_xlabel('Data e Hora', color=cor_titulo)
        ax.set_ylabel('MB', color=cor_titulo)
        ax.set_title('Download e Upload das últimas 3 consultas', color=cor_titulo)
        ax.set_xticks([i + bar_width / 2 for i in range(len(datas))])
        ax.set_xticklabels(datas, rotation=45, color=cor_titulo)
        ax.legend(facecolor=cor_fundo_figura)
        plt.tight_layout()

    # Retorna o gráfico como um widget Kivy
        return FigureCanvasKivyAgg(fig)
    """def plotar_grafico(self, item_id):
        # Obtém as três últimas entradas a partir do item atual
        item_index = next((index for (index, d) in enumerate(self.history) if d["id"] == item_id), None)
        if item_index is None:
            print("Item não encontrado para plotagem.")
            return
        
        ultimos_tres = self.history[max(0, item_index-2):item_index+1]

        # Extrair dados para o gráfico
        datas = [item['data_hora'] for item in ultimos_tres]
        downloads = [item['download'] for item in ultimos_tres]
        uploads = [item['upload'] for item in ultimos_tres]

        # Configurar e exibir o gráfico
        fig, ax = plt.subplots(facecolor='gray') 
        ax.set_facecolor("black")
        bar_width = 0.35

        # Barras de download e upload
        ax.bar(range(len(datas)), downloads, width=bar_width, color='blue', label='Download')
        ax.bar([i + bar_width for i in range(len(datas))], uploads, width=bar_width, color='green', label='Upload')

        # Configuração dos rótulos e título
        ax.set_xlabel('Data e Hora')
        ax.set_ylabel('MB')
        ax.set_title('Download e Upload das últimas 3 consultas')
        ax.set_xticks([i + bar_width / 2 for i in range(len(datas))])
        ax.set_xticklabels(datas, rotation=45)
        ax.legend()
        plt.tight_layout()

        # Retorna o gráfico como um widget Kivy
        return FigureCanvasKivyAgg(fig)"""
