package com.example.demo;
import java.util.ArrayList;
public class QuestionList {
    ArrayList<Question> questions = new ArrayList<Question>();
    public QuestionList() {
        Question q1 = new Question();
        q1.setQuestion("What is the first letter of the alphabet?");
        ArrayList<String> q1choices = new ArrayList<String>();
        q1choices.add("B"); q1choices.add("U"); q1choices.add("Z"); q1choices.add("A");
        q1.setChoices(q1choices);
        q1.setAnswer(4);
        Question q2 = new Question();
        q2.setQuestion("What is UConn's nickname?");
        ArrayList<String> q2choices = new ArrayList<String>();
        q2choices.add("Broncos"); q2choices.add("Huskies"); q2choices.add("Rebels"); q2choices.add("Tigers");
        q2.setChoices(q2choices);
        q2.setAnswer(2);
        this.questions.add(q1); this.questions.add(q2);
    }
    public ArrayList<Question> getQuestions() {
        return this.questions;
    }
}