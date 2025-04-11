import React, { useEffect } from 'react';
import { useState } from 'react';
import Tooltip from "../ToolTip/ToolTip.js";
import '../CourseCard/CourseCard';

interface CourseAdderProps {
    name: string;
    description: string;
    code: string;
    credits: number;
    onSubmit: (course: {
        courseName: string;
        courseDescription: string;
        courseCode: string;
        credits: number;
        majorRequirement: boolean;
      }) => void;

}

const CourseAdder: React.FC<CourseAdderProps> = ({ onSubmit }) => {
  const[courseData, setCourseData] = useState<CourseAdderProps[]>([]);
  const [selectedCourse, setSelectedCourse] = useState<CourseAdderProps | null>(null);
  

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

  const findCourseByName = (name: string) => {
    const course = courseData.find((course) => course.name === name);
    if (course) {
      setSelectedCourse(course); // Set the found course in state
      setCourseDescription(course.description);
      console.log(course.name);
      console.log(selectedCourse ? selectedCourse.description : "");
      return (true);
    } else {
      console.log('Course not found');
      return (false);
    }
  };

  useEffect(() => {
    if (selectedCourse) {
        setCourseDescription(selectedCourse.description);
        setCourseCode(selectedCourse.code);
        setCredits(selectedCourse.credits);

        console.log("useEffect")
        console.log(selectedCourse.description);
    } else {
        setCourseDescription("Default");
    }
  }, [selectedCourse]);

    const [courseName, setCourseName] = useState('');
    const [courseDescription, setCourseDescription] = useState('A');
    const [courseCode, setCourseCode] = useState('A');
    const [credits, setCredits] = useState(0);
    const [majorRequirement, setMajorRequirement] = useState(false);
    
  
    const handleSubmit = (e: React.FormEvent) => {
      
      e.preventDefault();
      if (findCourseByName(courseName)) {
        onSubmit({
          courseName,
          courseDescription,
          courseCode,
          credits,
          majorRequirement,
        });
      }

    };
    
    return (
        <form onSubmit={handleSubmit}>
          <div>
            <label>Course Name:</label>
            <input
              type="text"
              value={courseName}
              onChange={(e) => (setCourseName(e.target.value), findCourseByName(e.target.value))}
              required
            />
          </div>
        </form>
    );
};

export default CourseAdder;
