#from teste_internet_app.controller.wifi_scanner_controller import WifiScannerController
import trio
from teste_internet_app import MainApp


app = MainApp()
trio.run(app.async_run, "trio")