import React from 'react';
import { useRef, useState } from 'react'
import logo from './logo.svg';
import './App.css';

import CourseCard from './Components/CourseCard/CourseCard.js';
import Tooltip from "./Components/ToolTip/ToolTip.tsx";
import Search from "./Components/Search/search.tsx";


export function App() {
  return (
    <>
      <div style={{width: "100%", height: "50px", backgroundColor: "hsl(212, 65.70%, 27.50%)"}}></div>

      <div style={{width: "25%", minHeight: "90%", maxHeight: "90%", backgroundColor: "hsl(212, 32%, 92%)"}}>
        {CourseCard()},
        {CourseCard()},
        {CourseCard()},
        {CourseCard()},
        {CourseCard()},
        {CourseCard()}
      </div>
    </>

  );
}

export default App;
