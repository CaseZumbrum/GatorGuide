fetch(import.meta.env.VITE_API_HOST + "/courses", {
    credentials: 'include',
    method: 'GET',
    headers: {
        Accept: 'application/json',
        'Content-Type': 'application/json'
    }
}).then((response) => {
    if (response.status == 200) {
        response.json().then((courses) => {
            console.log(courses)
        });
    }

});

function LoginPage() {

    return ()
}

export default LoginPage