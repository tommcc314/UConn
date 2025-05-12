package com.example.demo;

import org.springframework.stereotype.Controller;
import org.springframework.web.bind.annotation.GetMapping;

@Controller 
public class HomeController {

  @GetMapping("/")
  public String defPage() {
    return "home";
  }
  @GetMapping("/home")
  public String homePage() {
    return "home";
  }
  @GetMapping("/quiz")
  public String quizPage() {
    return "quiz";
  }
  @GetMapping("/login")
  public String loginPage() {
    return "login";
  }
}