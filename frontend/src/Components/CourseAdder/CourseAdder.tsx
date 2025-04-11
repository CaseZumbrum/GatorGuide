import React, { useEffect } from 'react';
import { useState } from 'react';
import Tooltip from "../ToolTip/ToolTip.js";
import '../CourseCard/CourseCard';
import Course from '../../Types/Course.js';

interface CourseAdderProps {
    onSubmit: (course: Course) => void;

}

const CourseAdder: React.FC<CourseAdderProps> = ({onSubmit }) => {
  const[courseData, setCourseData] = useState<Course[]>([]);
  const [selectedCourse, setSelectedCourse] = useState<Course | null>(null);
  const [query, setQuery] = useState<string>("");

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
      });
      }
    
    });
  }, []);

  const findCourseByName = (name: string) =>  {
    const course = courseData.find((course) => course.name === name);
    return course
    // if (course) {
    //   setSelectedCourse(course); // Set the found course in state
    //   console.log(course.name);
    //   console.log(selectedCourse ? selectedCourse.description : "");
    //   return (true);
    // } else {
    //   console.log('Course not found');
    //   return (false);
    // }
  };




    
  
    const handleSubmit = (e: React.FormEvent) => {
      e.preventDefault();
      let c: Course | undefined = findCourseByName(query)
      console.log(c)

      if (c) {
        onSubmit(
          c
        );
      }

    };
    
    return (
        <form onSubmit={handleSubmit}>
          <div>
            <label>Course Name:</label>
            <input
              type="text"
              onChange={(e) => (setQuery(e.target.value))}
              required
            />
          </div>
        </form>
    );
};

export default CourseAdder;
