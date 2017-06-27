# Problem
## Description
Our hero is trapped in a maze. There's mud up to our hero's knees, and there are monsters in the maze! You must find a path so our hero can savely escape!

## Input
Our input is an ASCII-map of a maze. The map uses the following characters:
* '#' for wall - Our hero may not move here
* ' ' for empty space - Our hero may move here, but only vertically or horizontally (not diagonally). Moving here costs our hero 1HP (health point) because of mud.
* 'm' for monster - Our hero may move here, but only vertically or horizontally (not diagonally). Moving here costs our hero 11HP because of mud and a monster.
* 'S' this is where our hero is right now, the start.
* 'G' this is where our hero wishes to go, the goal, you may move here vertically or horizontally, costing 1HP. Your route should end here.
## Output
The same as the input, but mark the route which costs the least amount of HP with '*', as well as the cost of the route.

**More info: https://www.reddit.com/r/dailyprogrammer/comments/5vwwzg/20170224_challenge_303_hard_escaping_a_dangerous/**

# Solution
## Output
```
Georgantas$ python run.py input.txt
Computing cost...
Total cost: 598 HP
Generating image...
```

## Visualization
![Alt text](/image_zoom.png "Visualization.")

**Color Code**
```
Black: Wall ('#')
White: Empty Space (' ')
Red: Monster ('m')
Green: Start ('S')
Blue: Finish ('G')
Grey: Route Taken
```

# Dijkstra's Algorithm
Dijkstra's algorithm was used to solve this problem. This algorithm is used for finding the shortest paths between nodes in a graph, which may represent, for example, road networks. It was conceived by computer scientist Edsger W. Dijkstra in 1956 and published three years later.

## Algorithm
Let the node at which we are starting be called the initial node. Let the distance of node Y be the distance from the initial node to Y. Dijkstra's algorithm will assign some initial distance values and will try to improve them step by step.
* Assign to every node a tentative distance value: set it to zero for our initial node and to infinity for all other nodes.
* Set the initial node as current. Mark all other nodes unvisited. Create a set of all the unvisited nodes called the unvisited set.
* For the current node, consider all of its neighbors and calculate their tentative distances. Compare the newly calculated tentative distance to the current assigned value and assign the smaller one. For example, if the current node A is marked with a distance of 6, and the edge connecting it with a neighbor B has length 2, then the distance to B (through A) will be 6 + 2 = 8. If B was previously marked with a distance greater than 8 then change it to 8. Otherwise, keep the current value.
* When we are done considering all of the neighbors of the current node, mark the current node as visited and remove it from the unvisited set. A visited node will never be checked again.
* If the destination node has been marked visited (when planning a route between two specific nodes) or if the smallest tentative distance among the nodes in the unvisited set is infinity (when planning a complete traversal; occurs when there is no connection between the initial node and remaining unvisited nodes), then stop. The algorithm has finished.
* Otherwise, select the unvisited node that is marked with the smallest tentative distance, set it as the new "current node", and go back to step 3.

**Source: https://en.wikipedia.org/wiki/Dijkstra%27s_algorithm**

**More Info: https://www.youtube.com/watch?v=GazC3A4OQTE**
