from input_validator import InputValidator
from parser import CommandParser
from dispatcher import CommandDispatcher

#process
def process(rawInput:str) -> str:
    #instenciate all wiring for the pipeline
    validator = InputValidator()
    parser = CommandParser(validator)
    dispatcher = CommandDispatcher()

    #the actual pipeline
    command = parser.parse(rawInput)
    return dispatcher.dispatch(command)


#Providing example output
if __name__ == "__main__":
#testing inputs 
    print(process("CMD:PING"))
    print(process("CMD:STATUS"))







