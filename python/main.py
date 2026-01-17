from input_validator import InputValidator
from parser import CommandParser
from dispatcher import CommandDispatcher

def process(raw_input: str) -> str:
    validator = InputValidator()
    parser = CommandParser(validator)
    dispatcher = CommandDispatcher()

    command = parser.parse(raw_input)
    return dispatcher.dispatch(command)

if __name__ == "__main__":
    print(process("CMD:PING"))
    print(process("CMD:STATUS"))
