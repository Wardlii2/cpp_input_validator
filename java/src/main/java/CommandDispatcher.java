import java.util.HashMap;
import java.util.Map;
import java.util.function.Supplier;

public class CommandDispatcher {
    private final Map<String, Supplier<String>> handler;

    public CommandDispatcher() {
        handler = new HashMap<>();
        handler.put("PING", Handlers::ping);
        handler.put("STATUS", Handlers::status);
        handler.put("UPTIME", Handlers::uptime);
    }



    public String dispatch(Command command) {
        Supplier<String> hout = handler.get(command.getName());
        if (hout == null) {
            return "UNKNOWN_COMMAND";
        }
        return hout.get();
    }
}