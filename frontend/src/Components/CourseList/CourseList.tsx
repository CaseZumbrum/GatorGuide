import React, { useEffect, useState, useCallback } from "react";
import CourseCard from "../CourseCard/CourseCard";
import Course from "../../Types/Course";
import Course_Error from "../../Types/Course_Error";
import Major from "../../Types/Major";

interface CourseListProps {
  addToActiveSemester: (course: Course) => void;
  validate: (course: Course) => Course_Error[];
  major: Major;
}

const CourseList: React.FC<CourseListProps> = ({
  addToActiveSemester,
  validate,
  major,
}) => {
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
      <button
        onClick={(e) => {
          setCourses(major.critical_tracking);
        }}
      >
        PUSH ALL CRITICAL TRACKING
      </button>
      <button
        onClick={(e) => {
          setCourses(major.required);
        }}
      >
        PUSH ALL REQUIRED
      </button>

      {major.groups.map((group) => (
        <button
          key={group.name}
          onClick={(e) => {
            setCourses(group.courses);
          }}
        >
          PUSH ALL {group.name}
        </button>
      ))}

      <button onClick={clearList}>Clear</button>
      <input
        type="text"
        defaultValue={"Search by name or code"}
        onChange={(e) => {
          setQuery(e.target.value);
        }}
      ></input>
      <button onClick={search}>Search</button>
      <h2>Course List</h2>
      <div style={{maxHeight: "60vh", overflowY: "hidden"}}>
        <div style={{maxHeight: "60vh", overflowY: "scroll"}}>
          {courses.map((course, index) => (
            <CourseCard
              key={index}
              course={course}
              addToActiveSemester={addToActiveSemester}
              validate={validate}
              majorRequirement={false}
              inPlan={false}
              problematic={false}
            />
          ))}
        </div>
      </div>
    </div>
  );
};

export default CourseList;
