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
        # Note that we first append a forward edge and then a backward edge,
        # so all forward edges are stored at even indices (starting from 0),
        # whereas backward edges are stored at odd indices.
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
        # To get a backward edge for a true forward edge (i.e id is even), we should get id + 1
        # due to the described above scheme. On the other hand, when we have to get a "backward"
        # edge for a backward edge (i.e. get a forward edge for backward - id is odd), id - 1
        # should be taken.
        #
        # It turns out that id ^ 1 works for both cases. Think this through!
        self.edges[id].flow += flow
        self.edges[id ^ 1].flow -= flow


# self.edges[id].capacity -= flow
# self.edges[id ^ 1].capacity += flow


def read_data():
    vertex_count, edge_count = map(int, input().split())
    graph = FlowGraph(vertex_count)
    for _ in range(edge_count):
        u, v, capacity = map(int, input().split())
        graph.add_edge(u - 1, v - 1, capacity)
    return graph


def bfs(s, t, parent):
    for i in range(len(parent)):
        parent[i] = -1
    parent[s] = -2
    q = queue.Queue()
    q.put(s)
    flow = 1000000000
    # print(graph.edges)
    while not q.empty():
        curr_node = q.get()
        for id in graph.get_ids(curr_node):
            curr_edge = graph.get_edge(id)
            # print(curr_edge)
            if curr_edge.capacity > curr_edge.flow and parent[curr_edge.v] == -1:
                flow = min(flow, curr_edge.capacity - curr_edge.flow)
                parent[curr_edge.v] = id
                curr_node = curr_edge.v
                q.put(curr_node)
                if curr_edge.v == t:
                    return

    return


def max_flow(graph, from_, to):
    # print(graph.edges)
    flow = 0
    parent = [-1] * (graph.size())
    # your code goes here
    while True:
        bfs(from_, to, parent)
        # print('dont bfs')
        if parent[to] == -1:
            return flow
        cur = to
        new_flow = 200000000
        # print(parent)
        while cur != from_:
            # print(cur)
            edge = graph.get_edge(parent[cur])
            new_flow = min(new_flow, edge.capacity - edge.flow)
            cur = edge.u
        flow += new_flow
        cur = to
        while cur != from_:
            edge = graph.get_edge(parent[cur])
            prev = edge.u
            graph.add_flow(parent[cur], new_flow)
            cur = prev
        # print('done add_flow')
    return flow


if __name__ == '__main__':
    graph = read_data()
    print(max_flow(graph, 0, graph.size() - 1))
