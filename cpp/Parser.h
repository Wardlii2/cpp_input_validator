#pragma once
#include <string>

#include "input_validator.h"
#include "command.h"
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
        std::string payload = normalized.substr(4);

        //return Payload
        return Command(payload);


    }



};

