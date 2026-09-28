from flask import Flask, render_template_string

app = Flask(__name__)

HTML = """
<!doctype html>
<html lang="en">
<head>
  <meta charset="utf-8">
  <title>Pipeline Runner</title>
  <style>
    /* Simple modal styling */
    .modal {
      display: none;
      position: fixed;
      z-index: 1000;
      left: 0;
      top: 0;
      width: 100%;
      height: 100%;
      overflow: auto;
      background-color: rgba(0,0,0,0.4);
    }
    .modal-content {
      background-color: #fefefe;
      margin: 15% auto;
      padding: 20px;
      border: 1px solid #888;
      width: 300px;
      text-align: center;
    }
    .close-btn {
      color: #aaa;
      float: right;
      font-size: 28px;
      font-weight: bold;
      cursor: pointer;
    }
  </style>
</head>
<body>
  <button id="runPipelineBtn">Run Pipeline</button>

  <div id="welcomeModal" class="modal">
    <div class="modal-content">
      <span class="close-btn" id="closeModal">&times;</span>
      <p>welcome home</p>
    </div>
  </div>

  <script>
    document.getElementById('runPipelineBtn').addEventListener('click', function() {
      document.getElementById('welcomeModal').style.display = 'block';
    });
    document.getElementById('closeModal').addEventListener('click', function() {
      document.getElementById('welcomeModal').style.display = 'none';
    });
    // Close modal when clicking outside the content
    window.addEventListener('click', function(event) {
      var modal = document.getElementById('welcomeModal');
      if (event.target === modal) {
        modal.style.display = 'none';
      }
    });
  </script>
</body>
</html>
"""

@app.route('/')
def index():
    return render_template_string(HTML)

if __name__ == '__main__':
    app.run(debug=True)
