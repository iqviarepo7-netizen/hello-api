import { BrowserRouter, Route, Routes } from 'react-router-dom'
import Layout from './components/Layout'
import Dashboard from './pages/Dashboard'
import GetStarted from './pages/GetStarted'
import PatientList from './pages/PatientList'
import RegisterPatient from './pages/RegisterPatient'

export default function App() {
  return (
    <BrowserRouter>
      <Routes>
        <Route path="/" element={<GetStarted />} />
        <Route element={<Layout />}>
          <Route path="dashboard" element={<Dashboard />} />
          <Route path="patients" element={<PatientList />} />
          <Route path="patients/register" element={<RegisterPatient />} />
        </Route>
      </Routes>
    </BrowserRouter>
  )
}
