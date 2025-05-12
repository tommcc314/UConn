package com.example.demo;

import org.junit.jupiter.api.Test;

import org.springframework.beans.factory.annotation.Autowired;
import org.springframework.boot.test.context.SpringBootTest;
import org.springframework.boot.test.context.SpringBootTest.WebEnvironment;
import org.springframework.boot.test.web.client.TestRestTemplate;
import org.springframework.beans.factory.annotation.Value;

import static org.assertj.core.api.Assertions.assertThat;
@SpringBootTest(webEnvironment=WebEnvironment.RANDOM_PORT)
class DemoApplicationTests {
	@Value(value="${local.server.port}")
	private int port;
	@Autowired
	private TestRestTemplate restTemplate;
	@Test
	void quizHeaderLoads() {
		assertThat(this.restTemplate.getForObject("http://localhost:" + port + "/quiz", String.class)).contains("Quiz Framework");
	}
	@Test
	void quizContentLoads() {
		assertThat(this.restTemplate.getForObject("http://localhost:" + port + "/quiz", String.class)).contains("Question");
	}
	@Test
	void quizButtonLoads() {
		assertThat(this.restTemplate.getForObject("http://localhost:" + port + "/quiz", String.class)).contains("Next");
	}
}
