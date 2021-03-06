#!/usr/bin/env python
from __future__ import division
from subprocess import PIPE, Popen
import time
import psutil
import sys
import RPi.GPIO as GPIO

GPIO.setmode(GPIO.BCM)
GPIO.setup(18, GPIO.OUT)


def get_cpu_temperature():
    process = Popen(['vcgencmd', 'measure_temp'], stdout=PIPE)
    output, _error = process.communicate()
    return float(output[output.index('=') + 1:output.rindex("'")])

    if __name__ == '__main__':
        main()

try:
    compteur = 1
    while compteur<5:
        def main():
            cpu_temperature = get_cpu_temperature()
        
        max_temp = 41
        min_temp = 35

        if get_cpu_temperature() > max_temp:
            while get_cpu_temperature() > min_temp:
                GPIO.output(18, True)
                time.sleep(5)
            GPIO.output(18, False)
        else:
            GPIO.output(18, False)
            time.sleep(5)
        
        

except KeyboardInterrupt:
    GPIO.output(18, False)
    sys.exit(1)

    