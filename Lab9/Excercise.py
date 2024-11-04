
from collections import deque, defaultdict
import heapq

class Graph:
    def __init__(self):
        self.graph = {}
        self.weights = defaultdict(dict)  # For weighted graph

    def add_vertex(self, vertex):
        if vertex not in self.graph:
            self.graph[vertex] = []
    
    def add_edge(self, vertex1, vertex2, weight=1):
        self.add_vertex(vertex1)
        self.add_vertex(vertex2)
        self.graph[vertex1].append(vertex2)
        self.graph[vertex2].append(vertex1)  # For undirected graph
        self.weights[vertex1][vertex2] = weight
        self.weights[vertex2][vertex1] = weight  # For undirected graph

    def print_graph(self):
        for vertex in self.graph:
            print(f"{vertex}: {' '.join(map(str, self.graph[vertex]))}")

    def bfs_shortest_path(self, start_vertex, end_vertex):
        queue = deque([(start_vertex, [start_vertex])])
        visited = set([start_vertex])
        
        while queue:
            current_vertex, path = queue.popleft()
            for neighbor in self.graph[current_vertex]:
                if neighbor not in visited:
                    if neighbor == end_vertex:
                        return path + [neighbor]
                    visited.add(neighbor)
                    queue.append((neighbor, path + [neighbor]))
        return None  # No path found

    def has_cycle(self):
        visited = set()
        for vertex in self.graph:
            if vertex not in visited:
                if self._has_cycle_helper(vertex, visited, -1):
                    return True
        return False

    def _has_cycle_helper(self, vertex, visited, parent):
        visited.add(vertex)
        for neighbor in self.graph[vertex]:
            if neighbor not in visited:
                if self._has_cycle_helper(neighbor, visited, vertex):
                    return True
            elif parent != neighbor:
                return True
        return False

    def dijkstra(self, start_vertex):
        distances = {vertex: float('infinity') for vertex in self.graph}
        distances[start_vertex] = 0
        priority_queue = [(0, start_vertex)]  # (distance, vertex)
        
        while priority_queue:
            current_distance, current_vertex = heapq.heappop(priority_queue)
            for neighbor in self.graph[current_vertex]:
                weight = self.weights[current_vertex][neighbor]
                distance = current_distance + weight
                if distance < distances[neighbor]:
                    distances[neighbor] = distance
                    heapq.heappush(priority_queue, (distance, neighbor))
        
        return distances

    def is_bipartite(self):
        color = {}
        for vertex in self.graph:
            if vertex not in color:
                if not self._is_bipartite_helper(vertex, color, 0):
                    return False
        return True

    def _is_bipartite_helper(self, vertex, color, c):
        color[vertex] = c
        for neighbor in self.graph[vertex]:
            if neighbor not in color:
                if not self._is_bipartite_helper(neighbor, color, 1 - c):
                    return False
            elif color[neighbor] == c:
                return False
        return True

# Test the Graph class
g = Graph()
g.add_edge(0, 1)
g.add_edge(0, 2)
g.add_edge(1, 2)
g.add_edge(2, 3)
g.add_edge(3, 4)
g.add_edge(1, 4)

print("Graph:")
g.print_graph()

# Test shortest path using BFS
print("\nShortest path from vertex 0 to vertex 4 using BFS:")
shortest_path = g.bfs_shortest_path(0, 4)
print(" -> ".join(map(str, shortest_path)) if shortest_path else "No path found.")

# Test cycle detection
print("\nDoes the graph contain a cycle?", g.has_cycle())

# Test Dijkstra's algorithm on a weighted graph
g.add_edge(0, 1, 4)
g.add_edge(0, 2, 1)
g.add_edge(1, 2, 2)
g.add_edge(1, 3, 1)
g.add_edge(2, 3, 5)
g.add_edge(3, 4, 3)

print("\nWeighted graph:")
g.print_graph()

distances = g.dijkstra(0)
print("\nDijkstra's algorithm shortest distances from vertex 0:")
for vertex, distance in distances.items():
    print(f"Distance to {vertex}: {distance}")

# Test if the graph is bipartite
print("\nIs the graph bipartite?", g.is_bipartite())
