import { Link } from 'react-router-dom'

export default function GetStarted() {
  return (
    <div className="get-started">
      <div className="get-started-inner">
        <p className="get-started-eyebrow">HIS Hospital</p>
        <h1 className="get-started-title">Patient management, simplified</h1>
        <p className="get-started-lead">
          Register patients, view the patient list, and keep basic records in one place. No sign-in
          required for this demo.
        </p>
        <Link to="/dashboard" className="btn btn-primary get-started-cta">
          Get Started
        </Link>
      </div>
    </div>
  )
}
