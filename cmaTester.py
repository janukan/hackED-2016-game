import pygame

black = (0,0,0)
white = (255,255,255)	
pygame.init()
screen = pygame.display.set_mode((600,600))
pygame.display.set_caption('Astral Aversion')



clock = pygame.time.Clock()
screen.fill(black)
done = False

while not done:
	clock.tick(60)
	for event in pygame.event.get():
		if event.type == pygame.QUIT:
			done = True
	pygame.display.update()
		
