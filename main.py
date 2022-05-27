from parser import parser
from handler import handler
while True:
    command = input('Enter command: ')
    if command == '.':
        break
    parsed_command = parser(command)
    print(parsed_command)
    handler_result = handler(parsed_command)
    if handler_result == 'quit':
        break