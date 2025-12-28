
import org.junit.jupiter.api.Test;
import static org.junit.jupiter.api.Assertions.*;

public class InputValidatorSkeletonTest {

    private final InputValidatorSkeleton validator = new InputValidatorSkeleton();

    @Test
    void nullCommand_throws() {
        assertThrows(IllegalArgumentException.class,() -> validator.validateCommand(null));
    }


    @Test
    void emptyString_throws(){
        assertThrows(IllegalArgumentException.class,() -> validator.validateCommand(""));

    }

    @Test
    void whitespaceOnly_throws(){
        assertThrows(IllegalArgumentException.class,() -> validator.validateCommand("    "));
    }

    @Test
    void trimsLeadingAndTrailingWhitespace(){
        String result = validator.validateCommand("   ABC123   ");
        assertEquals("ABC123",result);
    }

    @Test
    void lowercaseLetter_throws(){
        assertThrows(IllegalArgumentException.class,() -> validator.validateCommand("abC123"));
    }

    @Test
    void symbol_throws(){
        assertThrows(IllegalArgumentException.class,() -> validator.validateCommand("ABC@123"));
    }

    @Test
    void lengthOverMax(){
        String tooLong = "A".repeat(58);
        assertThrows(IllegalArgumentException.class,() -> validator.validateCommand(tooLong));
    }

    @Test
    void lengthExactlyMax_isAllowed(){
        String max = "A".repeat(50);
        assertEquals (max, validator.validateCommand(max));
    }

    @Test
    void validUppercaseAndDigits_isAllowed(){
        assertEquals("HELLO123", validator.validateCommand("HELLO123"));
    }

}
