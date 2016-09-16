# -*- coding: utf-8 -*-
"""
Created on Wed Sep 14 15:19:47 2016

@author: chyam
"""

from __future__ import print_function
import imageutil as iu
import re
import os
  
def do_video2frames():
    file_avi = './data/normal_id001_1.avi'
    iu.video2frames(file_avi, file_avi[-18:-4]+'-', 0.25, detectBlobs=True)
    
    return
    
def do_box_sillouette():
    directory = './images/'
    flist = os.listdir(directory)
    # Sort according to frame number
    flist = sorted(flist, key=lambda x: (int(re.sub('\D','',x)),x))
    
    for f in flist:
        fname = os.path.join(directory, f); print(fname)
        iu.box_sillhouette(fname, show=True)
    return

if __name__ == '__main__':

    #do_video2frames()
    do_box_sillouette()
    

        
   
    


