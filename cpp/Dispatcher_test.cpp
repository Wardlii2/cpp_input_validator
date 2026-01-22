// Testing Dispatcher functionality for CMD:PING and CMD:STATUS commands
#include <cassert>
#include <iostream>

#include "Dispatcher.h"
#include "Command.h"

int main() {
    // Create a dispatcher with command handlers
    Dispatcher dispatcher;
    // Test dispatching commands
    assert(dispatcher.dispatch(Command("PING", "")) == "PONG");
    assert(dispatcher.dispatch(Command("STATUS", "")) == "STATUS:OK");
    assert(dispatcher.dispatch(Command("HELLO", "")) == "UNKNOWN_COMMAND");
    assert(dispatcher.dispatch(Command("UPTIME", "")) == "UPTIME:0");
    assert(dispatcher.dispatch(Command("ECHO", "HELLO")) == "HELLO");

    // If all assertions pass
    std::cout << "All Dispatcher tests passed!" << std::endl;

    return 0;

}

