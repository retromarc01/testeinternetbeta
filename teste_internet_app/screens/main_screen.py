import os
from kivy.uix.screenmanager import Screen
from kivy_reloader.utils import load_kv_path
from kivy.clock import Clock
from kivy.properties import StringProperty
import asyncio
main_screen_kv = os.path.join("teste_internet_app", "screens", "main_screen.kv")

load_kv_path(main_screen_kv)


class MainScreen(Screen):
    def __init__(self, controller, **kwargs):
        super().__init__(**kwargs)
        self.controller = controller
    
    def update_display(self,data):
        data = "teste de insercao"

        print(data)
        self.data = self.ids.in_data.text
        
    def on_some_event(self,*args):
        Clock.schedule_once(lambda dt: asyncio.run(self.controller.fetch_data()))
        self.data = str(args)
        self.controller.add_data(self.data)

        print(args)
        print(self.data)