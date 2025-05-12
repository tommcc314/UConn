package com.example.demo;
import org.junit.jupiter.api.Test;
import static org.assertj.core.api.Assertions.assertThat;

public class QuestionListTests {
    QuestionList list = new QuestionList();
    @Test
    public void testQuestion() {
        assertThat(list.questions.get(0).getQuestion() == "What is the first letter of the alphabet?").isTrue();
    }
    @Test
    public void testChoice() {
        assertThat(list.questions.get(0).getChoices().get(2) == "Z").isTrue();
    }
    @Test
    public void testAnswer() {
        assertThat(list.questions.get(1).getAnswer() == 2).isTrue();
    }
}