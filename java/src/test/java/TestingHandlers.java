import org.junit.jupiter.api.Test;
import static org.junit.jupiter.api.Assertions.assertEquals;

public class TestingHandlers {
    
    @Test
    void test_Ping_returns_Pong() {
        Command cmd1 = new Command("PING", null);
        assertEquals("PONG", Handlers.ping(cmd1));
       
        }

    @Test
    void test_Status_returns_Status_ok() {
        Command cmd2 = new Command("STATUS", null);
        assertEquals("STATUS:OK", Handlers.status(cmd2));
    }

    @Test
    void test_Uptime_returns_uptime() {
        Command cmd3 = new Command("UPTIME", null);
        assertEquals("UPTIME:0", Handlers.uptime(cmd3));
    }

    @Test
    void test_Echo_returns_echo() {
        Command cmd4 = new Command("ECHO", "HELLO");
        assertEquals("HELLO", Handlers.echo(cmd4));
    }
}
