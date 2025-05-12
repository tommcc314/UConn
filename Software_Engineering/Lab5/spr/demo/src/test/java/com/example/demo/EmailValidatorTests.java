package com.example.demo;
import org.junit.jupiter.api.Test;
import static org.assertj.core.api.Assertions.assertThat;

public class EmailValidatorTests {
    EmailValidator ev;
    @Test
    public void testNoAt() {
        ev = new EmailValidator("tomuconn.edu");
        assertThat(ev.validateEmail()).isFalse();
    }
    @Test
    public void testWithAt() {
        ev = new EmailValidator("tom@uconn.edu");
        assertThat(ev.validateEmail()).isTrue();
    }
}