import os
#from kivy.uix.screenmanager import Screen
from kivymd.uix.screen import MDScreen
from kivymd.uix.screenmanager import MDScreenManager
from kivy_reloader.utils import load_kv_path
from kivy.clock import Clock
from kivy.properties import StringProperty
import asyncio
from kivy.metrics import dp
main_screen_kv = os.path.join("teste_internet_app", "screens", "main_screen.kv")

load_kv_path(main_screen_kv)


class MainScreen(MDScreen):
    def __init__(self, controller, **kwargs):
        super().__init__(**kwargs)
        self.controller = controller
        #self.data = self.ids.in_data.text
        #print(self.ids.in_data.text)
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