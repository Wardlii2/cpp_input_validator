// Testing Dispatcher functionality for CMD:PING and CMD:STATUS commands
#define CATCH_CONFIG_MAIN
#include "include/Catch2/catch_amalgamated.hpp"

#include "Dispatcher.h"
#include "Command.h"

TEST_CASE("Dispatcher outputs commands properly for single return commands") {
    // Create a dispatcher with command handlers
    Dispatcher dispatcher;
    // Test dispatching commands
    REQUIRE(dispatcher.dispatch(Command("PING", "")) == "PONG");
    REQUIRE(dispatcher.dispatch(Command("STATUS", "")) == "STATUS:OK");
    REQUIRE(dispatcher.dispatch(Command("UPTIME", "")) == "UPTIME:0");
    REQUIRE(dispatcher.dispatch(Command("HELP", "")) == "PING,STATUS,UPTIME,ECHO,HELP");
}

TEST_CASE("Dispatcher outputs commands properly for name + payload commands") {
    // istenciate the dispatcher with its handlers.
    Dispatcher dispatcher; 
    //testing the actual handler for dispatcher.
    REQUIRE(dispatcher.dispatch(Command("ECHO", "HELLO")) == "HELLO");
}

TEST_CASE("Dispathcer returns UNKNOWN COMMAND properly") {

    Dispatcher dispatcher;
    REQUIRE(dispatcher.dispatch(Command("HELLO", "TEST")) == "UNKNOWN_COMMAND");
}


