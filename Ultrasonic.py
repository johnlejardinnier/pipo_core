#!/usr/bin/python
import RPi.GPIO as GPIO
import time


class Ultrasonic:

    SLEEP_INIT = 0.5
    SLEEP_TRIG = 0.00001
    GPIO_SIG = None

    GPIO_TRIGGER = None
    GPIO_ECHO = None

    MIN_DIST = 2
    MAX_DIST = 100
    COEFF_DIST = 10

    def __init__(self, GPIO_SIG, GPIO_TRIGGER, GPIO_ECHO):
        GPIO.setmode(GPIO.BOARD)
        self.GPIO_SIG = GPIO_SIG
        self.GPIO_TRIGGER = GPIO_TRIGGER
        self.GPIO_ECHO = GPIO_ECHO

    def __front_distance(self):
        self.MIN_DIST = 1
        GPIO.setmode(GPIO.BOARD)
        GPIO.setup(self.GPIO_SIG, GPIO.OUT)
        GPIO.output(self.GPIO_SIG, 0)
        time.sleep(self.SLEEP_INIT)

        GPIO.output(self.GPIO_SIG, 1)
        time.sleep(self.SLEEP_TRIG)
        GPIO.output(self.GPIO_SIG, 0)
        start = time.time()

        GPIO.setup(self.GPIO_SIG, GPIO.IN)

        while GPIO.input(self.GPIO_SIG) == 0:
            start = time.time()

        while GPIO.input(self.GPIO_SIG) == 1:
            stop = time.time()

        elapsed = stop - start
        distance = elapsed * 34000
        distance = distance / 2

        #print ("front: " + str(distance))

        return round(distance)

    def __back_distance(self):
        self.MIN_DIST = 10
        # use pin numbers
        GPIO.setmode(GPIO.BOARD)

        GPIO.setwarnings(False)

        GPIO.setup(self.GPIO_TRIGGER, GPIO.OUT)  # Trigger
        GPIO.setup(self.GPIO_ECHO, GPIO.IN)  # Echo

        GPIO.output(self.GPIO_TRIGGER, 0)

        time.sleep(self.SLEEP_INIT)

        GPIO.output(self.GPIO_TRIGGER, 1)
        time.sleep(self.SLEEP_TRIG)
        GPIO.output(self.GPIO_TRIGGER, 0)
        start = time.time()

        while GPIO.input(self.GPIO_ECHO) == 0:
            start = time.time()

        while GPIO.input(self.GPIO_ECHO) == 1:
            stop = time.time()

        elapsed = stop - start
        distance = elapsed * 34000
        distance = distance / 2

        #print ("back: " + str(distance))

        return round(distance)

    def get_speed_rate(self, mode):

        #print ("mode: " + str(mode))

        if mode == True:
            distance = self.__front_distance()
        else:
            distance = self.__back_distance()

        #print ("distance: " + str(distance))

        if distance <= self.MIN_DIST:
            return 0
        elif distance >= self.MAX_DIST:
            return abs(1 * self.COEFF_DIST)
        else:
            #print("calc: " + str(distance) + "/" + str(self.MAX_DIST) + "*" + str(self.COEFF_DIST))
            return abs(1 + (round(distance) / self.MAX_DIST) * self.COEFF_DIST)
