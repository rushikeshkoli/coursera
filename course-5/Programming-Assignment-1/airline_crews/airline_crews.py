# python3
import queue


class Edge:

    def __init__(self, u, v, capacity):
        self.u = u
        self.v = v
        self.capacity = capacity
        self.flow = 0


# This class implements a bit unusual scheme for storing edges of the graph,
# in order to retrieve the backward edge for a given edge quickly.
class FlowGraph:

    def __init__(self, n):
        # List of all - forward and backward - edges
        self.edges = []
        # These adjacency lists store only indices of edges in the edges list
        self.graph = [[] for _ in range(n)]

    def add_edge(self, from_, to, capacity):
        forward_edge = Edge(from_, to, capacity)
        backward_edge = Edge(to, from_, 0)
        self.graph[from_].append(len(self.edges))
        self.edges.append(forward_edge)
        self.graph[to].append(len(self.edges))
        self.edges.append(backward_edge)

    def size(self):
        return len(self.graph)

    def get_ids(self, from_):
        return self.graph[from_]

    def get_edge(self, id):
        return self.edges[id]

    def add_flow(self, id, flow):
        self.edges[id].flow += flow
        self.edges[id ^ 1].flow -= flow


class MaxMatching:
    def read_data(self):
        n, m = map(int, input().split())
        adj_matrix = [list(map(int, input().split())) for i in range(n)]
        return adj_matrix

    def write_response(self, matching):
        line = [str(-1 if x == -1 else x + 1) for x in matching]
        print(' '.join(line))

    def find_matching(self, adj_matrix):
        n = len(adj_matrix)
        m = len(adj_matrix[0])
        vertex_count = n + m + 2
        graph = FlowGraph(vertex_count)
        matching = [-1] * n
        for i in range(n):
            graph.add_edge(0, i + 1, 1)
            for j in range(m):
                if adj_matrix[i][j] == 1:
                    graph.add_edge(i + 1, n + j + 1, 1)
        for j in range(m):
            graph.add_edge(n + j + 1, n + m + 1, 1)
        max_flow(graph, 0, n + m + 1, matching)
        return matching

    def solve(self):
        adj_matrix = self.read_data()
        matching = self.find_matching(adj_matrix)
        self.write_response(matching)


def bfs(s, t, parent, graph):
    for i in range(len(parent)):
        parent[i] = -1
    parent[s] = -2
    q = queue.Queue()
    q.put(s)
    # print(graph.edges)
    curr_node = s
    while not q.empty():
        curr_node = q.get()
        for id in graph.get_ids(curr_node):
            curr_edge = graph.get_edge(id)
            # print(curr_edge)
            if curr_edge.capacity > curr_edge.flow and parent[curr_edge.v] == -1:
                parent[curr_edge.v] = id
                curr_node = curr_edge.v
                q.put(curr_node)
                if curr_edge.v == t:
                    return curr_node

    return curr_node


def max_flow(graph, from_, to, matching):
    # print(graph.edges)
    flow = 0
    parent = [-1] * (graph.size())
    # your code goes here
    while flow < len(matching):
        cur = bfs(from_, to, parent, graph)
        # print('dont bfs')
        # print(parent)
        flow += 1
        if parent[to] == -1:
            pass
        while cur != from_:
            edge = graph.get_edge(parent[cur])
            prev = edge.u
            graph.add_flow(parent[cur], 1)
            cur = prev            
        # print('done add_flow')
    for i in range(0, len(matching)):
        edges = graph.get_ids(i + 1)
        for id in edges:
            edge = graph.get_edge(id)
            if edge.flow == 1:
                matching[i] = edge.v - len(matching) - 1
    return


if __name__ == '__main__':
    max_matching = MaxMatching()
    max_matching.solve()
