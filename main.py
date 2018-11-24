from Bluetooth_Com import bluetooth_thread
from KeyboardListener import KeyboardListener
from IHMViewer import graphical_thread

commands = {'mode': 0,
            'forward':   0,
            'backward': 0,
            'right': 0,
            'left':  0,
            'up': 0,
            'down': 0,
            'speedmode': 0
            }


message = '00000000'

# I'ROBOT MAC ADRESS
# 00:1B:10:61:12:44
Mbluetooth_thread= bluetooth_thread('F4:60:E2:8F:A0:E7', message)
mgraphical_thread = graphical_thread(Mbluetooth_thread, commands)


Mbluetooth_thread.start()

MKeyboardListener = KeyboardListener(commands)


Mbluetooth_thread.set_params(mgraphical_thread, MKeyboardListener)

MKeyboardListener.start()

mgraphical_thread.run()