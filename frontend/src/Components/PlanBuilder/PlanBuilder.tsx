import React, { useEffect } from "react";
import { useState } from "react";
import CourseList from "../CourseList/CourseList";
import SemesterViewer from "../Semester/SemesterViewer";
import Course from "../../Types/Course";
import Semester from "../../Types/Semester";
import FourYearPlan from "../../Types/FourYearPlan";
import { validate_course } from "../../Logic/Course_Logic";
import Course_Error from "../../Types/Course_Error";
import Major_Error from "../../Types/Major_Error";
import { validate_plan } from "../../Logic/Major_Logic";

interface props {
  plan: FourYearPlan;
}

function PlanBuilder({ plan }: props) {
  const [activeSemester, setActiveSemester] = useState<Semester>(
    plan.semesters[0]
  );
  const [activeSemesterIndex, setActiveSemesterIndex] = useState<number>(0);
  const [fourYearPlan, setActiveFourYearPlan] = useState<FourYearPlan>(plan);
  const [majorErrors, setMajorErrors] = useState<Major_Error[]>([]);

  const validate = (course: Course): Course_Error[] => {
    return validate_course(course, fourYearPlan.semesters);
  };

  const addCourseToSemester = (newCourse: Course) => {
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
    }
  };

  const removeFromSemester = (course: Course) => {
    let newCourseList = activeSemester.courses.filter((e) => e !== course);
    setActiveSemester((prevState) => ({
      courses: newCourseList,
      credits: prevState.credits - course.credits,
      name: prevState.name,
    }));
    fourYearPlan.semesters[activeSemesterIndex].courses = newCourseList;

    fourYearPlan.semesters[activeSemesterIndex].credits -= course.credits;
  };

  const clearSemester = () => {
    setActiveSemester(() => ({
      courses: [],
      credits: 0,
      name: activeSemester.name,
    }));
    fourYearPlan.semesters[activeSemesterIndex] = {
      courses: [],
      credits: 0,
      name: fourYearPlan.semesters[activeSemesterIndex].name,
    };
  };

  const switchSemester = (index: number) => {
    setActiveSemester(fourYearPlan.semesters[index]);
    setActiveSemesterIndex(index);
  };

  useEffect(() => {
    console.log("ACTIVE", activeSemester);
    const nextSemesters = fourYearPlan.semesters.map((c, i) => {
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
    console.log("PLAN", fourYearPlan);
    setMajorErrors(validate_plan(fourYearPlan));
  }, [fourYearPlan]);

  const save = () => {
    fetch(import.meta.env.VITE_API_HOST + "/users/me/plan", {
      credentials: "include",
      method: "POST",
      body: JSON.stringify(fourYearPlan),
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
    <div>
      <div
        style={{
          width: "100vw",
          height: "10vh",
          backgroundColor: "hsl(212, 65.70%, 27.50%)",
          display: "inline-flex",
        }}
      >
        <h1>{"Major: " + fourYearPlan.major.name}</h1>
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
        <CourseList
          addToActiveSemester={addCourseToSemester}
          validate={validate}
          major={fourYearPlan.major}
        ></CourseList>
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
          activeSemester={fourYearPlan.semesters[activeSemesterIndex]}
          clearSemester={clearSemester}
          switchSemester={switchSemester}
          removeFromSemester={removeFromSemester}
          validate={validate}
        ></SemesterViewer>
      </div>
      <div>MAJOR ERRORS {JSON.stringify(majorErrors)}</div>
    </div>
  );
}

export default PlanBuilder;
