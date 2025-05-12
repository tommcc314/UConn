These unit tests use JUnit 4.13.2. Necessary JAR files:
- (JUnit 4.13.2 Jar)[https://repo1.maven.org/maven2/junit/junit/4.13.2/junit-4.13.2.jar]
- (Hamcrest 1.3 Jar)[https://repo1.maven.org/maven2/org/hamcrest/hamcrest-core/1.3/hamcrest-core-1.3.jar]
- (Windows H2 Database Installer)[https://github.com/h2database/h2database/releases/download/version-2.2.222/h2-setup-2023-08-22.exe]

## Building Unit Tests

New test classes and methods should be created in the test folder.

## Executing Unit Tests

We can compile in the terminal in the test folder: `javac -cp 'Path/to/junit-4.13.2.jar' ./Lab1/src/H2Connection.java ./Lab1/src/H2jdbcCreateScoreTable.java ./Lab1/test/TestScoreTable.java`

Then, execute using `java -cp 'Path/to/junit-4.13.2.jar;Path/to/hamcrest-core-1.3.jar;Path/to/h2-2.2.222.jar;./Lab1/src;' org.junit.runner.JUnitCore Lab1.test.TestScoreTable`