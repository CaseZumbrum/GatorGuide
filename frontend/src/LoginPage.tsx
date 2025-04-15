import { useEffect, useState } from "react";
import { login, get_user_data, create_user } from "./Logic/login";

function LoginPage() {
  const [userName, setUserName] = useState<string>("");
  const [email, setEmail] = useState<string>("");
  const [password, setPassword] = useState<string>("");

  return (
    <div>
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
          login(userName, password);
        }}
      >
        login
      </button>
      <button
        onClick={(e) => {
          create_user({ name: userName, email: email, plans: [] }, password);
        }}
      >
        create_user
      </button>
      <button
        onClick={(e) => {
          get_user_data().then((user) => {
            alert(JSON.stringify(user));
          });
        }}
      >
        get user data (make sure to sign in first)
      </button>
    </div>
  );
}

export default LoginPage;
