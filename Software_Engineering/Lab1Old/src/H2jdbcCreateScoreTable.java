package Lab1Old.src; 

/*
 * 
 * From https://www.tutorialspoint.com/h2_database/h2_database_jdbc_connection.htm
 * 
 */

public class H2jdbcCreateScoreTable { 
   // JDBC driver name and database URL 
   static final String JDBC_DRIVER = "org.h2.Driver";   
   static final String DB_URL = "jdbc:h2:tcp://localhost/~/test"; //   
   
   //  Database credentials 
   static final String USER = "sa"; 
   static final String PASS = ""; 
  
   public static void main(String[] args) { 
      System.out.println("Connecting to database..."); 
      H2Connection conn = new H2Connection();   
      System.out.println("Creating table in given database..."); 
      String sql = "CREATE TABLE quiz_takers " + 
      "(id INTEGER not NULL AUTO_INCREMENT, " + 
      " first VARCHAR(255), " + 
      " last VARCHAR(255), " + 
      " age INTEGER, " + 
      " PRIMARY KEY ( id ))";
      // String sql = "CREATE TABLE questions " + 
      // "(id INTEGER not NULL AUTO_INCREMENT, " + 
      // " question VARCHAR(1024), " + 
      // " a VARCHAR(1024), " + 
      // " b VARCHAR(1024), " + 
      // " c VARCHAR(1024), " + 
      // " d VARCHAR(1024), " + 
      // " e VARCHAR(1024), " + 
      // " Answer VARCHAR(1024), " + 
      // " explanation VARCHAR(1024), " +
      // " PRIMARY KEY ( id ))";

      // String sql =  "CREATE TABLE   score " + 
      //    "(id INTEGER not NULL AUTO_INCREMENT, " + 
      //    " usr varchar(255), " +  
      //    " questions_total INTEGER, " +  
      //    " questions_answered INTEGER, " + 
      //    " questions_correct INTEGER, " + 
      //    " PRIMARY KEY ( id ))";  
      conn.executeUpdate(sql);
      System.out.println("Created table in given database..."); 
      conn.close(); 
      System.out.println("Goodbye!");
   } 
}
