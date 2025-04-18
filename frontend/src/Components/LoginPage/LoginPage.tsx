import { useEffect, useState } from "react";
import { login, get_user_data, create_user } from "../../Logic/login";
import "./LoginPage.css";
import { Link, useNavigate } from "react-router-dom";
import CourseButton from '../CourseButton/CourseButton';
import { BUTTON_SIZES, BUTTON_VARIANTS } from '../../Constants/enums';

function LoginPage() {
  const [userName, setUserName] = useState<string>("");
  const [email, setEmail] = useState<string>("");
  const [password, setPassword] = useState<string>("");
  const navigate = useNavigate();

  return (
    <div 
    className="background"
    style={{display:"flex", 
    alignContent:"center", 
    justifyContent:"center", 
    alignItems:"center", 
    height:"100%",
    }}>
      <div className="loginContainer">
        <div style={{width: "100%"}}>
        <div style={{width: "100%"}}>
          <div className='loginTitle'>Login to GatorGuide </div>
          <div style={{textAlign : "left", alignSelf:"flex-end"}}>
            <h1 className="loginSubTitle">Username: </h1>
          </div>
          <input
            type="text"
            onChange={(e) => {
              setUserName(e.target.value);
            }}
            defaultValue={"username"}
            className="loginField"
          ></input>
        </div>
        
        <div style={{width: "100%"}}>
          <h1 className="loginSubTitle">Password: </h1>
          <input
            type="password"
            onChange={(e) => {
              setPassword(e.target.value);
            }}
            defaultValue={"password"}
            className="loginField"
          ></input>
        </div>
        </div>
        <div style={{display:"flex", alignContent:"space-evenly", justifyContent:"center", flexWrap:"wrap"}}>
          
        <div style={{padding:"10px"}} onClick={(e) => {login(userName, password)}}>
          <CourseButton variant={BUTTON_VARIANTS.login} size={BUTTON_SIZES.Wide} style={{fontWeight: 'bold'}}>
            <h1 style={{fontSize: '20px'}}>Sign In</h1>
          </CourseButton>
        </div>

          <div style={{padding:"10px"}}>
            <CourseButton variant={BUTTON_VARIANTS.signup} size={BUTTON_SIZES.Wide} style={{fontWeight: 'bold'}}>
              <Link to="/signup" style={{textDecoration:"none", color:"white"}}>
              <h1 style={{fontSize: '20px'}}>Sign Up</h1>
              </Link>
            </CourseButton>
          </div>
            
        </div>    

        <div>
        </div>
      </div>
      
    </div>
  );
}

export default LoginPage;
