import { useEffect, useState } from "react";
import FourYearPlan from "../../Types/FourYearPlan";
import "./PlanPopup.css";
import Major from "../../Types/Major";
import { get_majors } from "../../Logic/Major_Logic";
import { useNavigate } from "react-router-dom";
import Semester from "../../Types/Semester";
import CourseButton from '../CourseButton/CourseButton';
import { BUTTON_VARIANTS } from '../../Constants/enums';

interface props {
  plan?: FourYearPlan;
  setPlan: React.Dispatch<React.SetStateAction<FourYearPlan>>;
}

function PlanPopup({ plan, setPlan }: props) {
  const [name, setName] = useState<string>(plan ? plan.name : "NA");
  const [majorName, setMajorName] = useState<string>(
    plan ? plan.major.name : ""
  );
  const [majors, setMajors] = useState<Major[]>([]);
  const [activeMajor, setActiveMajor] = useState<Major>();

  const navigate = useNavigate();

  let baseSemesters: Semester[] = [
    { courses: [], credits: 0, name: "Freshman Fall" },
    { courses: [], credits: 0, name: "Freshman Spring" },
    { courses: [], credits: 0, name: "Freshman Summer" },
    { courses: [], credits: 0, name: "Sophmore Fall" },
    { courses: [], credits: 0, name: "Sophmore Spring" },
    { courses: [], credits: 0, name: "Sophmore Summer" },
    { courses: [], credits: 0, name: "Junior Fall" },
    { courses: [], credits: 0, name: "Junior Spring" },
    { courses: [], credits: 0, name: "Junior Summer" },
    { courses: [], credits: 0, name: "Senior Fall" },
    { courses: [], credits: 0, name: "Senior Spring" },
    { courses: [], credits: 0, name: "Senior Summer" },
  ];

  useEffect(() => {
    get_majors().then((m) => {
      setMajors(m);
      if (majorName == "") {
        setMajorName(m[0].name);
      }
    });
  }, []);

  useEffect(() => {
    fetch(import.meta.env.VITE_API_HOST + "/majors/" + majorName, {
      credentials: "include",
      method: "GET",
      headers: {
        Accept: "application/json",
        "Content-Type": "application/json",
      },
    }).then((response) => {
      if (response.status == 200) {
        response.json().then((major) => {
          setActiveMajor(major);
          console.log("ACTIVE MAJOR", major);
        });
      }
    });
  }, [majorName]);

  useEffect(() => {
    if (activeMajor) {
      if (plan) {
        setPlan({
          ...plan,
          name: name,
          major: activeMajor,
        });
      } else {
        setPlan({ name: name, major: activeMajor, semesters: baseSemesters });
      }
    }
  }, [activeMajor, name]);

  return (
    <div className="planpopup-wrapper">
      <div className="wrapper-title">Load Plan</div>
      <div className="wrapper-name">
        Name:
        <input
          type="text"
          onChange={(e) => {
            setName(e.target.value);
          }}
          defaultValue={name}
        ></input>
      </div>
      <div className="wrapper-major">
        Major:
        <select
          onChange={(e) => setMajorName(e.target.value)}
          value={majorName}
        >
          {majors.map((m) => (
            <option key={m.name} value={m.name}>
              {m.name}
            </option>
          ))}
        </select>
      </div>
      <div className="wrapper-next" onClick={(e) => navigate("/plan")}>
        <CourseButton variant={BUTTON_VARIANTS.addGroup}>
          Next
        </CourseButton>   
      </div>
    </div>
  );
}

export default PlanPopup;
