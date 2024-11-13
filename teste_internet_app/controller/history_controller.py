from teste_internet_app.model.database import Database
import logging
db=Database(db_name='testeinternet.db')

class HistoryController():
    def __init__(self):
        super().__init__()
        logging.basicConfig(level=logging.DEBUG, 
                            format='%(asctime)s - %(name)s - %(levelname)s - %(message)s', 
                            handlers=[ logging.FileHandler("history_controller.log"),
                                      logging.StreamHandler() ])
        self.logger = logging.getLogger('HistoryController')
        
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