import { render, screen } from '@testing-library/react';
import userEvent from '@testing-library/user-event'
import { BrowserRouter } from 'react-router-dom';
import '@testing-library/jest-dom';
import App from './app.js';
import qs from './components/sampleQuestions.js';
test('Home page renders', () => {
  render(<App />, {wrapper: BrowserRouter});
  const welcomeMessage = screen.getByText(/Welcome to 2102 Quizzes!/i);
  expect(welcomeMessage).toBeInTheDocument();
});
test('Nav renders', () => {
  render(<App />, {wrapper: BrowserRouter});
  const quizLink = screen.getByText(/New Quiz/i);
  const signupLink = screen.getByText(/Sign up/i);
  expect(quizLink).toBeInTheDocument();
  expect(signupLink).toBeInTheDocument();
});
test('Quiz page renders', async () => {
  render(<App />, {wrapper: BrowserRouter});
  const user = userEvent.setup();
  await user.click(screen.getByText(/New Quiz/i));
  for (let i = 0; i < qs.length; ++i) {
    let question = screen.getByText(qs[i].question);
    expect(question).toBeInTheDocument();
  }
});
test('Quiz scores correctly', async () => {
  // simulate selecting the first choice for each question and test whether the score is updated and displayed correctly
  render(<App />, {wrapper: BrowserRouter});
  const user = userEvent.setup();
  await user.click(screen.getByText(/New Quiz/i));
  let score = 0;
  for (let i = 0; i < qs.length; ++i) {
    if (qs[i].choices[0].correct) ++score;
    await user.click(screen.getByTestId("q" + (i + 1) + "choice1"));
  }
  await user.click(screen.getByTestId("submit"));
  // let scoreMessage = screen.getByText("You got a " + score + " out of " + qs.length + "!");
  let scoreMessage = screen.getByTestId("scoreMessage");
  expect(scoreMessage.innerHTML).toEqual("You got a " + score + " out of " + qs.length + "!");
  // let scoreMessage = screen.getByText("3. What is the signature, accessibility and return type of the Java main function?");
});
test('Signup page renders', async () => {
  render(<App />, {wrapper: BrowserRouter});
  const user = userEvent.setup();
  await user.click(screen.getByText(/Sign up/i));
  const signupButton = screen.getByText(/Create Account/i);
  expect(signupButton).toBeInTheDocument();
});
