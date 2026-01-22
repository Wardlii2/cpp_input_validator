import pytest
from handlers import Handlers
from command import Command

#testing handlers actually output the correct business logic.
class Test_Handlers:

    # Test that the Handlers.status function returns "PONG"
    def test_handle_PING_returns_PONG(self):
        result = Handlers.ping(Command("PING", None))
        assert result == "PONG"
        
    # Test that the Handlers.status function returns "STATUS:OK"
    def test_handle_STATUS_returns_OK(self):
        result = Handlers.status(Command("STATUS", None))
        assert result == "STATUS:OK"

    #Test that Handlers.uptime function returns "UPTIME:0"
    def test_handle_UPTIME_returns_ok(self):
        result = Handlers.uptime(Command("UPTIME", None))
        assert result == "UPTIME:0"

    #Test that Handlers.uptime function returns "UPTIME:0"
    def test_handle_ECHO_returns_ok(self):
        result = Handlers.echo(Command("ECHO", "HELLO"))
        assert result == "HELLO"

