
import org.junit.jupiter.api.Test;
import static org.junit.jupiter.api.Assertions.*;

public class InputValidatorSkeletonTest {

    private final InputValidatorSkeleton validator = new InputValidatorSkeleton();

    // invalid command tests to throw
    @Test
    void nullCommand_throws() {
        assertThrows(IllegalArgumentException.class,() -> validator.validateCommand(null));
    }


    @Test
    void empty_Payload_throws(){
        assertThrows(IllegalArgumentException.class,() -> validator.validateCommand("CMD:"));

    }

    @Test
    void whitespace_payload_throws(){
        assertThrows(IllegalArgumentException.class,() -> validator.validateCommand("  CMD:  "));
    }


    @Test
    void prefix_empty_throws(){
         assertThrows(IllegalArgumentException.class,() -> validator.validateCommand("ABC123"));
    }

    @Test
    void lowercaseLetter_throws(){
        assertThrows(IllegalArgumentException.class,() -> validator.validateCommand("CMD:abC123"));
    }

    @Test
    void digitAtstart_throws(){
        assertThrows(IllegalArgumentException.class,() -> validator.validateCommand("CMD:1TEST"));
    }

     @Test
    void digitAtstart_throws_also(){
        assertThrows(IllegalArgumentException.class,() -> validator.validateCommand("  CMD:123TEST  "));
    }

     @Test
    void digitAtstart_throws_also_too(){
        assertThrows(IllegalArgumentException.class,() -> validator.validateCommand("CMD:3"));
    }


    @Test
    void symbol_throws(){
        assertThrows(IllegalArgumentException.class,() -> validator.validateCommand("CMD:ABC@123"));
    }

    @Test
    void lengthOverMax(){
        String tooLong = "CMD:" + "A".repeat(54);
        assertThrows(IllegalArgumentException.class,() -> validator.validateCommand(tooLong));
    }

    //valid command tests

    @Test
    void trimsLeadingAndTrailingWhitespace(){
        String result = validator.validateCommand("   CMD:ABC123   ");
        assertEquals("CMD:ABC123",result);
    }

    @Test
    void lengthExactlyMax_isAllowed(){
        String max = "CMD:" + "A".repeat(46);
        assertEquals (max, validator.validateCommand(max));
    }

    @Test
    void validUppercaseAndDigits_isAllowed(){
        assertEquals("CMD:HELLO123", validator.validateCommand("CMD:HELLO123"));
    }

    @Test
    void validNonDigitFirst_isAllowed(){
        assertEquals("CMD:TEST1", validator.validateCommand("CMD:TEST1"));
    }

      @Test
    void echo_Command_is_Allowed(){
        assertEquals("CMD:ECHO:HELLO", validator.validateCommand("CMD:ECHO:HELLO"));
    }

        @Test
    void echo_Command_payload_Allowed_digits(){
        assertEquals("CMD:ECHO:123HELLO", validator.validateCommand("CMD:ECHO:123HELLO"));
    }


    //echo tests invalid

    @Test
    void echo_Command_throws_If_empty(){
        assertThrows(IllegalArgumentException.class,() -> validator.validateCommand("CMD:ECHO:"));
    } 

     @Test
    void echo_Command_throws_If_empty_And_missing_Colon(){
        assertThrows(IllegalArgumentException.class,() -> validator.validateCommand("CMD:ECHO"));
    }

     @Test
    void echo_Command_throws_If_lower_Case(){
        assertThrows(IllegalArgumentException.class,() -> validator.validateCommand("CMD:ECHO:hi"));
    }

     @Test
    void Command_throws_If_has_Payload_if_Not_echo(){
        assertThrows(IllegalArgumentException.class,() -> validator.validateCommand("CMD:PING:HI"));
    }




}
