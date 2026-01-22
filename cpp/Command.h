#pragma once
#include <string>
#include <utility>

// Command class declaration
class Command {
private:
    // Command name
    std::string name;
    std::string payload;

public:
    // Constructor
    Command(std::string name, std::string payload = "") : name(std::move(name)), payload(std::move(payload)) {}
    
    // Getter for command name
    const std::string& getName() const {
        return name;
    }


    // Getter for command Payload
    const std::string& getPayload() const {
        return payload;
    }

    
    bool hasPayload() const {
        return !payload.empty();
    }

};