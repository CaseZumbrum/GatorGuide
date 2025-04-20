import React, { useEffect, useImperativeHandle, forwardRef } from "react";
import { useState } from "react";
import CourseCard from "../CourseCard/CourseCard";
import CourseList from "../CourseList/CourseList";
import Course from "../../Types/Course";
import Semester from "../../Types/Semester";
import Course_Error from "../../Types/Course_Error";
import CourseButton from "../CourseButton/CourseButton";
import { BUTTON_SIZES, BUTTON_VARIANTS } from "../../Constants/enums";
import "./Semester.css";

interface SemesterProps {
  activeSemester: Semester;
  index: number;
  clearSemester: () => void;
  switchSemester: (index: number) => void;
  removeFromSemester: (course: Course) => void;
  validate: (course: Course) => Course_Error[];
}

const SemesterViewer: React.FC<SemesterProps> = ({
  activeSemester,
  index,
  clearSemester,
  switchSemester,
  removeFromSemester,
  validate,
}) => {
  return (
    <div className="semesterContainer">
      <div className="semesterHeader">
        <h1>Semester: {index + 1} |</h1>
        {/* Semester dropdown to select the active semester */}
        <div className="dropdown">
          <CourseButton size={BUTTON_SIZES.Large}>Semester</CourseButton>
          <div className="content">
            <button onClick={() => switchSemester(0)}> 1 </button>
            <button onClick={() => switchSemester(1)}> 2 </button>
            <button onClick={() => switchSemester(2)}> 3 </button>
            <button onClick={() => switchSemester(3)}> 4 </button>
            <button onClick={() => switchSemester(4)}> 5 </button>
            <button onClick={() => switchSemester(5)}> 6 </button>
            <button onClick={() => switchSemester(6)}> 7 </button>
            <button onClick={() => switchSemester(7)}> 8 </button>
            <button onClick={() => switchSemester(8)}> 9 </button>
            <button onClick={() => switchSemester(9)}> 10 </button>
            <button onClick={() => switchSemester(10)}> 11 </button>
            <button onClick={() => switchSemester(11)}> 12 </button>
          </div>
        </div>
        {/* Remove all courses from the semester */}
        <div onClick={clearSemester}>
          <CourseButton
            variant={BUTTON_VARIANTS.clear}
            size={BUTTON_SIZES.Large}
          >
            {" "}
            Clear{" "}
          </CourseButton>
        </div>
      </div>

      <div
        style={{
          width: "55vw",
          height: "5vh",
          alignContent: "flex-start",
          verticalAlign: "top",
          marginBottom: "15px",
        }}
      >
        <h2 style={{ marginBottom: "5px" }}>Course List</h2>
      </div>

      <div style={{ overflowY: "hidden" }}>
        <div
          className="semesterList"
          id="semesterScrollList"
          style={{ maxHeight: "66vh" }}
        >
          <div style={{ maxHeight: "66vh", width: "55vw" }}>
            {activeSemester.courses.map((course, index) => (
              <CourseCard
                key={index}
                course={course}
                inPlan={true}
                problematic={false}
                majorRequirement={false}
                removeFromSemester={removeFromSemester}
                validate={validate}
              />
            ))}
          </div>
        </div>
      </div>
    </div>
  );
};

export default SemesterViewer;
