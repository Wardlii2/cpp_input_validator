import org.junit.jupiter.api.Test;
import static org.junit.jupiter.api.Assertions.assertEquals;


public class TestingDispatcher {
    
    @Test
    void test_Ping_dispatched_ok() {

        CommandDispatcher dispatcher = new CommandDispatcher();

        Command command = new Command("PING", null);

        assertEquals("PONG", dispatcher.dispatch(command));


    }

    @Test
    void test_Status_dispatched_ok() {

        CommandDispatcher dispatcher = new CommandDispatcher();

        Command command = new Command("STATUS", null);

        assertEquals("STATUS:OK", dispatcher.dispatch(command));

    }


    @Test
    void test_Uptime_dispatched_ok() {

        CommandDispatcher dispatcher = new CommandDispatcher();

        Command command = new Command("UPTIME", null);

        assertEquals("UPTIME:0", dispatcher.dispatch(command));

    }
    

        @Test
    void test_Echo_dispatched_ok() {

        CommandDispatcher dispatcher = new CommandDispatcher();

        Command command = new Command("ECHO", "HELLO");

        assertEquals("HELLO", dispatcher.dispatch(command));

    }

     @Test
    void test_Unknown_dispatch_Leads_to_Unexpected_command() {

        CommandDispatcher dispatcher = new CommandDispatcher();

        Command command = new Command("NOPE", "NO");

        assertEquals("UNKNOWN_COMMAND", dispatcher.dispatch(command));


    }
}