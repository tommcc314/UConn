package Lab0.c;

public class TestMe {
	private double value = Double.NaN;
	public static void main(String[] args) {
		System.out.println("Hello world!");
	}

	public TestMe() {}

	public double square() { return value*value; }
    public double circleArea() {
        final double PI = 3.14159;
        return value * value * PI;
    }
    public double CTSalesTax() {
        return 0.635 * value;
    }
    public int flooredSqrt() {
        if (value < 0) {
            System.err.println("Square Root is undefined for numbers less than 0.");
        }
        int ans = 0;
        while (ans * ans < value)
            ans++;
        return ans - 1;
    }
	public void setValue(double v) {
		value = v;
	}

}
