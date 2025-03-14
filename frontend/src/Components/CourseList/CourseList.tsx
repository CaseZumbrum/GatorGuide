import React, { useState } from 'react';
import CourseForm from '../CourseAdder/CourseAdder';
import CourseCard from '../CourseCard/CourseCard';

const CourseList: React.FC = () => {
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
        <CourseForm onSubmit={handleAddCourse} />
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
  
  export default CourseList;