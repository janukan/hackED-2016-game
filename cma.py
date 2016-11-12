def mNeighbourLooped(grid,t_value,f_value):
	#counts number of neighbours in the Moore Neighbourhood, returns as a 2d array
	newGrid = [[f_value for tile in range(len(grid[0]))] for group in range(len(grid))]
	for x in range(len(grid)):
		for y in range(len(grid[0])):
			neighbours = 0
			if grid[(x-1)%len(grid)][(y+1)%len(grid[x])] == t_value:
				neighbours+=1
			if grid[x][(y+1)%len(grid[x])] == t_value:
				neighbours+=1
			if grid[(x+1)%len(grid)][(y+1)%len(grid[x])] == t_value:
				neighbours+=1
			
			if grid[(x-1)%len(grid)][y] == t_value:
				neighbours+=1
			if grid[(x+1)%len(grid)][y] == t_value:
				neighbours+=1
				
			if grid[(x-1)%len(grid)][(y-1)%len(grid[x])] == t_value:
				neighbours+=1
			if grid[x][(y-1)%len(grid[x])] == t_value:
				neighbours+=1
			if grid[(x+1)%len(grid)][(y-1)%len(grid[x])] == t_value:
				neighbours+=1
			newGrid[x][y] = neighbours
	return newGrid

def vNeighbourLooped(grid,t_value,f_value):
	newGrid = [[f_value for tile in range(len(grid[0]))] for group in range(len(grid))]
	for x in range(len(grid)):
		for y in range(len(grid[0])):
			neighbours = 0
			if grid[(x-1)%len(grid)][(y+1)%len(grid[x])] == t_value:
				neighbours+=1
			if grid[x][(y+1)%len(grid[x])] == t_value:
				neighbours+=1
			if grid[(x+1)%len(grid)][(y+1)%len(grid[x])] == t_value:
				neighbours+=1
			
			if grid[(x-1)%len(grid)][y] == t_value:
				neighbours+=1
			if grid[(x+1)%len(grid)][y] == t_value:
				neighbours+=1
				
			if grid[(x-1)%len(grid)][(y-1)%len(grid[x])] == t_value:
				neighbours+=1
			if grid[x][(y-1)%len(grid[x])] == t_value:
				neighbours+=1
			if grid[(x+1)%len(grid)][(y-1)%len(grid[x])] == t_value:
				neighbours+=1
			if grid[x][(y+2)%len(grid[x])] == t_value:
				neighbours+=1
			if grid[x][(y-2)%len(grid[x])] == t_value:
				neighbours+=1
			if grid[(x+2)%len(grid)][y] == t_value:
				neighbours+=1
			if grid[(x-2)%len(grid)][y] == t_value:
				neighbours+=1
			newGrid[x][y] = neighbours
	return newGrid
	

#testGrid = [[0,0,0,0,0],[0,0,0,0,0],[0,1,1,1,0],[0,0,0,0,0],[0,0,0,0,0]]
#print(vNeighbourLooped(testGrid,1,0))

