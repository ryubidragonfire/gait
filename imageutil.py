# -*- coding: utf-8 -*-
"""
Created on Wed Sep 14 15:12:45 2016

@author: chyam
"""
from __future__ import print_function

import cv2
import numpy as np

def box_sillhouette(fname, show=False):
    """ Put a rectangle box around the sillhouette. """
    img = cv2.imread(fname, -1) # -1 : read as it is
    cv2.imshow("img", img)  

    img_gray = cv2.cvtColor(img, cv2.COLOR_RGB2GRAY)
    cv2.imshow("img_gray", img_gray)
    
    #img_cvuint8 = cv2.convertScaleAbs(img_gray); print(img_cvuint8.dtype)


    ret,thresh = cv2.threshold(img_gray,200,255,cv2.THRESH_BINARY)
    #contours = cv2.findContours(thresh, mode=cv2.RETR_EXTERNAL, method=cv2.CHAIN_APPROX_SIMPLE)
    contours = cv2.findContours(thresh, mode=cv2.RETR_LIST, method=cv2.CHAIN_APPROX_SIMPLE)
    
    if len(contours)>0:
        cnt = contours[0]
        #print(type(cnt))
        area = cv2.contourArea(cnt); print(area)
        x,y,w,h = cv2.boundingRect(cnt); print(x, y, w, h)
        box_img = cv2.rectangle(img,(x,y),(x+w,y+h),(0,255,0),5)
    
        
    #contours = cv2.findContours(img, mode=1, method=2)
    #print(len(contours))    
    
    #cv2.imshow("contours[0]", contours[0])
    #cv2.waitKey(0)
    
    #for i, c in enumerate(contours):
        #area = cv2.contourArea(c); print(area)
    
    
    #cnt = contours[0]; #print(cnt)
    #area = cv2.contourArea(cnt); print(area)
    #cont_img = cv2.drawContours(img, contours[0], -1, (0,255,0), 3)    
    #cv2.imshow("cont_img", cont_img)
    #area = cv2.contourArea(contours[0]); print(area)
    
    ######################
    #x,y,w,h = cv2.boundingRect(cnt); print(x, y, w, h)
    #box_img = cv2.rectangle(img,(x,y),(x+w,y+h),(0,255,0),5)
    #contour_img = cv2.drawContours(img, cnt, -1, (0,255,0), 3)
    
    if show:                     
        # Show keypoints
        cv2.imshow("input image", img)
        cv2.imshow("box_img", box_img)
        cv2.imshow("contours[0]", contours[0])
        #cv2.imshow("img_cvt", img_cvt)
        cv2.waitKey(0)
    
    return

def video2frames(video, frame_prefix, ratio=1, detectBlobs=False):
    """ Take a video and convert to a series of frames in .jpg format. 'ratio' is for resizing the frame 
        Options: 
            ratio: resize the output frame
            detectBlobs: detect blobs
    """
    vid = cv2.VideoCapture(video)
    c=1
    
    if vid.isOpened():
        rval , frame = vid.read()
    else:
        rval = False
    
    while rval:
        print(c)
         
        ### Remove noise ###
        frame = remove_noise(frame)

        ### Fill gaps ###
        frame = fill_gap(frame)

        ### Detect blobs ###
        if detectBlobs:
            blob_keypoints = detect_blobs(frame)
            
            if blob_keypoints:
                ### Rescale frames ###
                if ratio!=1:
                    frame = cv2.resize(frame, None, fx=ratio, fy=ratio)
        
                ### Write frames to files ###            
                cv2.imwrite('./images/' + frame_prefix + str(c) + '.jpg', frame)
        
        c = c + 1
           
        rval, frame = vid.read()   
    vid.release()
    return 
   
def remove_noise(frame):
    """ Remove noise using morphological operation: erode, then diate."""
    ### Morphology: Opening ###
    kernel = np.ones((3,3),np.uint8)
    frame = cv2.morphologyEx(frame, cv2.MORPH_OPEN, kernel, iterations=1)
    return frame    
    
def fill_gap(frame):
    """ Filling gaps using morphological operation: dilate, then erode."""
    ### Morphology: Opening ###
    kernel = np.ones((3,3),np.uint8)
    frame = cv2.morphologyEx(frame, cv2.MORPH_CLOSE, kernel, iterations=5)
    return frame    

def detect_blobs(frame, show=False):
    """ Detect blobs in a frame, if blob detected, return 'keypoints', else, return 'None' """
    ## Set up the detector with parameters.
    params = cv2.SimpleBlobDetector_Params()
 
    # Change thresholds
    params.minThreshold = 0
    params.maxThreshold = 255
    params.thresholdStep = 100
    #params.minDistBetweenBlobs = 100;
    
    # Filter by Color.
    params.filterByColor = True
    params.blobColor = 255         
    
    # Filter by Area.
    params.filterByArea = True
    params.minArea = 200
    params.maxArea = 10000
     
    # Filter by Circularity
    params.filterByCircularity = False #True
    params.minCircularity = 0.01
     
    # Filter by Convexity
    params.filterByConvexity = False #True
    params.minConvexity = 0.01
     
    # Filter by Inertia
    params.filterByInertia =False #True
    params.minInertiaRatio = 0.01
    params.maxInertiaRatio = 0.90
     
    ## Create a detector with the above parameters
    detector = cv2.SimpleBlobDetector_create(params)
 
    # Detect blobs.
    keypoints = detector.detect(frame)
     
    if keypoints:
        #for i in range (0, len(keypoints)):
            #x = keypoints[i].pt[0]
            #y = keypoints[i].pt[1]
            #print(x,y)     
        if show:                     
            # Draw detected blobs as red circles.
            # cv2.DRAW_MATCHES_FLAGS_DRAW_RICH_KEYPOINTS ensures the size of the circle corresponds to the size of blob
            frame_with_keypoints = cv2.drawKeypoints(frame, keypoints, np.array([]), (0,0,255), cv2.DRAW_MATCHES_FLAGS_DRAW_RICH_KEYPOINTS)

            # Show keypoints
            cv2.imshow("Keypoints", frame_with_keypoints)
            cv2.waitKey(0)
    
        return keypoints    
    else:
        return None

if __name__ == '__main__':
    print("imageutil.py is being run directly")
else:
    print("imageutil.py is being imported into another module")
