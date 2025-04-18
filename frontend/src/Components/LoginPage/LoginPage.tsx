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
    <div style={{display:"flex", alignContent:"center", justifyContent:"center", alignItems:"center", height:"100%"}}>
      <div className="loginContainer">
        <div style={{justifyContent : "left"}}>
          <h1 className="loginTitle">Username: </h1>
        </div>
        <input
          type="text"
          onChange={(e) => {
            setUserName(e.target.value);
          }}
          defaultValue={"username"}
          className="field"
        ></input>
        <h1 className="loginTitle">Password: </h1>
        <input
          type="password"
          onChange={(e) => {
            setPassword(e.target.value);
          }}
          defaultValue={"password"}
          className="field"
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
      
    </div>
  );
}

export default LoginPage;
