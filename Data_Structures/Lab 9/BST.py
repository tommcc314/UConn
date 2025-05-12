class BSTNode:
    def __init__(self, data, parent = None):
        self.data = data
        self.parent = parent
        self.left = None
        self.right = None

class BinarySearchTree:
    def __init__(self):
        self.root = None

    ################ Task 1 ################
    def insert(self, data):
        if self.root == None:
            self.root = BSTNode(data, None)
        else:
            self._add_child(data, self.root)
        #use helper _add_child method to add children to existing parent

    def _add_child(self, data, p_node):
        if data == p_node.data: #duplicate items cannot be added
            return
        if data < p_node.data:
            if p_node.left == None:
                p_node.left = BSTNode(data, p_node)
            else:
                self._add_child(data, p_node.left)
        else:
            if p_node.right == None:
                p_node.right = BSTNode(data, p_node)
            else:
                self._add_child(data, p_node.right)

    def get_max(self):
        #retrieve the appropriate node with the help of
        # helper method _get_right_child
        if self.root == None:
            return None
        return self._get_right_child(self.root)

    def _get_right_child(self, node):
        #helper method to retrieve right node recursively
        if node.right == None:
            return node.data
        return self._get_right_child(node.right)

    def get_min(self):
        #retrieve the appropriate node with the help of
        # helper method _get_left_child
        if self.root == None:
            return None
        return self._get_left_child(self.root)

    def _get_left_child(self, node):
        #helper method to retrieve left node recursively
        if node.left == None:
            return node.data
        return self._get_left_child(node.left)

    def traverse_in_order(self, node, traversed_data):
        #traverse the tree in in-order fashion and keep
        #adding the elements in the traversed_data list
        if node:
            self.traverse_in_order(node.left, traversed_data)
            traversed_data.append(node.data)
            self.traverse_in_order(node.right, traversed_data)
        if node == self.root:
            return traversed_data


    def delete(self, data):
        #starting from root node, pass the data and node
        #to be deleted to the helper node _remove_node
        if self.root:
            self._remove_node(data, self.root)

    def _remove_node(self, data, node):
        #remove the specified node
        #separate cases for deleting leaf node, node with one child and
        #node with two children
        if node is None:
            return
        if data < node.data:
            self._remove_node(data, node.left)
        elif data > node.data:
            self._remove_node(data, node.right)

        else:
            # leaf node
            if node.left is None and node.right is None:
                parent = node.parent
                if parent is not None:
                    if parent.right == node:
                        parent.right = None
                    if parent.left == node:
                        parent.left = None
                else:
                    self.root = None
                del node
            #one child on right
            elif node.left is None and node.right is not None:
                parent = node.parent
                if parent is not None:
                    if parent.right == node:
                        parent.right = node.right
                    if parent.left == node:
                        parent.left = node.right
                else:
                    self.root = node.right
                node.right.parent = parent
                del node
            #one child on left
            elif node.left is not None and node.right is None:
                parent = node.parent
                if parent is not None:
                    if parent.right == node:
                        parent.right = node.left
                    if parent.left == node:
                        parent.left = node.left
                else:
                    self.root = node.left
                node.left.parent = parent
                del node
            #two children
            else:
                predecessor = self._get_predecessor(node.left)
                predecessor.data, node.data = node.data, predecessor.data
                self._remove_node(data, predecessor)
        #For deleting root node with two children, use the
        #helper method _get_predecessor to get the predecessor

    def _get_predecessor(self, node):
        if node.right:
            return self._get_predecessor(node.right)
        return node

    ################ Task 2 ################
    def traverse_pre_order(self, node, traversed_data):
        #traverse the tree in pre-order fashion and keep
        #adding the elements in the traversed_data list
        if node:
            traversed_data.append(node.data)
            self.traverse_pre_order(node.left, traversed_data)
            self.traverse_pre_order(node.right, traversed_data)
        if node == self.root:
            return traversed_data

    def traverse_post_order(self, node, traversed_data):
        #traverse the tree in post-order fashion and keep
        #adding the elements in the traversed_data list
        if node:
            self.traverse_post_order(node.left, traversed_data)
            self.traverse_post_order(node.right, traversed_data)
            traversed_data.append(node.data)
        if node == self.root:
            return traversed_data

if __name__ == "__main__":
    BST = BinarySearchTree()
    myBST = BinarySearchTree()
    random_data = [12, 4, 20, 8, 1, 16, 27]
    myrandom_data = [21, 13, 26, 5, 35, 19, 9, 43, 25]
    for data in random_data:
        BST.insert(data)
    for data in myrandom_data:
        myBST.insert(data)

    print("Testing Max...")
    assert(BST.get_max() == 27)
    assert(myBST.get_max() == 43)
    print("PASSED!")

    print()
    print("Testing Min...")
    assert(BST.get_min() == 1)
    assert (myBST.get_min() == 5)
    print("PASSED!")

    print()
    print("Testing In-order Traversal...")
    traversed_data = []
    mytraversed_data = []
    BST.traverse_in_order(BST.root, traversed_data)
    myBST.traverse_in_order(myBST.root, mytraversed_data)
    assert(traversed_data == [1, 4, 8, 12, 16, 20, 27])
    assert(mytraversed_data == [5, 9, 13, 19, 21, 25, 26, 35, 43])
    print("PASSED!")

    print()
    print("Testing Deletion of root node with two child...")
    BST.delete(12)
    myBST.delete(19)
    traversed_data = []
    mytraversed_data = []
    BST.traverse_in_order(BST.root, traversed_data)
    myBST.traverse_in_order(myBST.root, mytraversed_data)
    assert(traversed_data == [1, 4, 8, 16, 20, 27])
    assert(mytraversed_data == [5, 9, 13, 21, 25, 26, 35, 43])
    print("PASSED!")

    print()
    print("Checking new root after deletion...")
    assert(BST.root.data == 8)
    print("VERIFIED!")

    ########## Task2 ##########
    print()
    print("########## Task 2 ##########")
    BST2 = BinarySearchTree()
    #            12
    #       4         20
    #     1   8    16   27
    random_data = [12, 4, 20, 8, 1, 16, 27]
    for data in random_data:
        BST2.insert(data)
    # myBST:
    #               21
    #          13          26
    #       5           25     35
    #          9                   43

    print()
    print("Testing Pre-order Traversal...")
    traversed_data = []
    mytraversed_data = []
    BST2.traverse_pre_order(BST2.root, traversed_data)
    myBST.traverse_pre_order(myBST.root, mytraversed_data)
    assert(traversed_data == [12, 4, 1, 8, 20, 16, 27])
    assert(mytraversed_data == [21, 13, 5, 9, 26, 25, 35, 43])
    print("PASSED!")

    print()
    print("Testing Post-order Traversal...")
    traversed_data = []
    mytraversed_data = []
    BST2.traverse_post_order(BST2.root, traversed_data)
    myBST.traverse_post_order(myBST.root, mytraversed_data)
    assert(traversed_data == [1, 8, 4, 16, 27, 20, 12])
    assert(mytraversed_data == [9, 5, 13, 25, 43, 35, 26, 21])
    print("PASSED!")
