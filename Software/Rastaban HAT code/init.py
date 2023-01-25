"""
This code should be run once when the pi has been booted up. This code starts the PIGPIOD deamon.
After it has been run, the pigpiod functions should be usable.
"""

import subprocess
import pigpio
import time

# see if it is running already
status, process = subprocess.getstatusoutput('sudo pidof pigpiod')

if status:  # it wasn't running, so start it
    print("pigpiod was not running")
    subprocess.getstatusoutput('sudo pigpiod')  # try to  start it
    time.sleep(0.5)
    # check it again
    status, process = subprocess.getstatusoutput('sudo pidof pigpiod')

if not status:  # if it was started successfully (or was already running)...
    pigpiod_process = process
    print("pigpiod is running, process ID is {} ".format(pigpiod_process))

    try:
        pi = pigpio.pi()  # local GPIO only
        print("pigpio's pi instantiated")
    except Exception as e:
        start_pigpiod_exception = str(e)
        print("problem instantiating pi: {}".format(start_pigpiod_exception))
else:
    print("start pigpiod was unsuccessful.")
