#!/usr/bin/python
# coding=utf8

print("Start des Programms")
import serial
from time import *
import string
import subprocess


t = subprocess.Popen(['./sht21','S'], stdout=subprocess.PIPE)
T = str(t.stdout.read()[0:7])
print T

"""t.remove (0)
Temp, Humi = t[0:2]

print "%02i:%02i" % (Temp,Humi)"""
