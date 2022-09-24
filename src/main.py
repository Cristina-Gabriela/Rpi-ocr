import RPi.GPIO as GPIO
import os, time
import integrated

btnpin = 4
slow = False
init = False

GPIO.setmode(GPIO.BCM)
GPIO.setup(btnpin, GPIO.IN)

while True:
    GPIO.wait_for_edge(btnpin, GPIO.FALLING)
    GPIO.wait_for_edge(btnpin, GPIO.RISING)
    print("waiting")
    c = GPIO.wait_for_edge(btnpin, GPIO.FALLING, timeout=200)
    print(c)
    if c:
        # pressed twice
        
        print("pressed twice")
        os.system("aplay twice.wav")
        if init:
            integrated.replay(slow)
            slow = not slow
    else:
        # pressed once
        
        print("pressed once")
        os.system("aplay once.wav")
        success = integrated.main()
        if not init:
            init = success
        slow = True
        
    time.sleep(0.5)
    