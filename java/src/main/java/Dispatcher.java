import java.util.Map;
import java.util.function.Supplier;

public class Dispatcher {

    private final Map<String, Supplier<String>> handlers;

    public Dispatcher(Map<String, Supplier<String>> handlers) {
        this.handlers = handlers;
    }

    public String dispatch(Command command) {
        Supplier<String> handler = handlers.get(command.getName());
        if (handler == null) {
            return "UNKNOWN_COMMAND";
        }
        return handler.get();
    }
}
