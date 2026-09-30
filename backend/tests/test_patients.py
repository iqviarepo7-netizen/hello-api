def test_list_patients_empty(client):
    response = client.get("/api/patients")
    assert response.status_code == 200
    assert response.json() == []


def test_create_and_list_patient(client):
    payload = {
        "name": "Jane Doe",
        "age": 32,
        "gender": "Female",
        "phone": "555-123-4567",
        "address": "123 Main St",
        "country": "London",
    }
    create = client.post("/api/patients", json=payload)
    assert create.status_code == 201
    body = create.json()
    assert body["name"] == payload["name"]
    assert body["age"] == payload["age"]
    assert body["country"] == payload["country"]
    assert "id" in body
    assert "created_at" in body

    listing = client.get("/api/patients")
    assert listing.status_code == 200
    patients = listing.json()
    assert len(patients) == 1
    assert patients[0]["name"] == payload["name"]
    assert patients[0]["country"] == payload["country"]


def test_create_patient_missing_field(client):
    response = client.post(
        "/api/patients",
        json={"age": 25, "gender": "Male", "phone": "5551234567", "address": "A"},
    )
    assert response.status_code == 422


def test_create_patient_invalid_age(client):
    response = client.post(
        "/api/patients",
        json={
            "name": "Test",
            "age": 0,
            "gender": "Male",
            "phone": "5551234567",
            "address": "Address",
            "country": "India",
        },
    )
    assert response.status_code == 422


def test_create_patient_invalid_country(client):
    response = client.post(
        "/api/patients",
        json={
            "name": "Test",
            "age": 30,
            "gender": "Male",
            "phone": "5551234567",
            "address": "Address",
            "country": "InvalidCountry",
        },
    )
    assert response.status_code == 422
