import React, { useEffect, useState, useCallback } from "react";
import CourseCard from "../CourseCard/CourseCard";
import Course from "../../Types/Course";
import Course_Error from "../../Types/Course_Error";
import Major from "../../Types/Major";
import CourseButton from '../CourseButton/CourseButton';
import { BUTTON_SIZES, BUTTON_VARIANTS } from '../../Constants/enums';

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
    <div style={{width: "30vw", alignContent:"space-between"}}>
      <div style={{width: "30vw", alignContent:"space-between", display:"flex", flexWrap:"wrap"}}>
        <div onClick={(e) => {
            setCourses(major.critical_tracking);
          }} style={{margin:"0px", padding:"0px", width:"fit-content"}}>
          <CourseButton
          variant={BUTTON_VARIANTS.addGroup}
        >
          Add Critical Tracking
        </CourseButton></div>
        
        <div onClick={(e) => {
            setCourses(major.required);
          }} style={{margin:"0px", padding:"0px", width:"fit-content"}}>
            <CourseButton
          variant={BUTTON_VARIANTS.addGroup}
          
        >
          Add Required Courses
        </CourseButton>
        </div>
        

        {major.groups.map((group) => (
          <div onClick={(e) => {
            setCourses(group.courses);
          }} style={{margin:"0px", padding:"0px", width:"fit-content"}}>
            <CourseButton
              variant={BUTTON_VARIANTS.addGroup}
              key={group.name}
            >
              Add: {group.name}
            </CourseButton>
          </div>
          
        ))}
      </div>
      
      {/* <CourseButton variant={BUTTON_VARIANTS.clear} size={BUTTON_SIZES.Thin} onClick={clearList}>Clear</CourseButton> */}
      <h2 style={{marginLeft: "1rem"}}>Course List</h2>
      <input
        style={{marginLeft: "1rem"}}
        type="text"
        defaultValue={"Search by name or code"}
        onChange={(e) => {
          setQuery(e.target.value);
        }
      }
      ></input>
      <button onClick={search}>Search</button>
      <div style={{maxHeight: "60vh", overflowY: "hidden"}}>
        <div style={{maxHeight: "60vh", overflowY: "scroll"}} className="list" id="scrollList">
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
