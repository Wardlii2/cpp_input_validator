//End to End test for command processing
import org.junit.jupiter.api.Test;
import static org.junit.jupiter.api.Assertions.assertEquals;

public class End_to_End_test {
//testing the end to end functionality of the system
    //testing the PING command
    @Test
    public void End_to_End_test_PING() {
        assertEquals("PONG", Main.process("CMD:PING"));

    }
    //testing the STATUS command
     @Test
    public void End_to_End_test_STATUS() {
        assertEquals("STATUS_OK", Main.process("CMD:STATUS"));

    }

    //testing the UNKNOWN command
     @Test
    public void End_to_End_test_UNKNOWN() {
        assertEquals("UNKNOWN_COMMAND", Main.process("CMD:HELLO"));
    //wont return a response instead it will return UNKNOWN_COMMAND
    }

}