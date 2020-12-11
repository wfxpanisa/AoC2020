#!/usr/bin/python3
from pprint import pprint

class Graph:
  def __init__(self):
    self.nodes = {}

class Edge:
  def __init__(self, dst, amount):
    self.dst = dst
    self.amount = amount

class Node:
  def __init__(self, n):
    self.color = n
    self.edges = []
    self.visited = False

def clear_visited(g):
    for node in g.nodes.values():
        node.visited = False
    return g

def connect(u, v, c, g):
    g.nodes[u].edges.append(Edge(g.nodes[v], int(c)))

def parse_input(input_data):
    graph = Graph()
    nodes = []
    edges = []
    for line in input_data:
        # break the line into key and value
        key, not_key = line.split('contain')
        key = get_color_from_string(key)

        # create list of strings to parse
        aux_list = []
        if ',' in not_key:
            aux_list += not_key.split(',')
        else:
            aux_list.append(not_key)

        # parse strings into values
        value = []
        for item in aux_list:
            value.append(get_color_from_string(item))

        nodes.append(key)
        edges.append((key, value))

    for node in nodes:
        graph.nodes[node] = Node(node)

    for edge in edges:
        key, values = edge
        for v in values:
            if type(v) == str:
                continue
            connect(key, v[1], v[0], graph)
    return graph

def get_color_from_string(s):
    # remove useless chars
    s = s.strip()
    # check if we dealing with key or value
    if s[0].isdigit():
        # if value, return tuple with number and color
        return (s[:s.find(' ')], s[s.find(' ')+1:s.find('bag')].strip())
    else:
        # if key, return color
        return s[:s.find('bag')].strip()

def dfs(graph, src, target):
    # node is already visited, there is nothing to search
    if graph.nodes[src].visited == True:
        return False
    # target is on the node destination list
    elif graph.nodes[target] in [edge.dst for edge in graph.nodes[src].edges]:
        return True
    # new visit, and the destination list isn't helping
    # mark the visit, and recurse over the edges
    else:
        graph.nodes[src].visited = True
        return any([dfs(graph, edge.dst.color, target) for edge in graph.nodes[src].edges])

def fst(graph, target):
    count = 0
    for node in graph.nodes:
        clear_visited(graph)
        count += dfs(graph, node, target)
    return count

def ffs(graph, node):
    if not node.edges:
        return 1
    else:
        return 1 + sum([edge.amount * ffs(graph, edge.dst) for edge in node.edges])


def snd(graph, target):
    return ffs(graph, graph.nodes[target])-1

if __name__ == '__main__':
    #graph = parse_input(open('/tmp/test2.txt', 'r').readlines())
    graph = parse_input(open('/tmp/input.txt', 'r').readlines())
    for node in graph.nodes.values():
        print(node.color, [(edge.dst.color, edge.amount) for edge in node.edges])

    #print(fst(graph, 'shiny gold'))
    print(snd(graph, 'shiny gold'))
