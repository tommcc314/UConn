package Patterns.Factory;

public class UserFactory {
    public User getUser(int code) {
        if (code == 1) {
            User newUser = new FullUser();
            return newUser;
        }
        else if (code == 2) {
            User newUser = new Contributor();
            return newUser;
        }
        else if (code == 3) {
            User newUser = new Reader();
            return newUser;
        }
        System.err.println("Code is invalid.");
        return null;
    }
}
