import sys, getopt
import pygame
import time


def loadNoteSounds():
	lad1 = pygame.mixer.Sound("../data/sound/3-a#.wav")
	si1= pygame.mixer.Sound("../data/sound/3-b.wav")
	do1 = pygame.mixer.Sound("../data/sound/4-c.wav")
	dod1 = pygame.mixer.Sound("../data/sound/4-c#.wav")
	re1= pygame.mixer.Sound("../data/sound/4-d.wav") 
	red1 = pygame.mixer.Sound("../data/sound/4-d#.wav")
	mi1 = pygame.mixer.Sound("../data/sound/4-e.wav")
	fa1 = pygame.mixer.Sound("../data/sound/4-f.wav")
	fad1 = pygame.mixer.Sound("../data/sound/4-f#.wav")
	sol1 = pygame.mixer.Sound("../data/sound/4-g.wav")
	sold1 = pygame.mixer.Sound("../data/sound/4-g#.wav")
	la1 = pygame.mixer.Sound("../data/sound/4-a.wav")
	lad2 = pygame.mixer.Sound("../data/sound/4-a#.wav")
	si2 = pygame.mixer.Sound("../data/sound/4-b.wav")
	do2 = pygame.mixer.Sound("../data/sound/5-c.wav")
	return lad1, si1, do1, dod1, re1, red1, mi1, fa1, fad1, sol1, sold1, la1, lad2, si2, do2 

def main(argv):
	
	# inits pygame
	print("[INFO] Initializes pygame")
	pygame.init()
	pygame.mixer.init()
	
	#creates a window
	print("[INFO] Creates a default window")
	screen = pygame.display.set_mode((128, 96))
	pygame.display.set_caption('Piano_keyboard')
	pygame.mouse.set_visible(0)
	
	# loads the sounds corresponding to the notes
	print("[INFO] Loads note sounds")
	lad1, si1, do1, dod1, re1, red1, mi1, fa1, fad1, sol1, sold1, la1, lad2, si2, do2 = loadNoteSounds()
	
	# enters main loop checking for key inputs
	print("[INFO] Enters the main loop")
	print("[INFO] Plays piano using keyboard: A, Q, S, E, D, R, F, G, Y, H, U, J, I, K, L")
	try:
		while True:
			for event in pygame.event.get():
				if event.type == pygame.QUIT:
					pygame.quit()
					sys.exit()
				
				if event.type == pygame.KEYDOWN:	
					if event.key == pygame.K_x:
						pygame.quit()
						sys.exit()
						
					#clavier
					if event.key == pygame.K_a:
						pygame.mixer.Channel(0).play(pygame.mixer.Sound(lad1))
				
					if event.key == pygame.K_q:
						pygame.mixer.Channel(0).play(pygame.mixer.Sound(si1))
						
					if event.key == pygame.K_s:
						pygame.mixer.Channel(0).play(pygame.mixer.Sound(do1))
						
					if event.key == pygame.K_e:
						pygame.mixer.Channel(0).play(pygame.mixer.Sound(dod1))
						
					if event.key == pygame.K_d:
						pygame.mixer.Channel(0).play(pygame.mixer.Sound(re1))
						
					if event.key == pygame.K_r:
						pygame.mixer.Channel(0).play(pygame.mixer.Sound(red1))
						
					if event.key == pygame.K_f:
						pygame.mixer.Channel(0).play(pygame.mixer.Sound(mi1))
					
					if event.key == pygame.K_g:
						pygame.mixer.Channel(0).play(pygame.mixer.Sound(fa1))
						
					if event.key == pygame.K_y:
						pygame.mixer.Channel(0).play(pygame.mixer.Sound(fad1))
					
					if event.key == pygame.K_h:
						pygame.mixer.Channel(0).play(pygame.mixer.Sound(sol1))
						
					if event.key == pygame.K_u:
						pygame.mixer.Channel(0).play(pygame.mixer.Sound(sold1))
						
					if event.key == pygame.K_j:
						pygame.mixer.Channel(0).play(pygame.mixer.Sound(la1))
						
					if event.key == pygame.K_i:
						pygame.mixer.Channel(0).play(pygame.mixer.Sound(lad2))
						
					if event.key == pygame.K_k:
						pygame.mixer.Channel(0).play(pygame.mixer.Sound(si2))
						
					if event.key == pygame.K_l:
						pygame.mixer.Channel(0).play(pygame.mixer.Sound(do2))
						
					#harrypotter
					if event.key == pygame.K_c:
						pygame.mixer.Channel(0).play(pygame.mixer.Sound(si1))
						time.sleep(0.42857142857)
						pygame.mixer.Channel(1).play(pygame.mixer.Sound(mi1))
						time.sleep(0.63829787234)
						pygame.mixer.Channel(2).play(pygame.mixer.Sound(sol1))
						time.sleep(0.21276595744)
						pygame.mixer.Channel(3).play(pygame.mixer.Sound(fad1))
						time.sleep(0.42857142857)
						pygame.mixer.Channel(4).play(pygame.mixer.Sound(mi1))
						time.sleep(1)
						pygame.mixer.Channel(5).play(pygame.mixer.Sound(si2))
						time.sleep(0.42857142857)
						pygame.mixer.Channel(6).play(pygame.mixer.Sound(la1))
						time.sleep(1.5)
						pygame.mixer.Channel(7).play(pygame.mixer.Sound(fad1))
						time.sleep(1.5)
						pygame.mixer.Channel(8).play(pygame.mixer.Sound(mi1))
					
						
		print("[INFO] Closes the program, bye bye")
		
	except KeyboardInterrupt:
		print("[WARNING] Interruption of the main loop")

if __name__ == "__main__":
    main(sys.argv[1:])
