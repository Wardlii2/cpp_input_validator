from command import Command
#defining parser as a class.
class CommandParser:
    def __init__(self, validator):
        self.validator = validator
    #defining the parse as it self and the raw input as a string that is a command.
    def parse(self, rawInput:str) -> Command:

        #calling normalization from validator file for the raw input.
        normalized = self.validator.validate_command(rawInput)

        #payload removal of prefix using slicing to extract only the payload string.
        body = normalized[4:]

        #checking wether body after CMD: is removed still contains a : if so split it into name and payload.
        if ":" in body:
            name, payload = body.split(":",1)
            return Command(name, payload)


        return Command(body, None)





