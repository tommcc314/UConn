package Patterns.Prototype;
import java.util.List;
import Patterns.Prototype.Students;
public class TestStudents {
    public static void main(String[] args) throws CloneNotSupportedException {
		Students roster = new Students();
		roster.loadRoster();
		//Create copies
		Students newRoster = (Students) roster.clone();
		List<String> names = roster.getRoster();
		names.add("Mohammed");
		List<String> newNames = newRoster.getRoster();
		newNames.remove("James");
		
		System.out.println("Original Roster List: " + names);
		System.out.println("Copied List: " + newNames);
	}
}
