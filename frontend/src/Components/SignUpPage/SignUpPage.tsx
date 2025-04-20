import { useEffect, useState } from "react";
import { login, get_user_data, create_user } from "../../Logic/login";
import "./SignUpPage.css";
import { useNavigate } from "react-router-dom";
import CourseButton from '../CourseButton/CourseButton';
import { BUTTON_SIZES, BUTTON_VARIANTS } from '../../Constants/enums';

function SignUpPage() {
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
      <div className="signupContainer">
        <div style={{width: "100%"}}>
          <div style={{width: "100%"}}>
            <div className='signupTitle'>Sign up for GatorGuide </div>
            <div style={{textAlign : "left", alignSelf:"flex-end"}}>
              <h1 className="signupSubTitle">Enter Email </h1>
            </div>
            <input
              type="text"
              onChange={(e) => {
                setEmail(e.target.value);
              }}
              defaultValue={"email"}
              className='field'
            ></input>
          </div>
          
          <div style={{width: "100%"}}>
            <h1 className="signupSubTitle">Create Username </h1>
            <input
              type="text"
              onChange={(e) => {
                setUserName(e.target.value);
              }}
              defaultValue={"username"}
              className='field'
            ></input>
          </div>

          <div style={{width: "100%"}}>
            <h1 className="signupSubTitle">Create Password </h1>
            <input
              type="password"
              onChange={(e) => {
                setPassword(e.target.value);
              }}
              defaultValue={"password"}
              className='field'
            ></input>
          </div>
        </div>
        <div style={{display:"flex", alignContent:"space-evenly", justifyContent:"center", flexWrap:"wrap"}}>
          <div style={{padding:"10px", paddingLeft:"2vw"}} onClick={(e) => {create_user({ name: userName, email: email, plans: [] }, password)}}>
            <CourseButton variant={BUTTON_VARIANTS.signup} size={BUTTON_SIZES.Wide} style={{fontWeight: 'bold'}}>
            <h1 style={{fontSize: '20px'}}>Create an Account</h1>
            </CourseButton>
          </div>
              
        </div>    
      </div>
    </div>
    
  );
}

export default SignUpPage;
