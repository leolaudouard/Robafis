def message_builder(commands):
    message_list = [commands['mode'], commands['forward'], commands['backward'], commands['right'],
                    commands['left'], commands['up'], commands['down']]
    message_str = ''.join(str(e) for e in message_list)
    return message_str