import { useCallback, useEffect, useState } from 'react'
import { Link } from 'react-router-dom'
import { getPatients } from '../api/patients'
import PatientTable from '../components/PatientTable'

export default function PatientList() {
  const [patients, setPatients] = useState([])
  const [loading, setLoading] = useState(true)
  const [error, setError] = useState('')

  const load = useCallback(async () => {
    setLoading(true)
    setError('')
    try {
      const data = await getPatients()
      setPatients(data)
    } catch (err) {
      setError(err.message || 'Failed to load patients.')
    } finally {
      setLoading(false)
    }
  }, [])

  useEffect(() => {
    load()
  }, [load])

  return (
    <>
      <h1 className="page-title">Patients</h1>
      <p className="page-subtitle">All registered patients in the system.</p>

      <div className="toolbar">
        <button type="button" className="btn btn-secondary" onClick={load} disabled={loading}>
          {loading ? 'Refreshing…' : 'Refresh'}
        </button>
        <Link to="/patients/register" className="btn btn-primary">
          Register Patient
        </Link>
      </div>

      {error && <div className="alert alert-error">{error}</div>}

      <div className="card">
        {loading && patients.length === 0 ? (
          <div className="loading-state">Loading patients…</div>
        ) : (
          <PatientTable patients={patients} />
        )}
      </div>
    </>
  )
}
