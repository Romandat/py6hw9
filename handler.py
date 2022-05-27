contact_dict = {
    'username': '+380669999999'
}

OPERATIONS = {
    'add': add_func,
    'change': change_func,
    'show': show_func
}

def get_handler(operator):
    return OPERATIONS[operator]

def handler(args: list):
    show_actions = "phone", "show all"
    close_actions = "good bye", "close", "exit"
    list_args = list(args)

    if list_args[0] == 'hello':
        print("How can I help you?")
    if list_args[0] == 'add':
        get_handler(list_args[0])(list_args[1], list_args[2])
    if list_args[0] == 'change':
        get_handler(list_args[0])(list_args[1], list_args[2])
    if list_args[0] == 'phone':
        get_handler(list_args[0])(list_args[1], list_args[2])
    if list_args[0] in show_actions:
        if list_args[1] == 'all':
            print('show all actions')
    if list_args[0] in close_actions:
        print('"good bye", "close", "exit" actions')
    return

def command_processing(action, additional_action, user_param, phone_param):
    return

def add_func(user_param, phone_param):
    ...

def change_func(user_param, phone_param):
    ...

def show_func(user_param, phone_param, additional_action=None):
    ...