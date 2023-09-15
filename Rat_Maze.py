N = 4
def printSolution(sol):
	for i in range(N):
		for j in range(N):
			print(sol[i][j], end = " ")
		print()
def isSafe(maze, x, y):

	if (x >= 0 and x < N and y >= 0 and
		y < N and maze[x][y] != 0):
		return True
	return False
def solveMaze(maze):
	sol = [[0, 0, 0, 0],
		[0, 0, 0, 0],
		[0, 0, 0, 0],
		[0, 0, 0, 0]]
	if (solveMazeUtil(maze, 0, 0, sol) == False):
		print("Solution doesn't exist")
		return False
	printSolution(sol)
	return True
def solveMazeUtil(maze, x, y, sol):
	

	if (x == N - 1 and y == N - 1) :
		sol[x][y] = 1
		return True
		

	if (isSafe(maze, x, y) == True):

		sol[x][y] = 1
		
		for i in range(1, N):
			if (i <= maze[x][y]):

				if (solveMazeUtil(maze, x + i,
								y, sol) == True):
					return True
					
				if (solveMazeUtil(maze, x,
								y + i, sol) == True):
					return True
		sol[x][y] = 0
		return False
	return False

maze = [[2, 1, 0, 0],
		[3, 0, 0, 1],
		[0, 1, 0, 1],
		[0, 0, 0, 1]]
solveMaze(maze)

