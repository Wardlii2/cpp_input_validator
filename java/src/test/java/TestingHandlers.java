import org.junit.jupiter.api.Test;
import static org.junit.jupiter.api.Assertions.assertEquals;

public class TestingHandlers {
    
    @Test
    void test_Ping_returns_Pong() {
        assertEquals("PONG", Handlers.ping());
       
        }

    @Test
    void test_Status_returns_Status_ok() {
        assertEquals("STATUS:OK", Handlers.status());
    }
}
