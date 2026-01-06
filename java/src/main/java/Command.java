// Defining Command as a class.
public class Command {
    private String name;
    
    public Command (String name) {
        this.name = name;
    }
    //allows other classes to access the name of the command.
    public String getName() {
        return name;
    }
}
