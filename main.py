import trio
from teste_internet_app import MainApp


app = MainApp()
trio.run(app.async_run, "trio")