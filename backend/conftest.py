import sys
from pathlib import Path

# Ensure the backend directory (which contains the `app` package) is on sys.path
# so that `import app.xxx` works regardless of how pytest is invoked or from
# which working directory.
_BACKEND_DIR = Path(__file__).resolve().parent
if str(_BACKEND_DIR) not in sys.path:
    sys.path.insert(0, str(_BACKEND_DIR))
