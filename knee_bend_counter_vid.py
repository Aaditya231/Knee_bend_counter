# -*- coding: utf-8 -*-
"""
Created on Fri Dec  9 14:08:20 2022

@author: AADITYA
"""
# -*- coding: utf-8 -*-
"""
Created on Fri Dec  9 13:18:21 2022

@author: AADITYA
"""
import time
import numpy as np
import cv2
import mediapipe as mp
mp_drawing = mp.solutions.drawing_utils
mp_drawing_styles = mp.solutions.drawing_styles
mp_pose = mp.solutions.pose
mp_holistic = mp.solutions.holistic

start_time=0;
count = 0
temp=0
start=0
position=None
duration=8

cap = cv2.VideoCapture(r"C:\Users\AADITYA\Downloads\KneeBendVideo.mp4")
with mp_pose.Pose( static_image_mode=False,
               model_complexity=1,
               smooth_landmarks=True,
               enable_segmentation=False,
               smooth_segmentation=True,
               min_detection_confidence=0.5,
               min_tracking_confidence=0.5) as pose:
  while cap.isOpened():
    success, image = cap.read()
    if not success:
      print("Ignoring empty camera frame.")
      # If loading a video, use 'break' instead of 'continue'.
      break

    # To improve performance, optionally mark the image as not writeable to
    # pass by reference.
    image.flags.writeable = False
    image = cv2.cvtColor(image, cv2.COLOR_BGR2RGB)
    results = pose.process(image)
    imlist=[]
    # Draw the pose annotation on the image.
    image.flags.writeable = True
    image = cv2.cvtColor(image, cv2.COLOR_RGB2BGR)
    cv2.rectangle(image, (900,0), (600,80), (245,117,16), -1)
    cv2.rectangle(image, (900,150), (600,80), (30,255,255), -1)
    cv2.rectangle(image, (800,110), (650,140), (245,117,16), -1)
    
    cv2.putText(image, 'state of bendness', (640,100),
                cv2.FONT_HERSHEY_SIMPLEX, 0.5, (0,0,0), 1, cv2.LINE_AA)
    cv2.putText(image, 'Timer', (640,15),
                cv2.FONT_HERSHEY_SIMPLEX, 0.5, (0,0,0), 1, cv2.LINE_AA)
    cv2.putText(image, 'Knee Bends', (720,15),
                cv2.FONT_HERSHEY_SIMPLEX, 0.5, (0,0,0), 1, cv2.LINE_AA)
    
    if results.pose_landmarks:
        mp_drawing.draw_landmarks(
        image,results.pose_landmarks,mp_holistic.POSE_CONNECTIONS)
        for id,im in enumerate(results.pose_landmarks.landmark):
            h,w,_=image.shape
            X,Y=int(im.x*w),int(im.y*w)
            imlist.append([id,X,Y])
        radians = np.arctan2(imlist[27][2]-imlist[25][2], imlist[27][1]-imlist[25][1]) - np.arctan2(imlist[23][2]-imlist[25][2], imlist[23][1]-imlist[25][1])  
        angle = np.abs(radians*180.0/np.pi)
        if(start==2):
            end_time=time.time()
            duration = int(end_time-start_time)
            cv2.putText(image, str(duration), 
                        (635,60),
                        cv2.FONT_HERSHEY_SIMPLEX, 1.5, (255,255,255), 1, cv2.LINE_AA)
            if(duration==temp):
                
                if(temp==8):
                    count+=1
                temp+=1
            
        if(angle<140 and angle>70):
            cv2.putText(image, 'partially bent', (670,130),
                        cv2.FONT_HERSHEY_SIMPLEX, 0.5, (255,255,255), 1, cv2.LINE_AA)
        if(angle<70):
            cv2.putText(image, 'fully bent', (670,130),
                        cv2.FONT_HERSHEY_SIMPLEX, 0.5, (255,255,255), 1, cv2.LINE_AA)
        if(angle>140):
            cv2.putText(image, 'straight', (670,130),
                        cv2.FONT_HERSHEY_SIMPLEX, 0.5, (255,255,255), 1, cv2.LINE_AA)
        if(angle>140):
            position = "straight"
            start=1
            if(temp<9):
                cv2.putText(image, 'Keep your knee bent', (180,145),
                            cv2.FONT_HERSHEY_SIMPLEX, 1, (10,20,255), 1, cv2.LINE_AA)
                

                              
        if(angle<140 and position=='straight'):
           
           position = "bent"
           if(start==1):
               start_time=time.time()
               temp=0
               start=2
           
       
       
        cv2.putText(image, str(count), (715,60),
                    cv2.FONT_HERSHEY_SIMPLEX, 1.5, (255,255,255), 1, cv2.LINE_AA)
        
        cv2.imshow('knee bent pose', image)
        if cv2.waitKey(5) & 0xFF == 27:
            break
cap.release()







