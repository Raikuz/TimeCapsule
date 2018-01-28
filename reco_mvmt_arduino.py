# LIB A INSTALLER :
# pySerial
# moviepy
# pygame
# screeninfo
# imageio ?
# msvcrt ?
import imageio
imageio.plugins.ffmpeg.download()
from msvcrt import getch
from serial import Serial
import os
from threading import Thread
import moviepy
from moviepy.editor import *
import pygame
from screeninfo import get_monitors
ser = Serial(port='COM4', baudrate=9600)
m = get_monitors()
isPlaying = False
last_received = ''

#Fonction de recuperation de l'interaction arduino
def receiving(ser):
	global last_received
	while True:
		val = ser.readline()
		result = val.decode('ascii')
		last_received = result[0]

#Gestionnaire de la video
def playvideo():
	#I changed in Python\Python36-32\Lib\site-packages\moviepy\video\io preview.py line 94
	#screen = pg.display.set_mode(clip.size) to
	#screen = pg.display.set_mode(clip.size,pg.FULLSCREEN)
	pygame.init ()
	clip = VideoFileClip('thomas.mp4') #Changer le nom de la video
	clipresized = clip.resize (height=m[0].height,width=m[0].width)
	clipresized.set_pos((0,0))
	clipresized.preview ()
	pygame.quit ()
		
#Boucle Principale
Thread(target=receiving, args=(ser,)).start()
while True:
        # Absence d'objet: 1
        # Objet présent: 0
		if last_received == "0" and isPlaying == False:
			print("LANCEMENT VIDEO")
			last_received = "1"
			isPlaying = True
		elif isPlaying == True:
			playvideo()
			isPlaying = False