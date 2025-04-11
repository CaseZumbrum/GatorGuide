import React, { useEffect, useState, useCallback } from 'react';
import CourseAdder from '../CourseAdder/CourseAdder';
import CourseCard from '../CourseCard/CourseCard';
import App from 'C:/Users/Jack/Documents/GitHub/GatorGuide/frontend/src/App';

interface CourseListProps {
  addToSemester: () => void;
}

const CourseList: React.FC<CourseListProps> = ({addToSemester}) => {
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
  
    return (
      <div>
        <h1>Course Tray</h1>
        <CourseAdder onSubmit={handleAddCourse}/>
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
              addToSemester={addToSemester}
            />
          ))}
        </div>
      </div>
    );
  };
  

  export default CourseList;