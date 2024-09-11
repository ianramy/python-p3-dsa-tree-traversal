class Tree:
    def __init__(self, root=None):
        # Initialize the tree with a root element (a dictionary that represents a node)
        self.root = root

    def get_element_by_id(self, id):
        # Helper function to perform a depth-first search
        def dfs(node):
            if not node:
                return None

            # Check if the current node's id matches the target id
            if node.get('id') == id:
                return node

            # Recursively search through the node's children
            for child in node.get('children', []):
                result = dfs(child)
                if result:
                    return result

            return None

        # Start the search from the root
        return dfs(self.root)
