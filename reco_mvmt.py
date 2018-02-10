# LIB A INSTALLER :
# pySerial
# moviepy
# pygame
# screeninfo
# imageio ?
# msvcrt ?
import imageio
imageio.plugins.ffmpeg.download()
import getch
from serial import Serial
import os
from threading import Thread
import moviepy
from moviepy.editor import *
import pygame
from screeninfo import get_monitors

m = get_monitors()
isPlaying = False
last_received = ''


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
while True:
        # Absence d'objet: 1
        # Objet présent: 0
		playvideo()
