const GENDERS = ['Male', 'Female', 'Other']
const COUNTRIES = ['India', 'Vietnam', 'Japan', 'China', 'London']

const emptyForm = {
  name: '',
  age: '',
  gender: 'Male',
  phone: '',
  address: '',
  country: 'India',
}

export { emptyForm }

export default function PatientForm({
  values,
  onChange,
  onSubmit,
  submitting,
  fieldErrors,
}) {
  function handleChange(e) {
    const { name, value } = e.target
    onChange({ ...values, [name]: value })
  }

  return (
    <form
      className="form-grid"
      onSubmit={(e) => {
        e.preventDefault()
        onSubmit()
      }}
      noValidate
    >
      <div className="form-field">
        <label htmlFor="name">Patient Name *</label>
        <input
          id="name"
          name="name"
          value={values.name}
          onChange={handleChange}
          required
          autoComplete="name"
        />
        {fieldErrors.name && <div className="field-error">{fieldErrors.name}</div>}
      </div>

      <div className="form-field">
        <label htmlFor="age">Age *</label>
        <input
          id="age"
          name="age"
          type="number"
          min={1}
          max={150}
          value={values.age}
          onChange={handleChange}
          required
        />
        {fieldErrors.age && <div className="field-error">{fieldErrors.age}</div>}
      </div>

      <div className="form-field">
        <label htmlFor="gender">Gender *</label>
        <select id="gender" name="gender" value={values.gender} onChange={handleChange} required>
          {GENDERS.map((g) => (
            <option key={g} value={g}>
              {g}
            </option>
          ))}
        </select>
        {fieldErrors.gender && <div className="field-error">{fieldErrors.gender}</div>}
      </div>

      <div className="form-field">
        <label htmlFor="country">Country *</label>
        <select id="country" name="country" value={values.country} onChange={handleChange} required>
          {COUNTRIES.map((c) => (
            <option key={c} value={c}>
              {c}
            </option>
          ))}
        </select>
        {fieldErrors.country && <div className="field-error">{fieldErrors.country}</div>}
      </div>

      <div className="form-field">
        <label htmlFor="phone">Phone Number *</label>
        <input
          id="phone"
          name="phone"
          type="tel"
          value={values.phone}
          onChange={handleChange}
          required
        />
        {fieldErrors.phone && <div className="field-error">{fieldErrors.phone}</div>}
      </div>

      <div className="form-field">
        <label htmlFor="address">Address *</label>
        <textarea
          id="address"
          name="address"
          value={values.address}
          onChange={handleChange}
          required
        />
        {fieldErrors.address && <div className="field-error">{fieldErrors.address}</div>}
      </div>

      <div className="form-actions">
        <button type="submit" className="btn btn-primary" disabled={submitting}>
          {submitting ? 'Saving…' : 'Save Patient'}
        </button>
      </div>
    </form>
  )
}
