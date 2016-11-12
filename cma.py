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


