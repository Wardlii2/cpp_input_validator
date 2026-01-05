#imports from other files
from main import process

#testing the end to end functionality of the application
def test_end_to_end_functionality():
    # fake a user input
    raw_input ="CMD:PING"

    # processing raw input through the system and assigning output as the output of process(raw_input)
    output = process(raw_input)

    #asserting the output is as expected and defined.
    assert output == "PONG"