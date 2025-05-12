package Lab0.u;

import static org.junit.Assert.*;

import org.junit.Before;
import org.junit.Test;

import Lab0.c.TestMe;

public class TestMeTests {

	TestMe testMe;

	@Before
	public void setUp() throws Exception {
		testMe  = new TestMe();
    }

	@Test
	public void squareTest() {
		double baseValue = 3.0;
		double expected = baseValue*baseValue;
		testMe.setValue(baseValue);
		double actual = testMe.square();
		assertTrue(actual == expected);
	}
    @Test
	public void circleAreaTest() {

		double baseValue = 8.1;
		double expected = baseValue*baseValue*3.14159;
		testMe.setValue(baseValue);
		double actual = testMe.circleArea();
		assertTrue(actual == expected);
	}
    @Test
    public void CTSalesTaxTest() {
        double baseValue = 55.12;
        double expected = baseValue*0.635;
        testMe.setValue(baseValue);
        double actual = testMe.CTSalesTax();
        assertTrue(actual == expected);
    }
    @Test
    public void FlooredSqrtTest() {
        double baseValue = 65;
        int expected = 8;
        testMe.setValue(baseValue);
        int actual = testMe.flooredSqrt();
        assertTrue(actual == expected);
    }
}
