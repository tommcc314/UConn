package Lab1Old.test;

//package unit_tests;
import Lab1Old.src.H2Connection;
import static org.junit.Assert.*;
import java.sql.ResultSet;
import java.sql.SQLException;

//import org.junit.jupiter.api.Test;

import org.junit.Test; 

public class TestScoreTable {

	@Test
	public void test() {	
		H2Connection conn = new H2Connection();
	    try { 
	       // STEP 0: Register JDBC driver 
	       String sql =  "INSERT INTO  score " + 
	          "(usr,questions_total,questions_answered,questions_correct) " +
	          "VALUES ('Alan Turing', 100, -5, 2); ";
	       conn.executeUpdate(sql);
	       /* */
	       
	       // STEP 2: Select the rest row 
	       sql =  "SELECT * FROM score WHERE usr='Alan Turing' ;";
	       ResultSet rs = conn.executeQuery(sql);
	       while (rs.next()) {
	    	   String actualString = rs.getString("questions_total");
	    	   int actualInt = Integer.parseInt(actualString);
	    	   assertTrue(100 == actualInt);
	       }
	       
	     //STEP 3: Remove the test row
	       sql = "DELETE FROM score WHERE usr='Alan Turing' ;";
	       conn.executeUpdate(sql);
	       conn.close();
	    } catch(SQLException se) { 
	        //Handle errors for JDBC 
	        se.printStackTrace(); 
	    }
	}
}
