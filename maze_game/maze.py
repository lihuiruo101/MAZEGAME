import random

def generate_maze(width, height):
    # DFS 기반으로 반드시 해결 가능한 미로 생성
    maze = [[1 for _ in range(width)] for _ in range(height)]

    def carve(x, y):
        directions = [(0,2), (0,-2), (2,0), (-2,0)]
        random.shuffle(directions)
        for dx, dy in directions:
            nx, ny = x+dx, y+dy
            if 0 <= nx < width and 0 <= ny < height and maze[ny][nx] == 1:
                maze[ny][nx] = 0
                maze[y + dy//2][x + dx//2] = 0
                carve(nx, ny)

    maze[1][1] = 0
    carve(1, 1)
    return maze
