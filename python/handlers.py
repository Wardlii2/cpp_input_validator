class Handlers:
    @staticmethod
    def ping(command):
        return "PONG"

    @staticmethod
    def status(command):
        return "STATUS:OK"
    
    @staticmethod
    def uptime(command):
        return "UPTIME:0"
    
    @staticmethod
    def echo(command):
        return command.payload
