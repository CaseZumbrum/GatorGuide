import React, { useEffect, useState, useCallback } from "react";
import CourseAdder from "../CourseAdder/CourseAdder";
import CourseCard from "../CourseCard/CourseCard";
import App from "C:/Users/Jack/Documents/GitHub/GatorGuide/frontend/src/App";
import Course from "../../Types/Course";
import Course_Error from "../../Types/Course_Error";

interface CourseListProps {
  addToActiveSemester: (
    course: Course,
    setErrors: React.Dispatch<React.SetStateAction<Course_Error[]>>
  ) => void;
}

const CourseList: React.FC<CourseListProps> = ({ addToActiveSemester }) => {
  const [courses, setCourses] = useState<Course[]>([]);
  const [query, setQuery] = useState<string>("");
  const handleAddCourse = (newCourse: Course) => {
    setCourses([...courses, newCourse]);
  };

  const clearList = () => {
    setCourses(() => []);
  };

  const search = () => {
    fetch(
      import.meta.env.VITE_API_HOST +
        "/courses/search?query=" +
        query +
        "&limit=10",
      {
        credentials: "include",
        method: "GET",
        headers: {
          Accept: "application/json",
          "Content-Type": "application/json",
        },
      }
    ).then((response) => {
      if (response.status == 200) {
        response.json().then((courses) => {
          setCourses(courses);
        });
      }
    });
  };

  return (
    <div>
      <h1>Course Tray</h1>
      <button onClick={clearList}>Clear</button>
      <input
        type="text"
        defaultValue={"Search by name or code"}
        onChange={(e) => {
          setQuery(e.target.value);
        }}
      ></input>
      <button onClick={search}>Search</button>
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
