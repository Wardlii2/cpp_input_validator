import pytest
from input_validator import Input_Validator
from parser import Command_Parser

"""Testing if the parser returns the correct Command object based on raw input."""
def test_name_parser_returns_command_name_ping():
    """Test that Command_Parser returns Command with name 'PING'"""
    validator = Input_Validator()
    parser = Command_Parser(validator)

    command = parser.parse("CMD:PING")
    assert command.name == "PING"

"""Testing that the parser uses the validator to normalize input before parsing."""
def test_proving_parser_relies_on_validator_for_normalization():
    """testing that Command_Parser uses Input_Validator to normalize input"""
    validator = Input_Validator()
    parser = Command_Parser(validator)
    raw_input = "   CMD:STATUS   "
    normalized = validator.validate_command(raw_input)
    command = parser.parse(raw_input)
    assert command.name == normalized[4:]


"""Testing that invalid input raises ValueError in the parser."""
def test_invalid_input_raises_exception():
    """Test that invalid input raises ValueError"""
    validator = Input_Validator()
    parser = Command_Parser(validator)

    invalid_inputs = [
        "INVALID:PING",
        "CMDSTATUS",
    ]

    for raw_input in invalid_inputs:
        pytest.raises(ValueError, parser.parse, raw_input)



