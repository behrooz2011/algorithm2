class Graph:
    def __init__(self, directed=False):
        self.adjacency_list = {}
        self.adjacency_matrix = []
        self.directed = directed

    def add_vertex(self, vertex):
        if vertex not in self.adjacency_list:
            self.adjacency_list[vertex] = []
            # Update adjacency matrix
            for row in self.adjacency_matrix:
                row.append(0)
            self.adjacency_matrix.append([0] * (len(self.adjacency_matrix) + 1))

    def add_edge(self, u, v, weight=1):
        if u not in self.adjacency_list or v not in self.adjacency_list:
            raise ValueError("Both vertices must exist in the graph.")
       
        self.adjacency_list[u].append(v)
        if not self.directed:
            self.adjacency_list[v].append(u)
       
        # Update adjacency matrix
        u_index = list(self.adjacency_list.keys()).index(u)
        v_index = list(self.adjacency_list.keys()).index(v)
        self.adjacency_matrix[u_index][v_index] = weight
        if not self.directed:
            self.adjacency_matrix[v_index][u_index] = weight

    def remove_vertex(self, vertex):
        if vertex in self.adjacency_list:
            # Remove the vertex from the adjacency list of other vertices
            for v in self.adjacency_list:
                if vertex in self.adjacency_list[v]:
                    self.adjacency_list[v].remove(vertex)
           
            # Remove the vertex from the adjacency list
            del self.adjacency_list[vertex]
           
            # Update the adjacency matrix
            self.adjacency_matrix = [row[:i] + row[i+1:] for i, row in enumerate(self.adjacency_matrix) if i != list(self.adjacency_list.keys()).index(vertex)]

    def remove_edge(self, u, v):
        if u in self.adjacency_list and v in self.adjacency_list:
            if v in self.adjacency_list[u]:
                self.adjacency_list[u].remove(v)
           
            if not self.directed and u in self.adjacency_list[v]:
                self.adjacency_list[v].remove(u)
           
            # Update adjacency matrix
            u_index = list(self.adjacency_list.keys()).index(u)
            v_index = list(self.adjacency_list.keys()).index(v)
            self.adjacency_matrix[u_index][v_index] = 0
            if not self.directed:
                self.adjacency_matrix[v_index][u_index] = 0

    def get_neighbors(self, vertex):
        return self.adjacency_list.get(vertex, [])

    def dfs_iterative(self, start):
        visited = set()
        stack = [start]

        while stack:
            vertex = stack.pop()
            if vertex not in visited:
                visited.add(vertex)
                print(vertex, end=' ')
                # Add neighbors to the stack
                for neighbor in reversed(self.adjacency_list[vertex]):
                    if neighbor not in visited:
                        stack.append(neighbor)

    def bfs(self, start):
        visited = set()
        queue = [start]
        visited.add(start)

        while queue:
            vertex = queue.pop(0)
            print(vertex, end=' ')
            for neighbor in self.adjacency_list[vertex]:
                if neighbor not in visited:
                    visited.add(neighbor)
                    queue.append(neighbor)

# Example usage
if __name__ == "__main__":
    g = Graph(directed=False)

    # Adding vertices
    for vertex in ['A', 'B', 'C', 'D']:
        g.add_vertex(vertex)

    # Adding edges
    g.add_edge('A', 'B')
    g.add_edge('A', 'C')
    g.add_edge('B', 'D')
    g.add_edge('C', 'D')

    print("Adjacency List:")
    print(g.adjacency_list)

    print("\nDFS (Iterative) starting from A:")
    g.dfs_iterative('A')

    print("\n\nBFS starting from A:")
    g.bfs('A')