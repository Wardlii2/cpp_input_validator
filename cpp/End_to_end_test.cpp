# include <iostream>
#include <stdexcept>
#include <cassert>
#include "app.h"
// End-to-end test for the application process function
int main() {
        // Test valid commands
        assert(process("CMD:PING") == "PONG");
        assert(process("CMD:STATUS") == "STATUS:OK");
        assert(process("CMD:UPTIME") == "UPTIME:0");
        assert(process("CMD:HELP") == "PING,STATUS,UPTIME,ECHO,HELP");
        assert(process("CMD:ECHO:HI") == "HI");
        assert(process("CMD:HELLO") == "UNKNOWN_COMMAND");



        // Test invalid command format
        try {
            (void) process("CMD_BADINPUT");
            // If no exception is thrown, the test fails
            assert(false&& "Expected exception for invalid input");
        } catch (const std::invalid_argument&) {
            // Expected exception caught, test passes

        }

        // If all assertions pass
        std::cout << "All end-to-end tests passed!" << std::endl;
        return 0;
}