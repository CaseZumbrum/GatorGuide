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
import { course_in_semesters, validate_plan } from "../../Logic/Major_Logic";
import CourseButton from "../CourseButton/CourseButton";
import { BUTTON_VARIANTS } from "../../Constants/enums";
import "./PlanBuilder.css";

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

    // ensure the course is not in the plan
    activeSemester.courses.forEach((e) => {
      if (e == newCourse) {
        valid = false;
        alert("Already in Plan");
      }
    });

    // update the current semester
    if (valid) {
      setActiveSemester((prevState) => ({
        courses: [...prevState.courses, newCourse],
        credits: prevState.credits + newCourse.credits,
        name: prevState.name,
      }));
    }
  };

  const removeFromSemester = (course: Course) => {
    // remove the course from the semester
    let newCourseList = activeSemester.courses.filter((e) => e !== course);
    setActiveSemester((prevState) => ({
      courses: newCourseList,
      credits: prevState.credits - course.credits,
      name: prevState.name,
    }));
    fourYearPlan.semesters[activeSemesterIndex].courses = newCourseList;
  };

  const clearSemester = () => {
    // delete all courses from the current semester
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
    // move the index
    setActiveSemester(fourYearPlan.semesters[index]);
    setActiveSemesterIndex(index);
    // validate courses
    for (let i = 0; i < fourYearPlan.semesters[index].courses.length; i++) {
      validate(fourYearPlan.semesters[index].courses[i]);
    }
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

  // validate the major on each change to the plan
  useEffect(() => {
    console.log("PLAN", fourYearPlan);
    setMajorErrors(validate_plan(fourYearPlan));
  }, [fourYearPlan]);

  const save = () => {
    // save the plan, send it off to the database
    fetch(import.meta.env.VITE_API_HOST + "/users/me/plan", {
      credentials: "include",
      method: "POST",
      body: JSON.stringify(fourYearPlan),
      headers: {
        Accept: "application/json",
        "Content-Type": "application/json",
      },
    }).then((response) => {
      // fail
      if (response.status != 200) {
        alert("Issue with saving plan");
        response.json().then((data) => {
          console.log(data);
        });
      }
      // success
      else {
        alert("Saved Plan");
      }
    });
  };

  return (
    <div className="planbuilder-wrapper">
      <div className="wrapper-header">
        <h1 style={{ color: "#ffffff", flex: "flex", width: "50vw" }}>
          {"Major: " + fourYearPlan.major.name}
        </h1>
        <div onClick={save} style={{ alignSelf: "center" }}>
          <CourseButton variant={BUTTON_VARIANTS.savePlan}>Save</CourseButton>
        </div>
      </div>
      <div
        className="wrapper-list"
        style={{
          width: "26vw",
          minHeight: "90vh",
          maxHeight: "100%",
          backgroundColor: "hsl(237, 100.00%, 98.30%)",
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
        className="wrapper-viewer"
        style={{
          width: "60vw",
          minHeight: "90vh",
          backgroundColor: "hsl(237, 100.00%, 98.30%)",
          display: "inline-flex",
        }}
      >
        <SemesterViewer
          activeSemester={fourYearPlan.semesters[activeSemesterIndex]}
          index={activeSemesterIndex}
          clearSemester={clearSemester}
          switchSemester={switchSemester}
          removeFromSemester={removeFromSemester}
          validate={validate}
        ></SemesterViewer>
      </div>
      <div
        className="wrapper-errors"
        style={{
          width: "8vw",
          minHeight: "90vh",
          backgroundColor: "hsl(237, 100.00%, 98.30%)",
          display: "inline-flex",
        }}
      >
        <div style={{ marginTop: "1rem" }}>
          {majorErrors.length != 0 && (
            <div className="box" id="MajorErrorBox">
              {" "}
              Flaws with Plan:
              {majorErrors.map((item) => (
                <div
                  style={{
                    fontSize: "1rem",
                    display: "flex",
                    flexWrap: "wrap",
                  }}
                >
                  <p>{item.msg}</p>
                </div>
              ))}
            </div>
          )}
        </div>
      </div>
    </div>
  );
}

export default PlanBuilder;
