import java.util.HashMap;
import java.util.Map;
import java.util.function.Supplier;

public class Main {
    public static String process(String rawInput ) {
        // setting up validator and parser
        InputValidatorSkeleton validator = new InputValidatorSkeleton();
        Command_Parser parser = new Command_Parser(validator);

        // setting up handlers with map for commands due to java syntax
        Map<String, Supplier<String>> handlers = new HashMap<>();
        handlers.put("PING", () -> "PONG");
        handlers.put("STATUS", () -> "STATUS_OK");


        // dispatcher setup for handlers
        Dispatcher dispatcher = new Dispatcher(handlers);

        // example command processing loop
            Command command = parser.parse(rawInput);
            return dispatcher.dispatch(command);
    }
        
        
        public static void main(String[] args) {
            System.out.println(process("CMD:PING"));  // Output: PONG
            System.out.println(process("CMD:STATUS")); // Output: STATUS_OK
           
    

    }
}


