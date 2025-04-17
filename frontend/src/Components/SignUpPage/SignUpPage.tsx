import { useEffect, useState } from "react";
import { login, get_user_data, create_user } from "../../Logic/login";
import "./SignUpPage.css";
import { useNavigate } from "react-router-dom";
function SignUpPage() {
  const [userName, setUserName] = useState<string>("");
  const [email, setEmail] = useState<string>("");
  const [password, setPassword] = useState<string>("");
  const navigate = useNavigate();

  return (
    <div>
      SIGN UP PAGE
      <input
        type="text"
        onChange={(e) => {
          setEmail(e.target.value);
        }}
        defaultValue={"email"}
      ></input>
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
          create_user({ name: userName, email: email, plans: [] }, password);
        }}
      >
        create_user
      </button>
    </div>
  );
}

export default SignUpPage;
