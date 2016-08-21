#!/usr/bin/python
#-*- coding: utf-8 -*-

import serial
import time
import subprocess
import urllib
import json

lcd = serial.Serial("/dev/serial/by-id/usb-Silicon_Labs_CP2102_USB_to_UART_Bridge_Controller_0001-if00-port0", 9600)

# Hier kommen die Funktionsdefinitionen Rein +++++++++++++++++
# Start Communication ///////////////
def establishCommunication():
    lcd.write("\xFE")
    lcd.write("\x53")
    lcd.write("\x75")
    lcd.write("\x72")
    lcd.write("\x65")
    time.sleep(0.025)

# Clear a single Row (Parameter: Rownumber) /////////
def Clearline(row):
    lcd.write("\xFE")
    lcd.write("\x47")
    lcd.write("\x01")
    lcd.write(chr(row))
    lcd.write("                    ")
    time.sleep(0.025)

# Clears the whole screen ////////////////////////////
def Clearscreen():
    for row in range(1, 5):
        Clearline(row)

# Write a single Row (Parameter: Rownumber, Text) >row<////////////
def Write(row, text):
    # LCD in der Zeile >row< ausgeben koennen
    lcd.write("\xFE")
    lcd.write("\x47")
    lcd.write("\x01")
    lcd.write(chr(row))
    lcd.write(text)
    time.sleep(0.025)

# Ende der Funktionsdefinitionen ++++++++++++++++++++++++++++++++++++++++++++++++++++++++++

# Hier beginnt das Hauptprogramm ++++++++++++++++++++++++++++++++++++++++++++++

#// zuerst die Kommunikation starten
establishCommunication()
Clearscreen() #Loescht den gesamten aktuellen Inhalt des LCD

#Fuehrt die Schleife alle 10 Minuten aus(notwendig fuer Wetterdaten aus dem Internet und damit es immer aktuelle Werte gibt)
while True:
	#holt die Wetterdaten als JSON Objekt aus dem Internet ab
	jsonstr = urllib.urlopen('http://api.openweathermap.org/data/2.5/weather?q=Vienna,at&units=metric&lang=&lang=de&APPID=dd54446e9ff8c59e593931edfbdd6437').read()
	j = json.loads(jsonstr)
	
#Schleife die alle 60 Sekunden ausgeführt wird um aktuelle Anzeige der Zeit zu gewährleiste. Nach 10 Durchlaeufen beginnt das Programm von ganz vorn und holt neue Wetterdaten	
	i=0
	while  i<=9:

		# aktuelle, lokale Zeit als Tupel + entpacken des Tupels
		lt = time.localtime()
		YYYY, MM, DD, hh, mm = lt[0:5]
	
		#Clearscreen() #Loescht den gesamten aktuellen Inhalt des LCD
	
		#Zeit und Datum zusammenstellen
		Zeit = "%02i:%02i" % (hh,mm)
		Datum = "%02i.%02i.%04i" % (MM,DD,YYYY)

		#Ausfuehren des Programms sht21 >> liest die Temperatur und Luftfeuchte vom Sensor und gibt die Werte an T zurueck
		T = subprocess.Popen(['./sht21','S'], stdout=subprocess.PIPE)

		#Werte des Sensors in String wandeln und zurechtschneiden
		t = str (T.stdout.read()[0:7])
		temp = "%s 'C" % (t[0:4])
		humi = "Luftfeuchte %s %%" % (t[5:7])

		# Seite 1 Schreibt die Innentemperatur auf das LCD-Display legt dabei fest das alle Zeilen 20 Zeichen lang sind und der Inhalt Zentriert wird
		Write(1, "Raumtemperatur".center(20))
		Write(2, temp.center(20))
		Write(3, humi.center(20))
		Write(4, Zeit.center(20))

		#warte 20 Sekunden bis die Außen Temp angezeigt wird
		time.sleep(20)

		Clearscreen() #Loescht den gesamten aktuellen Inhalt des LCD

		# Seite 2 Schreibt die Außentemperatur auf das LCD-Display legt dabei fest das alle Zeilen 20 Zeichen lang sind und der Inhalt Zentriert wird
		Write(1, (j['name']+" "+j['sys']['country']).center(20))
		Write(2, ("Temp akt "+(str(j['main']['temp']))+" 'C").center(20))
		Write(3, ("Temp min "+(str(j['main']['temp_min']))+" 'C").center(20))
		Write(4, ("Temp max "+(str(j['main']['temp_max']))+" 'C").center(20))

		#wartet 20 Sekunden und zeigt min max Temp, sowie weitere Werte an
		time.sleep(20)

		# Seite 3 Schreibt weitere Wetterdaten auf das LCD-Display legt dabei fest das alle Zeilen 20 Zeichen lang sind und der Inhalt Zentriert wird
		#Write(1, (str(j['weather'][0]['description'])).center(20))
		Write(2, ("Wind "+(str(j['wind']['speed']))+" mps").center(20))
		Write(3, ("Luftfeuchtigkeit "+(str(j['main']['humidity']))+"%").center(20))
		Write(4, ("Luftdruck "+(str(j['main']['pressure']))+" hPa").center(20))	

		#wartet 20 Sekunden und beginnt die Schleife dann von vorn
		time.sleep(20)
		# Zaehler für die Schleife um 1 erhoehen
		i +=1


# Ende des Hauptprogramms ++++++++++++++++++++++++++++++++++++

