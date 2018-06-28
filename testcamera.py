#!/usr/bin/python
# -*-coding=utf-8
from __future__ import print_function, division
import unittest

from onvif import ONVIFCamera, ONVIFError

CAM_HOST = '10.1.3.131'
CAM_PORT = 80
CAM_USER = 'admin'
CAM_PASS = 'password'

DEBUG = False

cam = ONVIFCamera(CAM_HOST, CAM_PORT, CAM_USER, CAM_PASS)

time = cam.devicemgmt.GetSystemDateAndTime()

print(time)
