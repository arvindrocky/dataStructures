from typing import List


class Vertex:
    def __init__(self, name: str, state_code: str, population_count: int):
        self.name = name
        self.state_code = state_code
        self.population_count = population_count

    def get_name(self) -> str:
        return "{}, {}".format(self.name, self.state_code)

    def get_population_count(self) -> int:
        return '{:,}'.format(self.population_count)

    def get_vertex_details(self) -> str:
        return "Name is {} and population count is {}".format(self.get_name(), self.get_population_count())

    def print_vertex(self) -> None:
        print("Vertex is {} and population count is {}".format(self.get_name(), self.get_population_count()))


class Edge:
    def __init__(self, v1: Vertex, v2: Vertex, w: int):
        self.source_vertex: Vertex = v1
        self.destination_vertex: Vertex = v2
        self.weight: int = w

    def print_edge(self) -> None:
        print("Edge is from {} to {} and weight is {}".format(self.source_vertex.get_name(),
                                                              self.destination_vertex.get_name(),
                                                              self.weight))

    def get_source_vertex(self) -> Vertex:
        return self.source_vertex

    def get_destination_vertex(self) -> Vertex:
        return self.destination_vertex


class Graph:
    def __init__(self, name: str, list_of_vertices: List[Vertex] = [], list_of_edges: List[Edge] = None):
        self.name = name
        self.edge_list = list_of_edges
        self.vertex_list = {}
        for individual_vertex in list_of_vertices:
            self.add_vertex(individual_vertex)

    def add_vertex(self, new_vertex: Vertex) -> None:
        if new_vertex.get_name() in self.vertex_list:
            raise KeyError
        self.vertex_list[new_vertex.get_name()] = new_vertex

    def add_edge(self, new_edge: Edge) -> None:
        if new_edge:
            self.edge_list.append(new_edge)

    def get_neighbors_of_a_vertex(self, source_vertex: Vertex) -> List[Vertex]:
        if not source_vertex:
            return []
        neighbors = set()
        for edge in self.edge_list:
            if edge.get_source_vertex() == source_vertex:
                neighbors.add(edge.get_destination_vertex().get_name())
            if edge.get_destination_vertex() == source_vertex:
                neighbors.add(edge.get_source_vertex().get_name())
        return list(neighbors)


    def print_graph(self) -> None:
        print("Name of the Graph is {}".format(self.name))
        print("Number of Vertices is {}".format(len(self.vertex_list)))
        print("Number of Edges is {}".format(len(self.edge_list)))
        print("Vertices are {}".format(self.vertex_list))
        print("Edges are {}".format(self.edge_list))

        for vertex_name, vertex in self.vertex_list.items():
            print("Vertex key is {} and vertex details are: {}".format(vertex_name, vertex.get_vertex_details()))

        for edge in self.edge_list:
            edge.print_edge()


class Solution:
    def __init__(self):
        self.create_graph("City Graph")

    def create_graph(self, graph_name: str):
        city1 = Vertex("Atlanta", "GA", 100000)
        city2 = Vertex("Milpitas", "CA", 200000)
        city3 = Vertex("Chicago", "IL", 300000)
        city4 = Vertex("New York", "NY", 400000)
        city5 = Vertex("Atlanta", "GA", 500000)

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

        # print("=================Adding duplicate vertex==================")
        # g.add_vertex(city5)
        # g.print_graph()

        print("Printing all neighbors or Vertex {}: {}".format(city1.get_name(), g.get_neighbors_of_a_vertex(city1)))


sol = Solution()
