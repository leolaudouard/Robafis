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
            'speedmode': 0,
            'stopMode': 0
            }



# I'ROBOT MAC ADRESS
# 00:1B:10:61:12:44

mgraphical_thread = graphical_thread(commands)
MKeyboardListener = KeyboardListener(commands)
Mbluetooth_thread= bluetooth_thread('00:1B:10:61:12:44', mgraphical_thread, commands)



Mbluetooth_thread.start()
MKeyboardListener.start()
mgraphical_thread.run()
