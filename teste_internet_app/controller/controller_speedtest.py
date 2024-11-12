from teste_internet_app.model.database import Database
from threading import Thread
import speedtest 
#from speedtest import Speedtest
import time
import ssl
import logging
import requests


db=Database(db_name='testeinternet.db')


ssl._create_default_https_context = ssl._create_stdlib_context


class ControllerSpeedTest(Thread):
    def __init__(self):
        super().__init__()
        
        logging.basicConfig(level=logging.DEBUG, 
                            format='%(asctime)s - %(name)s - %(levelname)s - %(message)s', 
                            handlers=[ logging.FileHandler("controllerspeedtest.log"),
                                      logging.StreamHandler() ])
        self.logger = logging.getLogger('ControllerSpeedTest')
        self.logger.info("iniciando classe")
        self.logger.info("verificando se ha internet")
        """if self.verificar_conexao(): 
            print("Internet está disponível.")
            self.logger.info("internet disponivel")
        else: 
            print("Internet não está disponível.")
            self.logger.info("sem internet")"""
        self.logger.info("iniciando modulo speedtest")
        self.speedtest = speedtest.Speedtest(secure=True)
        self.speedtest.get_best_server()
        #self.test_speed()
        self._initialized = True
        
        
    def humansize(self,nbytes):
        self.logger.info("executando humanize")
        suffixes = ['B', 'KB', 'MB', 'GB', 'TB', 'PB']
        i = 0
        while nbytes >= 1024 and i < len(suffixes)-1:
            nbytes /= 1024.
            i += 1
        f = ('%.2f' % nbytes).rstrip('0').rstrip('.')
        return '%s %s' % (f, suffixes[i])

    def download_speed(self):
        self.logger.info("executando download")
        self.download = self.speedtest.download()
        self.download = self.humansize(self.download)
        print((self.download))
        return self.download#self.speedtest.download()

    def upload_speed(self):
        self.logger.info("executando upload")
        self.upload = self.speedtest.upload()
        self.upload = self.humansize(self.upload)
        print(self.upload)
        return self.upload

    def ping(self):
        self.logger.info("executando ping")
        print(self.speedtest.results.ping)
        #print(str(self.png))
        return self.speedtest.results.ping
    
    def lat(self):
        self.logger.info("executando lat")
        self.speedtest.get_config()
        self.lat = self.speedtest.results.client["lat"]
        #print(self.speedtest.results.client["lat"])
        #self.lat = self.speedtest["client"]["lat"]
        return self.lat
    
    def lon(self):
        self.logger.info("executando long")
        self.speedtest.get_config()
        self.lon = self.speedtest.results.client["lon"]
        #print(self.speedtest.results.client["lon"])
        #self.long = self.speedtest["client"]["lon"]
        return self.lon
    
    def ip(self):
        self.logger.info("executando ip")
        self.speedtest.get_config()
        self.ip = self.speedtest.results.client["ip"]
        #print(self.speedtest.results.client["ip"])
        #self.ip = self.speedtest["client"]["ip"]
        return self.ip
    
    def isp(self):
        self.logger.info("executando isp")
        print(self.speedtest.results.client["isp"])
        self.isp = self.speedtest.results.client["isp"]
        #print(self.speedtest.results.client["isp"])
        #self.isp = self.speedtest["client"]["isp"]
        return self.isp
    
    def pais(self):
        self.logger.info("executando pais")
        self.speedtest.get_config()
        self.pais = self.speedtest.results.client["country"]
        #print(self.speedtest.results.client["country"])
        #self.pais = self.speedtest["client"]["country"]
        return self.pais
    
    """def testando(self):
        self.logger.info("executando teste")
        self.speedtest.get_config()
        print(self.speedtest.results.client)
        #print(self.speedtest.results.server)"""
    

    def test_speed(self):
        self.logger.info("executando teste")
        thread_download = Thread(target=self.download_speed)
        thread_download.start()
        thread_upload = Thread(target=self.upload_speed)
        thread_upload.start()
        thread_ping = thread_ping = Thread(target=self.ping)
        thread_ping.start()
        while thread_download.is_alive() or thread_upload.is_alive() or thread_ping.is_alive():
            if thread_download.is_alive():
                print("Aguardando a thread de download terminar...")
            if thread_upload.is_alive():
                print("Aguardando a thread de upload terminar...")
            if thread_ping.is_alive():
                print("Aguardando a thread de ping terminar...")
            time.sleep(1)
        print("Todas as threads terminaram a execução")
        
    def test_speed_ping(self):
        thread_ping = thread_ping = Thread(target=self.ping)
        thread_ping.start()
        while thread_ping.is_alive():
            if thread_ping.is_alive():
                print("Aguardando a thread de ping terminar...")
            time.sleep(1)
        
    def verificar_conexao(self): 
        url = "http://www.google.com" 
        timeout = 5 
        try: # Enviar uma solicitação GET para a URL com um timeout de 5 segundos 
            request = requests.get(url, timeout=timeout) # Se a resposta do status for 200 (OK), há conexão com a internet 
            if request.status_code == 200: 
                print("Conexão com a internet estabelecida.") 
                return True 
        except requests.ConnectionError: 
            print("Não há conexão com a internet.") 
        return False
    
    def verificar_conexao(self): 
        url = "http://www.google.com" 
        timeout = 5 
        try: 
            request = requests.get(url, timeout=timeout) 
            if request.status_code == 200: 
                print("Conexão com a internet estabelecida.") 
                return True 
        except requests.ConnectionError: 
            print("Não há conexão com a internet.") 
            return False 
        return False
    
    """def teste_conectividade(self):
        self.logger.info("executando teste de conectividade")
        if self.verificar_conexao(): 
            print("Internet está disponível.")
            self.logger.info("internet disponivel")
        else: 
            print("Internet não está disponível.")
            self.logger.info("sem internet")
        return self.verificar_conexao()"""
    
    def data_hora(self):
        self.logger.info("executando data e horario")
        self.speedtest.get_config()
        self.data = self.speedtest.results.timestamp
        print(self.data)
        return self.data
    
    def save_results_to_db(self, data_hora, ping, ip, operadora, upload_speed, download_speed, lon, lat, pais):
        self.logger.info("salvando resultados no banco de dados")
        db.create_history(data_hora, ping, ip, operadora, upload_speed, download_speed, lon, lat, pais)
        
    def show_table(self):
        self.logger.info("exibindo tabela")
        db.show_columns()
        
    @staticmethod
    def get_history():
        #self.logger.info("exibindo historico")
        history = db.get_all_history()
        #print("historico controller")
        #print(type(history))
        return history
#teste = ControllerSpeedTest().data_hora()
#print(vars(ControllerSpeedTest()))
