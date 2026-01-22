import java.util.HashMap;
import java.util.Map;
import java.util.function.Function;

public class CommandDispatcher {
    private final Map<String, Function<Command, String>> handler;

    public CommandDispatcher() {
        handler = new HashMap<>();
        handler.put("PING", Handlers::ping);
        handler.put("STATUS", Handlers::status);
        handler.put("UPTIME", Handlers::uptime);
        handler.put("ECHO", Handlers::echo);
    }



    public String dispatch(Command command) {
        Function<Command, String> hout = handler.get(command.getName());
        if (hout == null) {
            return "UNKNOWN_COMMAND";
        }
        return hout.apply(command);
    }
}