# -*- coding: utf-8 -*-
"""
Created on Wed Sep 14 15:19:47 2016

@author: chyam
"""

from __future__ import print_function

import imageutilities as iu

file_avi = 'C:/Users/chyam/OneDrive - Microsoft/Data/Gait/tumiitgait/uploaded_video/Normal Walk/normal_id001_1.avi'
iu.video2frames(file_avi, file_avi[-18:-4]+'-', 0.25, detectBlobs=True)
    
if __name__ == '__main__':
    print("analyse-gait.py is being run directly")
else:
    print("analyse-gait.py is being imported into another module")

