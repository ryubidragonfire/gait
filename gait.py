# -*- coding: utf-8 -*-
"""
Created on Mon Sep 19 11:49:13 2016

@author: chyam
"""

from __future__ import print_function
import cv2
import numpy as np

class Silhouette:
    """ Base class for silhouette."""
    
    def __init__(self, contours):
        self.min_area = 50
        self.contours = contours
        self.area = None
        self.boundingRect = None
        self.findLargestSilhouette()
        #self.combineLargeSilhouette()

    def getLargestArea(self):
        return self.area
        
    def getBoundingRect(self):
        return self.boundingRect
        
    def findLargestSilhouette(self):
        areas = [cv2.contourArea(c) for c in self.contours]
        max_index = np.argmax(areas)
        self.area = areas[max_index]
        cnt = self.contours[max_index]        
        self.boundingRect = cv2.boundingRect(cnt); #print(self.boundingRect)
        return
        
    def combineLargeSilhouette(self):
        """ Combine multiple large areas as one.""" 
        # If there are >1 contours
        if len(self.contours)>1:
            centres = []

            # calculate areas -> a list of areas
            areas = [cv2.contourArea(c) for c in self.contours]
                     
            # calculate centres -> a list of centres
            moments = [cv2.moments(c) for c in self.contours]
            for m in moments:
                if m['m00']!=0:
                    centres.append((int(m['m10']/m['m00']), int(m['m01']/m['m00'])))
                else:
                    centres.append(None) # TODO: check if this will work
                     
                     
            #areas = np.array[areas]
            #large_area_index_tuple = np.where(areas > self.min_area)
            #large_area_index = list[large_area_index_tuple[0]]
            
            #large_areas = [a for a in areas if a>self.min_area]
            
                     
                     
            #area_index = np.argsort(areas)[::-1] #sort from big to small
            # calculate centre of blobs
            #moments = [cv2.moments(c) for c in self.contours]
            #for m in moments:
            #    centres.append((int(m['m10']/m['m00']), int(m['m01']/m['m00'])))
            print('==================')

        
        return
        
        