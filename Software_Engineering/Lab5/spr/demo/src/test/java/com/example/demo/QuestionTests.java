package com.example.demo;
import java.util.ArrayList;
import org.junit.jupiter.api.Test;
import static org.assertj.core.api.Assertions.assertThat;

public class QuestionTests {
    Question question = new Question();
    @Test
    public void testQuestion() {
        question.setQuestion("What year was UConn founded?");
        assertThat(question.getQuestion() == "What year was UConn founded?").isTrue();
    }
    @Test
    public void testChoice() {
        ArrayList<String> choices = new ArrayList<String>();
        choices.add("1845");
        choices.add("1868");
        choices.add("1881");
        choices.add("1903");
        question.setChoices(choices);
        assertThat(question.getChoices() == choices).isTrue();
    }
    @Test
    public void testAnswer() {
        question.setAnswer(3);
        assertThat(question.getAnswer() == 3).isTrue();
    }
}