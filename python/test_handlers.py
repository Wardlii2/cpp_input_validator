import pytest
from handlers import handle_ping, handle_status

#testing handlers actually output the correct business logic.
class Test_Handlers:

    # Test that the handle_ping function returns "PONG"
    def test_handle_PING_returns_PONG(self):
        result = handle_ping()
        assert result == "PONG"
        
    # Test that the handle_status function returns "STATUS_OK"
    def test_handle_STATUS_returns_OK(self):
        result = handle_status()
        assert result == "STATUS_OK"