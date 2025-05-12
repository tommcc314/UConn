package Patterns.Factory;

public interface User {
    boolean execRead();
    boolean execWrite();
    boolean execManage();
    int getNumUsers(); // Number of users of the same type
    double getCost(); // Cost incurred by users of that type
}
