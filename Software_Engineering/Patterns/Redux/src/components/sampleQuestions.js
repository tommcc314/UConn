const qdef1 = {
    id: 1,
    question: "1. Which of the following statements is NOT part of the agile manifesto?",
    choices: [
        {id:1, text:"Individuals and interactions over processes and tools", correct:false}, 
        {id:2, text:"Working software over comprehensive documentation", correct:false},
        {id:3, text:"Customer collaboration over contract negotiation", correct:false},
        {id:4, text:"Following a plan over responding to change", correct:true}
    ]
};
const qdef2 = {
    id: 2,
    question: "2. What does it mean to work iteratively?",
    choices: [
        {id:1, text:"Repeating a sequence of operations to improve upon the current state and move towards a desired result", correct:true}, 
        {id:2, text:"Working on small pieces of a system and building up to the desired result", correct:false}, 
        {id:3, text:"Using evidence to drive decisions", correct:false}
    ]
};
const qdef3 = {
    id: 3,
    question: "3. What is the signature, accessibility and return type of the Java main function?",
    choices: [
        {id:1, text:"private void main(String[] args)", correct: false},
        {id:2, text:"private static int main(String[] args)", correct: false},
        {id:3, text:"public static void main(String args)", correct: false},
        {id:4, text:"public static void main(String[] args)", correct: true}
    ]
}
const qdef4 = {
    id: 4,
    question: "4. True/False: Feature creep occurs when new features are added without proper consideration of their value for the general customer.",
    choices: [
        {id:1, text:"True", correct: true},
        {id:2, text:"False", correct: false}
    ]
}
const qdef5 = {
    id: 5,
    question: "5. Why is the adapter pattern useful?",
    choices: [
        {id:1, text:"It allows for lost-cost object creation", correct:false},
        {id:2, text:"It allows classes with incompatible interfaces to work together.", correct:true},
        {id:3, text:"It provides a unified interface for a set of interfaces", correct:false}
    ]
}
const qdef6 = {
    id: 6,
    question: "6. Using Javascript, how would you set the value of the element with id demo to the variable x?",
    choices: [
        {id:1, text:"document.getElementById(\"x\").innerHTML = demo;", correct:false},
        {id:2, text:"document.getElementById(\"demo\").innerHTML = x;", correct:true},
        {id:3, text:"document.getElementById(\"demo\").value = x;", correct: false},
        {id:4, text:"document.getElementById(\"x\").value = demo;", correct: false},
    ]
}
const qdef7 = {
    id: 7,
    question: "7. True/False: A multi-instance database system has multiple tenants' information in a database.",
    choices: [
        {id:1, text:"True", correct:false},
        {id:2, text:"False", correct:true}
    ]
}
const qdef8 = {
    id: 8,
    question: "8. True/False: React helps create responsive multi-page applications.",
    choices: [
        {id:1, text:"True", correct:false},
        {id:2, text:"False",correct:true}
    ]
}
const qdef9 = {
    id: 9,
    question: "9. In Javascript, what is a variable defined by the const keyword?",
    choices: [
        {id:1, text:"An immutable reference to a value", correct: true},
        {id:2, text:"An immutable value", correct: false}
    ]
}
const qdef10 = {
    id: 10,
    question: "10. Which of these is NOT a SOLID principle?",
    choices: [
        {id:1, text:"Open-Closed", correct: false},
        {id:2, text:"Dependency Inversion", correct: false},
        {id:3, text:"Interface Union", correct: true},
        {id:4, text:"Single Responsibility", correct: false}
    ]
}
const qs = [qdef1, qdef2, qdef3, qdef4, qdef5, qdef6, qdef7, qdef8, qdef9, qdef10]; 
export default qs;
