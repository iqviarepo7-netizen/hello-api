import { NavLink, Outlet } from 'react-router-dom'

export default function Layout() {
  return (
    <div className="app-shell">
      <header className="app-header">
        <div className="app-header-inner">
          <div className="app-brand">HIS Hospital</div>
          <nav className="app-nav" aria-label="Main">
            <NavLink to="/dashboard" end>
              Dashboard
            </NavLink>
            <NavLink to="/patients" end>
              Patients
            </NavLink>
            <NavLink to="/patients/register">Register Patient</NavLink>
          </nav>
        </div>
      </header>
      <main className="app-main">
        <Outlet />
      </main>
    </div>
  )
}
