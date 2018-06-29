#!/usr/bin/python
# -*-coding=utf-8
from __future__ import print_function, division
import unittest

from onvif import ONVIFCamera, ONVIFError

CAM_HOST = '10.1.3.10'
CAM_PORT = 80
CAM_USER = 'root'
CAM_PASS = 'password'

DEBUG = False


def log(ret):
    if DEBUG:
        print(ret)


class TestDevice(unittest.TestCase):
    # Class level cam. Run this test more efficiently..
    cam = ONVIFCamera(CAM_HOST, CAM_PORT, CAM_USER, CAM_PASS)

    # ***************** Test Capabilities ***************************
    def test_GetWsdlUrl(self):
        ret = self.cam.devicemgmt.GetWsdlUrl()

    def test_GetHostname(self):
        ''' Get the hostname from a device '''
        self.cam.devicemgmt.GetHostname()

    def test_GetServiceCapabilities(self):
        '''Returns the capabilities of the devce service.'''
        ret = self.cam.devicemgmt.GetServiceCapabilities()

    def test_GetDNS(self):
        ''' Gets the DNS setting from a device '''
        ret = self.cam.devicemgmt.GetDNS()
        self.assertTrue(hasattr(ret, 'FromDHCP'))
        if not ret.FromDHCP and len(ret.DNSManual) > 0:
            log(ret.DNSManual[0].Type)
            log(ret.DNSManual[0].IPv4Address)

    def test_GetNTP(self):
        ''' Get the NTP settings from a device '''
        ret = self.cam.devicemgmt.GetNTP()
        if ret.FromDHCP == False:
            self.assertTrue(hasattr(ret, 'NTPManual'))
            log(ret.NTPManual)


if __name__ == '__main__':
    unittest.main()
