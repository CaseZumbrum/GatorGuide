import React, { act, useEffect } from "react";
import { useRef, useState } from "react";
import "./App.css";
import PlanBuilder from "./Components/PlanBuilder/PlanBuilder";
import { Route, Routes, Link } from "react-router-dom";
import LoginPage from "./Components/LoginPage/LoginPage";
import { useCookies } from "react-cookie";
import { useNavigate } from "react-router-dom";
import SignUpPage from "./Components/SignUpPage/SignUpPage";
import { get_user_data } from "./Logic/login";
import HomePage from "./Components/HomePage/HomePage";
import User from "./Types/User";
import FourYearPlan from "./Types/FourYearPlan";
function App() {
  const [cookie, setCookie, removeCookie] = useCookies(["GatorGuide_Session"]);
  const [plan, setPlan] = useState<FourYearPlan>();

  const navigate = useNavigate();
  const [user, setUser] = useState<User>();
  useEffect(() => {
    console.log("COOKIE", cookie);
    if (cookie["GatorGuide_Session"]) {
      navigate("/");
      get_user_data().then((user) => {
        console.log(user);
        if (user) {
          setUser(user);
        } else {
          navigate("/login");
        }
      });
    } else {
      navigate("/login");
    }
  }, [cookie["GatorGuide_Session"]]);
  return (
    <div className="app" style={{maxHeight:"100%",}}>
      <div className="app-header">
        <div className="header-logo" onClick={(e) => navigate("/")}>
          The GatorGuide
        </div>
        {user ? (
          <div className="header-user">
            <img src="./user.png"></img>
          </div>
        ) : (
          <div className="header-login" onClick={(e) => navigate("login")}>
            Login
          </div>
        )}
      </div>
      <div className="app-content">
        <Routes>
          {user && (
            <Route
              path="/"
              element={<HomePage user={user} setPlan={setPlan} />}
            ></Route>
          )}
          {plan && <Route path="/plan" element={<PlanBuilder plan={plan} />} />}
          <Route path="/login" element={<LoginPage />} />
          <Route path="/signup" element={<SignUpPage />} />
        </Routes>
      </div>
    </div>
  );
}
export default App;
