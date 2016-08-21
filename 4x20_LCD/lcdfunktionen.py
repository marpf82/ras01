#!/usr/bin/python
# -*- coding: utf-8 -*-

import serial
import time

lcd = serial.Serial("/dev/serial/by-id/usb-Silicon_Labs_CP2102_USB_to_UART_Bridge_Controller_0001-if00-port0", 9600)


# Hier kommen die Funktionsdefinitionen Rein ##########################################################################

# 1. Write Text in Row  (Parameter: Rownumber)
def write(row, text):
    lcd.write("\xFE")
    lcd.write("\x47")
    lcd.write("\x01")
    lcd.write(chr(row))
    lcd.write(text)
    time.sleep(0.025)


# 1.1 Clear a single Row (Parameter: Rownumber)
def clearline(row):
    lcd.write("\xFE")
    lcd.write("\x47")
    lcd.write("\x01")
    lcd.write(chr(row))
    lcd.write("                    ")
    time.sleep(0.025)


# 1.1.1 Clears the whole screen
def clearscreen():
    for row in range(1, 5):
        clearline(row)


# 2. Adjust LCD Contrast Ranging from 0x01 to 0xFE (1 - 254) wobei 0 voller Contrast ist und 254 kein Contrast
def setcontrast(value):
    lcd.write("\xFE")
    lcd.write("\x50")
    lcd.write(chr(value))


# 3. Adjust Backlight Brightness Ranging from 0x01 to 0xFE (1 - 254)
def setbrightness(value):
    lcd.write("\xFE")
    lcd.write("\x98")
    lcd.write(chr(value))


# 4. Turn the Backlight off //////////////////////////
def backlight_off():
    lcd.write("\xFE")
    lcd.write("\x46")
    time.sleep(0.025)


# 5. Turn the Backlight on ///////////////////////////
def backlight_on():
    lcd.write("\xFE")
    lcd.write("\x42")
    lcd.write("\x00")
    time.sleep(0.025)


# 6. keine Ahnung was das tut
def pattern(row, text):
    lcd.write("\xFE")
    lcd.write("\x4E")
    lcd.write(chr(row))
    lcd.write(text)
    time.sleep(0.025)


# 7. Auslesen des LCD Contrast und gibt sie als Returnwert zurück
def getcontrast():
    lcd.write("\xFE")
    lcd.write("\x63")
    time.sleep(0.025)
    return lcd.readline(5)


# 8. Auslesen der LCD Backlight Stärke und gibt sie als Returnwert zurück
def getbrightness():
    lcd.write("\xFE")
    lcd.write("\x62")
    time.sleep(0.025)
    return lcd.readline(7)


# 9. Auslesen der Versionsnummer und gibt sie als Returnwert zurück
def getversion():
    lcd.write("\xFE")
    lcd.write("\x76")
    time.sleep(0.025)
    return lcd.readline(11)

# 9.1 Auslesen der Bildschirmauflösung aus dem Returnwert von getVersion()
def getresolution():
    lcd.write("\xFE")
    lcd.write("\x76")
    time.sleep(0.025)
    r = lcd.readline(11)
    Resolution = r[0:2] + "x" + r[2:4]
    return Resolution


# 10. Fragt die Temperatur des im Display verbauten Soc ab und gibt sie als Returnwert zurück
def gettemp():
    lcd.write("\xFE")
    lcd.write("\x77")
    time.sleep(0.025)
    return lcd.readline(5)


# 11. Schreibt Temp in die Uebergebene Zeile
def temp(row):
    lcd.write("\xFE")
    lcd.write("\x57")
    lcd.write(chr(row))
    time.sleep(0.025)


# 12. Serielle Kommunikation etablieren
def establishcommunication():
    lcd.write("\xFE")
    lcd.write("\x53")
    lcd.write("\x75")
    lcd.write("\x72")
    lcd.write("\x65")
    time.sleep(0.025)


# 13. Schreibt irgendwas in die Uebergebene Zeile
def unknown(row, text):
    lcd.write("\xFE")
    lcd.write("\x48")
    lcd.write("\x01")
    lcd.write(hex(row))
    lcd.write(text)
    time.sleep(0.025)


# 14. Temperatur Einheit festlegen (Parameter: Value kann  C oder F sein)
def settempunit(value):
    lcd.write("\xFE")
    lcd.write("\x57")
    lcd.write(value)
    time.sleep(0.025)


# 15. Anzeige auf dem LCD Aus/Anschalten ist optisch nicht sichtbar am Display.
# Einmal Ausführen = Display aus. Zweimal = Display an
def displayonoff():
    lcd.write("\xFE")
    lcd.write("\x64")
    time.sleep(0.025)


# 16. Schaltet zurück auf Demomode
def demo():
    lcd.write("\xFE")
    lcd.write("\x66")
    time.sleep(0.025)


# Ende der Funktionsdefinitionen ++++++++++++++++++++++++++++++++++++++++++++++++++++++++++

# Hier beginnt das Hauptprogramm ++++++++++++++++++++++++++++++++++++++++++++++

# // zuerst die Kommunikation starten

establishcommunication()
clearscreen()  # Loescht den gesamten aktuellen Inhalt des LCD

write(1, "DEBUG AUSGABE".center(20))

lt = time.localtime()
YYYY, MM, DD, hh, mm = lt[0:5]
Datum = "%02i.%02i.%04i" % (MM,DD,YYYY)
Zeit = "%02i:%02i" % (hh,mm)

write(3, Zeit.center(20))
write(4, Datum.center(20))
