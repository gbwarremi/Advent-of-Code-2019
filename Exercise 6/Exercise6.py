import networkx as nx

data = open("input_Day6.txt").read()
input_code = [i.split(')') for i in data.splitlines()]

graph = nx.DiGraph(input_code)

orbits = sum(len(nx.ancestors(graph, n)) for n in graph.nodes)    # Part 1: Sum up
print(orbits)

print(len(nx.shortest_path(nx.Graph(input_code), 'YOU', 'SAN'))-3)
