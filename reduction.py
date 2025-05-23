import graphviz
import pygraphviz as pgv

#Creation de la liste adjacent, je veux les nom puis les couts (a voir si on a besoin du flow)
def adjacentList(edgeList): #revoie un dico avec les voisins de chaque sommet composer de (nom, flow, cost)
    aL={}
    for edge in edgeList:
        if edge[0][0] not in aL:
            aL[edge[0][0]]=[]
        aL[edge[0][0]].append((edge[0][1],edge[1], edge[2]))
    
    print("Liste d'adja:", aL)
    return aL

def dijkstra(adjList,nodesList, start, end):#renvoie la liste des distances et le chemin vers la source
    
    updatedby={}
    dist={}
    
    for node in nodesList:
        dist[node]=float('inf')
        updatedby[node]=None
    print("dist:",dist)
    dist[start]=0

    toDo=[]
    toDo.append(start)
    visited=[]
    while toDo:
        node = toDo.pop(0)
        print("node actuel:", node[0])
        if node==end:
            break
        for n in adjList[node]:
            print("voisin en cours:", n[0])
            if n[0] not in visited:
                if n[0] not in toDo:
                    print("ajout de:", n[0])
                    toDo.append(n[0])
                if dist[n[0]] > dist[node]+float(n[2]):
                    dist[n[0]]=dist[node]+float(n[2])
                    updatedby[n[0]]=node
        print("toDo:", toDo)
        visited.append(node)

    print("distances:", dist)
    print("updatedby:", updatedby)
    return dist, updatedby

def fromAdjListToGraph(adjList):
    graph = pgv.AGraph(directed=True, comment='Linked List')
    for node in adjList:
        for n in adjList[node]:
            #graph.add_edge(node,n[0])
            addEdge(graph, node, n[0], n[1], n[2])
    return graph

def myGraph():
    graph = pgv.AGraph(directed=True, comment='Linked List')

    
    #exemple du cours
    graph.add_node('S') 
    graph.add_node('1') 
    graph.add_node('2') 
    graph.add_node('3')
    graph.add_node('4') 
    graph.add_node('5') 
    graph.add_node('T')
    addEdge(graph, 'S', '1', '16', '5.8')
    addEdge(graph, 'S', '3', '13', '4.0')
    addEdge(graph, '1', '2', '5', '4.6')
    addEdge(graph, '1', '4', '10', '4.5')
    addEdge(graph, '3', '2', '10', '6.0')
    addEdge(graph, '2', '3', '5', '5.8')
    addEdge(graph, '2', '4', '8', '3.3')
    addEdge(graph, '3', '5', '15', '4.6')
    addEdge(graph, '4', 'T', '25', '7.2')
    addEdge(graph, '5', 'T', '6', '6.8')

    graph.write('./res/graphDuCours.gv')
    graph.draw('./res/graphbase.png',prog='dot')


def myEdgeList(file):#renvoie la liste des arcs et les sommets dugraph dans file (oriante)
    EdgeList=[]
    graph = pgv.AGraph(file)
    #print(graph)
    for edge in graph.edges():
        #a revoir c'est horrible mais ca marche
        flow = edge.attr['label'].split(' ')[2]
        cost = edge.attr['label'].split(' ')[5].strip('()')
        name = edge
        EdgeList.append((name, flow, cost))
    #print(EdgeList)
    return EdgeList,graph.nodes()
    


def addEdge(graph, node1, node2, flow, cost):
    graph.add_edge(node1, node2, label='<<font color="blue"> '+flow+'|</font><font color="red">'+cost+' </font>>')


def printDijktra(AdjList,chemins, start, end):
    node=end
    graph = fromAdjListToGraph(AdjList)
    while node!=start:
        
        print("nodes:"+chemins[node],node)
        edge = graph.get_edge(chemins[node], node)
        edge.attr['color'] = 'red'

        #graph.edge(chemins[node], node, color='red')
        node=chemins[node]
    graph.write('./res/graphdijktra.gv')
    graph.draw('./res/graph.png',prog='dot')

def flowReduction(AdjList,chemins, start, end):
    #prend le graph et sont dijtra et revoie le graphe avec reduction des flows
    for e in AdjList:
        print(e)

#main

myGraph()
print("liste de noeuds")
el,nodes=myEdgeList('test.gv')
aL=adjacentList(el)
print("dijkstra")
dist,precedent =dijkstra(aL,nodes, 'S', 'T')
printDijktra(aL,precedent, 'S', 'T')

print("flow reduction")
flowReduction(aL,precedent, 'S', 'T')

# graph = pgv.AGraph(directed=True, comment='Linked List')
# graph.add_edge('a','b')
# graph.draw('graph.png',prog='dot')


''' 
digraph G {
    A -> B [label=< <font color="red">5</font> (<font color="blue">3</font>) >];
    B -> C [label=< <font color="red">10</font> <font color="blue">7</font> >];
    C -> A [label=< <font color="red">15</font> <font color="blue">12</font> >];
}
'''