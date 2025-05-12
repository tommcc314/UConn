package com.example.demo;
import org.junit.jupiter.api.Test;
import static org.assertj.core.api.Assertions.assertThat;

public class PasswordValidatorTests {
    PasswordValidator pv;
    @Test
    public void testLength() {
        pv = new PasswordValidator("1AB5fe");
        assertThat(pv.validatePassword()).isFalse();
    }
    @Test
    public void testNumber() {
        pv = new PasswordValidator("AtiwhTwoc");
        assertThat(pv.validatePassword()).isFalse();
    }
    @Test
    public void testUpper() {
        pv = new PasswordValidator("t5hg84ngs");
        assertThat(pv.validatePassword()).isFalse();
    }
    @Test
    public void testLower() {
        pv = new PasswordValidator("4GHW284G");
        assertThat(pv.validatePassword()).isFalse();
    }
    @Test
    public void testApproval() {
        pv = new PasswordValidator("4Gec284G");
        assertThat(pv.validatePassword()).isTrue();
    }
}