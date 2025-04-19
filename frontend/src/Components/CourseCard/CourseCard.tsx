import React, { useState, useCallback, useEffect } from "react";
import Tooltip from "../ToolTip/ToolTip";
import Course from "../../Types/Course";
import "./CourseCard.css";
import Course_Error from "../../Types/Course_Error";
import CourseButton from "../CourseButton/CourseButton";
import { BUTTON_SIZES, BUTTON_VARIANTS } from "../../Constants/enums";

interface CourseCardProps {
  course: Course;
  majorRequirement: boolean;
  inPlan: boolean;
  problematic: boolean;
  addToActiveSemester?: (addCourseName: Course) => void;
  removeFromSemester?: (course: Course) => void;
  validate: (course: Course) => Course_Error[];
}

const CourseCard: React.FC<CourseCardProps> = ({
  course = {
    name: "Default Name",
    description: "N/a",
    prerequisites: [],
    code: "NA001",
    credits: 0,
  },
  majorRequirement = false,
  inPlan = false,
  problematic = false,
  addToActiveSemester,
  removeFromSemester,
  validate,
}) => {
  const [buttonName, setButtonName] = useState<string>();
  const [buttonType, setbuttonType] = useState<BUTTON_VARIANTS>();

  const [visibleErrors, setVisibleErrors] = useState<Course_Error[]>();
  const [errors, setErrors] = useState<Course_Error[]>([]);
  let obj: Course_Error[] = [];

  useEffect(() => {
    // on load, set button and validate the course
    if (!inPlan) {
      setButtonName("Add Course");
      setbuttonType(BUTTON_VARIANTS.addCoruse);
    } else {
      setButtonName("Remove Course");
      setbuttonType(BUTTON_VARIANTS.removeCourse);
      setErrors(validate(course));
    }
  }, []);

  useEffect(() => {
    // display errors after validation
    if (errors.length != 0) {
      console.log(course.name, "ERRORS", errors);
      obj = JSON.parse(JSON.stringify(errors));
      console.log(obj[0].msg);
      if (visibleErrors) {
        console.log(visibleErrors[0].msg);
      }
    }
  }, [errors]);

  const handleAddToSemester = () => {
    // if the course is not in the plan already, add it too it
    if (!inPlan) {
      addToActiveSemester!(course);
    }
    // of the course is in the plan, remove it
    else if (inPlan) {
      removeFromSemester!(course);
    }
  };

  const resolveError = () => {
    // hide errors
    setErrors([]);
  };

  return (
    <div
      style={{
        display: "flex",
        flexDirection: "row",
        flexWrap: "wrap",
        alignItems: "flex-start",
      }}
    >
      <div className="container">
        <div className="box" id="TitleBox">
          {" "}
          {course.code}: {course.name}{" "}
        </div>
        <div className="box" id="CreditsBox">
          Credits: {course.credits}
        </div>
        <div className="box" id="DescriptionBox">
          {course.description}
        </div>
        <div className="box" id="ButtonBox">
          <div onClick={handleAddToSemester} id="addCourse">
            <CourseButton variant={buttonType} size={BUTTON_SIZES.Small}>
              {buttonName}
            </CourseButton>
          </div>
        </div>
      </div>
      <div style={{ marginTop: "1rem" }}>
        {errors.length != 0 && (
          <div
            className="box"
            id="ErrorBox"
            style={{ display: "flex", flex: "row", flexWrap: "wrap" }}
          >
            Problems:
            <div className="close-x-error" onClick={resolveError}>
              &#10006;
            </div>
            {errors.map((item) => (
              <div>{item.msg}</div>
            ))}
          </div>
        )}
      </div>
    </div>
  );
};

export default CourseCard;
