async function parseError(response) {
  let detail = 'Something went wrong. Please try again.'
  try {
    const data = await response.json()
    if (data.detail) {
      if (Array.isArray(data.detail)) {
        return data.detail.map((e) => e.msg || String(e)).join(' ')
      }
      detail = String(data.detail)
    }
  } catch {
    /* ignore */
  }
  return detail
}

export async function getPatients() {
  const response = await fetch('/api/patients')
  if (!response.ok) {
    throw new Error(await parseError(response))
  }
  return response.json()
}

export async function createPatient(payload) {
  const response = await fetch('/api/patients', {
    method: 'POST',
    headers: { 'Content-Type': 'application/json' },
    body: JSON.stringify(payload),
  })
  if (!response.ok) {
    throw new Error(await parseError(response))
  }
  return response.json()
}
