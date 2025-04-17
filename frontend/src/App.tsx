import React, { act, useEffect } from 'react';
import { useRef, useState } from 'react'
import logo from './logo.svg';
import './App.css';
import CourseCard from './Components/CourseCard/CourseCard';
import Tooltip from "./Components/ToolTip/ToolTip";
import CourseList from "./Components/CourseList/CourseList";
import CourseAdder from "./Components/CourseAdder/CourseAdder"
import SemesterViewer from './Components/Semester/SemesterViewer';
import Course from './Types/Course';
import Semester from './Types/Semester';
import FourYearPlan from './Types/FourYearPlan';
import { get_majors } from './Logic/Major_Logic';
import Major from './Types/Major';
import PlanBuilder from './Components/PlanBuilder/PlanBuilder';

function App() {

  return(
    <>
    
      <PlanBuilder/>

    </>
  )
}
export default App;