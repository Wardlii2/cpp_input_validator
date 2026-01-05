
#defining command as a class.
class Command:
    def __init__(self, name: str):
        self.name = name
#defining parser as a class.
class Command_Parser:
    def __init__(self, validator):
        self.validator = validator
    #defining the parse as it self and the raw input as a string that is a command.
    def parse(self, raw_input:str) -> Command:

        #calling normalization from validator file for the raw input.
        normalized = self.validator.validate_command(raw_input)

        #payload removal of prefix using slicing to extract only the payload string.
        payload = normalized[4:]

        return Command(name = payload)





