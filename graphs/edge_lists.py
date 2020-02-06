from typing import List


class Vertex:
    def __init__(self, name: str, state_code: str):
        self.name = name
        self.state_code = state_code

    def get_name(self) -> str:
        return "{}, {}".format(self.name, self.state_code)

    def print_vertex(self) -> None:
        print("Vertex is {}".format(self.get_name()))


class Edge:
    def __init__(self, v1: Vertex, v2: Vertex, w: int):
        self.source_vertex: Vertex = v1
        self.destination_vertex: Vertex = v2
        self.weight: int = w

    def print_edge(self) -> None:
        print("Edge is from {} to {} and weight is {}".format(self.source_vertex.get_name(),
                                                              self.destination_vertex.get_name(),
                                                              self.weight))


class Graph:
    def __init__(self, name: str, list_of_vertices: List[Vertex] = None, list_of_edges: List[Edge] = None):
        self.name = name
        self.vertex_list = list_of_vertices
        self.edge_list = list_of_edges

    def add_vertex(self, new_vertex: Vertex) -> None:
        if new_vertex:
            self.vertex_list.append(new_vertex)

    def add_edge(self, new_edge: Edge) -> None:
        if new_edge:
            self.edge_list.append(new_edge)

    def print_graph(self) -> None:
        print("Name of the Graph is {}".format(self.name))
        print("Number of Vertices is {}".format(len(self.vertex_list)))
        print("Number of Edges is {}".format(len(self.edge_list)))
        print("Vertices are {}".format(self.vertex_list))
        print("Edges are {}".format(self.edge_list))

        for vertex in self.vertex_list:
            vertex.print_vertex()

        for edge in self.edge_list:
            edge.print_edge()


class Solution:
    def __init__(self):
        self.create_graph("City Graph")

    def create_graph(self, graph_name: str):
        city1 = Vertex("Atlanta", "GA")
        city2 = Vertex("Milpitas", "CA")
        city3 = Vertex("Chicago", "IL")
        city4 = Vertex("New York", "NY")

        edge1 = Edge(city1, city2, 100)
        edge2 = Edge(city1, city3, 200)
        edge3 = Edge(city3, city4, 500)
        edge4 = Edge(city4, city1, 600)

        g = Graph(graph_name, [city1, city2, city3], [edge1, edge2, edge3])

        g.print_graph()

        print("==========================================================")

        g.add_vertex(city4)
        g.add_edge(edge4)

        g.print_graph()


sol = Solution()
