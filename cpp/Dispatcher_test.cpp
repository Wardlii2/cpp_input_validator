// Testing Dispatcher functionality for CMD:PING and CMD:STATUS commands
#include <cassert>
#include <iostream>
#include <unordered_map>
#include <functional>
#include "dispatcher.h"
#include "command.h"
#include <string>

int main() {
    // Create a dispatcher with command handlers
    Dispatcher dispatcher({
        {"PING", []() { return std::string("PONG"); }},
        {"STATUS", []() { return std::string("STATUS_OK"); }}
    });
    // Test dispatching commands
    assert(dispatcher.dispatch(Command("PING")) == "PONG");
    assert(dispatcher.dispatch(Command("STATUS")) == "STATUS_OK");
    assert(dispatcher.dispatch(Command("HELLO")) == "UNKNOWN_COMMAND");
    // If all assertions pass
    std::cout << "All Dispatcher tests passed!" << std::endl;

    return 0;

}

