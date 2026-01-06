#pragma once
#include <string>
#include <unordered_map>
#include <functional>
#include <utility>
#include "command.h"

// Dispatcher implementation /
class Dispatcher {
private:
    std::unordered_map<std::string, std::function<std::string()>> handlers;
public:
    explicit Dispatcher(std::unordered_map<std::string, std::function<std::string()>> h)
        : handlers(std::move(h)) {}

    std::string dispatch(const Command& command) const {
        auto it = handlers.find(command.getName());

        if(it == handlers.end()) {
            return "UNKNOWN_COMMAND";
        }

        

        return it->second();

}
};



