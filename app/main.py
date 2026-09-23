"""Main application module.

This module contains a simple authentication function and a helper
function to display an alert message.  After a successful login the
alert "Welcome World" is triggered.
"""

import logging

# Configure a basic logger. In a real application this would be
# configured elsewhere.
logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)


def alert(message: str) -> None:
    """Display an alert message.

    In this simple example the alert is implemented by logging the
    message.  The function is intentionally lightweight so that it can
    be easily patched in tests.
    """
    logger.info(message)


def login(username: str, password: str) -> bool:
    """Authenticate a user.

    For demonstration purposes the credentials are hard‑coded.  In a
    real system this would query a database or an external service.
    """
    # Dummy authentication logic
    if username == "user" and password == "pass":
        # Successful login – trigger the alert
        alert("Welcome World")
        return True
    return False
