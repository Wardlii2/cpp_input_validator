#imports from other files
from input_validator import Input_Validator
from parser import Command_Parser
from dispatcher import Dispatcher
from handlers import handle_ping
from handlers import handle_status 

# assignment of classes for the glue and their function.
validator = Input_Validator()
parser = Command_Parser(validator)

dispatcher = Dispatcher({
    "PING": handle_ping,
    "STATUS": handle_status
})

def process(raw_input: str):
    command = parser.parse(raw_input)
    return dispatcher.dispatch(command)

#Example of output:
if __name__ == "__main__":
    print(process("CMD:PING"))
    print(process("CMD:STATUS"))

