#include <string>
#include "Handlers.h"
#include "Parser.h"
#include "Dispatcher.h"
#include "input_validator.h"
#include "app.h"
#include <unordered_map>
#include <functional>
// Application process function implementation
std::string process(const std::string& rawInput) {
    // Create an input validator
    InputValidator validator;

    // Create a parser with the validator
    Parser parser(validator);

    // Parse the raw input to get a Command
    Command command = parser.parse(rawInput);

    // Create a dispatcher with command handlers
    std::unordered_map<std::string, std::function<std::string()>> handlers = {
        {"PING", Handlers::handlePing},
        {"STATUS", Handlers::handleStatus}
    };
    Dispatcher dispatcher(handlers);

    // Dispatch the command and get the response
    return dispatcher.dispatch(command);
}




