package Lab1Old.src;

import java.sql.Connection;
import java.sql.DriverManager;
import java.sql.ResultSet;
import java.sql.SQLException;
import java.sql.Statement;

public class H2Connection {
    private static final String JDBC_DRIVER = "org.h2.Driver";   
	private static final String DB_URL = "jdbc:h2:tcp://localhost/~/test"; 
	
	private static final String USER = "sa"; 
	private static final String PASS = ""; 
    private Connection conn = null; 
    private Statement stmt = null; 
    private ResultSet rs;
    public H2Connection() {
        try {
	       // STEP 0: Register JDBC driver 
	       Class.forName(JDBC_DRIVER); 
	           
	       //STEP 0: Open a connection 
	       conn = DriverManager.getConnection(DB_URL,USER,PASS);  
	    } catch(SQLException se) { 
	        //Handle errors for JDBC 
	        se.printStackTrace(); 
	    } catch(Exception e) { 
	        //Handle errors for Class.forName 
	        e.printStackTrace(); 
	    } 
    }
    public void executeUpdate(String sql) {
        try {
            stmt = conn.createStatement(); 
	        stmt.executeUpdate(sql);
	    } catch(SQLException se) { 
	        //Handle errors for JDBC 
	        se.printStackTrace(); 
	    } catch(Exception e) { 
	        //Handle errors for Class.forName 
	        e.printStackTrace(); 
	    }
    }
    public ResultSet executeQuery(String sql) {
        try {
            stmt = conn.createStatement(); 
	        rs = stmt.executeQuery(sql);
	    } catch(SQLException se) { 
	        //Handle errors for JDBC 
	        se.printStackTrace(); 
	    } catch(Exception e) { 
	        //Handle errors for Class.forName 
	        e.printStackTrace(); 
	    } 
        return rs;
    }
    public void close() {
        try{ 
            if(stmt!=null) stmt.close(); 
        } catch(SQLException se2) { 
        }
        try { 
            if(conn!=null) conn.close(); 
        } catch(SQLException se){ 
            se.printStackTrace(); 
        }
    }
}
