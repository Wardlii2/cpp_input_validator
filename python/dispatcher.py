from handlers import Handlers
from command import Command

class CommandDispatcher:
    def __init__(self):
        self.handlers = {
            "PING": Handlers.ping,
            "STATUS": Handlers.status,
        }

    def dispatch(self, command):
        handler = self.handlers.get(command.name)
        if handler is None:
            return "UNKNOWN_COMMAND"
        return handler()
