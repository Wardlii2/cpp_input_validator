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
    assert v.validate_command("  CMD:ABC123  ") == "CMD:ABC123"
    

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
    
#checking if uppercase and digits are accepted
def test_valid_uppercase_and_digits_is_allowed():
    v = InputValidator()
    assert v.validate_command("CMD:HELLO123") == "CMD:HELLO123"

# testing to see if digit not at the start is valid
def test_valid_not_Digit_at_start_allowed():
    v = InputValidator()
    assert v.validate_command("CMD:TES1T") == "CMD:TES1T"

# testing to see if digit not at the start is valid also
def test_valid_not_Digit_at_start_allowed_also():
    v = InputValidator()
    assert v.validate_command("CMD:T1E2S3T4") == "CMD:T1E2S3T4"

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
