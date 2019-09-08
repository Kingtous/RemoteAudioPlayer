import bluetooth
from common import *

uuid = "fa288726-b927-4c4e-bf4b-f616f386332d"

def startBT():
    while True:
        server_sock = bluetooth.BluetoothSocket(bluetooth.RFCOMM)
        server_sock.bind(("", bluetooth.PORT_ANY))
        server_sock.listen(1)



class bluetooth_unlock_local_tr(threading.Thread):
    def __init__(self):
        super().__init__()

    def run(self):
        startBT()

if __name__ == "__main__":
    startBT()
