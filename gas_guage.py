import rumps
import requests
import threading
import json

class GasGuage(rumps.App):
    def __init__(self):
        super(GasGuage, self).__init__('Gas Guage')
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

        threading.Timer(300, self.check_gas_price).start()

if __name__ == '__main__':
    GasGuage().run()
