import pytest
from dispatcher import Dispatcher

#Testing that the dispatcher correctly routes commands to their handlers.
def test_dispatcher_routes_to_handler_ping():

    #arranging a dummy handler for PING command and testing dispatching.
    def dummy_handle_ping():
        return "PONG"

    #acting as the dispatcher with the dummy handler.
    dispatcher = Dispatcher({"PING": dummy_handle_ping})

    #creating a dummy command object, with the value PING, remember to add () to instantiate the object.
    command = type("Command", (object,), {"name": "PING"})()

    #dispatching the command and asserting the result.
    result = dispatcher.dispatch(command)
    assert result == "PONG"
   

#Prove safe behavior when an unknown command is dispatched.
def test_that_dispatcher_handles_UNKNOWN_COMMAND():

    dummy_command_name = "UNKNOWN_COMMAND"

    #Firstly arranging the dispatcher with no handlers.
    dispatcher = Dispatcher({})

    #Creating a dummy command with no know handler. remember to add () to instantiate the object.
    command = type("Command", (object,), {"name": dummy_command_name})()

    #Now dispatching the command
    result = dispatcher.dispatch(command)
    assert result == "UNKNOWN_COMMAND"

