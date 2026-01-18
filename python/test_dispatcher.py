import pytest
from dispatcher import CommandDispatcher
from command import Command

#Testing that the dispatcher correctly routes commands to their handlers.
def test_dispatcher_routes_to_handler_ping():

    #acting as the dispatcher with the dummy handler.
    dispatcher = CommandDispatcher()

    command = Command("PING")

    #dispatching the command and asserting the result.
    result = dispatcher.dispatch(command)
    assert result == "PONG"
   

#Prove safe behavior when an unknown command is dispatched.
def test_that_dispatcher_handles_UNKNOWN_COMMAND():

    #Firstly instenciating dispatcher.
    dispatcher = CommandDispatcher()

    #Calling command
    command = Command("Nope")

    #Now dispatching the command
    result = dispatcher.dispatch(command)
    assert result == "UNKNOWN_COMMAND"

