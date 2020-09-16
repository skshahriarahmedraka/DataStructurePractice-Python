import heapq
import sys
class Graph:
    def __init__(self):
        self.Vertices={}
    def Add_Vertex(self,node,neighbours):
        self.Vertices[node]=neighbours
    def Shortest_Path(self,start,finish):

        distance={}
        previous={}
        nodes=[]

        for v in self.Vertices:
            if v== start:
                distance[v]=0
                heapq.heappush(nodes,[0,v])
            else:
                distance[v]=sys.maxsize
                heapq.heappush(nodes,[sys.maxsize,v])
            previous[v]=None

        while nodes:
            smallest=heapq.heappop(nodes)[1]

            if smallest ==finish:
                path=[]
                while previous[smallest]:
                    path.append(smallest)
                    smallest=previous[smallest]
                return path
            if distance[smallest]==sys.maxsize:
                print("Look at all the nodes that this vertex is attached to")
                break
            for neighbour in self.Vertices[smallest]:
                alt=distance[smallest] +self.Vertices[smallest][neighbour]
                if alt<distance[neighbour]:
                    distance[neighbour]=alt
                    previous[neighbour]=smallest
                    for n in nodes:
                        if n[1]==neighbour:
                            n[0]=alt
                            break
                    heapq.heapify(nodes)
        return distance







def Create_Graph():
    G=Graph()
    v=int(input("how many vertices in the whole Graph :"))
    for i in range(v):
        A=input(f"Name of the {i+1} vertex :")
        B=int(input(f"Number of edges {A} has :"))
        print("Name , Weight")
        di={}
        for _ in range(B):
            s=input()
            Name , Weight=s.split(" ")
            Weight=int(Weight)
            di[Name]=Weight
        G.Add_Vertex(A,di)
    return G





def main():
    g1=Create_Graph()
    source=(input("give the source Node : "))
    destination=(input("give the destination node : "))
    print(g1.Shortest_Path(source,destination))



if __name__=="__main__":
    main()
