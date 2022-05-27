def input_error(func):
    def inner(command: str):
        
        result = func(command)
        return result
    return inner


@input_error
def parser(command: str) -> list:
    command_list = []
    command_list = command.split(' ')
    # handler (KeyError, ValueError, IndexError) 
    # "Enter user name", "Give me name and phone please"
    return command_list