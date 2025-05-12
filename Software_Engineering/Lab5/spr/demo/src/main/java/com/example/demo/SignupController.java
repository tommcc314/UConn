package com.example.demo;
import java.util.ArrayList;
import org.springframework.stereotype.Controller;
import org.springframework.ui.Model;
import org.springframework.web.bind.annotation.GetMapping;
import org.springframework.web.bind.annotation.ModelAttribute;
import org.springframework.web.bind.annotation.PathVariable;
import org.springframework.web.bind.annotation.PostMapping;

@Controller
public class SignupController {
    @GetMapping("/signup")
    public String signupPage(Model model) {
        model.addAttribute("creds", new LoginCredentials());
        return "signup";
    }
    @PostMapping("/signup")
    public String signupValidate(Model model, @ModelAttribute("creds") LoginCredentials login) {
        EmailValidator ev = new EmailValidator(login.getemail());
        PasswordValidator pv = new PasswordValidator(login.getpassword());
        model.addAttribute("emailok", ev.validateEmail());
        model.addAttribute("passwordok", pv.validatePassword());
        return "signup";
    }
}