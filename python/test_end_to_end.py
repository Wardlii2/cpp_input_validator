#imports from other files
from main import process

#testing the end to end functionality of the application
def test_end_to_end_functionality():
    # fake a user input
    rawInput ="CMD:PING"

    # processing raw input through the system and assigning output as the output of process(rawInput)
    output = process(rawInput)

    #asserting the output is as expected and defined.
    assert output == "PONG"