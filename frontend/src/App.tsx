import React, { useEffect } from 'react';
import { useRef, useState } from 'react'
import logo from './logo.svg';
import './App.css';

import CourseCard from './Components/CourseCard/CourseCard';
import Tooltip from "./Components/ToolTip/ToolTip";
import CourseList from "./Components/CourseList/CourseList";
import CourseAdder from "./Components/CourseAdder/CourseAdder"
import Semester from './Components/Semester/Semester';
import Course from './Types/Course';







function App() {
  const[courseData, setCourseData] = useState([]);
  const[coursesInSemester, setCoursesInSemester] = useState<Course[]>([])


  const FetchCourses = () => {
    useEffect(() => {
      fetch("http://127.0.0.1:8000/courses/", {
        credentials: 'include',
        method: 'GET',
        headers: {
          Accept: 'application/json',
          'Content-Type': 'application/json'
        }
      }).then((response) => {
        if (response.status == 200) {
        response.json().then((courses) => {
            console.log("Set Course Data Working")
            console.log(courses)
            setCourseData(courses)
            return courseData;
        });
        }
      
      });
    }, [])
    
  }
  
  const addCourseToSemester = (course: Course) => {
    alert("Adding Course to Semester")
    alert(course.name)
    setCoursesInSemester((prevState) => ([
      ...prevState,
      course
    ]));
  }


  return (
    <>
      
      <div style={{width: "100vw", height: "10vh", backgroundColor: "hsl(212, 65.70%, 27.50%)", display: "inline-flex"}}></div>
      <div style={{width: "25vw", minHeight: "90vh", backgroundColor: "hsl(212, 32%, 92%)", display: "inline-flex"}}>
        <CourseList addToSemester={addCourseToSemester}></CourseList>
      </div>
      <div style={{width: "70vw", minHeight: "90vh", backgroundColor: "hsl(286, 18.90%, 41.60%)", display: "inline-flex"}}>
        <Semester courses={coursesInSemester}></Semester>
      </div>
      

    </>

  );
  
}

export default App;