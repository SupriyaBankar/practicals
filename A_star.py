import heapq

class Astar:
    def __init__(self, grid, start, goal):
        self.grid, self.start, self.goal = grid, start, goal
        self.rows, self.cols = len(grid), len(grid[0])
        
    def heuristic(self, a, b):
        return abs(a[0] - b[0]) + abs(a[1] - b[1])  # Manhattan distance
    
    def neighbours(self, node):
        dirs = [(0,1), (1,0), (0,-1), (-1,0)]
        return [(x+dx, y+dy) for dx, dy in dirs
                if 0 <= (x := node[0]+dx) < self.rows and
                   0 <= (y := node[1]+dy) < self.cols and
                   self.grid[x][y] == 0]
        
    def search(self):
        open_list = [(self.heuristic(self.start, self.goal), self.start)]
        came_from, g_score = {}, {self.start: 0}
        
        while open_list:
            _, current = heapq.heappop(open_list)
            if current == self.goal:
                return self.reconstruct(came_from, current)
            for neighbour in self.neighbours(current):
                g = g_score[current] + 1
                if g < g_score.get(neighbour, float('inf')):
                    came_from[neighbour] = current
                    g_score[neighbour] = g
                    f = g + self.heuristic(neighbour, self.goal)
                    heapq.heappush(open_list, (f, neighbour))
        return []
    
    def reconstruct(self, came_from, node):
        path = []
        while node in came_from:
            path.append(node)
            node = came_from[node]
        return [self.start] + path[::-1]

# Grid: 0 = walkable, 1 = blocked
grid = [
    [0,1,0,0,0],
    [0,1,0,1,0],
    [0,0,0,1,0],
    [1,1,0,0,0],
    [0,0,0,1,0]
]

start = (0,0)
goal = (4,4)

astar = Astar(grid, start, goal)
print("Path:", astar.search())
