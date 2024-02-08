import heapq


class Graph:
    def __init__(self):
        self.vertices = {}

    def add_vertex(self, vertex):
        self.vertices[vertex] = {}

    def add_edge(self, start_vertex, end_vertex, weight):
        self.vertices[start_vertex][end_vertex] = weight

    def dijkstra(self, start_vertex):
        shortest_paths = {vertex: float('inf') for vertex in self.vertices}
        shortest_paths[start_vertex] = 0
        priority_queue = [(0, start_vertex)]  # бінарна купа для оптимізації

        while priority_queue:
            current_weight, current_vertex = heapq.heappop(priority_queue)

            if current_weight > shortest_paths[current_vertex]:
                continue

            for neighbor, weight in self.vertices[current_vertex].items():
                path_weight = current_weight + weight

                if path_weight < shortest_paths[neighbor]:
                    shortest_paths[neighbor] = path_weight
                    heapq.heappush(priority_queue, (path_weight, neighbor))

        return shortest_paths


def print_shortest_paths(shortest_paths, start_vertex):
    print(f"Найкоротший шлях від: {start_vertex}:")
    for vertex, distance in shortest_paths.items():
        print(f"від: {start_vertex} до: {vertex}: {distance}")


if __name__ == "__main__":
    graph = Graph()
    graph.add_vertex('A')
    graph.add_vertex('B')
    graph.add_vertex('C')
    graph.add_vertex('D')
    graph.add_vertex('E')
    graph.add_vertex('F')
    graph.add_vertex('G')

    graph.add_edge('A', 'B', 3)
    graph.add_edge('A', 'C', 4)
    graph.add_edge('B', 'E', 7)
    graph.add_edge('C', 'D', 2)
    graph.add_edge('D', 'E', 4)
    graph.add_edge('C', 'E', 5)
    graph.add_edge('E', 'F', 2)
    graph.add_edge('F', 'C', 3)
    graph.add_edge('F', 'G', 2)

    # Знаходимо найкоротші шляхи
    shortest_paths = graph.dijkstra('A')
    print_shortest_paths(shortest_paths, 'A')
