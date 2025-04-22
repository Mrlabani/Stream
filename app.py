from flask import Flask, render_template, request
import subprocess

app = Flask(__name__)

@app.route('/', methods=['GET', 'POST'])
def index():
    stream_url = None
    if request.method == 'POST':
        magnet = request.form.get('magnet')
        if magnet:
            subprocess.Popen(["webtorrent", magnet, "--out", "static"], stdout=subprocess.PIPE)
            stream_url = "/static/output.mp4"  # update as needed
    return render_template('index.html', stream_url=stream_url)

if __name__ == '__main__':
    import os
    port = int(os.environ.get("PORT", 8000))
    app.run(host='0.0.0.0', port=port)
