from picamera2 import Picamera2, Preview
from picamera2.encoders import H264Encoder
import time
picam2 = Picamera2()
camera_config = picam2.create_still_configuration(main={"size": (2028, 1080)}, lores={"size": (640, 480)}, display="lores")
picam2.configure(camera_config)
picam2.start_preview(Preview.QTGL)
picam2.start()
time.sleep(2)
picam2.capture_file("test3.jpg")
picam2.stop()

video_config = picam2.create_video_configuration()
picam2.configure(video_config)
encoder = H264Encoder(10000000)
picam2.start_recording(encoder, 'test3.h264')
time.sleep(10)
picam2.stop_recording()