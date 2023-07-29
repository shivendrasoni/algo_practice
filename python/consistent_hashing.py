import bisect

class ConsistentHashing:
    def __init__(self):
        self.nodes = []

    def add_node(self, node):
        hashed_node = hash(node)
        bisect.insort(self.nodes, hashed_node)

    def remove_node(self, node):
        hashed_node = hash(node)
        index = bisect.bisect_left(self.nodes, hashed_node)
        if index != len(self.nodes) and self.nodes[index] == hashed_node:
            self.nodes.pop(index)

    def get_node(self, key):
        hashed_key = hash(key)
        index = bisect.bisect(self.nodes, hashed_key)
        return self.nodes[index % len(self.nodes)]