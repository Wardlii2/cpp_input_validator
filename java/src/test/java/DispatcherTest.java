import org.junit.jupiter.api.Test;
import java.util.HashMap;
import java.util.Map;
import java.util.function.Supplier;
import static org.junit.jupiter.api.Assertions.assertEquals;
//dispatcher tests go here
public class DispatcherTest {
//testing dispatcher to see if it routes correct ping command.
    @Test
    public void test_PINGCommand() {
        // Setting up a simple command handler map
        Map<String, Supplier<String>> commandHandlers = new HashMap<>();
        // Adding a handler for the PING command
        commandHandlers.put("PING", () -> "PONG");
        // Creating the dispatcher with the command handlers
        Dispatcher dispatcher = new Dispatcher(commandHandlers);
        // Creating a PING command
        Command command = new Command("PING");
        // Dispatching the command and capturing the response
        String response = dispatcher.dispatch(command);
        // Asserting that the response is as expected
        assertEquals("PONG", response);
    }

    @Test
    //testing dispatcher to see if it routes correct status command.
    public void test_STATUSCommand() {
        // Setting up a simple command handler map
        Map<String, Supplier<String>> commandHandlers = new HashMap<>();
        // Adding a handler for the STATUS command
        commandHandlers.put("STATUS", () -> "STATUS_OK");
        // Creating the dispatcher with the command handlers
        Dispatcher dispatcher = new Dispatcher(commandHandlers);
        // Creating a STATUS command
        Command command = new Command("STATUS");
        // Dispatching the command and capturing the response
        String response = dispatcher.dispatch(command);
        // Asserting that the response is as expected
        assertEquals("STATUS_OK", response);
    }

    @Test
    public void test_UNKNOWNCommand() {
        // Setting up a simple command handler map without any handlers
        Map<String, Supplier<String>> commandHandlers = new HashMap<>();
        // Creating the dispatcher with the empty command handlers
        Dispatcher dispatcher = new Dispatcher(commandHandlers);
        // Creating an UNKNOWN command
        Command command = new Command("UNKNOWN");
        // Dispatching the command and capturing the response
        String response = dispatcher.dispatch(command);
        // Asserting that the response indicates an unknown command
        assertEquals("UNKNOWN_COMMAND", response);
    }
    
}