
import React, { useState } from 'react';
import Tooltip from "../ToolTip/ToolTip.js";
import './CourseCard.css';


const CourseCard = () => {
    const [courseCard, setCourseCard] = useState({
        courseName: 'Default Name',
        courseDescription: 'N/A',
        courseCode: 'DEF000',
        credits: 0,
        preReqs: [],
        coReqs: [],
        neededFor: [],
        majorRequirement: false
    });

    return (
    <div className="CourseCard" style={{backgroundColor: courseCard.majorRequirement?"red" : "inherit"}}>

        <div style={{width: "75%", height: "30px"}}>
            <h2 className="CourseCard-Title"> 
                    {courseCard.courseName}                  
            </h2>
        </div>

        <div style={{width: "25%", height: "30px", justifySelf: "flex-end"}}>
            <Tooltip content={courseCard.majorRequirement.toString()}>
                <p className="CourseCard-Requirement">
                    Major Required?
                </p>
            </Tooltip> 
        </div>
        
        <div style={{width: "90%", height: "20%"}}>
            <p className="CourseCard-Text"> 
                {courseCard.courseDescription}
            </p>
        </div>
        <div style={{width: "10%", height: "20%", alignContent: "right"}}>
            <p className="CourseCard-Text"> 
                {courseCard.credits}
            </p>
        </div>

    </div>
    );
}

export default CourseCard