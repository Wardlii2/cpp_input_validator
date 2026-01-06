import java.util.HashMap;
import java.util.Map;
import java.util.function.Supplier;

public class Main {
    public static void main(String[] args){
        // setting up validator and parser
        InputValidatorSkeleton validator = new InputValidatorSkeleton();
        Command_Parser parser = new Command_Parser(validator);

        // setting up handlers with map for commands due to java syntax
        Map<String, Supplier<String>> handlers = new HashMap<>();
        handlers.put("PING", () -> "PONG");
        handlers.put("STATUS", () -> "STATUS_OK");


        // dispatcher setup for handlers
        Dispatcher dispatcher = new Dispatcher(handlers);



        // end to end example command processing
        String rawInput = "  CMD:PING  ";
        Command command = parser.parse(rawInput);
        String response = dispatcher.dispatch(command);

        System.out.println(response);
           
    

    }
}


