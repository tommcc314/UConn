import {createSlice} from '@reduxjs/toolkit';
import qs from './sampleQuestions.js'
export const resultSlice = createSlice({
    name: 'results',
    initialState: {
        arr: new Array(qs.length).fill(false),
    },
    reducers: {
        gradeQuestion: (state, action) => {
            state.arr = state.arr.map(
                (result, i) => {
                    if (i === action.payload[0] - 1) return action.payload[1];
                    return result;
                }
            )
        }
    }
})
export const {gradeQuestion} = resultSlice.actions;
export default resultSlice.reducer;