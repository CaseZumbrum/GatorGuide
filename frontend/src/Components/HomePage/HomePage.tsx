import React, { act, useEffect, useState } from "react";
import "./HomePage.css";
import User from "../../Types/User";
import FourYearPlan from "../../Types/FourYearPlan";
import PlanPopup from "../PlanPopup/PlanPopup";

interface props {
  user: User;
  setPlan: React.Dispatch<React.SetStateAction<FourYearPlan>>;
}
function HomePage({ user, setPlan }: props) {
  const [activePlan, setActivePlan] = useState<FourYearPlan>();
  const [displayPopup, setDisplayPopup] = useState<boolean>(false);
  const [image, setImage] = useState<string>("../../../dist/CenturyTower.jpg");
  const [randomNumber, setRandomNumber] = useState<number>();
  
  const images: string[] = [
    "../../../dist/CenturyTower.jpg",
    "../../../dist/Football.jpg",
    "../../../dist/Marston.jpg",
    "../../../dist/Albert&Alberta.jpg",
    "../../../dist/WorldGator.jpg",
    "../../../dist/Potato.jpg",
    "../../../dist/BatHouse.jpg",
    "../../../dist/OldGuy.jpg",
    "../../../dist/FireWorks.jpg",
    "../../../dist/FinanceArch.jpg",
  ];

  useEffect(() => {
    console.log(activePlan);
  }, [activePlan]);

  return (
    <div className="homepage" style={{width: "100%", height:"75%"}}>
      <div className="homepage-plans" style={{overflowY:"scroll", width: "100%", height:"100%"}}>
        <div
            className="plans-button-default"
            style={{display:"flex", flexWrap:"wrap"}}
            onClick={(e) => {
              setDisplayPopup(true);
            }}
          >
            <div
              className="button-top-default"
            >+</div>
            <div className="button-bottom">
              <div className="bottom-name"> Create New Plan </div>
            </div>
          </div>

        {user.plans.map((plan) => (
          <div
            key={plan.name}
            className="plans-button"
            onClick={(e) => {
              setActivePlan(plan);
              setDisplayPopup(true);
            }}
          >
            <div
              className="button-top"
              style={{
                backgroundImage: `url(${images[plan.name.charCodeAt(0) % images.length]})`}}
            ></div>
            <div className="button-bottom">
              <div className="bottom-name">{plan.name}</div>
              <div className="bottom-major">{plan.major.name}</div>
            </div>
          </div>
        ))}
      </div>


        <div className="homepage-intro">
        <div style={{height:"2vh"}}></div>
        <div className="intro-welcome">
          <div className="welcome-title">Who are we?</div>
          <div className="welcome-description">
            <ul>
              <p style={{width: "80%", rowGap: "3px"}}>GatorGuide is a new tool for creating your UF schedule! We use the official UF schedule of courses (and UF College of
                Engineering requirements) to help you build out your four year
                plan. Simply select your major and the semester you want to lay out and add the courses you want and need, then save 
                your progress and refer back to it as needed. Our goal is for this to be a useful tool when planning your academic career at UF and make lif just a little bit easier.
              </p>
            </ul>
          </div>
          <div className="welcome-title">How does it work?</div>
          <div className="welcome-description">
            <ul>
              <p style={{width: "80%", rowGap: "3px"}}>Gatorguide keeps it's own database of all UF courses drawn from the UF course API.
                 We link together prerequisites, corequisites, major
                requirements, electives, and anything else you might need to
                graduate. You can search for a particular course by either the course name or code or simply use a shortcut
                for required categories of courses.
              </p>

              <p style={{width: "80%", rowGap: "3px"}}> It is important to note that while we flag any issues with your schedule we detect, we do not stop you
              from adding any courses to your Four-Year-Plan. Additionally, not all issues may be detected such as whether a class is 
              offered during a particular semester.
              </p>
              
            </ul>
          </div>
        </div>
      </div>
      {displayPopup && (
        <div className="homepage-popupwrapper">
          <div className="homepage-popup">
            <div className="popup-close">
              <div
                className="close-x"
                onClick={(e) => {
                  setActivePlan(undefined);
                  setDisplayPopup(false);
                }}
              >
                &#10006;
              </div>
            </div>
            <PlanPopup
              key={activePlan?.name}
              plan={activePlan}
              setPlan={setPlan}
            ></PlanPopup>
          </div>
        </div>
      )}
    </div>
  );
}

export default HomePage;
