from fastapi import FastAPI
from fastapi.responses import HTMLResponse

app = FastAPI()

@app.get("/run-pipeline", response_class=HTMLResponse)
def run_pipeline_page():
    html_content = """
    <!DOCTYPE html>
    <html>
    <head>
        <title>Run Pipeline</title>
        <script>
            function handleRunPipeline() {
                alert('welcome home');
            }
        </script>
    </head>
    <body>
        <button id="run-pipeline" onclick="handleRunPipeline()">Run Pipeline</button>
    </body>
    </html>
    """
    return html_content
