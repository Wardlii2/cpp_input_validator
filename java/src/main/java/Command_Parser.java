// defining Command_Parser as a class.
public class Command_Parser {
    private InputValidatorSkeleton validator;

    public Command_Parser(InputValidatorSkeleton validator) {
        this.validator = validator;
    }


    public Command parse(String rawInput) {
        
        String validatedInput = validator.validateCommand(rawInput);
        String commandName = validatedInput.substring(4);
        return new Command(commandName);
}

}