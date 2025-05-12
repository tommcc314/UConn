import { configureStore } from '@reduxjs/toolkit';
import resultsReducer from './resultSlice.js';
export default configureStore({
  reducer: {
    results: resultsReducer
  },
})