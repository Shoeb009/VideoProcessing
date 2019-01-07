import subprocess
import os
import cv2

import subprocess
import os
os.chdir(r"C:\Users\IBM_ADMIN\Documents\Shoeb\DataAnalytics\Automation\PyScene\IPL\IPL\Frames_FSW")
count=0
with open("Test_FSW.txt") as f:
	for line in f.readlines():
                start, end = line.strip().split(',')
                filename=str(count)+".mp4"
                cmd = ["ffmpeg", "-i", "HDP000041001.mp4", "-ss", start, "-to", end, "-c", "copy", filename]
                subprocess.run(cmd, stderr=subprocess.STDOUT)
                count=count+1

        

