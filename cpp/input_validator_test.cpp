#include <iostream>
#include <stdexcept>
#include <string>
#include <cassert>
#include "input_validator.h"


static void expectInvalidArguments(InputValidator& v, const std::string& input) {
    try {
        (void)v.validateCommand(input);
        assert(false&& "expected std::invalid_argument but no exception was thrown");

    } catch (const std::invalid_argument&){
        // expected
    }


}


static void expectValid(InputValidator& v, const std::string& input, const std::string& expected) {
    try {
        std::string out = v.validateCommand(input);
        assert(out == expected && "Output did not match expected normalized result");

    } catch (...){
        assert(false && "Did not expect an exception for valid input");
    }


}

int main() {
    InputValidator v;


    // 1) empty string
    expectInvalidArguments(v, "");

    // 2) whitespace-only
    expectInvalidArguments(v, "   ");
    expectInvalidArguments(v, "\t\t");
    expectInvalidArguments(v, "\n");

    // 3) trimming works
    expectValid(v, "  ABC123  ", "ABC123");

    // 4) lowercase rejected
    expectInvalidArguments(v, "abc");
    expectInvalidArguments(v, "ABCd");

    // 5) symbols rejected
    expectInvalidArguments(v, "ABC-123");
    expectInvalidArguments(v, "ABC_123");
    expectInvalidArguments(v, "ABC 123"); // internal space should fail


// 6) length > 50 rejected
    expectInvalidArguments(v, std::string(51, 'A'));

    // 7) length == 50 allowed
    expectValid(v, std::string(50, 'A'), std::string(50, 'A'));

    // 8) valid input allowed
    expectValid(v, "A1B2C3", "A1B2C3");


    std::cout << "All tests passed. \n";
    return 0;

}
