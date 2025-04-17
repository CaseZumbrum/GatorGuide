import { useEffect, useState } from "react";
import { login, get_user_data, create_user } from "../../Logic/login";
import "./LoginPage.css";
import { Link, useNavigate } from "react-router-dom";
function LoginPage() {
  const [userName, setUserName] = useState<string>("");
  const [email, setEmail] = useState<string>("");
  const [password, setPassword] = useState<string>("");
  const navigate = useNavigate();
  return (
    <div>
      LOGIN PAGE
      <input
        type="text"
        onChange={(e) => {
          setUserName(e.target.value);
        }}
        defaultValue={"username"}
      ></input>
      <input
        type="password"
        onChange={(e) => {
          setPassword(e.target.value);
        }}
        defaultValue={"password"}
      ></input>
      <button
        onClick={(e) => {
          login(userName, password);
        }}
      >
        login
      </button>
      <button>
        <Link to="/signup"> Sign Up</Link>
      </button>
    </div>
  );
}

export default LoginPage;
