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

  useEffect(() => {
    console.log(activePlan);
  }, [activePlan]);

  return (
    <div className="homepage">
      <div>HOME</div>
      <button
        onClick={(e) => {
          setDisplayPopup(true);
        }}
      >
        NEW PLAN
      </button>
      {user.plans.map((plan) => (
        <button
          key={plan.name}
          onClick={(e) => {
            setActivePlan(plan);
            setDisplayPopup(true);
          }}
        >
          {plan.name}
        </button>
      ))}
      {displayPopup && (
        <PlanPopup
          key={activePlan?.name}
          plan={activePlan}
          setPlan={setPlan}
        ></PlanPopup>
      )}
    </div>
  );
}

export default HomePage;
