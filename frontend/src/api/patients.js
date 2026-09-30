import axios from 'axios'

const API_BASE = '/api'

const patientsApi = axios.create({
  baseURL: API_BASE,
  headers: { 'Content-Type': 'application/json' },
})

export async function getPatients() {
  const response = await patientsApi.get('/patients')
  return response.data
}

export async function createPatient(patient) {
  const response = await patientsApi.post('/patients', patient)
  return response.data
}
