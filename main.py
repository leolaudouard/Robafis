from Bluetooth_Com import bluetooth_thread
from KeyboardListener import KeyboardListener
from IHMViewer import graphical_thread

commands = {'mode': 0,
            'forward':   0,
            'backward': 0,
            'right': 0,
            'left':  0,
            'up': 0,
            'down': 0
            }


message = '0000000'
Mbluetooth_thread= bluetooth_thread('00:1B:10:61:12:44', message)
mgraphical_thread = graphical_thread(Mbluetooth_thread, commands)
Mbluetooth_thread.set_graph_param(mgraphical_thread)

mgraphical_thread.start()
Mbluetooth_thread.start()




MKeyboardListener = KeyboardListener(Mbluetooth_thread, commands, mgraphical_thread)
MKeyboardListener.run()