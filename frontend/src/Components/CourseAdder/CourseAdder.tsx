import React, { useState } from 'react';
import Tooltip from "../ToolTip/ToolTip.js";
import '../CourseCard/CourseCard.tsx';

interface CourseAdderProps {
    onSubmit: (course: {
        courseName: string;
        courseDescription: string;
        courseCode: string;
        credits: number;
        majorRequirement: boolean;
      }) => void;
}

const CourseAdder: React.FC<CourseAdderProps> = ({ onSubmit }) => {
    const [courseName, setCourseName] = useState('');
    const [courseDescription, setCourseDescription] = useState('Default Description');
    const [courseCode, setCourseCode] = useState('ABC123');
    const [credits, setCredits] = useState(-1);
    const [majorRequirement, setMajorRequirement] = useState(false);
  
    const handleSubmit = (e: React.FormEvent) => {
      e.preventDefault();
      onSubmit({
        courseName,
        courseDescription,
        courseCode,
        credits,
        majorRequirement,
      });
      // Reset form fields
      setCourseName('');
      setCourseDescription('Default Description');
      setCourseCode('ABC123');
      setCredits(-1);
      setMajorRequirement(false);
    };

    return (
        <form onSubmit={handleSubmit}>
          <div>
            <label>Course Name:</label>
            <input
              type="text"
              value={courseName}
              onChange={(e) => setCourseName(e.target.value)}
              required
            />
          </div>
        </form>
    );
};

export default CourseAdder;
