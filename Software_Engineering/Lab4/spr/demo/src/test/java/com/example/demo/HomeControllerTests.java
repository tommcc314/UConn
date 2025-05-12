package com.example.demo;

import static org.hamcrest.Matchers.containsString;
import static org.springframework.test.web.servlet.request.MockMvcRequestBuilders.get;
import static org.springframework.test.web.servlet.result.MockMvcResultMatchers.content;
import static org.springframework.test.web.servlet.result.MockMvcResultMatchers.status;
import static org.springframework.test.web.servlet.result.MockMvcResultMatchers.view;

import org.junit.jupiter.api.Test;
import org.springframework.beans.factory.annotation.Autowired;
import org.springframework.boot.test.autoconfigure.web.servlet.WebMvcTest;
import org.springframework.test.web.servlet.MockMvc;

@WebMvcTest(HomeController.class)   // <1>
public class HomeControllerTests {

  @Autowired
  private MockMvc mockMvc;   // 

    @Test
    public void testHomePage() throws Exception {
        mockMvc.perform(get("/"))   
        .andExpect(status().isOk()) 
        .andExpect(view().name("home"))
        .andExpect(content().string(       
            containsString("Welcome to 2102 Quizzes!")));
    }
    @Test
    public void testQuizPage() throws Exception {
        mockMvc.perform(get("/quiz"))   
        .andExpect(status().isOk()) 
        .andExpect(view().name("quiz"))
        .andExpect(content().string(       
            containsString("Quiz Framework")));
    }
    @Test
    public void testLoginPage() throws Exception {
        mockMvc.perform(get("/login"))   
        .andExpect(status().isOk()) 
        .andExpect(view().name("login"))
        .andExpect(content().string(       
            containsString("Login")));
    }

}