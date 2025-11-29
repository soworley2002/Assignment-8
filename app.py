from flask import Flask, jsonify, render_template_string, request

app = Flask(__name__)

HTML = """
<!doctype html>
<html lang="en">
  <head>
    <meta charset="utf-8">
    <meta name="viewport" content="width=device-width, initial-scale=1">
    <title>StudyBuddy — MVP</title>
    <style>
      body { font-family: Arial, sans-serif; padding: 2rem; }
      .card { border: 1px solid #ddd; padding: 1rem; border-radius: 6px; max-width: 700px }
      input, button { padding: .5rem; margin: .25rem 0 }
    </style>
  </head>
  <body>
    <h1>StudyBuddy — MVP (Flask)</h1>
    <div class="card">
      <p>This is a minimal demonstration of the StudyBuddy MVP. It includes a static UI placeholder for creating a study session and a health endpoint at <code>/api/health</code>.</p>

      <h3>Create a study session (demo)</h3>
      <form id="session-form" action="#" onsubmit="createSession(event)">
        <label>Session name<br><input id="name" placeholder="Study for CS"/></label><br>
        <label>Time (ISO)<br><input id="time" placeholder="2025-12-01T19:00"/></label><br>
        <button>Create (demo)</button>
      </form>
      <pre id="out"></pre>
    </div>

    <script>
    function createSession(e) {
      e.preventDefault();
      const name = document.getElementById('name').value || 'Demo Session';
      const time = document.getElementById('time').value || new Date().toISOString();
      document.getElementById('out').textContent = JSON.stringify({name,time,notes:'This is a UI-only demo for the MVP.'}, null, 2);
    }
    </script>
  </body>
</html>
"""


@app.route('/')
def index():
    return render_template_string(HTML)


@app.route('/api/health')
def health():
    return jsonify({'status': 'ok', 'service': 'StudyBuddy MVP'})


if __name__ == '__main__':
    # For local debug only; CI/Docker will run via gunicorn
    app.run(host='0.0.0.0', port=8080, debug=True)
