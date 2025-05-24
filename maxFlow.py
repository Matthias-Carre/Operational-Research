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

def dfsAccessible(adjList, source):
    visited = set()
    stack = [source]
    while stack:
        node = stack.pop()
        if node not in visited:
            visited.add(node)
            for neighbor in adjList[node]:
                nextNode = neighbor[0]
                if nextNode not in visited:
                    stack.append(nextNode)
    return visited
    

#dfs qui revoie le chemin de la source a la cible
def dfs(adjList, source, target, visited=None, path=None):
    if visited is None:
        visited = set()
    if path is None:
        path = []
    visited.add(source)
    path.append(source)

    # on arrive sur le sink
    if source == target:
        return path

    #pour tout les voisin actuel on check autour et on jump dessus si besoin
    for neighbor in adjList[source]:
        nextNode = neighbor[0]
        if nextNode not in visited:
            result = dfs(adjList, nextNode, target, visited, path)
            if result:  # Si un chemin est trouvé, on le retourne
                return result

    #le chemin actuel n'arrive pas sur le sink (on remonte dans le dfs)
    path.pop()
    return ""

#renvoie les infos de node1 vers node2
def getEdge(adjList, node1, node2):
    for neighbor in adjList[node1]:
        if neighbor[0] == node2:
            return neighbor
    return False

#modifie le chemin etre node1 et node2 avec newflow
def reduceFlowEgde(adjList,resi, node1, node2, newFlow,removeEdge):
    for neighbor in adjList[node1]:
        if neighbor[0] == node2:
            neighbor[3] += newFlow
            if neighbor[1] - neighbor[3] <= 0:
                try:
                    print("remove", neighbor[0], "from", node1)
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



#prend un chemin et une liste daj et revoie le residuel
def residuel(chemin, adjList,resi, removeedges):
    #on veux le plus petit flow
    
    minFlow = getEdge(adjList, chemin[0], chemin[1])[1]-getEdge(adjList, chemin[0], chemin[1])[3]
    previus = chemin[0]
    for node in chemin[1:]:
        flow = getEdge(adjList, previus, node)[1]-getEdge(adjList, previus, node)[3]
        if flow < minFlow:
            minFlow = flow
        previus = node
    #print("minFlow", minFlow)

    #on reduit le flow du chemin:
    for node in chemin:
        if node == chemin[0]:
            previus = node
            continue
        reduceFlowEgde(adjList,resi, previus, node, minFlow,removeedges)
        increaseFlowEgde(adjList, node, previus, minFlow)
        previus = node
    #print("adjList", adjList)
    return adjList

#prityprint
def prettyprint(adjList):
    for node, neighbors in adjList.items():
        for neighbor in neighbors:
            if len(neighbor) == 4:
                print(f"from Node {node} to {neighbor[0]} (flow used: {neighbor[3]}/{neighbor[1]})")
    print("")



def ex1():
    #parser l'info
    data = parser.main()
    adjList = adjacentList(data[1], data[0]["numNodes"])

    #setup pour calcul
    removeEdges = []
    resi = copieDico(adjList)
    path = dfs(resi, data[0]["Source"], data[0]["Sink"])

    #application du residuel autant qui faut
    while path != "":
        #print("Chemin trouvé :", path)
        residuel(path, adjList,resi,removeEdges)
        path = dfs(resi, data[0]["Source"], data[0]["Sink"])
    #resultat
    maxFlow = 0
    for neighbor in adjList[data[0]["Source"]]:
        maxFlow += neighbor[3]
    print("\nResult for max flow:", maxFlow)
    print("")


    prettyprint(adjList)

    #recuperation de la coupe minimale ex2
    #on a juste a regarder paris les arretes retire les quelles sont accessible que d'un et unique noeud depuis la source
    axcessible = dfsAccessible(resi, data[0]["Source"])

    print("Minumum cut:")
    for edge in removeEdges:
        if (edge[0] in axcessible and edge[1] not in axcessible) or (edge[1] in axcessible and edge[0] not in axcessible):
            print(edge)
    print("")


if __name__ == "__main__":
    ex1()