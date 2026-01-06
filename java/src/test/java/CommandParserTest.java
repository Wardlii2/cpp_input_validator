import org.junit.jupiter.api.Test;
import java.util.HashMap;
import java.util.Map;
import java.util.function.Supplier;
import static org.junit.jupiter.api.Assertions.assertEquals;
import static org.junit.jupiter.api.Assertions.assertThrows;
//CommandParserTests go here
public class CommandParserTest {
    @Test
    //testing command parser to see if it correctly parses PING command.
    public void test_PARSE_PINGCommand() {
        InputValidatorSkeleton validator = new InputValidatorSkeleton();
        Command_Parser parser = new Command_Parser(validator);
        Command command = parser.parse("CMD:PING");
        assertEquals("PING", command.getName());
    }

    @Test
    //testing command parser to see if it correctly parses STATUS command.
    public void test_PARSE_STATUSCommand_with_Whitespace() {
        InputValidatorSkeleton validator = new InputValidatorSkeleton();
        Command_Parser parser = new Command_Parser(validator);
        Command command = parser.parse("  CMD:STATUS  ");
        assertEquals("STATUS", command.getName());
    }

    @Test
    //testing command parser to see if it correctly handles unknown commands.
    public void test_PARSE_UNKNOWNCommand() {
        InputValidatorSkeleton validator = new InputValidatorSkeleton();
        Command_Parser parser = new Command_Parser(validator);
        Command command = parser.parse("CMD:UNKNOWN");
        assertEquals("UNKNOWN", command.getName());
    }

    @Test
    //testing command parser to see if it throws exception on invalid command.
    public void test_PARSE_InvalidCommand_ThrowsException() {
        InputValidatorSkeleton validator = new InputValidatorSkeleton();
        Command_Parser parser = new Command_Parser(validator);

        assertThrows(IllegalArgumentException.class, () -> {
            parser.parse("INVALID_COMMAND");
        });

    }

}
