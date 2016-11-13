import pygame
import random 
import math
from cmaTester import rset3
import imageio
import requests

black = (0,0,0)
white = (255,255,255)	
pygame.init()
screen = pygame.display.set_mode((600,600))
pygame.display.set_caption('Inferno')

startMenu = True
bar = 0

inferno = False
iGrid = [[False for x in range(20)] for y in range(20)]
cGrid = iGrid
count1 = 200
p1=[3,3]
def iInit():
	p1 = [3,3]
	cGrid = [[False for x in range(20)] for y in range(20)]
	for i in range(len(iGrid)):
		for y in range(len(iGrid[i])):
			if random.randint(0,2) > 1:
				iGrid[i][y] = True
images = []

def boundDraw(grid,x,y):
	b = random.randint(0,50)
	if not grid[(x-1)%len(grid)][y]:
		pygame.draw.rect(screen,(255,255-b,0),(30*x,30*y,5,30),0)
	if not grid[(x+1)%len(grid)][y]:
		pygame.draw.rect(screen,(255,255-b,0),(30*x+25,30*y,5,30),0)
	if not grid[x][(y-1)%20]:
		pygame.draw.rect(screen,(255,255-b,0),(30*x,30*y,30,5),0)
	if not grid[x][(y+1)%20]:
		pygame.draw.rect(screen,(255,255-b,0),(30*x,30*y+25,30,5),0)
	if not grid[(x-1)%20][(y-1)%20]:
		pygame.draw.rect(screen,(255,255-b,0),(30*x,30*y,5,5),0)
	if not grid[(x+1)%20][(y-1)%20]:
		pygame.draw.rect(screen,(255,255-b,0),(30*x+25,30*y,5,5),0)
	if not grid[(x-1)%20][(y+1)%20]:
		pygame.draw.rect(screen,(255,255-b,0),(30*x,30*y+25,5,5),0)
	if not grid[(x+1)%20][(y+1)%20]:
		pygame.draw.rect(screen,(255,255-b,0),(30*x+25,30*y+25,5,5),0)

clock = pygame.time.Clock()
screen.fill(black)
done = False

i = 0
while not done:
	i+=1
	screen.fill(black)
	clock.tick(60)
	for event in pygame.event.get():
		if event.type == pygame.QUIT:
			done = True
		elif event.type == pygame.KEYDOWN:
			if startMenu:
				if event.key == pygame.K_UP:
					print("pressed")
					bar = (bar+1)%2
				elif event.key == pygame.K_DOWN:
					bar -= 1
					if bar < 0:
						bar*=-1
				elif event.key == pygame.K_RETURN:
					iInit()
					startMenu = False
					if bar == 0:
						inferno = True
						print("Inferno")
			if inferno:
				if event.key == pygame.K_ESCAPE:
					startMenu = True
					inferno = False
					i=0
					iInit()

				elif event.key == pygame.K_UP:
					if iGrid[p1[0]][(p1[1]-1)%20] == False:
						p1[1]=(p1[1]-1)%20

				elif event.key == pygame.K_DOWN:
					if iGrid[p1[0]][(p1[1]+1)%20] == False:
						p1[1]=(p1[1]+1)%20
				elif event.key == pygame.K_LEFT:
					if iGrid[(p1[0]-1)%20][p1[1]] == False:
						p1[0]=(p1[0]-1)%20
				elif event.key == pygame.K_RIGHT:
					if iGrid[(p1[0]+1)%20][p1[1]] == False:
						p1[0]=(p1[0]+1)%20



	if startMenu:
		pygame.draw.rect(screen,(125,0,125),(50,125+bar*200,500,100),0)
		if i%50 < i%100:
			pygame.draw.rect(screen,(255,0,5*(i%50)),(50,125,500,100),5)
			pygame.draw.rect(screen,(0,5*(i%50),255),(50,325,500,100),5)
		else:
			pygame.draw.rect(screen,(255,0,250-(5*(i%50))),(50,125,500,100),5)
			pygame.draw.rect(screen,(0,250-(5*(i%50)),255),(50,325,500,100),5)

	if inferno:
		bg = int(math.sin(i/count1))*200
		if i%count1==0:
			if i>0:
				iGrid = cGrid
				i=1
				count1-=5
				if count1 == 0:
					count1 = 5
			cGrid=rset3(cGrid)

		for m in range(0,20):
			for l in range(0,20):
				pygame.draw.rect(screen,(bg,0,bg),(30*m,30*l,30,30),0)
				if cGrid[m][l]:
					pygame.draw.rect(screen,(255,0,255-(i%count1)),(30*m,30*l,30,30),0)
				if iGrid[m][l]:
					pygame.draw.rect(screen,(200+random.randint(0,50),0,50),(30*m,30*l,30,30),0)
					boundDraw(iGrid,m,l)
				if [m,l] == p1:
					pygame.draw.rect(screen,(0,0,250),(30*m+5,30*l+5,20,20),0)
	pygame.display.update()
	pygame.image.save(screen,"image"+str(i)+".png")
	images.append(imageio.imread("image"+str(i)+".png"))
imageio.mimwrite("lmao.gif",images[-20:])

parameters = {"grant_type":"client_credentials","client_id":"{{2_bZfbte}}","client_secret":"{{EuSECvztvjiAxkCFNj3Mfqd5Gl0NGiVyXtET0S7N-12fY8fr4jdmMLxqyfK3gT8J}}"}
response = requests.get("https://api.gfycat.com/v1/oauth/token",params = parameters)
print(response)
