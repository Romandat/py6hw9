from parser import parser
from handler import handler
while True:
    command = input('Enter command: ')
    if command == '.':
        break
    parsed_command = parser(command)
    handler_result = handler(parsed_command)
    print(handler_result)
    if handler_result == 'Good bye!':
        break
    