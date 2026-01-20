#include <iostream>
#include <stdexcept>
#include <cassert>

#include "Parser.h"
#include "input_validator.h"
#include "Command.h"

// End-to-end test for the application process function

    static void expectInvalid(const Parser& parser, const std::string& input) {
        try {
            (void) parser.parse(input);
            // If no exception is thrown, the test fails
            assert(false && "Expected exception for invalid input");
        } catch (const std::invalid_argument&) {
            // Expected exception caught, test passes
        }
}

int main() {
    InputValidator validator;
    Parser parser(validator);

        // Test valid commands
        Command cmd1 = parser.parse("CMD:PING");
        assert(cmd1.getName() == "PING");

        // Test with leading/trailing whitespace
        Command cmd2 = parser.parse("   CMD:STATUS   ");
        assert(cmd2.getName() == "STATUS");

        // Unknown command test is still valid for parsing
        Command cmd3 = parser.parse("CMD:HELLO");
        assert(cmd3.getName() == "HELLO");


        // Test invalid command format
        expectInvalid(parser, "CMD_BADINPUT");
        expectInvalid(parser, "INVALID_CMD:PING");
        expectInvalid(parser, "CMD:");
        expectInvalid(parser, "CMD:   ");
        expectInvalid(parser, "CMD:PING_EXTRA");
        expectInvalid(parser, "1CMD:PING_EXTRA");

        // If all assertions pass
        std::cout << "All Parser tests passed!" << std::endl;
        return 0;

}
