#Defining dispatcher class to communicate with handler.
class Dispatcher:
    def __init__(self, handlers:dict):
       self.handlers = handlers
    #Defining despatch as the result of command from parser.
    def dispatch(self, command):
        handler = self.handlers.get(command.name)

        #If there is no Handler for the incoming command then cast to.
        if handler is None:
            return "UNKNOWN_COMMAND"
        
        #Returning the correct handler.
        return handler()