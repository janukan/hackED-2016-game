import pygame
import cma
import time
import random

black = (0,0,0)
white = (255,255,255)	
pygame.init()
screen = pygame.display.set_mode((800,800))
pygame.display.set_caption('HackED 2016')

world = [[False for row in range(100)] for rows in range(100)]

for mi in range(40):
	for mm in range(40):
		if random.random() < 0.25:
			world[mi][mm] = True
			print(1)
	#print(mi)

clock = pygame.time.Clock()
screen.fill(black)
done = False
def rset3(grid):
	gridData=cma.vNeighbourLooped(grid,True,False)
	for r in range(len(gridData)):
		for  c in range(40):
			if gridData[r][c] < 1:
				grid[r][c] = False
				#print("y")
			elif gridData[r][c] < 5:
				grid[r][c] = True
			elif gridData[r][c] < 7:
				grid[r][c] = False	
			else:
				grid[r][c] == grid[r][c]
				#print("Happend")
def rSetVoting(grid):
	gridData=cma.vNeighbourLooped(grid,True,False)
	for r in range(len(gridData)):
		for  c in range(len(gridData[i])):
			if gridData[r][c] < 4:
				grid[r][c] = False
				#print("y")
			elif gridData[r][c] > 4:
				grid[r][c] = True	
			else:
				grid[r][c] == grid[r][c]
				#print("Happend")
def iterate(grid):
	#print(newGrid)
	gridData=cma.vNeighbourLooped(grid,True,False)
	for r in range(len(gridData)):
		for  c in range(len(gridData[i])):
			if gridData[r][c] < 1 or gridData[r][c] > 2:
				grid[r][c] = False
				#print("y")	
			elif gridData[r][c] == 1:
				grid[r][c] = True
				#print(newGrid[r][c])
				#print("Occurs")
			elif gridData[r][c] == 2:
				grid[r][c] == grid[r][c]
				#print("Happend")
	
	#print(newGrid == grid)	
	#newGrid
i=0
while not done:	
	i+=1
	#if random.random() > 0.9999999999999999999999999999999999999:
	if i%60 == 0:
		rset3(world)
	screen.fill(black)
	clock.tick(60)
	for event in pygame.event.get():
		if event.type == pygame.QUIT:
			done = True
	for row in range(len(world)):
		for tile in range(len(world)):
			if world[row][tile]:
				pygame.draw.rect(screen,(255,0,255),(20*row,20*tile,20,20),0)
	#for newi in range(len(temp)):
	#	for newy in range(len(temp[0])):
	#		world[newi][newy] = temp[newi][newy]
	pygame.display.update()
	
