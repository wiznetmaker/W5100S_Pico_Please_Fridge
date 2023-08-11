import os
import subprocess
import ultralytics

def run_detect():
    cmd = ["python", "/home/pi/yolov5ss/detect.py",
    "--weights", "total.pt",
    "--img", "480",
    "--source", "0",
    "--save-txt",
    "--project", "/home/pi/yolov5ss/result"
    ]
    subprocess.run(cmd)
if __name__ == "__main__":
    run_detect()
    