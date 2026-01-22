// Defining Command as a class.
public class Command {
    private final String name;
    private final String payload;
    
    public Command (String name, String payload) {
        this.name = name;
        this.payload = payload;
    }
    //allows other classes to access the name of the command.
    public String getName() {
        return name;
    }

        //allows other classes to access the name of the command.
    public String getPayload() {
        return payload;
    }
}
