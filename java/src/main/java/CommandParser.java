// defining CommandParser as a class.
public class CommandParser {
    private InputValidatorSkeleton validator;

    public CommandParser(InputValidatorSkeleton validator) {
        this.validator = validator;
    }


    public Command parse(String rawInput) {
        
        String validatedInput = validator.validateCommand(rawInput);
        String body = validatedInput.substring(4);

        //adding split for command so it becomes 
        if (body.contains(":")) {
            String [] parts = body.split(":",2); //spiliting into name and syntax
            String name = parts[0];
            String payload = parts[1];
            return new Command(name, payload);
        }


        return new Command(body, null);
}

}