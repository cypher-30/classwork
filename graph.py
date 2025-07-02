class Graphs:
    def __init__(self, directed=False):
        self.directed = directed

        self.adj_list = dict()  # holds key value pairs

        # graph = {
        #     A: (B,2), (C,27), (D,89)
        # }
        #

    def __repr__(self):
        graph_string = ''

        for node, neighbours in self.adj_list.items():
            graph_string += f'{node} -> {neighbours}\n'

        return graph_string

    def add_node(self, node):
        if node not in self.adj_list:
            self.adj_list[node] = set()
        else:
            raise ValueError(f'{node} already exists')

    def add_edge(self, from_node, to_node, weight=None):
        if from_node not in self.adj_list:
            self.add_node(from_node)

        if to_node not in self.adj_list:
            self.add_node(to_node)

        if weight is None:
            self.adj_list[from_node].add(to_node)

            if not self.directed:
                self.adj_list[to_node].add(from_node)
        else:
            self.adj_list[from_node].add((to_node, weight))

            if not self.directed:
                self.adj_list[to_node].add((from_node, weight))

    def bfs(self, start_node):
        visited = set()
        queue = [start_node]
        order = []

        while queue:
            node = queue.pop(0)

            if node not in visited:  # Check if visited AFTER popping
                visited.add(node)
                order.append(node)  # Add to order once confirmed as unvisited

                neighbours = self.obtain_neighbours(node)

                for neighbor_info in neighbours:  # Renamed variable
                    if isinstance(neighbor_info, tuple):
                        neighbor = neighbor_info[0]  # Extract actual node
                    else:
                        neighbor = neighbor_info

                    if neighbor not in visited:
                        queue.append(neighbor)
        return order

    def dfs(self, start_node):
        visited = set()
        stack = [start_node]
        order = []

        while stack:
            node = stack.pop()

            if node not in visited:  # Check if visited AFTER popping
                visited.add(node)
                order.append(node)  # Add to order once confirmed as unvisited

                neighbours = self.obtain_neighbours(node)

                # Convert to list and reverse for consistent stack behavior.
                # Sorting can be added here with a key if strict order is needed.
                neighbors_to_add = list(neighbours)

                # We reverse the order when pushing to the stack to achieve a
                # more predictable (e.g., "alphabetical") order when popping.
                for neighbor_info in reversed(neighbors_to_add):
                    if isinstance(neighbor_info, tuple):
                        neighbor = neighbor_info[0]  # Extract actual node
                    else:
                        neighbor = neighbor_info

                    if neighbor not in visited:
                        stack.append(neighbor)
        return order

    def obtain_neighbours(self, node):
        # Correctly call the .get() method and provide a default empty set
        return self.adj_list.get(node, set())


if __name__ == '__main__':
    graph_obj = Graphs(directed=True)

    graph_obj.add_edge('A', 'B', 2)
    graph_obj.add_edge('A', 'C', 2)
    graph_obj.add_edge('A', 'J', 3)
    graph_obj.add_edge('A', 'D', 4)
    graph_obj.add_edge('B', 'D', 4)
    graph_obj.add_edge('D', 'C', 7)

    print(graph_obj)
    print("Breadth First Search: \n")
    print(graph_obj.bfs("A"))
    print("Depth First Search: \n")
    print(graph_obj.dfs("A"))