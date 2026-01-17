from input_validator import InputValidator
from parser import CommandParser
from dispatcher import CommandDispatcher

#process
def process(rawInput:str, parser: CommandParser, dispatcher: CommandDispatcher) -> str:
    command = parser.parse(rawInput)
    return dispatcher.dispatch(command)


#Providing example output
if __name__ == "__main__":
    validator = InputValidator()
    parser = CommandParser(validator)
    dispatcher = CommandDispatcher()

#testing inputs 
    print(process("CMD:PING", parser, dispatcher))
    print(process("CMD:STATUS", parser, dispatcher))







