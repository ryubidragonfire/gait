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
        self.contours = contours
        self.area = None
        self.boundingRect = None

    def getLargestArea(self):
        return self.area
        
    def getBoundingRect(self):
        return self.boundingRect
        
    def findLargestSilhouette(self):
        areas = [cv2.contourArea(c) for c in self.contours]
        max_index = np.argmax(areas)
        self.area = areas[max_index]
        cnt = self.contours[max_index]        
        self.boundingRect = cv2.boundingRect(cnt); print(self.boundingRect)
        
        
        