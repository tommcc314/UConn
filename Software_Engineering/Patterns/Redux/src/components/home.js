import { Link } from "react-router-dom";
import '../styles/home.css'
export default function Home() {
  return (
    <div className="home">
    <h1>Welcome to 2102 Quizzes!</h1>
    <div className="text-center">
      <Link to="/quiz" className="btn btn-success" role="button">Test Your Knowledge {'>'} </Link>
    </div>
    <div className="container custom">
      <div className="row">
        <div className="col-md-7">
          <img className="img-fluid rounded mb-3 mb-md-0" src="https://via.placeholder.com/700x300" alt=""/>
        </div>
        <div className="col-md-5">
          <h3>High-quality questions</h3>
          <p>Quizzes are automatically generated from a databank of interesting and tricky questions.</p>
        </div>
      </div>
      <hr/>
      <div className="row">
        <div className="col-md-5">
          <h3>Personalized experience</h3>
          <p>Registered users will receive questions based on the categories and performance on previous questions.</p>
        </div>
        <div className="col-md-7">
          <img className="img-fluid rounded mb-3 mb-md-0" src="https://via.placeholder.com/700x300" alt=""/>
        </div>
      </div>
      <hr/>
    </div>
    </div>
  );
}
