import User from "../Types/User";

// login with username and password, no return
const login = (username: string, password: string) => {
  fetch(
    import.meta.env.VITE_API_HOST +
      "/users/" +
      username +
      "/login?password=" +
      password,
    {
      credentials: "include",
      method: "GET",
      headers: {
        Accept: "application/json",
        "Content-Type": "application/json",
      },
    }
  ).then((response) => {
    if (response.status != 200) {
      if (response.status == 404) {
        alert("User not found!");
      } else if (response.status == 401) {
        alert("Incorrect password!");
      } else {
        alert("Unknown error occured, sorry!");
      }
      response.json().then((data) => {
        console.log(data);
      });
    }
  });
};

// creates a user based on User (look into User.ts) and password, no return needed
// executes rather quickly
const create_user = (user: User, password: string) => {
  // send a request to create a user
  console.log("Create_user is called");
  fetch(import.meta.env.VITE_API_HOST + "/users/?password=" + password, {
    credentials: "include",
    method: "POST",
    body: JSON.stringify(user),
    headers: {
      Accept: "application/json",
      "Content-Type": "application/json",
    },
  }).then((response) => {
    // success
    if (response.status == 200) {
      // login with new user
      login(user.name, password);
    }
    // fail
    if (response.status != 200) {
      if (response.status == 409) {
        alert("Username or email already exists!");
      } else {
        alert("Unknown error occured, sorry!");
      }
      response.json().then((data) => {
        console.log(data);
      });
    }
  });
};

// needs to be run after the session cookie is set (user has been logged in)
// get_user_data.then((user)=>{do_something(user)})
const get_user_data = async (): Promise<any> => {
  // fetch the user data
  const response = await fetch(import.meta.env.VITE_API_HOST + "/users/me", {
    credentials: "include",
    method: "GET",
    headers: {
      Accept: "application/json",
      "Content-Type": "application/json",
    },
  });

  // success
  if (response.status == 200) {
    return response.json();
  }
  // fail
  else {
    response.json().then((data) => {
      console.error(data);
      throw new Error("User not found!");
    });
  }
};

export { login, create_user, get_user_data };
