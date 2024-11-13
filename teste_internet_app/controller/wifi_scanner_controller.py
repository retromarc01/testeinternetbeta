# wifi_scanner_controller.py
from jnius import autoclass, cast
from kivy.utils import platform

class WifiScannerController:
    def __init__(self):
        # Verifica se está rodando no Android
        if platform == 'android':
            self.wifi_manager = autoclass('android.content.Context').WIFI_SERVICE
            self.context = autoclass('org.kivy.android.PythonActivity').mActivity.getApplicationContext()
            self.wifi = self.context.getSystemService(self.wifi_manager)
        else:
            self.wifi = None
            print("Wi-Fi scanning is only available on Android")

    def scan_networks(self):
        if not self.wifi:
            print("Wi-Fi service not available.")
            return []
        
        # Inicia o escaneamento
        self.wifi.startScan()
        results = self.wifi.getScanResults()
        
        # Extrai informações de cada rede
        wifi_networks = []
        for result in results.toArray():
            ssid = result.SSID
            bssid = result.BSSID
            level = result.level  # Nível do sinal
            capabilities = result.capabilities  # Segurança da rede
            wifi_networks.append({
                "ssid": ssid,
                "bssid": bssid,
                "signal_level": level,
                "capabilities": capabilities
            })
        
        return wifi_networks
