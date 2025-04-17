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
function App() {
  const [cookie, setCookie, removeCookie] = useCookies(["GatorGuide_Session"]);
  const navigate = useNavigate();
  const [user, setUser] = useState<User>({
    name: "default",
    email: "default",
    plans: [],
  });
  useEffect(() => {
    console.log("COOKIE", cookie);
    if (cookie["GatorGuide_Session"]) {
      navigate("/");
      get_user_data().then((user) => {
        console.log(user);
        setUser(user);
      });
    } else {
      navigate("/login");
    }
  }, [cookie["GatorGuide_Session"]]);
  return (
    <div className="app">
      <div className="app-header">
        <Link to="/">The GatorGuide</Link> <Link to="/login">Login</Link>
      </div>
      <Routes>
        <Route path="/" element={<HomePage user={user} />}></Route>
        <Route path="/plan" element={<PlanBuilder />} />
        <Route path="/login" element={<LoginPage />} />
        <Route path="/signup" element={<SignUpPage />} />
      </Routes>
    </div>
  );
}
export default App;
