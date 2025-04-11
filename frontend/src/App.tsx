import React, { useEffect } from 'react';
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

function App() {
  const[coursesInActiveSemester, setCoursesInActiveSemester] = useState<Course[]>([]);
  const[activeSemester, setActiveSemester] = useState<Semester>({courses: [], credits: 0});
  
  const addCourseToSemester = (newCourse: Course) => {
    setActiveSemester((prevState) => ({courses: [...prevState.courses, newCourse], credits: (prevState.credits + newCourse.credits)}))
  }

  const clearSemester = () => {
    setActiveSemester((prevState) => ({courses: [], credits: 0}))
  }


  return (
    <>
      
      <div style={{width: "100vw", height: "10vh", backgroundColor: "hsl(212, 65.70%, 27.50%)", display: "inline-flex"}}></div>
      <div style={{width: "25vw", minHeight: "90vh", backgroundColor: "hsl(212, 32%, 92%)", display: "inline-flex"}}>
        <CourseList addToActiveSemester={addCourseToSemester}></CourseList>
      </div>
      <div style={{width: "70vw", minHeight: "90vh", backgroundColor: "hsl(286, 18.90%, 41.60%)", display: "inline-flex"}}>
        <SemesterViewer activeSemester={activeSemester} clearSemester={clearSemester}></SemesterViewer>
      </div>
      

    </>

  );
  
}

export default App;