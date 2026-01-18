#defining the class correctly.
class InputValidator:
    MAX_COMMAND_LENGTH = 50
    #defining the main method.
    def validate_command(self, command: str) -> str:
        self._validate_Not_Null(command)
        normalized = self._normalize_command(command)
        self._validate_CMD_Present(normalized)
        payload = (normalized[4:]) 
        self._validate_payload_not_empty(payload)
        self._validate_digit_not_at_start(payload)
        self._validate_length(normalized)
        self._validate_Command_Characters(payload)

        return normalized



    def _validate_Not_Null(self, command:str) -> None:
        if command is None:
            raise ValueError("The command is null or an error of input has occured")
        

    def _normalize_command(self, command:str) -> str:
        trimmed = command.strip()
        if trimmed == "":
            raise ValueError("sorry but the string is empty")
        return trimmed
    
    #adding validation for presence of CMD:
    def _validate_CMD_Present(self, command:str) -> None:
        if (command.startswith("CMD:")):
            pass
        else: raise ValueError("command is missing its prefix CMD:")


    #checking payload is not empty or white space.
    def _validate_payload_not_empty(self, payload: str) -> None:
        if (payload.strip() == ""):
            raise ValueError("sorry but the payload is empty is empty")


    #added in a validation to check if command starts with a digit at position one.
    def _validate_digit_not_at_start(self, command: str) -> None:
            if (command[0].isdigit()):
                raise ValueError("command may not start with a number")
            

    def _validate_length(self, command: str) -> None:
        if len(command) > self.MAX_COMMAND_LENGTH:
            raise ValueError("length of command is too long")


    def _validate_Command_Characters(self, command: str) -> None:
        for ch in command:
            if not (ch.isupper() or ch.isdigit()):
                raise ValueError(f"Invalid character: '{ch}'")
            
        
