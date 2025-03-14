import React, { useState } from 'react';
import Tooltip from "../ToolTip/ToolTip";
import './CourseCard.css';


interface CourseCardProps {
    courseName: string,
    courseDescription: string,
    courseCode: string,
    credits: number,
    majorRequirement: boolean
}

const CourseCard: React.FC<CourseCardProps> = ({
    courseName = 'Default Name',
    courseDescription = 'N/a',
    courseCode = "NA001",
    credits = 0,
    majorRequirement = false }) => {

    return (
    <div className="CourseCard" style={{backgroundColor: majorRequirement?"red" : "inherit"}}>
        <div style={{display: "flex", alignItems: "center", gap: "2%", maxWidth: "80%", overflow: "wrap"}}>
            <h2 className="CourseCard-Title" style={{flex: 4}}> 
                {courseCode}: {courseName}                  
            </h2>
            <p className="CourseCard-Requirement">
                Major Required?
            </p>
            <div style={{flex: 1}}>
                <button>Add Course</button> 
            </div>
        </div>
        
        <div style={{display: "flex", maxWidth: "80%"}}> 
            <div style={{flex: 7, height: "20%"}}>
                <p className="CourseCard-Text"> 
                    {courseDescription}
                </p>
            </div>
            <div style={{flex: 3, height: "20%", alignContent: "right"}}>
                <p className="CourseCard-Text" style={{textAlign: "right"}}> 
                    Credits: {credits}
                </p>
            </div>
        </div>
        

    </div>
    );
}

export default CourseCard