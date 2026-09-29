export default function PatientTable({ patients }) {
  if (patients.length === 0) {
    return (
      <div className="empty-state">
        <p>No patients yet.</p>
        <p>Register a patient to see them listed here.</p>
      </div>
    )
  }

  return (
    <div className="table-wrap">
      <table className="patient-table">
        <thead>
          <tr>
            <th>Name</th>
            <th>Age</th>
            <th>Gender</th>
            <th>Phone</th>
            <th>Address</th>
          </tr>
        </thead>
        <tbody>
          {patients.map((p) => (
            <tr key={p.id}>
              <td>{p.name}</td>
              <td>{p.age}</td>
              <td>{p.gender}</td>
              <td>{p.phone}</td>
              <td>{p.address}</td>
            </tr>
          ))}
        </tbody>
      </table>
    </div>
  )
}
