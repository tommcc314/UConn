import { Link } from "react-router-dom";
export default function Nav() {
    return (
        <nav className="navbar navbar-expand-lg navbar-dark bg-dark">
            <div className="container">
                <ul className="navbar-nav ms-3">
                    <li className="nav-item me-3">
                        <Link className="nav-link d-flex align-items-center" to="/">2102 Quizzes</Link>
                    </li>
                    <li className="nav-item me-3">
                        <Link className="nav-link d-flex align-items-center" to="/quiz">New Quiz</Link>
                    </li>
                    <li className="nav-item me-3">
                        <Link className="nav-link d-flex align-items-center" to="/signup">Sign Up</Link>
                    </li>
                </ul>
            </div>
        </nav>
    );
}