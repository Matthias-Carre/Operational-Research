# Operations Research Project

Master Computer Science 1st year
Université Côte d'Azur
**Author:** Matthias Carre

## Description:

This project implements algorithms to compute:

* Max Flow
* Minimum Cut
* Max Flow Min Cost
  of a graph.

## How to use it

### Input files:

The graph is extracted from a file containing its list of nodes, arcs, upper bound capacities and costs. The file is a text file and its format is the following:

* The first line contains 4 numbers: **numNodes** **numArcs** **sourceNode** **sinkNode**, where *numNodes* is the number of nodes in the graph, *numArcs* is its number of arcs, *sourceNode* is *s*, the source node of the flow, and *sinkNode* is *t*, the sink of the flow.
* Then, each line contains the description of an arc in the form: emanatingNode, terminatingNode, maxCapacity, cost. This defines the arc (emanatingNode, terminatingNode) whose upper bound capacity is *maxCapacity* and whose cost is *cost*.

**Example of input:**

```
0 1 10 5  
0 2 5 2  
1 2 15 1  
1 3 10 3  
2 3 10 2  
```

Some files are available in the *TestFiles* folder.

### How to run:

* Clone the repo
* Run either:

  * `python *pythonFile*`
  * `python *pythonFile* --file *./pathToFile.txt*`

*pythonFile*: maxFlow\.py or maxFlowMinCost.py

**Example of use:**

```bash
python ./maxFlow.py --file ./TestFiles/inputfileExample.txt
```

### Outcome:

#### For Max Flow:

Starts with the value of the max flow, followed by the list of the capacity of each edge and the minimum cut.

#### For Max Flow Min Cost:

Starts with the value of the max flow, the minimum cost value, and the list of the capacity of each edge and the minimum cut.

