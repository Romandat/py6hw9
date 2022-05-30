def input_error(func):
    def inner(command: str):
        greetings_actions = 'hello',
        close_actions = "good bye", "close", "exit"
        allowed_commands = "add", "phone", "change"
        command_list = command.strip().lower().split(' ')
        if command_list[0] == 'good' and command_list[1] == 'bye':
            command_list[0] = f'{command_list[0]} {command_list[1]}'
        elif command_list[0] == 'show' and command_list[1] == 'all':
            pass
        elif command_list[0] in greetings_actions:
            command_list = 'hello', None, None, None
        elif command_list[0] in close_actions:
            command_list = 'quit', None, None, None
        elif command_list[0] in allowed_commands:
            if len(command_list) < 2:
                command_list = 'error_func', f'Add arguments for command {command_list[0]}', None, None
            elif len(command_list) < 3 and not (command_list[0] == 'phone'):
                command_list = 'error_func', f'Give me name and phone please for command: {command_list[0]} ', None, None
        else:
            command_list = 'error_func', 'Command error', None, None
        # try:
            # sanitize_phone_number()
            # command_list = command.lower().split(' ')
                # handler (KeyError, ValueError, IndexError) 
            # "Enter user name", "Give me name and phone please"
        if command_list[0] == 'add' or command_list[0] == 'change':
            try:
                command_list[2] = sanitize_phone_number(command_list[2])
            except Exception:
                command_list = 'error_func', 'Incorect phone', None, None


        result = func(command_list)
        return result
    return inner


@input_error
def parser(command: list) -> list:
    if 'show' in command:
        if 'all' in command:
            command.remove('all')
            command.append(None)
            command.append(None)
            command.append('all')
    elif 'add' in command:
        command.append(None)
    elif 'phone' in command:
        command.append(None)
        command.append(None)
    elif 'change' in command:
        command.append(None)
    return command

def format_phone_number(func):
    def inner(phone):
        result = func(phone)
        if len(result) == 12:
            result = '+' + result    
        elif len(result) == 10:
            result = '+38' + result
        else:
            return None
        return result
    return inner

@format_phone_number
def sanitize_phone_number(phone: str):
    new_phone = (
        phone.strip()
            .removeprefix("+")
            .replace("(", "")
            .replace(")", "")
            .replace("-", "")
            .replace(" ", "")
    )
    
    if new_phone.isdigit():
        return new_phone