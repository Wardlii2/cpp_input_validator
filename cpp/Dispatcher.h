#pragma once
#include <string>
#include <unordered_map>
#include <functional>

#include "Command.h"
#include "Handlers.h"

// Dispatcher class implementation /
class Dispatcher {
    private: 
    std::unordered_map<std::string, std::function< std::string(const Command&)>> handler;

    public:
    Dispatcher() {
        handler.emplace("PING", Handlers::ping);
        handler.emplace("STATUS", Handlers::status);
        handler.emplace("UPTIME", Handlers::uptime);
        handler.emplace("ECHO", Handlers::echo);

    }

    std::string dispatch(const Command& command) const {
        auto it = handler.find(command.getName());
        if (it == handler.end()) {
            return "UNKNOWN_COMMAND";
        }
        return it->second(command);
    };

};



