#pragma once
#include <string>

#include "input_validator.h"
#include "Command.h"

// Parser implementation /
class Parser {
private:
    const InputValidator& validator;

public:
    explicit Parser(const InputValidator& v) : validator(v) {}

    Command parse(const std::string& rawInput) const {
        //validate plus normalise referencing input validator
        std::string normalized = validator.validateCommand(rawInput);

        //strip CMD prefix
        std::string body = normalized.substr(4);

        auto pos = body.find(':');
        if (pos != std::string::npos) {
            std::string name = body.substr(0, pos);
            std::string payload = body.substr(pos + 1);
            return Command(name, payload);
        }
         //return Payload
        return Command(body);
        }  

};

