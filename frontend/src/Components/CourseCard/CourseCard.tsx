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
    if (errors.length != 0) {
      console.log(course.name, "ERRORS", errors);
      obj =JSON.parse(JSON.stringify(errors));
      console.log(obj[0].msg);
      if (visibleErrors) {
        console.log(visibleErrors[0].msg);
      }
    }
  }, [errors]);

  const handleAddToSemester = () => {
    if (!inPlan) {
      addToActiveSemester!(course);
    } else if (inPlan) {
      removeFromSemester!(course);
    }
  };

  return (
    <div style={{display:"flex", flexDirection:"row", flexWrap:"wrap", alignItems:"flex-start"}}>
      <div className="container">
        <div className="box" id="TitleBox"> {course.code}: {course.name} </div>
        <div className="box" id="CreditsBox">Credits: {course.credits}</div>
        <div className="box" id="DescriptionBox">{course.description}</div>
        <div className="box" id="ButtonBox">
          <div onClick={handleAddToSemester} id="addCourse">
            <CourseButton variant={buttonType} size={BUTTON_SIZES.Small}>{buttonName}</CourseButton>
          </div>
        </div>
      </div>
      <div style={{marginTop:"1rem"}}>{errors.length != 0 && <div className="box" id="ErrorBox"> Errors: 
        { errors.map( item => <div>{item.msg}</div>)}
        </div>}</div>
    </div>
    
    
  );

  // return (
  //   <div
  //     className="CourseCard"
  //     style={{
  //       backgroundColor: inPlan && errors.length == 0 ? "red" : "inherit",
  //       borderColor: !inPlan ? "green" : "inherit",
  //     }}
  //   >
  //     <div
  //       style={{
  //         display: "flex",
  //         alignItems: "center",
  //         gap: "2%",
  //         maxWidth: "80%",
  //         overflow: "wrap",
  //       }}
  //     >
  //       <h2 className="CourseCard-Title" style={{ flex: 4 }}>
  //         {course.code}: {course.name}
  //       </h2>
  //       <p className="CourseCard-Requirement">Major Required?</p>
  //       <div style={{ flex: 1 }}>
  //         <div onClick={handleAddToSemester} id="addCourse">
  //           <CourseButton variant={buttonType} size={BUTTON_SIZES.Small}>{buttonName}</CourseButton>
  //         </div>
  //       </div>
  //     </div>

  //     <div style={{ display: "flex", maxWidth: "80%" }}>
  //       <div style={{ flex: 7, height: "20%" }}>
  //         <p className="CourseCard-Text">{course.description}</p>
  //       </div>
  //       <div style={{ flex: 3, height: "20%", alignContent: "right" }}>
  //         <p className="CourseCard-Text" style={{ textAlign: "right" }}>
  //           Credits: {course.credits}
  //         </p>
  //       </div>
  //     </div>
  //   </div>
  // );
};

export default CourseCard;
