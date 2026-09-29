import pytest
from app import main

def test_startup_no_exceptions():
    """Ensure that the start function runs without raising any exceptions."""
    # The start function should complete without error; any unexpected exception
    # will cause the test to fail.
    main.start()
