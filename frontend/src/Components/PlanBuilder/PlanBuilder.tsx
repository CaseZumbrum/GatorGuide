import React, { act, useEffect } from "react";
import { useRef, useState } from "react";
import logo from "./logo.svg";
import CourseCard from "../CourseCard/CourseCard";
import Tooltip from "../ToolTip/ToolTip";
import CourseList from "../CourseList/CourseList";
import CourseAdder from "../CourseAdder/CourseAdder";
import SemesterViewer from "../Semester/SemesterViewer";
import Course from "../../Types/Course";
import Semester from "../../Types/Semester";
import FourYearPlan from "../../Types/FourYearPlan";
import { get_majors } from "../../Logic/Major_Logic";
import Major from "../../Types/Major";
import { validate_course } from "../../Logic/Course_Logic";
import Course_Error from "../../Types/Course_Error";
import { validate_plan } from "../../Logic/Major_Logic";

function PlanBuilder() {
  let baseSemesters: Semester[] = [
    { courses: [], credits: 0, name: "Freshman Fall" },
    { courses: [], credits: 0, name: "Freshman Spring" },
    { courses: [], credits: 0, name: "Freshman Summer" },
    { courses: [], credits: 0, name: "Sophmore Fall" },
    { courses: [], credits: 0, name: "Sophmore Spring" },
    { courses: [], credits: 0, name: "Sophmore Summer" },
    { courses: [], credits: 0, name: "Junior Fall" },
    { courses: [], credits: 0, name: "Junior Spring" },
    { courses: [], credits: 0, name: "Junior Summer" },
    { courses: [], credits: 0, name: "Senior Fall" },
    { courses: [], credits: 0, name: "Senior Spring" },
    { courses: [], credits: 0, name: "Senior Summer" },
  ];

  const [supportedMajors, setSupportedMajors] = useState<Major[]>([]);
  const [activeSemester, setActiveSemester] = useState<Semester>({
    courses: [],
    credits: 0,
    name: baseSemesters[0].name,
  });
  const [activeSemesterIndex, setActiveSemesterIndex] = useState<number>(0);
  const [activeFourYearPlan, setActiveFourYearPlan] = useState<FourYearPlan>({
    name: "default",
    semesters: baseSemesters,
    major: {
      name: "Loading...",
      critical_tracking: [],
      required: [],
      groups: [],
    },
  });

  const addCourseToSemester = (
    newCourse: Course,
    setErrors: React.Dispatch<React.SetStateAction<Course_Error[]>>
  ) => {
    let valid: boolean = true;

    activeSemester.courses.forEach((e) => {
      if (e == newCourse) {
        valid = false;
        alert("Already in Plan");
      }
    });

    if (valid) {
      setActiveSemester((prevState) => ({
        courses: [...prevState.courses, newCourse],
        credits: prevState.credits + newCourse.credits,
        name: prevState.name,
      }));
      let errors: Course_Error[] = validate_course(
        newCourse,
        activeFourYearPlan.semesters
      );
      setErrors(errors);
      if (errors.length > 0) {
        for (const error of errors) {
          alert(error.msg);
        }
      }
    } else {
    }
  };

  const removeFromSemester = (course: Course) => {
    let newCourseList = activeSemester.courses.filter((e) => e !== course);
    setActiveSemester((prevState) => ({
      courses: newCourseList,
      credits: prevState.credits - course.credits,
      name: prevState.name,
    }));
    activeFourYearPlan.semesters[activeSemesterIndex].courses = newCourseList;

    activeFourYearPlan.semesters[activeSemesterIndex].credits -= course.credits;
  };

  const clearSemester = () => {
    setActiveSemester(() => ({
      courses: [],
      credits: 0,
      name: activeSemester.name,
    }));
    activeFourYearPlan.semesters[activeSemesterIndex] = {
      courses: [],
      credits: 0,
      name: activeFourYearPlan.semesters[activeSemesterIndex].name,
    };
  };

  const switchSemester = (index: number) => {
    setActiveSemester(activeFourYearPlan.semesters[index]);
    setActiveSemesterIndex(index);
  };

  useEffect(() => {
    get_majors().then((majors: Major[]) => {
      setSupportedMajors(majors);
    });
  }, []);

  useEffect(() => {
    console.log("MAJORS", supportedMajors);
    if (supportedMajors.length > 0) {
      setActiveFourYearPlan((prevState) => ({
        ...prevState,
        major: supportedMajors[0],
      }));
    }
  }, [supportedMajors]);

  useEffect(() => {
    console.log("ACTIVE", activeSemester);
    const nextSemesters = activeFourYearPlan.semesters.map((c, i) => {
      if (i === activeSemesterIndex) {
        // Increment the clicked counter
        return activeSemester;
      } else {
        // The rest haven't changed
        return c;
      }
    });
    setActiveFourYearPlan((prevstate) => ({
      ...prevstate,
      semesters: nextSemesters,
    }));
  }, [activeSemester, activeSemesterIndex]);

  useEffect(() => {
    console.log("PLAN", activeFourYearPlan);
  }, [activeFourYearPlan]);

  const save = () => {
    fetch(import.meta.env.VITE_API_HOST + "/users/me/plan", {
      credentials: "include",
      method: "POST",
      body: JSON.stringify(activeFourYearPlan),
      headers: {
        Accept: "application/json",
        "Content-Type": "application/json",
      },
    }).then((response) => {
      if (response.status != 200) {
        alert("Issue with saving plan");
        response.json().then((data) => {
          console.log(data);
        });
      }
    });
  };

  return (
    <>
      <div
        style={{
          width: "100vw",
          height: "10vh",
          backgroundColor: "hsl(212, 65.70%, 27.50%)",
          display: "inline-flex",
        }}
      >
        <h1>{"Major: " + activeFourYearPlan.major.name}</h1>
        <button onClick={save}>SAVE</button>
      </div>
      <div
        style={{
          width: "25vw",
          minHeight: "90vh",
          backgroundColor: "hsl(212, 32%, 92%)",
          display: "inline-flex",
        }}
      >
        <CourseList addToActiveSemester={addCourseToSemester}></CourseList>
      </div>
      <div
        style={{
          width: "70vw",
          minHeight: "90vh",
          backgroundColor: "hsl(286, 18.90%, 41.60%)",
          display: "inline-flex",
        }}
      >
        <SemesterViewer
          activeSemester={activeFourYearPlan.semesters[activeSemesterIndex]}
          clearSemester={clearSemester}
          switchSemester={switchSemester}
          removeFromSemester={removeFromSemester}
        ></SemesterViewer>
      </div>
    </>
  );
}

export default PlanBuilder;
