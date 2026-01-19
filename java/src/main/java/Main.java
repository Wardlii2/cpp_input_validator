public class Main {
    
    public static String process(String rawInput) {
        InputValidatorSkeleton validator = new InputValidatorSkeleton();
        CommandParser parser = new CommandParser(validator);
        CommandDispatcher dispatcher = new CommandDispatcher();


        Command command = parser.parse(rawInput);
        return dispatcher.dispatch(command);

    }
    
    
    
    public static void main(String[] args) {
        System.out.println(process("CMD:PING"));
        System.out.println(process("CMD:STATUS"));
        System.out.println(process("CMD:NOPE"));

    }

}


