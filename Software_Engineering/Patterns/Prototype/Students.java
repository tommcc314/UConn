package Patterns.Prototype;
import java.util.List;
import java.util.ArrayList;

public class Students implements Cloneable{

	private List<String> roster;
	
	public Students(){
		roster = new ArrayList<String>();
	}
	
	public Students(List<String> list){
		this.roster=list;
	}
	public void loadRoster(){
        // Protoypes are useful if loading a roster required retrieving a lot of data from a database.
        String[] studentNames = {"James","Mark","Caroline","Beth"};  
		for (String student : studentNames) {
            roster.add(student);
        }
	}
    public List<String> getRoster() {
		return roster;
	}

	@Override
	public Object clone() throws CloneNotSupportedException{
        // To clone a roster, copy the students
        List<String> rosterCopy = new ArrayList<String>();
        for(String s : this.getRoster()){
            rosterCopy.add(s);
        }
        return new Students(rosterCopy);
	}
	
}
