public class InputValidatorSkeleton {

    public String validateCommand(String command){
        validateNotNull(command);
        String normalized = normalizeCommand(command);
        validatePrefixExists(normalized);
        validateLength(normalized);


        //adding new logic to mimic python but in java for implementation of "CMD:ECHO:HI"" command
        String body = normalized.substring(4);
        if (body.trim().isEmpty()) {
            throw new IllegalArgumentException("body cannot be empty");
        }


        //Split it in to name plus payload:
        String name;
        String payload = null;

        // we have to make an index of the item colon as we use it as a delimmitter
        int colonIndex = body.indexOf(':');
        if (colonIndex >= 0) {
            name = body.substring(0, colonIndex);
            payload = body.substring(colonIndex + 1);

        } else {
            name = body;
        }

        //validate name
        validateNameNotEmpty(name);
        validateDigitNotAtStart(name);
        validateCharactersUppercaseDigits(name);


        //New rules for payload
        if ("ECHO".equals(name)) {
            if (payload == null || payload.trim().isEmpty()) {
                throw new IllegalArgumentException("Payload cannot be empty if name is ECHO");
            }
            validateCharactersUppercaseDigits(payload);
        }else {
            //Non echo must not have payload
            if(payload != null) {
                throw new IllegalArgumentException(name + " must not include a payload.");
            }
        }

        return normalized;

    }


    private void validateNotNull(String command){
        if (command == null) {
            throw new IllegalArgumentException("command is empty it cannot be.");

        }

    }

    private static final int MAX_COMMAND_LENGTH = 50;

    private String normalizeCommand(String command){
        String trimmed = command.trim();
        if(trimmed.isEmpty()){
            throw new IllegalArgumentException("this is an empty string please enter a command");
        }



        return trimmed;
    }

    // checking if the payload in payload is empty.
      private void validateNameNotEmpty(String name){
        if (name.trim().isEmpty()){
            throw new IllegalArgumentException("name must not be empty.");
        }


    }


    private void validatePrefixExists(String command){
        if (!command.startsWith("CMD:")){
            throw new IllegalArgumentException("this command is missing the required prefix.");
        }


    }

    /** validating character at start is a digit and if it is throwing exeption */
    private void validateDigitNotAtStart(String command){
        if (command.isEmpty()) return;
        char currentChar = command.charAt(0);
        if (Character.isDigit(currentChar))
            throw new IllegalArgumentException("Cannot have digit at the start");

    }



    private void validateLength(String command){
        if (command.length() > MAX_COMMAND_LENGTH)
            throw new IllegalArgumentException("the length of the command is too long sorry enter again");

    }

    private void validateCharactersUppercaseDigits(String command){
        for(int i = 0; i < command.length(); i++){
            char currentChar = command.charAt(i);
            if (!Character.isUpperCase(currentChar) && !Character.isDigit(currentChar)){
                throw new IllegalArgumentException("Character is not within the bounds that are accepted" + currentChar);
            }
        }


    }
}








