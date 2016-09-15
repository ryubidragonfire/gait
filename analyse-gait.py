# -*- coding: utf-8 -*-
"""
Created on Wed Sep 14 15:19:47 2016

@author: chyam
"""

from __future__ import print_function
import imageutil as iu
  
if __name__ == '__main__':

    file_avi = './data/normal_id001_1.avi'
    iu.video2frames(file_avi, file_avi[-18:-4]+'-', 0.25, detectBlobs=True)


