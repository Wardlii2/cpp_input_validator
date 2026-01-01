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
    expectInvalidArguments(v, "  ABC123  ");
    expectInvalidArguments(v, "ABC123");


    // 3) trimming works
    expectValid(v, "  CMD:ABC123  ", "CMD:ABC123");

    // 4) lowercase rejected
    expectInvalidArguments(v, "CMD:abc");
    expectInvalidArguments(v, "CMD:ABCd");

    // 5) symbols rejected
    expectInvalidArguments(v, "CMD:ABC-123");
    expectInvalidArguments(v, "CMD:ABC_123");
    expectInvalidArguments(v, "CMD:ABC 123"); // internal space should fail

    //5.5 checking empty for CMD
    expectInvalidArguments(v, "CMD:");
    expectInvalidArguments(v, "   CMD:  ");


   // 6) length > 50 rejected
    expectInvalidArguments(v, "CMD:" + std::string(47, 'A'));

   // 7)digit at start rejection cases
    expectInvalidArguments(v, "CMD:1TEST");
    expectInvalidArguments(v, "  CMD:123TEST  ");
    expectInvalidArguments(v, "CMD:1");
    expectInvalidArguments(v, "CMD:\t\t3");
    

    // 8) length == 50 allowed
    expectValid(
    v,
    "CMD:" + std::string(46, 'A'),
    "CMD:" + std::string(46, 'A')
);

    // 9) valid input allowed
    expectValid(v, "CMD:A1B2C3", "CMD:A1B2C3");

    expectValid(v, "CMD:TEST1", "CMD:TEST1");

    expectValid(v, "CMD:T1E2S3T4", "CMD:T1E2S3T4");


    std::cout << "All tests passed. \n";
    return 0;

}
