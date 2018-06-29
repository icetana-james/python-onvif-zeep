#!/usr/bin/python
# -*-coding=utf-8
from __future__ import print_function, division
import signal
from contextlib import contextmanager
from onvif import ONVIFCamera, ONVIFError


class TimeoutException(Exception):
    pass


@contextmanager
def time_limit(seconds):
    """
    Provides a means to cap the maximum amount of time that a function can run before it is forcefully aborted.
    This is particularly useful when using libraries that create socket connections without providing the ability to
    set a timeout value.
    Usage:
    >>> try:
    >>>   with time_limit(10):
    >>>     long_function_call()
    >>> except TimeoutException as e:
    >>>   print("Timed out!")
    :param seconds: the number of seconds that a function can run before it is terminated.
    """

    # https://stackoverflow.com/questions/366682/how-to-limit-execution-time-of-a-function-call-in-python
    def signal_handler(signum, frame):
        raise TimeoutException("Timed out!")

    signal.signal(signal.SIGALRM, signal_handler)
    signal.alarm(seconds)
    try:
        yield
    finally:
        signal.alarm(0)


CAM_PORT = 80

DEBUG = False

auth_attempts = [
    ('admin', 'password'),
    ('root', 'password',),
    ('-', '-')
]

for index in range(100, 255):
    CAM_HOST = '10.1.3.' + str(index)
    print("checking {} ...".format(CAM_HOST))
    for CAM_USER, CAM_PASS in auth_attempts:
        try:
            with time_limit(5):
                cam = ONVIFCamera(CAM_HOST, CAM_PORT, CAM_USER, CAM_PASS)
                deviceInfo = cam.devicemgmt.GetDeviceInformation()
                model = deviceInfo.Model
                manufacturer = deviceInfo.Manufacturer
                print("                OK:{}-{}:{}".format(CAM_HOST, manufacturer, model))
            break
        except ONVIFError as e:
            pass

print("done")
