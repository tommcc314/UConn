package Patterns.Factory;

public class Reader implements User {
    private boolean canRead;
    private boolean canWrite;
    private boolean canManage;
    private double costPerUser = 15.50;
    private static int userLimit = 10; // every full user after 5 will incur extra cost.
    private static int numUsers = 0;
    public Reader() {
        canRead = true;
        canWrite = false;
        canManage = false;
        numUsers++;
    }
    public double getCost() {
        double extraCost = 0;
        for (int i = 1; i <= numUsers - userLimit; ++i) {
            extraCost += costPerUser * Math.pow(1.03, i); // every full user above 10 will incur 3% extra compounding.
        }
        return costPerUser * Math.min(userLimit, numUsers) + extraCost;
    }
    public int getNumUsers() {
        return numUsers;
    }
    public boolean execRead() {
        return canRead;
    }
    public boolean execWrite() {
        return canWrite;
    }
    public boolean execManage() {
        return canManage;
    }
}
