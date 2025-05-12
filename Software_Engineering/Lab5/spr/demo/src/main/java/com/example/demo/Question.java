package com.example.demo;

import java.util.ArrayList;


public class Question {
    String ques;
    ArrayList<String> choices = new ArrayList<String>();
    int answer;
    public Question() {}
    public void setQuestion(String question) {
        this.ques = question;
    }
    public void setChoices(ArrayList<String> choices) {
        this.choices = choices;
    }
    public void setAnswer(int answer) {
        this.answer = answer;
    }
    public String getQuestion() {
        return this.ques;
    }
    public ArrayList<String> getChoices() {
        return this.choices;
    }
    public int getAnswer() {
        return this.answer;
    }
}