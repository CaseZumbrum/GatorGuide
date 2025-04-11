import React, { useEffect, useImperativeHandle, forwardRef } from 'react';
import { useState } from 'react';
import CourseForm from '../CourseAdder/CourseAdder';
import CourseCard from '../CourseCard/CourseCard';
import CourseList from '../CourseList/CourseList';

interface SemesterProps {
    courseAdded: boolean;
}

const Semester: React.FC<SemesterProps> = ({courseAdded}) => {
    const [courses, setCourses] = useState<
        {
        courseName: string;
        courseDescription: string;
        courseCode: string;
        credits: number;
        majorRequirement: boolean;
        }[]
    >([]);

      
    const handleAddCourse = (newCourse: {
        courseName: string;
        courseDescription: string;
        courseCode: string;
        credits: number;
        majorRequirement: boolean;
    }) => {
        setCourses([...courses, newCourse]);
    };

    const addToSemester = () => {
        handleAddCourse({courseName: "Name", courseDescription: "Default", courseCode: "ABC123",credits:  0,  majorRequirement: true})
    };

    return (
      <div>
        <button onClick={addToSemester}> Hi </button>
        <h1>Semester</h1>
        <div>
          <h2>Course List</h2>
          {courses.map((course, index) => (
            <CourseCard
              key={index}
              courseName={course.courseName}
              courseDescription={course.courseDescription}
              courseCode={course.courseCode}
              credits={course.credits}
              majorRequirement={course.majorRequirement}
            />
          ))}
        </div>
      </div>
    );
  };
  
  export default Semester;