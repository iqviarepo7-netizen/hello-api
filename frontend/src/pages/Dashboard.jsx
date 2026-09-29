import { Link } from 'react-router-dom'

export default function Dashboard() {
  return (
    <>
      <h1 className="page-title">Dashboard</h1>
      <p className="page-subtitle">
        Welcome to IQVIA HIS patient management. Register patients and view the patient
        list from the links below.
      </p>
      <div className="card-grid">
        <Link to="/patients" className="card-link">
          <strong>Patient List</strong>
          View all registered patients and refresh the list.
        </Link>
        <Link to="/patients/register" className="card-link">
          <strong>Register Patient</strong>
          Add a new patient with name, age, gender, phone, and address.
        </Link>
      </div>
    </>
  )
}
