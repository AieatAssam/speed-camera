import sys
import time
from threading import Thread

from picamera.array import PiRGBArray, PiArrayOutput
from picamera import PiCamera


class PiVideoStream:
    def __init__(self, resolution,
                 framerate, format='bgr', rotation=0):
        """ initialize the camera and stream """
        try:
            self.camera = PiCamera()
        except:
            sys.exit(1)
        self.camera.resolution = resolution
        self.camera.rotation = rotation
        self.camera.framerate = framerate

        self.rawCapture = PiArrayOutput(self.camera)  # PiRGBArray(self.camera, size=resolution)

        self.stream = self.camera.capture_continuous(self.rawCapture,
                                                     format=format,
                                                     use_video_port=True)
        """
        initialize the frame and the variable used to indicate
        if the thread should be stopped
        """
        self.thread = None
        self.frame = None
        self.stopped = False
        self.fresh_frame = False

    def start(self):
        """ start the thread to read frames from the video stream """
        self.thread = Thread(target=self.update, args=())
        self.thread.setDaemon(True)
        self.thread.setName('video_grabber')
        self.thread.start()
        return self

    def update(self):
        """ keep looping infinitely until the thread is stopped """
        for f in self.stream:
            # grab the frame from the stream and clear the stream in
            # preparation for the next frame
            self.frame = f.array
            self.rawCapture.truncate(0)
            self.fresh_frame = True

            # if the thread indicator variable is set, stop the thread
            # and resource camera resources
            if self.stopped:
                self.stream.close()
                self.rawCapture.close()
                self.camera.close()
                return

    def read(self):
        """ return the frame most recently read """
        while not self.stopped and not self.fresh_frame:
            time.sleep(0.005)
            # pass
        frame = self.frame
        self.fresh_frame = False
        return frame

    def stop(self):
        """ indicate that the thread should be stopped """
        self.stopped = True
        if self.thread is not None:
            self.thread.join()


# width, height, fps, format
tests = [
    # (1920, 1080, 15),
    # (1920, 1080, 30),
    # (1280, 720, 15),
    # (1280, 720, 20),
    # (1280, 720, 25),
    # (1280, 720, 30),
    # (640, 480, 15),
    # (640, 480, 30),
    # (640, 480, 40),
    # (640, 480, 45),
    # (640, 480, 60),
    # (320, 240, 15),
    # (320, 240, 30),
    # (320, 240, 60)
    (1280, 720, 30, 'bgr'),
    (1280, 720, 30, 'bgra'),
    (1280, 720, 30, 'yuv'),
    (1280, 720, 30, 'rgb'),
    (1280, 720, 30, 'rgba'),
    (1280, 720, 30, 'jpeg'),
    (1280, 720, 30, 'png')
]

if __name__ == '__main__':
    for (width, height, framerate, format) in tests:
        print(f'starting processing {width}x{height} at {framerate}fps ({format})')

        stream = PiVideoStream((width, height), framerate, format)
        stream.start()
        frame_counter = 0
        start = time.time()
        while frame_counter < 100:
            if frame_counter == 0:
                start = time.time()
            frame = stream.read()
            frame_counter += 1
            if frame_counter == 100:
                print(f'FPS {float(100) / (time.time() - start)}')
        stream.stop()
    print('finished')


