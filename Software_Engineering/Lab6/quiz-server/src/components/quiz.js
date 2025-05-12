import Question from "./question.js";
import { useState } from 'react';
import '../styles/quiz.css';
import qs from './sampleQuestions.js'
export default function Quiz() {
    const results = new Array(qs.length).fill(false);
    const gradeQuestion = (id, correct) => {
        results[id - 1] = correct;
    }
    const Questions = qs.map(((q)=><Question def={q} grader={gradeQuestion}/>));
    const [submitted, setSubmitted] = useState(0);
    const [score, setScore] = useState(0);
    const submitQuiz = () => {
        let s = 0;
        for (let i = 0; i < qs.length; ++i) {
            s += results[i];
        }
        setScore(s);
        setSubmitted(1);
    }
    return (
        <div className="container custom mt-sm-5 my-1">
            {Questions}
            <div className="d-flex align-items-center pt-3">
                <div className="ml-auto mr-sm-5">
                    {submitted ? <button onClick={() => window.location.reload()} className="btn btn success">Try Again</button> : <button onClick={() => submitQuiz()} data-testid="submit" className="btn btn-success">Submit</button>}
                </div>
            </div>
            {(submitted > 0) && <p data-testid="scoreMessage">{"You got a " + score + " out of " + qs.length + "!"}</p>}
        </div>
    );
}