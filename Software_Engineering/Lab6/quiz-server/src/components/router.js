import React from 'react';
import { BrowserRouter, Routes, Route } from 'react-router-dom';
import Home from './home.js';
import Quiz from './quiz.js';
import Signup from './signup.js';
export default function router() {
    return (
        <Routes>
            <Route path='/' element={<Home/>}></Route>
            <Route path='/quiz' element={<Quiz/>}></Route>
            <Route path='/signup' element={<Signup/>}></Route>
        </Routes>
    );
}