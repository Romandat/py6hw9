def input_error(func):
    def inner(command: str):
        allowed_commands = "good bye", "close", "exit"
        command_list = command.strip().lower().split(' ')
        # try:
            # sanitize_phone_number()
            # command_list = command.lower().split(' ')
                # handler (KeyError, ValueError, IndexError) 
            # "Enter user name", "Give me name and phone please"

        result = func(command_list)
        return result
    return inner


@input_error
def parser(command: list) -> list:
    # command_list = []
    # command_list = command.lower().split(' ')
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
            print(result)    
        elif len(result) == 10:
            result = '+38' + result
            print(result)
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
    return new_phone