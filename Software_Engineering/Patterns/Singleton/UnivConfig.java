package Patterns.Singleton;

public class UnivConfig {
    protected String name = "UConn Stamford";
    protected String[] CSEProfessors = {"Hasan Baig", "Elham Sherafat", "Philip Bradford", "Kriti Bhargava", "Arinjita Paul"};
    private UnivConfig() {}
    private static UnivConfig Instance = new UnivConfig();
    public static UnivConfig getUnivConfig() {
        return Instance;
    }
}
