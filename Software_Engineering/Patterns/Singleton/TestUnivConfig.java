package Patterns.Singleton;
import Patterns.Singleton.UnivConfig;
public class TestUnivConfig {
    public static void main(String[] args) {
        UnivConfig config1 = UnivConfig.getUnivConfig();
        UnivConfig config2 = UnivConfig.getUnivConfig();
        if (config1 == config2) {
            System.out.println("Same config.");
        }
    }
}
