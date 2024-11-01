import asyncio
from kivy.clock import Clock
from teste_internet_app.model.database import Database
from teste_internet_app.screens.main_screen import MainScreen

class MainController:
    #view = MainScreen()
    
    def __init__(self, view):
        self.view = view
        self.db = Database('my_database.db')
        #self.test_init()
        #self.fetch_data()
        self.show_table()


    async def fetch_data(self):
        await asyncio.sleep(1)  # Simulação de operação assíncrona 
        data = self.db.fetch_data()
        Clock.schedule_once(lambda dt: self.view.update_display(data))
        

    def add_data(self, data):
        self.db.insert_data(data)
        Clock.schedule_once(lambda dt: self.fetch_data())
        #Clock.schedule_once(lambda dt: self.fetch_data())
        
    def show_table(self):
        tabela = self.db.show_table()
        print(tabela[1])
        
        
        
