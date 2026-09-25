from fastapi import FastAPI
from fastapi.responses import HTMLResponse

app = FastAPI()


@app.get("/", response_class=HTMLResponse)
def read_root():
    return """<!DOCTYPE html>
<html>
<head>
    <title>Run Pipeline</title>
</head>
<body>
    <button id=\"run-pipeline-btn\">Run Pipeline</button>
    <script>
        document.getElementById('run-pipeline-btn').addEventListener('click', async () => {
            const resp = await fetch('/run-pipeline');
            const data = await resp.json();
            alert(data.message);
        });
    </script>
</body>
</html>"""


@app.get("/run-pipeline")
def run_pipeline():
    return {"message": "welcome home"}
