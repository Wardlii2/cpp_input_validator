import pytest
from input_validator import InputValidator
from parser import CommandParser

#Testing if the parser returns the correct Command object based on raw input.
def test_name_parser_returns_command_name_ping():
    #Test that Command_Parser returns Command with name 'PING
    validator = InputValidator()
    parser = CommandParser(validator)

    command = parser.parse("CMD:PING")
    assert command.name == "PING"
    assert command.payload is None


    #Testing if the parser returns the correct Command object based on raw input.
def test_name_parser_returns_command_name_echo():
    #Test that Command_Parser returns Command with name 'PING
    validator = InputValidator()
    parser = CommandParser(validator)

    command = parser.parse("CMD:ECHO:HELLO")
    assert command.name == "ECHO"
    assert command.payload == "HELLO"

#Testing that the parser uses the validator to normalize input before parsing.
def test_proving_parser_relies_on_validator_for_normalization():
    #testing that Command_Parser uses Input_Validator to normalize input
    validator = InputValidator()
    parser = CommandParser(validator)
    rawInput = "   CMD:STATUS   "
    normalized = validator.validate_command(rawInput)
    command = parser.parse(rawInput)

    #adding different normalisation logic due to new name, payload configuration
    body = normalized[4:]
    assert command.name == body
    assert command.payload is None


#Testing that invalid input raises ValueError in the parser.
def test_invalid_input_raises_exception():
    #Test that invalid input raises ValueError
    validator = InputValidator()
    parser = CommandParser(validator)

    invalid_inputs = ["INVALID:PING", "CMDSTATUS", "CMD:ECHO:",]

    for rawInput in invalid_inputs:
        with pytest.raises(ValueError): 
            parser.parse(rawInput)



