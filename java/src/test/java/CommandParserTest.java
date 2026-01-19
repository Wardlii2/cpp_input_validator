import org.junit.jupiter.api.Test;
import static org.junit.jupiter.api.Assertions.assertEquals;

public class TestingParser {
    
    @Test
    void test_Ping_parsed_ok() {

        InputValidatorSkeleton validator = new InputValidatorSkeleton();

        CommandParser parser = new CommandParser(validator);

        Command command = parser.parse("CMD:PING");

        assertEquals("PING", command.getName());

    }

    @Test
    void test_Unknown_parsed_throws() {

        InputValidatorSkeleton validator = new InputValidatorSkeleton();

        CommandParser parser = new CommandParser(validator);

        assertThrows(IllegalArgumentException.class,
        () -> parser.parse("cmd:Nope"));

    }
}