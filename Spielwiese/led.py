#!/usr/bin/python
#-*- coding: utf-8 -*-

import RPi.GPIO as gpio
import time
#gpio.cleanup()

gpio.setmode(gpio.BCM)

#gpio.setup(17,gpio.IN,pull_up_down=gpio.PUD_UP)
gpio.setup(4, gpio.OUT)

#while True:
#	buttonPressed = gpio.input(17)
#	if buttonPressed == 1:
#		gpio.output(4, gpio.LOW)
#	if buttonPressed == 0:
#		gpio.output(4, gpio.HIGH)


#gpio.setup(17,gpio.OUT)

#farbe = input("gelb oder grün?")

#if farbe == "gelb":
#    gpio.output(4, gpio.HIGH)
#    time.sleep(2)
#    gpio.output(4, gpio.LOW)

#if farbe == "grün"#:
#    gpio.output(17, gpio.HIGH)
#    time.sleep(2)
#    gpio.output(17, gpio.LOW)

sek = input("Stoppuhr Sekunden: ")

while sek > 0:
	sek = int(sek)
	sek = sek - 1
	time.sleep(1)
	print(sek)

gpio.output(4, gpio.HIGH)
time.sleep(1)
gpio.output(4, gpio.LOW)


gpio.cleanup()
