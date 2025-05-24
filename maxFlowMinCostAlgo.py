import parser

def copieDico(dico):
    newDico = {}
    for key, value in dico.items():
        newDico[key] = value.copy()
    return newDico

def adjacentList(edgeList,nnode): #revoie un dico avec les voisins de chaque sommet composer de (nom, flow, cost, flowuse)
    aL={}
    for i in range(nnode):
        aL[i] = []
    for egde in edgeList:
        if egde[0] not in aL:
            aL[egde[0]] = [egde[1:]+[0]]#.append(0)
        else:
            aL[egde[0]].append(egde[1:]+[0])#.append(0))

    #print("Liste d'adja:", aL)
    return aL

def dijkstra(adjList, start, end):#renvoie la liste des distances et le chemin vers la source
    
    updatedby={}
    dist={}
    
    for node in adjList:
        dist[node]=float('inf')
        updatedby[node]=None

    dist[start]=0

    toDo=[]
    toDo.append(start)
    visited=[]
    while toDo:
        node = toDo.pop(0)
        #print("node actuel:", node[0])
        if node==end:
            break
        for n in adjList[node]:
            #print("voisin en cours:", n[0])
            if n[0] not in visited:
                if n[0] not in toDo:
                    #print("ajout de:", n[0])
                    toDo.append(n[0])
                if dist[n[0]] > dist[node]+float(n[2]):
                    dist[n[0]]=dist[node]+float(n[2])
                    updatedby[n[0]]=node
        #print("toDo:", toDo)
        visited.append(node)

    #print("distances:", dist)
    #print("updatedby:", updatedby)
    return dist, updatedby

def prettyprint(adjList):
    for node, neighbors in adjList.items():
        for neighbor in neighbors:
            if len(neighbor) == 4:
                print(f"from Node {node} to {neighbor[0]} (flow used: {neighbor[3]}/{neighbor[1]})") #and cost: {neighbor[2]})")
    print("")

def reduceFlowEgde(adjList,resi, node1, node2, newFlow,removeEdge):
    for neighbor in adjList[node1]:
        if neighbor[0] == node2:
            neighbor[3] += newFlow
            #print("reduce flow from", node1, "to", neighbor[0], "by", newFlow)
            if neighbor[1] - neighbor[3] <= 0:
                try:
                    #print("remove", neighbor[0], "from", node1)
                    removeEdge.append((node1,neighbor[0]))
                    resi[node1].remove(neighbor)
                except:
                    pass
            return


def increaseFlowEgde(adjList, node1, node2, newFlow):
    for neighbor in adjList[node1]:
        if neighbor[0] == node2:
            neighbor[1] += newFlow
            return
    adjList[node1].append([node2, newFlow,0])

#renvoie les infos de node1 vers node2
def getEdge(adjList, node1, node2):
    for neighbor in adjList[node1]:
        if neighbor[0] == node2:
            return neighbor
    return False

def reduceCost(adjList, resi, node1, node2,distances):
    for neighbor in adjList[node1]:
        if neighbor[0] == node2:
            #print("REDUCE act val:", neighbor[2])
            neighbor[2] = distances[node1] + neighbor[2] - distances[node2]
            #print("REDUCE new val:", neighbor[2])
            
def ex3():
    #parser l'info
    data = parser.main()
    adjList = adjacentList(data[1], data[0]["numNodes"])

    resi = copieDico(adjList)
    #idee generale: on cherche avec dijktra le chemin le "moins cher", 
    #on reduit puis on reduit les cout avec c_i,j = d(i) + c_i,j - d(j) 
    #avec d distance et c le cout
    #on repetrer tant qu'il y a un chemin de la source au puit

    distances,updatedby = dijkstra(resi, data[0]["Source"], data[0]["Sink"])
    while distances[data[0]["Sink"]] != float('inf'):
        #on recup les valeurs de dijkstra
    
        #on reduit le flow et puis les couts

        node1 = data[0]["Sink"]
        node2 = updatedby[data[0]["Sink"]]
        #on veux le plus petit flow
        minFlow = getEdge(adjList, node2, node1)[1]-getEdge(adjList, node2, node1)[3]
        node1 = node2
        node2 = updatedby[node1]
        while node2 is not None:
            #print("MIN FLOW ACTUAL from ",node1,"to ",node2, minFlow)
            flow = getEdge(adjList, node2, node1)[1]-getEdge(adjList, node2, node1)[3]
            if flow < minFlow:
                minFlow = flow
            node1 = node2
            node2 = updatedby[node1]

        #print("MINFLOW", minFlow)
        

        node1 = data[0]["Sink"]
        node2 = updatedby[data[0]["Sink"]]
        while node2 is not None:
            #print("node1:", node1, "node2:", node2)
            
            reduceFlowEgde(adjList, resi, node2, node1, minFlow, [])
            increaseFlowEgde(adjList, node1, node2, minFlow)
            reduceCost(adjList, resi, node2, node1, distances)
            node1 = node2
            node2 = updatedby[node1]
        
        #prettyprint(adjList)
        #prettyprint(resi)

        distances,updatedby = dijkstra(resi, data[0]["Source"], data[0]["Sink"])
    prettyprint(adjList)


if __name__ == "__main__":
    ex3()