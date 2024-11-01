from teste_internet_app.screens.main_screen import MainScreen
from kivy_reloader.app import App
from teste_internet_app.controller.main_controller import MainController
from teste_internet_app.model.database import Database
from kivy.clock import Clock



class MainApp(App):

    def build(self):
        self.controller = MainController(None)
        self.view = MainScreen(self.controller)
        self.controller.view = self.view
        #self.controller = MainController(self.view)
        self.db = Database('my_database.db')
        #print(self.controller.data)
        self.db.create_table()

        return self.view


