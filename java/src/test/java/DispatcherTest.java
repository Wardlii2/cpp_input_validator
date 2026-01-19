import org.junit.jupiter.api.Test;
import static org.junit.jupiter.api.Assertions.assertEquals;


public class TestingDispatcher {
    
    @Test
    void test_Ping_dispatched_ok() {

        CommandDispatcher dispatcher = new CommandDispatcher();

        Command command = new Command("PING");

        assertEquals("PONG", dispatcher.dispatch(command));


    }

    @Test
    void test_Status_dispatched_ok() {

        CommandDispatcher dispatcher = new CommandDispatcher();

        Command command = new Command("STATUS");

        assertEquals("STATUS:OK", dispatcher.dispatch(command));

    }
    

     @Test
    void test_Unknown_dispatch_Leads_to_Unexpected_command() {

        CommandDispatcher dispatcher = new CommandDispatcher();

        Command command = new Command("NOPE");

        assertEquals("UNKNOWN_COMMAND", dispatcher.dispatch(command));


    }
}