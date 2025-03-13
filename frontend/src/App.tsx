import React from 'react';
import { useRef, useState } from 'react'
import logo from './logo.svg';
import './App.css';

import CourseCard from './Components/CourseCard/CourseCard.js';
import Tooltip from "./Components/ToolTip/ToolTip.tsx";
import Search from "./Components/Search/search.tsx";
import CourseList from "./Components/CourseList/CourseList.tsx";
import CourseAdder from "./Components/CourseAdder/CourseAdder.tsx"


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
