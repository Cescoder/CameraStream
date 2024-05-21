#MODULES
from fastapi import FastAPI
from fastapi.responses import FileResponse
import uvicorn
from cv2 import VideoCapture, imwrite
import asyncio

#CAMERA SETTINGS
cam_port = 0
cam = VideoCapture(cam_port) 


app = FastAPI(title="CameraStream")

@app.get('/GetCameraFrame')
def get_camera_frame():
	result, image = cam.read() 
	imwrite(filename='frame.jpg', img=image)
	return FileResponse('frame.jpg')


if __name__ == "__main__":
    uvicorn.run(app, host="127.0.0.1", port=8000)
