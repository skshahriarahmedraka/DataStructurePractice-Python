import heapq
import sys

class Graph:
    
    def __init__(self):
        self.vertices = {}
        
    def add_vertex(self, name, edges):
        self.vertices[name] = edges
    
    def shortest_path(self, start, finish):
        distances = {} # Distance from start to node
        previous = {}  # Previous node in optimal path from source
        nodes = [] # Priority queue of all nodes in Graph

        for vertex in self.vertices:
            if vertex == start: # Set root node as distance of 0
                distances[vertex] = 0
                heapq.heappush(nodes, [0, vertex])
            else:
                distances[vertex] = sys.maxsize
                heapq.heappush(nodes, [sys.maxsize, vertex])
            previous[vertex] = None
        
        while nodes:
            smallest = heapq.heappop(nodes)[1] # Vertex in nodes with smallest distance in distances
            if smallest == finish: # If the closest node is our target we're done so print the path
                #return distances
                path = []
                while previous[smallest]: # Traverse through nodes til we reach the root which is 0
                    path.append(smallest)
                    smallest = previous[smallest]
                return path
            if distances[smallest] == sys.maxsize: # All remaining vertices are inaccessible from source
                break
            print(f"self.vertices[smallest] : {self.vertices[smallest]}")
            for neighbor in self.vertices[smallest]: # Look at all the nodes that this vertex is attached to
                print(f"neighbor : {neighbor}")
                print(f"self.vertices[smallest][neighbor] : {self.vertices[smallest][neighbor]}")
                alt = distances[smallest] + self.vertices[smallest][neighbor] # Alternative path distance
                if alt < distances[neighbor]: # If there is a new shortest path update our priority queue (relax)
                    distances[neighbor] = alt
                    previous[neighbor] = smallest
                    for n in nodes:
                        if n[1] == neighbor:
                            n[0] = alt
                            break
                    heapq.heapify(nodes)
        return distances
        
    def __str__(self):
        return str(self.vertices)

if __name__ == '__main__':
    # g = Graph()
    # g.add_vertex('A', {'B': 7, 'C': 8})
    # g.add_vertex('B', {'A': 7, 'F': 2})
    # g.add_vertex('C', {'A': 8, 'F': 6, 'G': 4})
    # g.add_vertex('D', {'F': 8})
    # g.add_vertex('E', {'H': 1})
    # g.add_vertex('F', {'B': 2, 'C': 6, 'D': 8, 'G': 9, 'H': 3})
    # g.add_vertex('G', {'C': 4, 'F': 9})
    # g.add_vertex('H', {'E': 1, 'F': 3})
    # print(g.shortest_path('A', 'H'))

    # g=Graph()

    # g.add_vertex("A",{"B":1,"C":100})
    # g.add_vertex("B",{"A":1,"C":1,"H":100})
    # g.add_vertex("C",{"D":1,"E":50,"B":1})
    # g.add_vertex("D",{"A":100,"C":1,"G":40})
    # g.add_vertex("E",{"C":50,"F":1})
    # g.add_vertex("F",{"G":30,"E":1,"H":100})
    # g.add_vertex("G",{"D":40,"F":30})
    # g.add_vertex("H",{"B":100,"F":100})

    g=Graph()

    g.add_vertex("A",{"B":1,"C":2,"D":1})
    g.add_vertex("B",{"A":1,"G":5})
    g.add_vertex("C",{"F":10,"A":1})
    g.add_vertex("D",{"A":1,"E":100})
    g.add_vertex("E",{"D":100,"I":50})
    g.add_vertex("F",{"C":10,"H":2})
    g.add_vertex("G",{"B":5,"I":50})
    g.add_vertex("H",{"I":2,"F":2})
    g.add_vertex("I",{"H":2,"E":50,"G":50})

    print(g.shortest_path('A',"I"))