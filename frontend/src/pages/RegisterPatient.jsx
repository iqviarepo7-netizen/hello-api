import { useState } from 'react'
import { useNavigate } from 'react-router-dom'
import { createPatient } from '../api/patients'
import PatientForm, { emptyForm } from '../components/PatientForm'

function clientValidate(values) {
  const errors = {}
  if (!values.name.trim()) errors.name = 'Name is required.'
  const age = Number(values.age)
  if (!values.age && values.age !== 0) errors.age = 'Age is required.'
  else if (Number.isNaN(age) || age < 1 || age > 150) errors.age = 'Age must be between 1 and 150.'
  if (!values.phone.trim()) errors.phone = 'Phone is required.'
  if (!values.address.trim()) errors.address = 'Address is required.'
  if (!values.country) errors.country = 'Country is required.'
  return errors
}

export default function RegisterPatient() {
  const navigate = useNavigate()
  const [values, setValues] = useState(emptyForm)
  const [fieldErrors, setFieldErrors] = useState({})
  const [submitting, setSubmitting] = useState(false)
  const [error, setError] = useState('')
  const [success, setSuccess] = useState('')

  async function handleSubmit() {
    setError('')
    setSuccess('')
    const errors = clientValidate(values)
    setFieldErrors(errors)
    if (Object.keys(errors).length > 0) return

    setSubmitting(true)
    try {
      await createPatient({
        name: values.name.trim(),
        age: Number(values.age),
        gender: values.gender,
        phone: values.phone.trim(),
        address: values.address.trim(),
        country: values.country,
      })
      setSuccess('Patient registered successfully.')
      setValues(emptyForm)
      setTimeout(() => navigate('/patients'), 1200)
    } catch (err) {
      setError(err.message || 'Registration failed.')
    } finally {
      setSubmitting(false)
    }
  }

  return (
    <>
      <h1 className="page-title">Register Patient</h1>
      <p className="page-subtitle">Enter patient details below. All fields are required.</p>

      {success && <div className="alert alert-success">{success}</div>}
      {error && <div className="alert alert-error">{error}</div>}

      <div className="card">
        <PatientForm
          values={values}
          onChange={setValues}
          onSubmit={handleSubmit}
          submitting={submitting}
          fieldErrors={fieldErrors}
        />
      </div>
    </>
  )
}
