public class InputValidatorSkeleton {

    public String validateCommand(String command){
        validateNotNull(command);
        String normalized = normalizeCommand(command);
        validateLength(normalized);
        validateCharacters(normalized);


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

    private void validateLength(String command){
        if (command.length() > MAX_COMMAND_LENGTH)
            throw new IllegalArgumentException("the length of the command is too long sorry enter again");

    }

    private void validateCharacters(String command){
        for(int i = 0; i < command.length(); i++){
            char currentChar = command.charAt(i);
            if (!Character.isUpperCase(currentChar) && !Character.isDigit(currentChar)){
                throw new IllegalArgumentException("Character is not within the bounds that are accepted" + currentChar);
            }
        }


    }
}








