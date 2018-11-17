def message_builder(commands):
    message_list = [commands['mode'], commands['up'], commands['down'], commands['right'],
                    commands['left'], commands['arm_up'], commands['arm_down']]
    message_str = ''.join(str(e) for e in message_list)
    return message_str