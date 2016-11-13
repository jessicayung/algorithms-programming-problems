class BinaryTreeNode:
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None

    def insert_left(self, value):
        self.left = BinaryTreeNode(value)
        return self.left

    def insert_right(self, value):
        self.right = BinaryTreeNode(value)
        return self.right


def is_superbalanced(root):

    # Initialise variables
    max_depth = 1
    min_depth = None
    not_ended = []
    for node in [root.left, root.right]:
        if node is not None:
            not_ended.append(node)

    while not_ended is not None:
        layer_nodes = not_ended

        # Reset variables
        ended = 0
        not_ended = []

        # Go through nodes in layer and check if any have ended
        for node in layer_nodes:
            if node.left is None and node.right is None:
                ended += 1
                if min_depth is None:
                    min_depth = max_depth
            else:
                not_ended.append(node)

        # Check if tree seems superbalanced so far
        if max_depth - min_depth > 1:
            return False

    return True
