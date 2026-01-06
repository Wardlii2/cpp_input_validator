//main file for demo of the validation pipeline 
#include <iostream>
#include "app.h"

int main() {
    try{

    // Test cases for the application process function
    std::cout << process("CMD:PING") << std::endl;      // Expected output: PONG
    std::cout << process("CMD:STATUS") << std::endl;    // Expected output: STATUS_OK
    std::cout << process("CMD:HELLO") << std::endl;   // Expected output: UNKNOWN_COMMAND

    // Testing invalid input that should raise an exception
    std::cout << process("CMD_BADINPUT") << std::endl; // Expected output: Error: Invalid command format
    } catch (const std::invalid_argument& e) {
        std::cout << "INVALID ARGUMENT: " << e.what() << std::endl;


    }

    return 0;
    

}