#Defining different handlers as functions not as classes to not cause abstruction.
#A method for handling PING and PONG Commands
def handle_ping():
    return "PONG"

#A method/function for handling Status Commands
def handle_status():
    return "STATUS_OK"

