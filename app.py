from flask import Flask, render_template
import cv2
import threading
import time
import atexit

app = Flask(__name__)

# Global variables
camera = cv2.VideoCapture(0)
recording = True
out = None
lock = threading.Lock()

def record_video():
    global camera, out, recording
    fourcc = cv2.VideoWriter_fourcc(*'XVID')
    filename = f"recording_{int(time.time())}.avi"
    out = cv2.VideoWriter(filename, fourcc, 20.0, (640, 480))

    while recording:
        success, frame = camera.read()
        if not success:
            break
        out.write(frame)

    out.release()

@app.route('/')
def index():
    return render_template('index.html')

@atexit.register
def cleanup():
    global camera, out
    if camera.isOpened():
        camera.release()
    if out is not None:
        out.release()
    cv2.destroyAllWindows()

if __name__ == '__main__':
    # Start recording thread when Flask starts
    recording_thread = threading.Thread(target=record_video, daemon=True)
    recording_thread.start()

    app.run(debug=True)

    # When you stop Flask server with CTRL+C, recording will stop
    recording = False
    recording_thread.join()
