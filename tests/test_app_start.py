import subprocess
import sys
from pathlib import Path

def test_startup_message():
    # Run the app and capture output
    result = subprocess.run([sys.executable, str(Path(__file__).parents[1] / "app" / "main.py")],
                            capture_output=True, text=True)
    assert result.stdout.strip() == "hello world"
