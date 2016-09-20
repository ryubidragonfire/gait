# -*- coding: utf-8 -*-
"""
Created on Mon Sep 19 11:49:13 2016

@author: chyam
"""

from __future__ import print_function
import cv2
import numpy as np
from scipy.spatial.distance import pdist, squareform

class Silhouette:
    """ Base class for silhouette."""
    
    def __init__(self, contours):
        self.min_area = 50
        self.contours = contours
        self.finalContour = None
        self.area = None
        self.boundingRect = None
        #self.findLargestSilhouette()
        self.combineLargeSilhouette()

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
                     
            # calculate centres -> a list of centres of type tuple
            # moments is a list of dict; m is a dict
            moments = [cv2.moments(c) for c in self.contours]
            for m in moments:
                if m['m00']!=0:
                    centres.append((int(m['m10']/m['m00']), int(m['m01']/m['m00'])))
                else:
                    centres.append(None) # TODO: check if this will work
                    
            #apply condition for area: True if it is bigger than min_area
            area_boolean = (np.array(areas)>self.min_area)
            area_boolean_list = area_boolean.tolist()
            true_list = [i for i, elem in enumerate(area_boolean_list, 0) if elem==True]
            
            # if > 1 large contours found, check distance of centres, if close enough, join contours as one contour
            if len(true_list) > 1:
                centres_for_large_areas = []
                
                for i in range(len(true_list)):
                    centres_for_large_areas.append(centres[true_list[i]])
                #centres_for_large_areas = centres[area_boolean_list.index(True)]
            #extract centres for large area
            #centres_arr = np.array(centres)
            #large_area_centres_arr = centres_arr[area_boolean]
            
            # join large contours as one contour, if > 1 large contours found
            #if len(large_area_centres_arr) > 1:
             #   join_contour()
                
            #else: 
                #self.finalContour = self.contours[]
                
            #large_area_centres = centres[list(area_condition[0])]
            #large_area_centres = np.extract(area_condition, np.array(centres))
            
            #centres_dist = pdist(large_area_centres)
                     
                     
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
        
    def join_contour(self):
        print("join_contour() --------")
        
        #self.finalContour
        return 
        
        