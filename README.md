# Operations Research Project

Master Computer Science 1st year
Université Côte d'Azur
Autor: Matthias Carre

## Description:
This project implements Algorithms to compute:
- max flow
- minimum cut
- max flow min cost
of a graph.

## how to use it
### input files:
The graph is extracted from a file containing its list of nodes, arcs, upper bound capcities and costs. The file is a text file and its format is the following one:
- The first line contains 4 numbers : **numNodes** **numArcs** **sourceNode** **sinkNode**, where numNodes is the number of nodes of the graph, numArcs is its number of arcs, sourceNode is s, the source node of the flow and sinkNode is t, the sink of the flow
- Then, each line contains the description of an arc under the form: emanatingNode, terminatingNode, maxCapacity, cost. This defines the arc (emanatingNode, terminatingNode)  hose upper bound capacity is maxCapacity and whose cost is cost.

**example:**
0 1 10 5
0 2 5 2
1 2 15 1
1 3 10 3
2 3 10 2
### how to run


