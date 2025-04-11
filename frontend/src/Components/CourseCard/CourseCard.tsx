import React, { useState, useCallback } from 'react';
import Tooltip from "../ToolTip/ToolTip";
import Course from "../../Types/Course"
import './CourseCard.css';


interface CourseCardProps {
    course: Course,
    majorRequirement: boolean,
    inPlan: boolean,
    problematic: boolean,
    addToSemester?: (addCourseName: Course) => void;
}

const CourseCard: React.FC<CourseCardProps> = ({
    course ={name:"Default Name", description:"N/a", code:"NA001", credits:0},
    majorRequirement = false,
    inPlan = false,
    problematic = false,
    addToSemester}) => {

    const addCourse = () => {
        inPlan = !inPlan;
        console.log(inPlan);
    }

    const handleAddToSemester = () => {
        addToSemester(course);
      };

    return (
    <div className="CourseCard" style={{backgroundColor: majorRequirement?"red" : "inherit"}}>
        <div style={{display: "flex", alignItems: "center", gap: "2%", maxWidth: "80%", overflow: "wrap"}}>
            <h2 className="CourseCard-Title" style={{flex: 4}}> 
                {course.code}: {course.name}                  
            </h2>
            <p className="CourseCard-Requirement">
                Major Required?
            </p>
            <div style={{flex: 1}}>
                <button onClick={handleAddToSemester} id="addCourse">Add Course</button> 
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