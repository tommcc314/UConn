package com.example.demo;
public class LoginCredentials {
    public String email;
    public String password;
    public void setemail(String email) {
        this.email = email;
    }
    public void setpassword(String password) {
        this.password = password;
    }
    public String getemail() {
        return this.email;
    }
    public String getpassword() {
        return this.password;
    }
}