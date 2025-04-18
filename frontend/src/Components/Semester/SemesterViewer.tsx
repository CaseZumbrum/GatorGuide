import React, { useEffect, useImperativeHandle, forwardRef } from 'react';
import { useState } from 'react';
import CourseForm from '../CourseAdder/CourseAdder';
import CourseCard from '../CourseCard/CourseCard';
import CourseList from '../CourseList/CourseList';
import Course from '../../Types/Course';
import Semester from '../../Types/Semester';

interface SemesterProps {
    activeSemester: Semester,
    clearSemester: () => void,
    switchSemester: (index: number) => void,
    removeFromSemester: (course: Course) => void,

}


const SemesterViewer: React.FC<SemesterProps> = ({activeSemester, clearSemester, switchSemester, removeFromSemester}) => {

    return (
      <div>
        <button onClick={clearSemester}> Clear </button>
        <button onClick={() => switchSemester(0)}> Switch to Freshman Fall </button>
        <button onClick={() => switchSemester(1)}> Switch to Freshman Spring </button>
        <button onClick={() => switchSemester(2)}> Switch to Freshman Summer </button>
        <button onClick={() => switchSemester(3)}> Switch to Sophmore Fall </button>
        <button onClick={() => switchSemester(4)}> Switch to Sophmore Spring </button>
        <button onClick={() => switchSemester(5)}> Switch to Sophmore Summer </button>
        <button onClick={() => switchSemester(6)}> Switch to Junior Fall </button>
        <button onClick={() => switchSemester(7)}> Switch to Junior Spring </button>
        <button onClick={() => switchSemester(8)}> Switch to Junior Summer </button>
        <button onClick={() => switchSemester(9)}> Switch to Senior Fall </button>
        <button onClick={() => switchSemester(10)}> Switch to Senior Spring </button>
        <button onClick={() => switchSemester(11)}> Switch to Senior Summer </button>


        <h1>Semester: {activeSemester.name} | Credits: {activeSemester.credits}</h1>
        <div>
          <h2>Course List</h2>
          {activeSemester.courses.map((course, index) => (
            <CourseCard
              key={index}
              course={course}
              inPlan={true}
              problematic={false}
              majorRequirement={false}
              removeFromSemester={removeFromSemester}
            />
          ))}
        </div>
      </div>
    );
  };
  
  export default SemesterViewer;