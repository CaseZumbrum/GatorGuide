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

  const colors: string[] = [
    "#025e96",
    "#B63BF5",
    "#F59C27",
    "#0E19F5",
    "#F5200F",
  ];

  useEffect(() => {
    console.log(activePlan);
  }, [activePlan]);

  return (
    <div className="homepage">
      <div className="homepage-message">
        <div className="message-create">Create Your Four-Year-Plan:</div>
      </div>
      <div className="homepage-plans">
        <div
          className="plans-button-default"
          onClick={(e) => {
            setDisplayPopup(true);
          }}
        >
          +
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
                backgroundColor:
                  colors[plan.name.charCodeAt(0) % colors.length],
              }}
            ></div>
            <div className="button-bottom">
              <div className="bottom-name">{plan.name}</div>
              <div className="bottom-major">{plan.major.name}</div>
            </div>
          </div>
        ))}
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
      <div className="homepage-intro">
        <div className="intro-welcome">
          <div className="welcome-title">Who are we?</div>
          <div className="welcome-description">
            <ul>
              <li>GatorGuide is a new tool for creating your UF schedule!</li>
              <li>
                We use the official UF schedule of courses (and UF College of
                Engineering requirements) to help you build out your four year
                plan!
              </li>
            </ul>
          </div>
          <div className="welcome-title">How does it work?</div>
          <div className="welcome-description">
            <ul>
              <li>Gatorguide keeps it's own database of all UF courses</li>
              <li>
                We link together prerequisites, corequisites, major
                requirements, electives, and anything else you might need to
                graduate
              </li>
            </ul>
          </div>
        </div>
      </div>
    </div>
  );
}

export default HomePage;
