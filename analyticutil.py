# -*- coding: utf-8 -*-
"""
Created on Mon Sep 19 12:43:20 2016

@author: chyam
"""

from __future__ import print_function

import numpy as np
import gait
import statistics as s

def find_sillhouette_mode_area(sil_list):
    area_list = [sil.area for sil in sil_list]
    mode_area = s.mode(area_list); #print(mode_area)
    return mode_area
    
def find_sillhouette_mode_boundingRect(sil_list):
    boundingRect_list = [sil.boundingRect for sil in sil_list]
    w_list = [b[2] for b in boundingRect_list]
    h_list = [b[3] for b in boundingRect_list]   
    mode_w = s.mode(w_list)
    mode_h = s.mode(h_list)
    return (mode_w, mode_h)
    
if __name__ == '__main__':
    print("analyticutil.py is being run directly")
else:
    print("analyticutil.py is being imported into another module")