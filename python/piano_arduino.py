import sys, getopt
import pygame
import time
import serial

_arduinoPort = '/dev/ttyACM0'
_arduinoBaudrate = 115200
_nbKeys = 6
_minDelayBetweenNotes =0.8
_minThresholdNotes = 850

def loadNoteSounds():
	do = pygame.mixer.Sound("../data/sound/4-c.wav")
	re = pygame.mixer.Sound("../data/sound/4-d.wav")  
	mi = pygame.mixer.Sound("../data/sound/4-e.wav")
	fa = pygame.mixer.Sound("../data/sound/4-f.wav")
	sol = pygame.mixer.Sound("../data/sound/4-g.wav")
	la = pygame.mixer.Sound("../data/sound/4-a.wav")
	
	return do, re, mi, fa, sol, la

def main(argv):
	
	# inits pygame
	print("[INFO] Initializes pygame")
	pygame.init()
	pygame.mixer.init()
	
	# loads the sounds corresponding to the notes
	print("[INFO] Loads note sounds")
	do, re, mi, fa, sol, la = loadNoteSounds()
	notes = [do, re, mi, fa, sol, la] 
	notesCurrentState = [0, 0, 0, 0, 0, 0]
	notesLastState = [0, 0, 0, 0, 0, 0]
	notesFirstTimeClicked = [time.time() for i in range(_nbKeys)]  
	
	#inits connection to Arduino board
	print("[INFO] Connects to Arduino board")
	ser = serial.Serial(_arduinoPort, _arduinoBaudrate) 
	
	# discards data to reset the serial buffer
	for i in range(20):             
		line = ser.readline()
	
	# enters main loop checking for key inputs
	print("[INFO] Enters the main loop")
	print("[INFO] Plays piano using velostat keys")
	try:
		while True:
			line = ser.readline().decode().strip()
			keysValues = line.split(',')
			print(keysValues)
			for i in range(len(keysValues[:-1])):
				if int(keysValues[i]) >= _minThresholdNotes:
					notesCurrentState[i] = 1
				else:
					notesCurrentState[i] = 0
				if notesCurrentState[i] != notesLastState[i]:
					if time.time() - notesFirstTimeClicked[i] >= _minDelayBetweenNotes:
						pygame.mixer.Channel(i).play(pygame.mixer.Sound(notes[i]))
				
					notesFirstTimeClicked[i] = time.time()

				notesLastState[i] = notesCurrentState[i]
						
		print("[INFO] Closes the program, bye bye")
		
	except KeyboardInterrupt:
		print("[WARNING] Interruption of the main loop")

if __name__ == "__main__":
    main(sys.argv[1:])
