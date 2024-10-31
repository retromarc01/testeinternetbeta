from teste_internet_app.screens.main_screen import MainScreen
from kivy_reloader.app import App


class MainApp(App):
    def build(self):
        return MainScreen()