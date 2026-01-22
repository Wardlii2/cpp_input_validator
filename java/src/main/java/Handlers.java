public class Handlers {
    public static String ping(Command command) {
        return "PONG";
    }

    public static String status(Command command) {
        return "STATUS:OK";
    }

    public static String uptime(Command command) {
        return "UPTIME:0";
    }

        public static String echo(Command command) {
        return command.getPayload();
    }
}
