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
      alert("Issue with user login");
      response.json().then((data) => {
        console.log(data);
      });
    }
  });
};

// creates a user based on User (look into User.ts) and password, no return needed
// executes rather quickly
const create_user = (user: User, password: string) => {
  fetch(import.meta.env.VITE_API_HOST + "/users/?password=" + password, {
    credentials: "include",
    method: "POST",
    body: JSON.stringify(user),
    headers: {
      Accept: "application/json",
      "Content-Type": "application/json",
    },
  }).then((response) => {
    if (response.status != 200) {
      alert("Issue with user creation");
      response.json().then((data) => {
        console.log(data);
      });
    }
  });
};

// needs to be run after the session cookie is set (user has been logged in)
// get_user_data.then((user)=>{do_something(user)})
const get_user_data = async (): Promise<any> => {
  let found_user: User;
  const response = await fetch(import.meta.env.VITE_API_HOST + "/users/me", {
    credentials: "include",
    method: "GET",
    headers: {
      Accept: "application/json",
      "Content-Type": "application/json",
    },
  });

  if (response.status == 200) {
    return response.json();
  } else {
    response.json().then((data) => {
      console.error(data);
      throw new Error("User not found!");
    });
  }
};

export { login, create_user, get_user_data };
