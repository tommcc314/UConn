import { useState } from 'react';
export default function Signup() {
    const [email, setEmail] = useState("");
    const [password, setPassword] = useState("");
    const [emailValidation, setEmailValidation] = useState("");
    const [passwordValidation, setPasswordValidation] = useState("");
    const validate = (event) => {
        event.preventDefault();
        if (!/^[a-zA-Z0-9.!#$%&'*+/=?^_`{|}~-]+@[a-zA-Z0-9-]+(?:\.[a-zA-Z0-9-]+)*$/.test(email)) setEmailValidation("Email is invalid!");
        else setEmailValidation("");
        if (password.length < 8 || !/\d/.test(password) || !/[A-Z]/.test(password) || !/[a-z]/.test(password)) {setPasswordValidation("Passwords must be at least 8 characters, contain an uppercase letter, lowercase letter and a number.");}
        else setPasswordValidation("");
    }
    return (
        <form onSubmit={validate} className="container custom">
            <h1>Sign Up</h1>
            <div className="form-outline form-white mb-4">
                <input className="form-control form-control-lg" onChange={(e) => setEmail(e.target.value)}/>
                <label className="form-label">Email</label>
            </div>
            {emailValidation !== "" && <p className="error">{emailValidation}</p>}
            <div className="form-outline form-white mb-4">
                <input type="password" className="form-control form-control-lg" onChange={(e) => setPassword(e.target.value)}/>
                <label className="form-label">Password</label>
            </div>
            {passwordValidation !== "" && <p className="error">{passwordValidation}</p>}
            <div className="d-flex align-items-center pt-3">
                <div className="ml-auto mr-sm-5">
                    <button type="submit" value="Submit" className="btn btn-success">Create Account</button>
                </div>
            </div>
        </form>
    );
}