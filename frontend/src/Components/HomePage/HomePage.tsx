import React, { act, useEffect } from "react";
import "./HomePage.css";
import User from "../../Types/User";

interface props {
  user: User;
}
function HomePage({ user }: props) {
  return (
    <div className="homepage">
      <div>HOME</div>
      <div>{JSON.stringify(user)}</div>
    </div>
  );
}

export default HomePage;
