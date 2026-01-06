#pragma once
#include <string>
#include <utility>

// Command class declaration
class Command {
private:
    // Command name
    std::string name;

public:
    // Constructor
    explicit Command(std::string n) : name(std::move(n)) {}
    // Getter for command name
    const std::string& getName() const {
        return name;
    }

};