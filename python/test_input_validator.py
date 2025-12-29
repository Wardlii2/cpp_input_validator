import pytest
from input_validator import Input_Validator
#testing Not Null
def test_null_throws():
    v = Input_Validator()
    with pytest.raises(ValueError):
        v.validate_command(None)

#testing empty string throws
def test_empty_string_throws():
    v = Input_Validator()
    with pytest.raises(ValueError):
        v.validate_command("")
        
        
#testing for whitespace only
def test_whitespace_only_throws():
    v = Input_Validator()
    with pytest.raises(ValueError):
        v.validate_command("    ")
        

#testing leading and trailing whitespacing
def test_trims_leading_and_trailing_whitespace():
    v = Input_Validator()
    assert v.validate_command("  ABC123  ") == "ABC123"
    

#testing lower case throws
def test_lower_case_trows():
    v = Input_Validator()
    with pytest.raises(ValueError):
        v.validate_command("abC123")

#testing symbals
def test_symbol_throws():
    v = Input_Validator()
    with pytest.raises(ValueError):
        v.validate_command("ABC@123")

#testing if length is over maximum acceptence
def test_length_over_max_throws():
    v = Input_Validator()
    too_long = "A" * 58
    with pytest.raises(ValueError):
        v.validate_command(too_long)
        
#testing if max length boundaries are correct
def test_length_exactly_max_is_allowed():
    v = Input_Validator()
    max_len = "A" * 50
    assert v.validate_command(max_len) == max_len
    
#checking if uppercase and digits are accepted
def test_valid_uppercase_and_digits_is_allowed():
    v = Input_Validator()
    assert v.validate_command("HELLO123") == "HELLO123"

# testing to see if digit not at the start is valid
def test_valid_not_Digit_at_start_allowed():
    v = Input_Validator()
    assert v.validate_command("TES1T") == "TES1T"

# testing to see if digit not at the start is valid also
def test_valid_not_Digit_at_start_allowed_also():
    v = Input_Validator()
    assert v.validate_command("T1E2S3T4") == "T1E2S3T4"

# testing to see if digit at the start throws correctly
def test_invalid_Digit_at_start_not_allowed():
    v = Input_Validator()
    with pytest.raises(ValueError):
        v.validate_command("1TEST")
        
# testing to see if digit at the start throws correctly and with whitespace
def test_invalid_Digit_at_start_not_allowed_and_trailling_whitespace_and_whitespace():
    v = Input_Validator()
    with pytest.raises(ValueError):
        v.validate_command("  123TEST  ")

# testing to see if digit at the start throws correctly and with whitespace
def test_invalid_Digit_at_start_not_allowed_and_trailling_whitespace():
    v = Input_Validator()
    with pytest.raises(ValueError):
        v.validate_command("123TEST   ")













    
    


