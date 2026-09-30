from pydantic import BaseModel


class User(BaseModel):
    email: str
    password: str

# In‑memory user store
users = [
    User(email="user1@test.com", password="Test@123"),
    User(email="user2@test.com", password="Test@123"),
]


def verify_credentials(email: str, password: str) -> bool:
    """Return True if a user with matching email and password exists."""
    for user in users:
        if user.email == email and user.password == password:
            return True
    return False
