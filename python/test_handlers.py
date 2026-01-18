import pytest
from handlers import Handlers

#testing handlers actually output the correct business logic.
class Test_Handlers:

    # Test that the Handlers.status function returns "PONG"
    def test_handle_PING_returns_PONG(self):
        result = Handlers.ping()
        assert result == "PONG"
        
    # Test that the Handlers.status function returns "STATUS:OK"
    def test_handle_STATUS_returns_OK(self):
        result = Handlers.status()
        assert result == "STATUS:OK"