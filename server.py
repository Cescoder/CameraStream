#MODULES
from flask import Flask, render_template, Response, request, jsonify
import cv2

PORT = 5000
HOST = 'localhost'
PASSWORD = 'password'

app = Flask('Camera System')
camera = cv2.VideoCapture(0)


def gen_frames():
    while True: 
        success, frame = camera.read()
        if not success: 
            break 
        else: 
            ret, buffer = cv2.imencode('.jpg', frame) 
            frame = buffer.tobytes() 
            yield (b'--frame\r\n' b'Content-Type: image/jpeg\r\n\r\n' + frame + b'\r\n') # concat frame one by one and show result

@app.route('/')
def home():
    return render_template('index.html')

@app.route('/video_feed')
def video_feed():
    return Response(gen_frames(), mimetype='multipart/x-mixed-replace; boundary=frame')

@app.route('/login', methods=['POST'])
def login():
    password = request.get_json()['password']

    if password == PASSWORD:
        return jsonify({"message": "ok"}), 200
    else:
        return jsonify({"message": "Password is incorrect"}), 401
    

if __name__ == "__main__":
    app.run(HOST, PORT)
