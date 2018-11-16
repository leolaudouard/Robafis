from builtins import str
from pynput.keyboard import Key, Listener



class KeyboardListener:

    def __init__(self, bluetooth_thread, commands, graphical_thread):
        self.commands = commands
        self.bluetooth_thread = bluetooth_thread
        self.graphical_thread = graphical_thread


    def message_builder(self):
        message_list = [self.commands['mode'], self.commands['up'], self.commands['down'], self.commands['right'], self.commands['left'], self.commands['arm_up'], self.commands['arm_down']]
        message_str = ''.join(str(e) for e in message_list)
        return message_str

    def on_key_release(self, key):
        if key == Key.up:
            self.commands['up'] = 0
            self.graphical_thread.released('up')
        elif key == Key.down:
            self.commands['down']= 0
            self.graphical_thread.released('down')
        elif key == Key.left:
            self.commands['left'] = 0
            self.graphical_thread.released('left')
        elif key == Key.right:
            self.commands['right']= 0
            self.graphical_thread.released('right')
        # TODO : change arm up and arm down
        elif '{0}'.format(key) == "'z'":
            self.commands['arm_up'] = 0
            self.graphical_thread.released('arm_up')
        elif '{0}'.format(key) == "'q'":
            self.commands['arm_down'] = 0
            self.graphical_thread.released('arm_down')

        self.bluetooth_thread.message = self.message_builder()

    def on_key_press(self, key):

        if key == Key.up:
            self.commands['up'] = 1
            self.graphical_thread.pressed('up')
        elif key == Key.down:
            self.commands['down']= 1
            self.graphical_thread.pressed('down')
        elif key == Key.left:
            self.commands['left'] = 1
            self.graphical_thread.pressed('left')
        elif key == Key.right:
            self.commands['right']= 1
            self.graphical_thread.pressed('right')
        # TODO : change arm up and arm down
        elif '{0}'.format(key) == "'z'":
            self.commands['arm_up'] = 1
            self.graphical_thread.pressed('arm_up')
        elif '{0}'.format(key) == "'q'":
            self.commands['arm_down'] = 1
            self.graphical_thread.pressed('arm_down')

        self.bluetooth_thread.message = self.message_builder()


    def run(self):
        with Listener(on_press= self.on_key_press, on_release= self.on_key_release) as listener:
            listener.join()