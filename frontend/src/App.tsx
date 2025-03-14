import React from 'react';
import { useRef, useState } from 'react'
import logo from './logo.svg';
import './App.css';

import CourseCard from './Components/CourseCard/CourseCard';
import Tooltip from "./Components/ToolTip/ToolTip";
import CourseList from "./Components/CourseList/CourseList";
import CourseAdder from "./Components/CourseAdder/CourseAdder"


export function App() {
  return (
    <>
      <div style={{width: "100vw", height: "10vh", backgroundColor: "hsl(212, 65.70%, 27.50%)", display: "inline-flex"}}></div>
      <div style={{width: "25vw", minHeight: "90vh", backgroundColor: "hsl(212, 32%, 92%)", display: "inline-flex"}}>
        <CourseList></CourseList>
      </div>

    </>

  );
}

export default App;
