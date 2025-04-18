import React, { useEffect, useImperativeHandle, forwardRef } from "react";
import { useState } from "react";
import CourseCard from "../CourseCard/CourseCard";
import CourseList from "../CourseList/CourseList";
import Course from "../../Types/Course";
import Semester from "../../Types/Semester";
import Course_Error from "../../Types/Course_Error";
import CourseButton from '../CourseButton/CourseButton';
import { BUTTON_VARIANTS } from '../../Constants/enums';

interface SemesterProps {
  activeSemester: Semester;
  clearSemester: () => void;
  switchSemester: (index: number) => void;
  removeFromSemester: (course: Course) => void;
  validate: (course: Course) => Course_Error[];
}

const SemesterViewer: React.FC<SemesterProps> = ({
  activeSemester,
  clearSemester,
  switchSemester,
  removeFromSemester,
  validate,
}) => {
  return (
    <div>
      <div className="dropdown">
        <button>Semester</button>
        <div className='content'>
          <button onClick={() => switchSemester(0)}> 0 </button>
        </div>
      </div>
      <button onClick={clearSemester}> Clear </button>
      <button onClick={() => switchSemester(0)}>
        {" "}
        Switch to Freshman Fall{" "}
      </button>
      <button onClick={() => switchSemester(1)}>
        {" "}
        Switch to Freshman Spring{" "}
      </button>
      <button onClick={() => switchSemester(2)}>
        {" "}
        Switch to Freshman Summer{" "}
      </button>
      <button onClick={() => switchSemester(3)}>
        {" "}
        Switch to Sophmore Fall{" "}
      </button>
      <button onClick={() => switchSemester(4)}>
        {" "}
        Switch to Sophmore Spring{" "}
      </button>
      <button onClick={() => switchSemester(5)}>
        {" "}
        Switch to Sophmore Summer{" "}
      </button>
      <button onClick={() => switchSemester(6)}> Switch to Junior Fall </button>
      <button onClick={() => switchSemester(7)}>
        {" "}
        Switch to Junior Spring{" "}
      </button>
      <button onClick={() => switchSemester(8)}>
        {" "}
        Switch to Junior Summer{" "}
      </button>
      <button onClick={() => switchSemester(9)}> Switch to Senior Fall </button>
      <button onClick={() => switchSemester(10)}>
        {" "}
        Switch to Senior Spring{" "}
      </button>
      <button onClick={() => switchSemester(11)}>
        {" "}
        Switch to Senior Summer{" "}
      </button>

      <h1>
        Semester: {activeSemester.name} | Credits: {activeSemester.credits}
      </h1>
      <h2>Course List</h2>
      <div style={{maxHeight: "60vh", overflowY: "hidden"}}>
        <div style={{maxHeight: "60vh", overflowY: "scroll"}}>
          {activeSemester.courses.map((course, index) => (
            <CourseCard
              key={index}
              course={course}
              inPlan={true}
              problematic={false}
              majorRequirement={false}
              removeFromSemester={removeFromSemester}
              validate={validate}
            />
          ))}
        </div>
      </div>
      
    </div>
  );
};

export default SemesterViewer;
