from flask import Flask, render_template, request, redirect
import subprocess
import os

app = Flask(__name__)

@app.route('/', methods=['GET', 'POST'])
def index():
    stream_url = None
    if request.method == 'POST':
        magnet = request.form.get('magnet')
        if magnet:
            subprocess.Popen(["webtorrent", magnet, "--out", "static", "--vlc"], stdout=subprocess.PIPE)
            stream_url = "/static/output.mp4"  # Adjust based on actual stream file
    return render_template('index.html', stream_url=stream_url)

if __name__ == '__main__':
    app.run(debug=True)
  
