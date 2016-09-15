# Gait Recognition Deep Learning
# Installation
Go to http://www.lfd.uci.edu/~gohlke/pythonlibs/#opencv to get the precompiled binaries for windows. For example: `opencv_python-3.1.0-cp34-cp34m-win_amd64.whl` means openCV3.1.0, python 3.4 on Windows 64-bit. In your `winpython`, do:
	`pip install --upgrade --no-deps opencv_python-3.1.0-cp34-cp34m-win_amd64.whl`

Then try:
   
    > python
    >> import cv2


### Data for human gaits

| Databases | Release Agreement |
|-----------|-------------------|
| [Osaka University](http://www.am.sanken.osaka-u.ac.jp/BiometricDB/GaitLP.html)       | Yes |
| [Technische Universität München](https://www.mmk.ei.tum.de/verschiedenes/tum-iitkgp-gait-database) | No|
| [Southampton University](http://www.gait.ecs.soton.ac.uk/database/)| Yes |
| [Centre for Biometrics & Security Research](http://www.cbsr.ia.ac.cn/english/Gait%20Databases.asp) | Yes |

Database used in this example is from Technische Universität München.

### Image Pre-processing

A series of image processing techniques are used to extract only frames with human walking. They include noise removal and blob detection. The code is available [here](https://github.com/ryubidragonfire/gait).


    