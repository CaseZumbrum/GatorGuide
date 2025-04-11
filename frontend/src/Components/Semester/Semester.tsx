import React, { useEffect, useImperativeHandle, forwardRef } from 'react';
import { useState } from 'react';
import CourseForm from '../CourseAdder/CourseAdder';
import CourseCard from '../CourseCard/CourseCard';
import CourseList from '../CourseList/CourseList';
import Course from '../../Types/Course';

interface SemesterProps {
    courseAdded: boolean;
    courses: Course[]
}

const Semester: React.FC<SemesterProps> = ({courseAdded, courses}) => {
    // const [courses, setCourses] = useState<
    //     {
    //     courseName: string;
    //     courseDescription: string;
    //     courseCode: string;
    //     credits: number;
    //     majorRequirement: boolean;
    //     }[]
    // >([]);

      
    // const handleAddCourse = (newCourse: {
    //     courseName: string;
    //     courseDescription: string;
    //     courseCode: string;
    //     credits: number;
    //     majorRequirement: boolean;
    // }) => {
    //     setCourses([...courses, newCourse]);
    // };

    // const addToSemester = () => {
    //     handleAddCourse({courseName: "Name", courseDescription: "Default", courseCode: "ABC123",credits:  0,  majorRequirement: true})
    // };

    return (
      <div>
        {/* <button onClick={addToSemester}> Hi </button> */}
        <h1>Semester</h1>
        <div>
          <h2>Course List</h2>
          {courses.map((course, index) => (
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
  
  export default Semester;