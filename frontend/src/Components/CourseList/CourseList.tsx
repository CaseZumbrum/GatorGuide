import React, { useEffect, useState, useCallback } from 'react';
import CourseAdder from '../CourseAdder/CourseAdder';
import CourseCard from '../CourseCard/CourseCard';
import App from 'C:/Users/Jack/Documents/GitHub/GatorGuide/frontend/src/App';
import Course from '../../Types/Course';

interface CourseListProps {
  addToActiveSemester: (course: Course) => void;
}

const CourseList: React.FC<CourseListProps> = ({addToActiveSemester}) => {
    const [courses, setCourses] = useState<Course[]>([]);
  
    const handleAddCourse = (newCourse: Course) => {
      setCourses([...courses, newCourse]);
    };

    const clearList = () => {
      setCourses(() => (
        []
      ));
    }
  
    return (
      <div>
        <h1>Course Tray</h1>
        <button onClick={clearList}>Clear</button>
        <CourseAdder onSubmit={handleAddCourse}/>
        <div>
          <h2>Course List</h2>
          {courses.map((course, index) => (
            <CourseCard
              key={index}
              course={course}
              addToActiveSemester={addToActiveSemester}
              majorRequirement={false}
              inPlan={false}
              problematic={false}
            />
          ))}
        </div>
      </div>
    );
  };
  

  export default CourseList;