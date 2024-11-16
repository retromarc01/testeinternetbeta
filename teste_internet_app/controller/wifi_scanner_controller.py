# wifi_scanner_controller.py
from jnius import autoclass, cast, PythonJavaClass, java_method
from kivy.utils import platform

class WifiScannerController:
    def __init__(self):
        if platform == 'android':
            self.activity = autoclass('org.kivy.android.PythonActivity').mActivity
            self.context = self.activity.getApplicationContext()
            self.WifiManager = autoclass('android.net.wifi.WifiManager')
            self.wifi = cast(self.WifiManager, self.context.getSystemService(self.WifiManager.WIFI_SERVICE))
            self.check_permissions()

    def check_permissions(self):
        # Verifica e solicita permissões em tempo de execução, se necessário
        if platform == 'android':
            Permission = autoclass('android.Manifest$permission')
            ActivityCompat = autoclass('androidx.core.app.ActivityCompat')
            PackageManager = autoclass('android.content.pm.PackageManager')
            
            # Permissões necessárias
            permissions = [
                Permission.ACCESS_FINE_LOCATION,
                Permission.ACCESS_WIFI_STATE,
                Permission.CHANGE_WIFI_STATE
            ]
            
            # Checa permissões
            for perm in permissions:
                if ActivityCompat.checkSelfPermission(self.context, perm) != PackageManager.PERMISSION_GRANTED:
                    ActivityCompat.requestPermissions(self.activity, permissions, 1)

    def scan_networks(self):
        if not self.wifi:
            print("Wi-Fi service not available.")
            return []
        
        try:
            # Inicia a varredura
            self.wifi.startScan()
            results = self.wifi.getScanResults()
            
            # Coleta resultados
            wifi_networks = []
            for result in results.toArray():
                ssid = result.SSID
                bssid = result.BSSID
                level = result.level
                capabilities = result.capabilities
                wifi_networks.append({
                    "ssid": ssid,
                    "bssid": bssid,
                    "signal_level": level,
                    "capabilities": capabilities
                })
            return wifi_networks
        
        except Exception as e:
            print(f"Erro ao escanear redes Wi-Fi: {e}")
            return []
