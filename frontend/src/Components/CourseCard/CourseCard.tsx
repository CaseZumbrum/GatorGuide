import React, { useState, useCallback, useEffect } from 'react';
import Tooltip from "../ToolTip/ToolTip";
import Course from "../../Types/Course"
import './CourseCard.css';


interface CourseCardProps {
    course: Course,
    majorRequirement: boolean,
    inPlan: boolean,
    problematic: boolean,
    addToActiveSemester?: (addCourseName: Course) => void;
    removeFromSemester?: (course: Course) => void;
}

const CourseCard: React.FC<CourseCardProps> = ({
    course ={name:"Default Name", description:"N/a", prerequisites: [], code:"NA001", credits:0},
    majorRequirement = false,
    inPlan = false,
    problematic = false,
    addToActiveSemester,
    removeFromSemester}) => {
    const[buttonName, setButtonName] = useState<string>();

    
    useEffect(()=>{
        if (!inPlan) {
            setButtonName("Add Course")
        }
        else {
            setButtonName("Remove Course")
        }
    },[])

    const handleAddToSemester = () => {
        if (!inPlan) {
            addToActiveSemester!(course);
        }
        else if (inPlan) {
            removeFromSemester!(course);
        }
      };

    return (
    <div className="CourseCard" style={{backgroundColor: majorRequirement?"red" : "inherit", borderColor: !inPlan?"green" : "inherit"}}>
        <div style={{display: "flex", alignItems: "center", gap: "2%", maxWidth: "80%", overflow: "wrap"}}>
            <h2 className="CourseCard-Title" style={{flex: 4}}> 
                {course.code}: {course.name}                  
            </h2>
            <p className="CourseCard-Requirement">
                Major Required?
            </p>
            <div style={{flex: 1}}>
                <button onClick={handleAddToSemester} id="addCourse"> {buttonName} </button> 
            </div>
        </div>
        
        <div style={{display: "flex", maxWidth: "80%"}}> 
            <div style={{flex: 7, height: "20%"}}>
                <p className="CourseCard-Text"> 
                    {course.description}
                </p>
            </div>
            <div style={{flex: 3, height: "20%", alignContent: "right"}}>
                <p className="CourseCard-Text" style={{textAlign: "right"}}> 
                    Credits: {course.credits}
                </p>
            </div>
        </div>
        

    </div>
    );
}

export default CourseCard