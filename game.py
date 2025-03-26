import random
import time
import os

def initializeGrid(width, height):
    return [[random.choice([0, 1]) for _ in range(width)] for _ in range(height)]

def countLiveNeighbors(grid, x, y, width, height):
    neighbors = [
        (-1, -1), (-1, 0), (-1, 1),
        (0, -1),         (0, 1),
        (1, -1), (1, 0), (1, 1)
    ]
    count = 0
    for dx, dy in neighbors:
        nx, ny = x + dx, y + dy
        if 0 <= nx < height and 0 <= ny < width:
            count += grid[nx][ny]
    return count

def nextGeneration(grid, width, height):
    newGrid = [[0] * width for _ in range(height)]
    for x in range(height):
        for y in range(width):
            liveNeighbors = countLiveNeighbors(grid, x, y, width, height)
            if grid[x][y] == 1:
                newGrid[x][y] = 1 if liveNeighbors in [2, 3] else 0
            else:
                newGrid[x][y] = 1 if liveNeighbors == 3 else 0
    return newGrid

def printGrid(grid):
    os.system('cls' if os.name == 'nt' else 'clear')
    for row in grid:
        print("".join("#" if cell else "." for cell in row))

def gameOfLife(width=20, height=20, generations=100, delay=1):
    grid = initializeGrid(width, height)
    for _ in range(generations):
        printGrid(grid)
        grid = nextGeneration(grid, width, height)
        time.sleep(delay)

gameOfLife()
