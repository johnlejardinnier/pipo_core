#!/usr/bin/python
import Pipo
import time

M_CONF = [
    {
        "name": "M1",
        "pins":[36, 38, 40],
        "pwm_pin": 40,
        "forward":[1, 0, 1],
        "backward":[0, 1, 1],
    },
    {
        "name": "M2",
        "pins":[19, 21, 23],
        "pwm_pin": 19,
        "forward":[1, 0, 1],
        "backward":[1, 1, 0]
    },
    {
        "name": "M3",
        "pins":[11, 13, 15],
        "pwm_pin": 11,
        "forward":[1, 1, 0],
        "backward":[1, 0, 1]
    },
    {
        "name": "M4",
        "pins":[22, 24, 26],
        "pwm_pin": 26,
        "forward":[0, 1, 1],
        "backward":[1, 0, 1]
    }

]

S_CONF = {
    "pin_sig": 33,
    "pin_trig": 31,
    "pin_echo": 29
}


Pipo = Pipo.Pipo(M_CONF, S_CONF)
time.sleep(2)
#Pipo.backward()
#time.sleep(10)
Pipo.forward()
#time.sleep(20)
#Pipo.stop()

#Pipo.backward()
#time.sleep(2)
#Pipo.stop()
