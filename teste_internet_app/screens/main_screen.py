from teste_internet_app.controller.controller_speedtest import ControllerSpeedTest
import os
#from kivy.uix.screenmanager import Screen
from kivymd.uix.screen import MDScreen
from kivymd.uix.screenmanager import MDScreenManager
from kivy_reloader.utils import load_kv_path
from kivy.clock import Clock
from kivy.properties import StringProperty
import asyncio
from kivy.metrics import dp
#from kivy_reloader.app import App
from threading import Thread
import time

#from teste_internet_app.controller.controller_speedtest import ControllerSpeedTest
main_screen_kv = os.path.join("teste_internet_app", "screens", "main_screen.kv")

load_kv_path(main_screen_kv)


class MainScreen(MDScreen):
    def __init__(self, controller, **kwargs):
        super().__init__(**kwargs)
        self.controller = controller
        print(self.ids)
        
    def update_display(self,data):
        self.controller = self.controller
        data = "teste de insercao"
        self.data = self.ids.in_data.text
        
    def on_some_event(self,*args):
        Clock.schedule_once(lambda dt: asyncio.run(self.controller.fetch_data()))
        self.data = str(args)
        self.controller.add_data(self.data)

        print(args)
        print(self.data)
        
    def iniciar_teste(self):
        self.ids.pb.value = 0
        Clock.unschedule(self.atualizar_progress_bar)
        
        self.threads_ativas = 8 # Inicializa o contador de threads ativas
        """thread_download = Thread(target=self.update_download)
        thread_download.start()
        thread_upload = Thread(target=self.update_upload)
        thread_upload.start()
        thread_ping = thread_ping = Thread(target=self.update_ping)
        thread_ping.start()"""
        self.thread_download = Thread(target=self.update_download)
        self.thread_upload = Thread(target=self.update_upload) 
        self.thread_ping = Thread(target=self.update_ping) 
        self.thread_lat = Thread(target=self.update_lat)
        self.thread_lon = Thread(target=self.update_lon)
        self.thread_ip = Thread(target=self.update_ip)
        self.thread_isp = Thread(target=self.update_operadora)
        self.thread_pais = Thread(target=self.update_pais)
        
        
        self.thread_download.start() 
        self.thread_upload.start() 
        self.thread_ping.start()
        self.thread_lat.start()
        self.thread_lon.start()
        self.thread_ip.start()
        self.thread_isp.start()
        self.thread_pais.start()
        
        # Agendar a atualização da barra de progresso 
        Clock.schedule_interval(self.atualizar_progress_bar, 0.1)
        
        
        
        
        
        
        """while thread_ping.is_alive() or thread_download.is_alive():
            if thread_download.is_alive():
                print("Aguardando a thread de download terminar...")
                Clock.schedule_interval(self.atualizar_progress_bar, 0.5)
            if thread_upload.is_alive():
                print("Aguardando a thread de upload terminar...")
                Clock.schedule_interval(self.atualizar_progress_bar, 0.5)
            if thread_ping.is_alive():
                print("Aguardando a thread de ping terminar...")
                
        print("Todas as threads terminaram a execução")"""
        
        """print("Aguardando a thread de ping terminar...")
            time.sleep(1) # Este bloco será executado quando a thread terminar 
        print("Thread de ping finalizada")"""
            
            
        """if thread_ping.is_alive():
                print("Aguardando a thread de ping terminar...")
            else:
                print("Thread de ping finalizada")
            time.sleep(1)"""
   
        
    def update_ping(self):
        self.speed_test_ping = ControllerSpeedTest().ping()
        self.speed_test_ping = str(self.speed_test_ping)
        #png = self.controller.ping()
        self.ids.campo_ping.text = str(self.speed_test_ping)
        self.threads_ativas -= 1
        print("Thread de ping finalizada")
        
    def update_download(self):
        self.speed_test_download = ControllerSpeedTest().download_speed()
        self.speed_test_download = str(self.speed_test_download)
        #download = self.controller.download_speed()
        self.ids.campo_download.text = str(self.speed_test_download)
        self.threads_ativas -= 1
        print("Thread de download finalizada") 
        
    def update_upload(self):
        self.speed_test_upload = ControllerSpeedTest().upload_speed()
        self.speed_test_upload = str(self.speed_test_upload)
        
        #upload = self.controller.upload_speed()
        self.ids.campo_upload.text = str(self.speed_test_upload)
        self.threads_ativas -= 1
        print("Thread de upload finalizada")
        
    def update_lat(self):
        self.speed_test_lat = ControllerSpeedTest().lat()
        self.speed_test_lat = str(self.speed_test_lat)
        self.ids.campo_lat.text = str(self.speed_test_lat)
        self.threads_ativas -= 1
        print("Thread de lat finalizada")
        
    def update_lon(self):
        self.speed_test_lon = ControllerSpeedTest().lon()
        self.speed_test_lon = str(self.speed_test_lon)
        self.ids.campo_lon.text = str(self.speed_test_lon)
        self.threads_ativas -= 1
        print("Thread de lon finalizada")
        
    def update_ip(self):
        self.speed_test_ip = ControllerSpeedTest().ip()
        self.speed_test_ip = str(self.speed_test_ip)
        self.ids.campo_ip.text = str(self.speed_test_ip)
        self.threads_ativas -= 1
        print("Thread de ip finalizada")
        
    def update_operadora(self):
        self.speed_test_isp = ControllerSpeedTest().isp()
        self.speed_test_isp = str(self.speed_test_isp)
        self.ids.campo_operadora.text = str(self.speed_test_isp)
        self.threads_ativas -= 1
        print("Thread de operadora finalizada")
        
    def update_pais(self):
        self.speed_test_pais = ControllerSpeedTest().pais()
        self.speed_test_pais = str(self.speed_test_pais)
        self.ids.campo_pais.text = str(self.speed_test_pais)
        self.threads_ativas -= 1
        print("Thread de pais finalizada")
        
        
    def atualizar_progress_bar(self, dt):
        total_threads = 8
        threads_restantes = self.threads_ativas 
        progresso = ((total_threads - threads_restantes) / total_threads) * 100 
        self.ids.pb.value = progresso # Atualizar o valor da barra de progresso 
        print(f"Progresso: {self.ids.pb.value:.2f}%") 
        
        if threads_restantes == 0: 
            Clock.unschedule(self.atualizar_progress_bar) 
            print("Todas as threads terminaram a execução")
        
    """def atualizar_progress_bar(self, dt): 
        current = self.ids.pb.value # Obter o valor atual da barra de progresso 
        if current >= 100.0: 
            Clock.unschedule(self.atualizar_progress_bar) 
            print("Todas as threads terminaram a execução") 
        else: 
            current += 1.0 # Atualizar o valor da barra de progresso 
            self.ids.pb.value = current 
            print(f"Progresso: {current}%")"""
