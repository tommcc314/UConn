package com.example.demo;
import java.util.ArrayList;
import org.springframework.stereotype.Controller;
import org.springframework.ui.Model;
import org.springframework.web.bind.annotation.GetMapping;
import org.springframework.web.bind.annotation.ModelAttribute;
import org.springframework.web.bind.annotation.PathVariable;
import org.springframework.web.bind.annotation.PostMapping;

@Controller
public class QuizController {
    @GetMapping("/quiz")
    public String quizPage(Model model) {
        final QuestionList questionlist = new QuestionList();
        final ArrayList<Question> questions = questionlist.getQuestions();
        model.addAttribute("questions", questions);
        return "quiz";
    }
}