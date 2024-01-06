#!/usr/bin/env python3
import cv2 
import numpy as np 
import time 

nframes = 200
interval = 0.75

cap = cv2.VideoCapture(-1)

cap.set(cv2.CAP_PROP_FRAME_WIDTH, 9999)
cap.set(cv2.CAP_PROP_FRAME_HEIGHT, 9999)

time.sleep(2)

if not cap.isOpened():
    print("Cannot open camera")
    exit()
    
for i in range(nframes):
    ret, img = cap.read()
    cv2.imwrite(f"./img{400+i}.jpeg", img)
    time.sleep(interval)

cap.release()
    
