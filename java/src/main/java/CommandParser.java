// defining CommandParser as a class.
public class CommandParser {
    private InputValidatorSkeleton validator;

    public CommandParser(InputValidatorSkeleton validator) {
        this.validator = validator;
    }


    public Command parse(String rawInput) {
        
        String validatedInput = validator.validateCommand(rawInput);
        String commandName = validatedInput.substring(4);
        return new Command(commandName);
}

}