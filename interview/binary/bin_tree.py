class Node:
    def __init__(self, data):
        self.data = data
        self.left = self.right = None


class Tree:
    def __init__(self):
        self.root = None

    def append(self, obj):
        if self.root is None:
            self.root = obj
            return obj
