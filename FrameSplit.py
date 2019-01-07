import subprocess
import os
import cv2

#os.chdir(r"C:\Users\IBM_ADMIN\Documents\Shoeb\DataAnalytics\Automation\PyScene\IPL\IPL\Frames_FSW\FSW_vids")

for video in os.listdir(r"C:\Users\IBM_ADMIN\Documents\Shoeb\DataAnalytics\Automation\PyScene\IPL\IPL\Frames_FSW\FSW_vids"):
        vid = r"C:/Users/IBM_ADMIN/Documents/Shoeb/DataAnalytics/Automation/PyScene/IPL/IPL/Frames_FSW/FSW_vids/" +video
        capture=cv2.VideoCapture(vid)
        fps= capture.get(cv2.CAP_PROP_FPS)
        print("FPS:",fps)
        ret,frame=capture.read()
        ret=True
        os.chdir(r"C:\Users\IBM_ADMIN\Documents\Shoeb\DataAnalytics\Automation\PyScene\IPL\IPL\Frames_FSW\FSW_Frames")
        count=0
    #Enable below statement to capture frames
        while (ret):
                ret,frame=capture.read()
                cv2.imwrite(video+"Frame%d.jpg" %count ,frame)
                count=count+1
        

    
