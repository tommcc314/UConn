## Quiz Server with Redux

Redux allows for state to be shared across components without passing it through props.

In this example, I use Redux in my quiz server from lab 6.

Originally, there was a results array defined in the Quiz component which contains the result for each question. The Quiz component passes the gradeQuestion method to each Question component. The Question component accesses this method through props, which works fine in this server but it can quickly become messy if there are multiple layers of components passing methods to each other for updating a shared value, or state.

Now, gradeQuestion is a reducer in `src/components/resultSlice.js`. The Quiz component simply takes the state of results and uses it to calculate the score. The Question component now calls the gradeQuestion using Redux. 