from Bluetooth_Com import bluetooth_thread
from KeyboardListener import KeyboardListener
from IHMViewer import graphical_thread
# import ipdb; ipdb.set_trace()

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
Mbluetooth_thread= bluetooth_thread('00:1B:10:61:12:44', message)
mgraphical_thread = graphical_thread(Mbluetooth_thread, commands)


Mbluetooth_thread.start()

MKeyboardListener = KeyboardListener(commands)


Mbluetooth_thread.set_params(mgraphical_thread, MKeyboardListener)

MKeyboardListener.start()

mgraphical_thread.run()