#IMPORT POTRZEBNYCH BIBLIOTEK
import gaugette.ssd1306
import time
import sys

#USTAWIENIE ZMIENNYCH
RESET_PIN = 5 #(GPIO 24)
DC_PIN    = 4 #(GPIO 23)

led = gaugette.ssd1306.SSD1306(reset_pin=RESET_PIN, dc_pin=DC_PIN)
led.begin()
led.clear_display()

led.draw_text2(0,0,"KRPi!",2)
led.draw_text2(0,16,"KRPi!",1)
led.draw_text2(32,25,"KRPi!",1)
led.display()
