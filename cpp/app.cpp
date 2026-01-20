#include <string>
#include "input_validator.h"
#include "Parser.h"
#include "Dispatcher.h"
#include "app.h"

// Application process function implementation
std::string process(const std::string& rawInput) {
    // Create an input validator
    InputValidator validator;
    // Create a parser with the validator
    Parser parser(validator);
    //Created a dispartcher Instance
    Dispatcher dispatcher;

    // Parse the raw input to get a Command
    Command command = parser.parse(rawInput);
    // Dispatch the command and get the response
    return dispatcher.dispatch(command);
}




