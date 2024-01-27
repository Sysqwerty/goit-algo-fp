import uuid
import heapq
import networkx as nx
import matplotlib.pyplot as plt


class MinHeapNode:
    def __init__(self, key=None, color="skyblue"):
        self.left = None
        self.right = None
        self.val = key
        self.color = color
        self.id = str(uuid.uuid4())

    def build_heap(self, _nums):
        heapq.heapify(_nums)
        _root = MinHeapNode(_nums[0])

        min_heap_nodes = [_root]
        for i in range(1, len(_nums)):
            new_node = MinHeapNode(_nums[i])
            min_heap_nodes.append(new_node)

            parent_index = (i - 1) // 2
            if i % 2 == 0:
                min_heap_nodes[parent_index].right = new_node
            else:
                min_heap_nodes[parent_index].left = new_node

        return _root


def add_edges(graph, node, pos, x=0, y=0, layer=1):
    if node is not None:
        graph.add_node(node.id, color=node.color, label=str(node.val))
        if node.left:
            graph.add_edge(node.id, node.left.id)
            l = x - 1 / 2 ** layer
            pos[node.left.id] = (l, y - 1)
            l = add_edges(graph, node.left, pos, x=l, y=y - 1, layer=layer + 1)
        if node.right:
            graph.add_edge(node.id, node.right.id)
            r = x + 1 / 2 ** layer
            pos[node.right.id] = (r, y - 1)
            r = add_edges(graph, node.right, pos, x=r, y=y - 1, layer=layer + 1)
    return graph


def draw_heap(heap_root):
    heap = nx.DiGraph()
    pos = {heap_root.id: (0, 0)}
    heap = add_edges(heap, heap_root, pos)

    colors = [node[1]['color'] for node in heap.nodes(data=True)]
    labels = {node[0]: node[1]['label'] for node in heap.nodes(data=True)}

    plt.figure(figsize=(8, 5))
    nx.draw(heap, pos=pos, labels=labels, arrows=False, node_size=2500, node_color=colors)
    plt.show()


if __name__ == '__main__':
    nums = [4, 0, 5, 10, 1, 3, 6, 11, 2, 7, 8, 9, 12, 13, 14]
    root = MinHeapNode()
    heap_root = root.build_heap(nums)

    draw_heap(heap_root)
