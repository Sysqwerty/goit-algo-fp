import uuid
import networkx as nx
import matplotlib.pyplot as plt


class Node:
    def __init__(self, key, color="#245907"):
        self.left = None
        self.right = None
        self.val = key
        self.base_color = color
        self.color = color
        self.id = str(uuid.uuid4())


def add_edges(graph, node, pos, x=0, y=0, layer=1):
    if node is not None:
        graph.add_node(node.id, color=node.color, label=node.val)
        if node.left:
            graph.add_edge(node.id, node.left.id)
            l = x - 1 / 2 ** layer
            pos[node.left.id] = (l, y - 1)
            add_edges(graph, node.left, pos, x=l, y=y - 1, layer=layer + 1)
        if node.right:
            graph.add_edge(node.id, node.right.id)
            r = x + 1 / 2 ** layer
            pos[node.right.id] = (r, y - 1)
            add_edges(graph, node.right, pos, x=r, y=y - 1, layer=layer + 1)
    return graph


def draw_tree(tree_root):
    tree = nx.DiGraph()
    pos = {tree_root.id: (0, 0)}
    tree = add_edges(tree, tree_root, pos)

    colors = [node[1]['color'] for node in tree.nodes(data=True)]
    labels = {node[0]: node[1]['label'] for node in tree.nodes(data=True)}

    plt.figure(figsize=(8, 5))
    nx.draw(tree, pos=pos, labels=labels, arrows=False,
            node_size=2500, node_color=colors)
    plt.show()


def dfs_traversal(node, visited, base_color):
    if node is not None:
        visited.add(node.id)
        node.color = get_color(base_color, len(visited))
        dfs_traversal(node.left, visited, base_color)
        dfs_traversal(node.right, visited, base_color)


def bfs_traversal(root, base_color):
    if root is not None:
        visited = set()
        queue = [root]
        while queue:
            node = queue.pop(0)
            if node.id not in visited:
                visited.add(node.id)
                node.color = get_color(base_color, len(visited))
                if node.left:
                    queue.append(node.left)
                if node.right:
                    queue.append(node.right)


def get_color(base_color, index):
    # Change the base color
    base_rgb = tuple(int(base_color.lstrip('#')[i:i + 2], 16) for i in (0, 2, 4))
    step = 15  # Step between colors
    new_rgb = tuple(min(255, c + index * step) for c in base_rgb)
    return "#{:02X}{:02X}{:02X}".format(*new_rgb)


if __name__ == "__main__":
    # Creation of tree
    root = Node(0)
    root.left = Node(4)
    root.left.left = Node(5)
    root.left.right = Node(10)
    root.right = Node(1)
    root.right.left = Node(3)
    root.right.right = Node(6)
    root.left.left.left = Node(7)
    root.left.left.right = Node(8)
    root.left.right.left = Node(9)
    root.right.left.left = Node(11)
    root.right.left.right = Node(12)

    # Visualisation of tree
    draw_tree(root)

    # Visualization of DFS
    dfs_traversal(root, set(), root.base_color)
    draw_tree(root)

    # Visualisation of BFS
    bfs_traversal(root, root.base_color)
    draw_tree(root)
