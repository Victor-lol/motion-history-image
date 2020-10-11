#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri Oct  9 13:52:51 2020

@author: victor
"""

import numpy as np
import cv2


cap = cv2.VideoCapture(0)
tau = 200
thres = 130
delta = 40

while cap.isOpened():
    ret,frame = cap.read()
    frame = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
    if not ret:
        break
    
    prev = frame.copy()
    H = np.zeros(frame.shape)

    while True:

        ret,frame = cap.read()
        frame = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
        diff = np.abs(frame, prev)
    
        idx = diff > thres
        mhi = np.maximum(0, H - delta)
        mhi[idx] = tau
        H = mhi
    
        cv2.imshow("mhi", mhi)
        prev = frame.copy()

        if cv2.waitKey(1) & 0xFF == ord('q'):
            break 
cap.release()
cv2.destroyAllWindows()



