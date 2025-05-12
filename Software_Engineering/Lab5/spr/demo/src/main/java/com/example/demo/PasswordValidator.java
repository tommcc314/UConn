package com.example.demo;
public class PasswordValidator {
    String password;
    boolean hasUpperCase = false;
    boolean hasLowerCase = false;
    boolean hasNumber = false;
    public PasswordValidator(String pwd) {
        this.password = pwd;
    }
    Boolean validatePassword() {
        if (this.password.length() < 8) return false;
        char ch;
        for(int i=0;i < this.password.length();i++) {
            ch = this.password.charAt(i);
            if( Character.isDigit(ch)) {
                this.hasNumber = true;
            }
            else if (Character.isUpperCase(ch)) {
                this.hasUpperCase = true;
            } else if (Character.isLowerCase(ch)) {
                this.hasLowerCase = true;
            }
        }
        return this.hasUpperCase && this.hasLowerCase && this.hasNumber;
    }
}