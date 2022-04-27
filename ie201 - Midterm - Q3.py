"""
	(15 points)

	Use the graph classes DAG, Node and Arc that we developed in the lectures, as summarized below:
	Make the following modifications:

	1. Add object variables "successor_nodes" and "predecessor_nodes" to the Node class as lists.
	2. Write function "initialize_pred_succ_nodes" in class DAG which fills these lists as intended by their names using lists "nodes" and "arcs".

"""

class Node:
    def __init__(self, code: str) -> None:
        self.code = code
        
class Arc:
    def __init__(self, from_node: Node, to_node: Node, distance: int) -> None:
        self.from_node = from_node
        self.to_node = to_node
        self.distance = distance

class DAG:
    def __init__(self) -> None:
         self.nodes = []
         self.arcs = []