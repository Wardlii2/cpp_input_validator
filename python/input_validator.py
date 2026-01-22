#defining the class correctly.
class InputValidator:
    MAX_COMMAND_LENGTH = 50
    #defining the main method.
    def validate_command(self, command: str) -> str:
        self._validate_Not_Null(command)
        normalized = self._normalize_command(command)
        self._validate_CMD_Present(normalized)
        self._validate_length(normalized)

        #new addititon for adding support for CMD:ECHO:HI
        body = normalized[4:]
        if body.strip() == "":
            raise ValueError("body cannot be empty")
        
        #we must check if body contains a : in order to verify if we split
        if ":" in body:
            name, payload = body.split(":",1)
        else:
            name, payload = body, None

        #validate that name is not empty seperately
        self._validate_name_not_empty(name)
        self._validate_name_characters(name)

        #validate payload for the same as name
        if payload is not None:
            self._validate_payload_not_empty(payload)
            self._validate_payload_characters(payload)

        #if command name is Echo allow payload but must not be empy
        if name == "ECHO":
            if payload is None:
                raise ValueError("Payload is not allowed to be empty for Echo")
            #dont allow payload as there is not ment to be any.
        else:
            if payload is not None:
                raise ValueError(f"{name},must not incluede payload.")
        
        return normalized

    #old functions that have been kept after refactor.
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
    

    def _validate_length(self, command: str) -> None:
        if len(command) > self.MAX_COMMAND_LENGTH:
            raise ValueError("length of command is too long")
            
        
    #validation specifically for name:

    def _validate_name_not_empty(self, name: str) -> None:
        if (name.strip() == ""):
            raise ValueError("sorry but the payload is empty is empty")
        
        
    def _validate_name_characters(self, name: str) -> None:
        for ch in name:
            if not (ch.isupper()):
                raise ValueError(f"Invalid character: '{ch}'")
            
    #validation specifically for payload:

    def _validate_payload_not_empty(self, payload: str) -> None:
        if (payload.strip() == ""):
            raise ValueError("sorry but the payload is empty is empty")
        
        
    def _validate_payload_characters(self, payload: str) -> None:
        for ch in payload:
            if not (ch.isupper() or ch.isdigit()):
                raise ValueError(f"Invalid character: '{ch}'")