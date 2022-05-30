from parser import sanitize_phone_number


contact_dict = {
    'username': '+380669999999'
}

def add_func(user_param, phone_param: str, additional_action=None):
    if not additional_action:
        contact_dict[user_param] = phone_param
        return 'Done'
    
    
def change_func(user_param, phone_param, additional_action=None):
    if contact_dict.get(user_param, 0):
        contact_dict[user_param] = phone_param
        return 'Done'
    return 'Change action Failed. User not found'

def show_func(user_param, phone_param, additional_action=None):
    if additional_action == 'all':
        return contact_dict
    if user_param:
        try:
            return f'{user_param} phone: {contact_dict[user_param]}'
        except KeyError:
            return 'Phone action Failed. User not found'

def error_func(error, *_):
    return error

OPERATIONS = {
    'add': add_func,
    'change': change_func,
    'show': show_func,
    'phone': show_func,
    'error_func': error_func
}

def get_handler(operator):
    return OPERATIONS[operator]

def handler(args: list):
    
    list_args = list(args)
    handler_result = None
    if list_args[0] == 'hello':
        handler_result = 'How can I help you?'
    elif list_args[0] =='quit':
        handler_result = 'Good bye!'
    else:
        handler_result = get_handler(list_args[0])(list_args[1], list_args[2], list_args[3])
    return handler_result
