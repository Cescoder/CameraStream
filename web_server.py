from flask import Flask, render_template

PORT = 5000
HOST = '0.0.0.0'

app = Flask('CameraStream')

@app.route("/")
def stream():
    return render_template('index.html')

app.run(HOST, PORT)