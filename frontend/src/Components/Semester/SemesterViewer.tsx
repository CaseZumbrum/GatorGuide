import React, { useEffect, useImperativeHandle, forwardRef } from 'react';
import { useState } from 'react';
import CourseForm from '../CourseAdder/CourseAdder';
import CourseCard from '../CourseCard/CourseCard';
import CourseList from '../CourseList/CourseList';
import Course from '../../Types/Course';
import Semester from '../../Types/Semester';

interface SemesterProps {
    activeSemester: Semester,
    clearSemester: () => void
}

const SemesterViewer: React.FC<SemesterProps> = ({activeSemester, clearSemester}) => {

    return (
      <div>
        <button onClick={clearSemester}> Clear </button>
        <h1>Semester | Credits: {activeSemester.credits}</h1>
        <div>
          <h2>Course List</h2>
          {activeSemester.courses.map((course, index) => (
            <CourseCard
              key={index}
              course={course}
              inPlan={true}
              problematic={false}
              majorRequirement={false}
            />
          ))}
        </div>
      </div>
    );
  };
  
  export default SemesterViewer;