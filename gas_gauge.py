import rumps
import requests
import threading
import json

class GasGauge(rumps.App):
    def __init__(self):
        super(GasGauge, self).__init__('Gas Gauge')
        try:
            self.check_gas_price()
        except Exception:
            pass

    def check_gas_price(self):
        try:
            r = requests.get('https://api.etherscan.io/api?module=gastracker&action=gasoracle')
            res = json.loads(r.text)
            gas_price = res['result']['FastGasPrice']
            self.title = gas_price
        except Exception:
            pass

        threading.Timer(60, self.check_gas_price).start()

if __name__ == '__main__':
    GasGauge().run()
