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
        payload = normalized[4:]

        return Command(payload)





