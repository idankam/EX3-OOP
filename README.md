# EX3-OOP
python implementation for Directed Weighted Graphs and Algorithms

![image](https://user-images.githubusercontent.com/79406881/147505114-0ff881c2-fccb-45fc-9cb5-acd41036d855.png)


Graphs and graphs-algorithms explanations:

### Class Edge : This class represents the edges between two nodes , source and destinations in the graph.

### Class Node : This class represents a Node in the graph. The node holds an id, position, weight, the edges out (from him to another node),the edges in (from another node to him) and a tag.

#### Class Node functions:

add_edge_in – adding an edge from node to this node.

add_edge_out – adding an edge from this node to another node.

Copy – coping the object node.

remove_edge_out - removing a specific edge out of this node.

remove_edge_in - removing a specific edge in of this node.

remove_all_edges_out - removing all edges out of this node.

remove_all_edges_in - removing all edges in of this node.

__str__ – representig the node as a string.

### Class Location : This class represents the locations to each node by x axis y axis and z axis.

copy - coping the same location.

distance - calculating the distance from this node to another node.

### Class DiGraph: This class represents the Directed graph the graph holds all the nodes and all the edges.

#### Class DiGraph functions:

v_size- returning number of nodes in the graph.

edgeSize – returning number of edges in the graph.

addNode – Adding a node to the graph.

add_edge – connecting two nodes with an edge (that holds weight).

removeNode – Removing a node from the graph.

removeEdge – Removing an Edge from the graph.

get_mc – returning all the changes in the graph.

get_all_v - returning a dictionary of all the nodes in the Graph, each node is represented using a pair (node_id, node_data).

all_in_edges_of_node - return a dictionary of all the nodes connected to (into) node_id each node is represented using a pair (other_node_id, weight)

all_out_edges_of_node - return a dictionary of all the nodes connected from node_id , each node is represented using a pair (other_node_id, weight)

__str__ - returning a string representing the DiGraph.

colorWhite – iterating the nodes and changing the tag to be white(the options for the tag are three colors).

transpose – creating a transpose graph by changing the directions of the edges(that will help us with algorithms in the next class).

### Class GraphAlgo: A class that holds a DiGraph(Directed weighted Graph). This class has the algorithms we can run on the graph.

#### Class GraphAlgo functions –

Init – The constructor getting a graph an returning it.

getGraph – returning the graph.

BFS – a searching algorithm that is getting the graph and a node and painting every node he get to.

Dijkstra – this is the an algorithm that we are using to get the shortest path, this algorithm is returning the shortest paths from a node to all the other nodes. For more information: (https://en.wikipedia.org/wiki/Dijkstra%27s_algorithm).

Is connected – a function that is checking if the graph is connected by using BFS algorithm we are checking on one node and after that using the transpose dunction and checking on the transpose if there is a rout from this node in the graph and also in the transpose graph so the graph is connected.

sortestPathDist – calling the Dijkstra algorithm and by that returning the shortest path weight.

shortest_path – calling the dijekstra and returning a tuple of list of the shortest path and float of the path.

getPath – a helper function that is putting the shortest path after using the dijekstra into a list(the dijektra returning a hushMap).

centerPoint – returning the center of the graph , the point where the longest destination of the point is the shortest (using the dijekstra algorithm).

Tsp – this algorithm is finding the shortest path between a list of nodes. We are doing it by rotating the list of cities that we are getting , every rotation we are checking the closest on by using the dijekstra and by using the transpose function we are checking what will be a shorter path to add this city to the end of the rout or to the start(we are looking for the shortest path).

save_to_json – saving the graph into a json file , using a NodeToDisplay class(helper class).

load_from_json – loading from json file.

nodesEdgesToDisplay - a helper function we are using to save the nodes into a json file with.

plot_graph - the function that is calling the Gui to plot the graph.

nodesListToIntLis -  converting node list to their id wich is int.


### Class GraphToDisplay: holds an array of nods and of edges , this class is helping us to save and load to json because any json file holds edges and nodes, this class also help us to represent a node to a json file as we want , therefore holds also a class of NodeToDisplay.

### Class PriorityQueue: a class that is implementing a priorityQueue which has the functions isEmpty, insert, size, delete. this priorityqueue is giving priority to the node with the minimum weight.To read more about the functions above https://docs.oracle.com/javase/7/docs/api/java/util/PriorityQueue.html


## GUI explanations:

After loading the graph there is a screen that we created by using pygame.

In this screen we have several options the we created in the bar , by using the Jbar of gui.

File – Where the options are to Save and to load from the file, by using the algorithms of save and load that we explained.

UPDATE – where are the options to edit the nodes and the edges of the graph(removing and addition).

![image](https://user-images.githubusercontent.com/79406881/145828412-b4c21116-edbb-43e7-b5fb-01ade4afa00d.png)

USE ALGORITHMS – where there are all the algorithms we can find in Class DWGAlgorithms.

![image](https://user-images.githubusercontent.com/79406881/145828485-200b4dd1-b795-470b-9259-e57ab50586f7.png)


### We did it by building 5 classes:

GUI\_WINDOW – this is the class which is showing the screen.

GUI\_MANUE – this class is building the menu That we explained at the beginning of this explanation.

GUI\_ADDITIONAL\_WINDOW – that is showing the results of every algorithm on the screen every time.

GUI\_EDGES – drawing the lines between the nodes by normalizing them by the location and the screen size.

GUI\_NODES – drawing the circles(nodes) by normalizing them by the location and the screen size and showing the id.

NOTE : we also added a function that while searching the shortest path between the nodes(while running shortest path algorithm or tsp) we drawing the path and showing the weight of the edge. This is happening also when we are adding an edge. We also showing the node while adding it and the center while searching it.

GUI example (shortest path algoritm):

![image](https://user-images.githubusercontent.com/79406881/145829442-678a257a-740c-42a3-b52c-5e0a5e7a9a96.png)

# Performance report:

LOAD TIME:

1000Nodes.json: 0.135766 seconds.

10000Nodes.json: 0.6116749 seconds.

100000Nodes.json: 7.9033062 seconds.

1000000Nodes.json: 15.345706 seconds.

IS CONNECTED TIME:

1000Nodes.json: 0.0212987 seconds.

10000Nodes.json: 0.3410193 seconds.

100000Nodes.json: 5.7483396 seconds.

1000000Nodes.json:was not able to create a connected graph.

CENTER TIME:

1000Nodes.json: 1.5033647 seconds.

10000Nodes.json: 413.4222973 seconds.

100000Nodes.json: time out.

1000000Nodes.json: time out.
