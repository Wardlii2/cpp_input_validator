class Handlers:
    @staticmethod
    def ping():
        return "PONG"

    @staticmethod
    def status():
        return "STATUS:OK"
    
    @staticmethod
    def uptime():
        return "UPTIME:0"
