import pytest
from input_validator import InputValidator
#testing Not Null
def test_null_throws():
    v = InputValidator()
    with pytest.raises(ValueError):
        v.validate_command(None)

#testing that no prefix throws correctly
def test_missing_prefix_throws():
    v = InputValidator()
    with pytest.raises(ValueError):
        v.validate_command("HELLO123")
        

#testing empty string throws
def test_empty_string_payload_throws():
    v = InputValidator()
    with pytest.raises(ValueError):
        v.validate_command("CMD:")
        
        
#testing for whitespace only
def test_whitespace_only_empty_payload_throws():
    v = InputValidator()
    with pytest.raises(ValueError):
        v.validate_command("  CMD:  ")
        

#testing leading and trailing whitespacing
def test_trims_leading_and_trailing_whitespace_payload():
    v = InputValidator()
    assert v.validate_command("  CMD:ABC  ") == "CMD:ABC"

#testing that a valid argument for echo is accepted.
def test_echo_is_accepted():
    v = InputValidator()
    assert v.validate_command("CMD:ECHO:HELLO") == "CMD:ECHO:HELLO"

#testing ivalid input for Echo throws
def test_lower_case_throws():
    v = InputValidator()
    with pytest.raises(ValueError):
        v.validate_command("CMD:ECHO:hi")

#testing ivalid input for Echo throws
def test_empty_payload_no_colon_throws():
    v = InputValidator()
    with pytest.raises(ValueError):
        v.validate_command("CMD:ECHO")

#testing ivalid input for Echo throws
def test_empty_echo_throws():
    v = InputValidator()
    with pytest.raises(ValueError):
        v.validate_command("CMD:ECHO:")


#testing ivalid input for Echo throws
def test_Payload_throws_When_Invalid():
    v = InputValidator()
    with pytest.raises(ValueError):
        v.validate_command("CMD:PING:HI")

#testing lower case throws
def test_lower_case_trows():
    v = InputValidator()
    with pytest.raises(ValueError):
        v.validate_command("CMD:abC123")

#testing symbals
def test_symbol_throws():
    v = InputValidator()
    with pytest.raises(ValueError):
        v.validate_command("CMD:ABC@123")

#testing if length is over maximum acceptence
def test_length_over_max_throws():
    v = InputValidator()
    too_long = "CMD:" + "A" * 54
    with pytest.raises(ValueError):
        v.validate_command(too_long)
        
#testing if max length boundaries are correct
def test_length_exactly_max_is_allowed():
    v = InputValidator()
    max_len = "CMD:" + "A" * 46
    assert v.validate_command(max_len) == max_len
    
#checking if uppercase and digits are accepted in payload
def test_valid_uppercase_and_digits_is_allowed_in_payload():
    v = InputValidator()
    assert v.validate_command("CMD:ECHO:123HI") == "CMD:ECHO:123HI"

# testing to see if digit not at the start is valid
def test_valid_not_Digit_at_start_allowed_in_payload():
    v = InputValidator()
    assert v.validate_command("CMD:ECHO:TES1T") == "CMD:ECHO:TES1T"


# testing to see if digit at the start throws correctly
def test_invalid_Digit_at_start_not_allowed():
    v = InputValidator()
    with pytest.raises(ValueError):
        v.validate_command("CMD:1TEST")
        
# testing to see if digit at the start throws correctly and with whitespace
def test_invalid_Digit_at_start_not_allowed_and_trailling_whitespace_and_whitespace():
    v = InputValidator()
    with pytest.raises(ValueError):
        v.validate_command("  CMD:123TEST  ")

# testing to see if digit at the start throws correctly and with whitespace
def test_invalid_Digit_at_start_not_allowed_and_trailling_whitespace():
    v = InputValidator()
    with pytest.raises(ValueError):
        v.validate_command("CMD:123TEST   ")
