package com.example.demo;

import java.util.regex.Matcher;
import java.util.regex.Pattern;

public class EmailValidator {
    String email;
    public EmailValidator(String email) {
        this.email = email;
    }
    Boolean validateEmail() {
        Pattern pattern = Pattern.compile("^(.+)@(.+)$");
        Matcher matcher = pattern.matcher(this.email);
        return matcher.matches();
    }
}