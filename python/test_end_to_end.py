#imports from other files
from main import process

#testing the end to end functionality of the application
def test_end_to_end_functionality_for_PING():
    # fake a user input
    rawInput ="CMD:PING"
    # processing raw input through the system and assigning output as the output of process(rawInput)
    output = process(rawInput)
    #asserting the output is as expected and defined.
    assert output == "PONG"


#testing the end to end functionality of the application for uptime command.
def test_end_to_end_functionality_for_UPTIME():

    #fake an input
    rawInput = "CMD:UPTIME"
    #assigning output as the process of raw input.
    output = process(rawInput)
    #asserting output to correct answer.
    assert output == "UPTIME:0"


def test_end_to_end_functionality_for_echo():

    #fake an input
    rawInput = "CMD:ECHO:TESTING12"
    #assigning output as the process of raw input.
    output = process(rawInput)
    #asserting output to correct answer.
    assert output == "TESTING12"

