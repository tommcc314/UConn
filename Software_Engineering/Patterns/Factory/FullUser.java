package Patterns.Factory;
public class FullUser implements User {
    private boolean canRead;
    private boolean canWrite;
    private boolean canManage;
    private double costPerUser = 75.30;
    private static int userLimit = 5; // every full user after 5 will incur extra cost.
    private static int numUsers = 0;
    public FullUser() {
        canRead = true;
        canWrite = true;
        canManage = true;
        numUsers++;
    }
    public double getCost() {
        double extraCost = 0;
        for (int i = 1; i <= numUsers - userLimit; ++i) {
            extraCost += costPerUser * Math.pow(1.1, i); // every full user above 5 will incur 10% extra compounding.
        }
        return costPerUser * Math.min(5, numUsers) + extraCost;
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
