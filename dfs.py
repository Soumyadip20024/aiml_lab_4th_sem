# Graph represented as an adjacency list
class Graph:
    def __init__(self, num_vertices):
        self.num_vertices = num_vertices
        self.adj_list = {i: [] for i in range(num_vertices)}
    
    def add_edge(self, src, dest):
        self.adj_list[src].append(dest)
        self.adj_list[dest].append(src)  # For undirected graph
    
    def dfs_recursive(self, start_vertex, visited=None):
        if visited is None:
            visited = [False] * self.num_vertices
        
        # Mark the current vertex as visited
        visited[start_vertex] = True
        print(start_vertex, end=" ")
        
        # Recur for all the adjacent vertices
        for neighbor in self.adj_list[start_vertex]:
            if not visited[neighbor]:
                self.dfs_recursive(neighbor, visited)


# Example usage
if __name__ == "__main__":
    # Create a graph with 6 vertices
    g = Graph(6)
    
    # Add edges to the graph
    g.add_edge(0, 1)
    g.add_edge(0, 3)
    g.add_edge(1, 2)
    g.add_edge(1, 4)
    g.add_edge(2, 5)
    g.add_edge(4, 5)
    
    print("Depth-First Search starting from vertex 0:")
    g.dfs_recursive(0)
