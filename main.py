from Bluetooth_Com import bluetooth_thread
from pynput.keyboard import Key, Listener



commands = {'mode': 0,
            'up':   0,
            'down': 0,
            'right': 0,
            'left':  0,
            'arm_up': 0,
            'arm_down': 0
            }

message = '0000000'
Bluetooth_Thread = bluetooth_thread('00:1B:10:61:12:44', message)
Bluetooth_Thread.start()

def on_key_release(key):
    if key == Key.up:
        commands['up'] = 0
    elif key == Key.down:
        commands['down']= 0
    elif key == Key.left:
        commands['left'] = 0
    elif key == Key.right:
        commands['right']= 0
    # TODO : change arm up and arm down
    elif '{0}'.format(key) == "'z'":
         commands['arm_up'] = 0
    elif '{0}'.format(key) == "'q'":
        commands['arm_down'] = 0

    Bluetooth_Thread.set_message(message_builder())

def on_key_press(key):

    if key == Key.up:
        commands['up'] = 1
    elif key == Key.down:
        commands['down']= 1
    elif key == Key.left:
        commands['left'] = 1
    elif key == Key.right:
        commands['right']= 1
    # TODO : change arm up and arm down
    elif '{0}'.format(key) == "'z'":
         commands['arm_up'] = 1
    elif '{0}'.format(key) == "'q'":
        commands['arm_down'] = 1


    # elif key == Key.a:
    #     print('a ok ok ')
    Bluetooth_Thread.set_message(message_builder())

def message_builder():
    message_list = [commands['mode'], commands['up'], commands['down'], commands['right'], commands['left'], commands['arm_up'], commands['arm_down']]
    message_str = ''.join(str(e) for e in message_list)
    return message_str


with Listener(on_press = on_key_press, on_release = on_key_release) as listener:
    listener.join()