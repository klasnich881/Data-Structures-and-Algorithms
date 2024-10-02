"""
-------------------------------------------------------
Linked version of the BST ADT.
-------------------------------------------------------
Author:  David Brown
ID:      999999999
Email:   dbrown@wlu.ca
__updated__ = "2023-07-11"
-------------------------------------------------------
"""
# Imports
from copy import deepcopy


class _BST_Node:

    def __init__(self, value):
        """
        -------------------------------------------------------
        Initializes a BST node containing value. Child pointers 
        are None, height is 1.
        Use: node = _BST_Node(value)
        -------------------------------------------------------
        Parameters:
            value - value for the node (?)
        Returns:
            A _BST_Node object (_BST_Node)            
        -------------------------------------------------------
        """
        self._value = deepcopy(value)
        self._left = None
        self._right = None
        self._height = 1

    def _update_height(self):
        """
        -------------------------------------------------------
        Updates the height of the current node.
        Use: node._update_height()
        -------------------------------------------------------
        Returns:
            _height is 1 plus the maximum of the node's two children.
        -------------------------------------------------------
        """
        if self._left is None:
            left_height = 0
        else:
            left_height = self._left._height

        if self._right is None:
            right_height = 0
        else:
            right_height = self._right._height

        self._height = max(left_height, right_height) + 1
        return

    def __str__(self):
        """
        USE FOR TESTING ONLY
        -------------------------------------------------------
        Returns node height and value as a string - for debugging.
        -------------------------------------------------------
        """
        return "h: {}, v: {}".format(self._height, self._value)


class BST:

    def __init__(self):
        """
        -------------------------------------------------------
        Initializes an empty BST.
        Use: bst = BST()
        -------------------------------------------------------
        Returns:
            A BST object (BST)
        -------------------------------------------------------
        """
        self._root = None
        self._count = 0

    def is_empty(self):
        """
        -------------------------------------------------------
        Determines if bst is empty.
        Use: b = bst.is_empty()
        -------------------------------------------------------
        Returns:
            True if bst is empty, False otherwise.
        -------------------------------------------------------
        """
        return self._root is None

    def __len__(self):
        """
        -------------------------------------------------------
        Returns the number of nodes in the BST.
        Use: n = len(bst)
        -------------------------------------------------------
        Returns:
            the number of nodes in the BST.
        -------------------------------------------------------
        """
        return self._count

    def insert(self, value):
        """
        -------------------------------------------------------
        Inserts a copy of value into the bst. Values may appear 
        only once in a tree.
        Use: b = bst.insert(value)
        -------------------------------------------------------
        Parameters:
            value - data to be inserted into the bst (?)
        Returns:
            inserted - True if value is inserted into the BST,
                False otherwise. (boolean)
        -------------------------------------------------------
        """
        self._root, inserted = self._insert_aux(self._root, value)
        return inserted

    def _insert_aux(self, node, value):
        """
        -------------------------------------------------------
        Inserts a copy of value into the bst. Values may appear 
        only once in a tree.
        Private recursive operation called only by insert.
        Use: node, inserted = self._insert_aux(node, value)
        -------------------------------------------------------
        Parameters:
            node - a bst node (_BST_Node)
            value - data to be inserted into the node (?)
        Returns:
            node - the current node (_BST_Node)
            inserted - True if value is inserted into the BST,
                False otherwise. (boolean)
        -------------------------------------------------------
        """
        if node is None:
            # Base case: add a new node containing the value.
            node = _BST_Node(value)
            self._count += 1
            inserted = True
        elif value < node._value:
            # General case: check the left subtree.
            node._left, inserted = self._insert_aux(node._left, value)
        elif value > node._value:
            # General case: check the right subtree.
            node._right, inserted = self._insert_aux(node._right, value)
        else:
            # Base case: value is already in the BST.
            inserted = False

        if inserted:
            # Update the node height if any of its children have been changed.
            node._update_height()
        return node, inserted

    def retrieve(self, key):
        """
        -------------------------------------------------------
        Retrieves a copy of a value matching key in a BST. (Iterative)
        Use: v = bst.retrieve(key)
        -------------------------------------------------------
        Parameters:
            key - data to search for (?)
        Returns:
            value - value in the node containing key, otherwise None (?)
        -------------------------------------------------------
        """
        node = self._root
        value = None

        while node is not None and value is None:

            if node._value > key:
                node = node._left
            elif node._value < key:
                node = node._right
            elif node._value == key:
                # for comparison counting
                value = deepcopy(node._value)
        return value

    def remove(self, key):
        """
        -------------------------------------------------------
        Removes a node with a value matching key from the bst.
        Returns the value matched. Updates structure of bst as 
        required.
        Use: value = bst.remove(key)
        -------------------------------------------------------
        Parameters:
            key - data to search for (?)
        Returns:
            value - value matching key if found, otherwise None.
        -------------------------------------------------------
        """
        self._root, value = self._remove_aux(self._root, key)
        return value
    

    def _remove_aux(self, node, key):
        """
        -------------------------------------------------------
        Attempts to find a value matching key in a BST node. Deletes the node
        if found and returns the sub-tree root.
        Private recursive operation called only by remove.
        Use: node, value = self._remove_aux(node, key)
        -------------------------------------------------------
        Parameters:
            node - a bst node to search for key (_BST_Node)
            key - data to search for (?)
        Returns:
            node - the current node or its replacement (_BST_Node)
            value - value in node containing key, None otherwise.
        -------------------------------------------------------
        """
        if node is None:
            # Base Case: the key is not in the tree.
            value = None
        elif key < node._value:
            # Search the left subtree.
            node._left, value = self._remove_aux(node._left, key)
        elif key > node._value:
            # Search the right subtree.
            node._right, value = self._remove_aux(node._right, key)
        else:
            # Value has been found.
            value = node._value
            self._count -= 1
            # Replace this node with another node.
            if node._left is None and node._right is None:
                # node has no children.
                node = None
            elif node._left is None:
                # node has no left child.
                node = node._right
            elif node._right is None:
                # node has no right child.
                node = node._left
            else:
                # Node has two children
                if node._left._right is None:
                    repl_node._left = node._left
                else:
                    repl_node = self._delete_node_left(node._left)
                    repl_node._left = node._left
                repl_node._right = node._right
                node = repl_node  

        if node is not None and value is not None:
            # If the value was found, update the ancestor heights.
            node._update_height()
        return node, value

    def _delete_node_left(self, parent):
        """
        -------------------------------------------------------
        Finds a replacement node for a node to be removed from the tree.
        Private operation called only by _remove_aux.
        Use: repl_node = self._delete_node_left(node, node._right)
        -------------------------------------------------------
        Parameters:
            parent - node to search for largest value (_BST_Node)
        Returns:
            repl_node - the node that replaces the deleted node. This node 
                is the node with the maximum value in the deleted node's left
                subtree (_BST_Node)
        -------------------------------------------------------
        """
        repl_node = parent._left
        # Move to the rightmost node in the left subtree
        while repl_node._right is not None:
            parent = repl_node
            repl_node = repl_node._right
        # Update the parent's reference
        if parent._right == repl_node:
            parent._right = repl_node._left
        else:
            parent._left = repl_node._left
        return repl_node

    def __contains__(self, key):
        """
        ---------------------------------------------------------
        Determines if the bst contains key.
        Use: b = key in bst
        -------------------------------------------------------
        Parameters:
            key - a comparable data element (?)
        Returns:
            True if the bst contains key, False otherwise.
        -------------------------------------------------------
        """

        # your code here


    def height(self):
        """
        -------------------------------------------------------
        Returns the maximum height of a BST, i.e. the length of the
        largest path from root to a leaf node in the tree.
        Use: h = bst.height()
        -------------------------------------------------------
        Returns:
            maximum height of bst (int)
        -------------------------------------------------------
        """

        # your code here


    def __eq__(self, target):
        """
        ---------------------------------------------------------
        Determines whether two BSTs are equal.
        Values in self and target are compared and if all values are equal
        and in the same location, returns True, otherwise returns False.
        Use: equals = source == target
        ---------------
        Parameters:
            target - a bst (BST)
        Returns:
            equals - True if source contains the same values
                as target in the same location, otherwise False. (boolean)
        -------------------------------------------------------
        """

        # your code here
        
        return self._eq_aux(self._root, target._root)
    
    def _eq_aux(self, node1, node2):
        """
        ---------------------------------------------------------
        Helper function - determines whether trees rooted at node1 and node2
        are identical.
        Use: equal = self._eq_aux(node1, node2)
        ---------------------------------------------------------
        Parameters:
            node1 - a bst node (_BST_Node)
            node2 - another bst node (_BST_Node)
        Returns:
            equal - True if nodes are equal, False otherwise (boolean)
        ---------------------------------------------------------
        """
        if node1 is None and node2 is None:
            equal = True
        elif node1 is not None and node2 is not None:
            equal = node1._value == node2._value and \
                self._eq_aux(node1._left, node2._left) and \
                self._eq_aux(node1._right, node2._right)
        else:
            equal = False
        return equal
    def parent(self, key):
        """
        ---------------------------------------------------------
        Returns the value of the parent node of a key node in a bst.
        ---------------------------------------------------------
        Parameters:
            key - a key value (?)
        Returns:
            value - a copy of the value in a node that is the parent of the
            key node, None if the key is not found. (?)
        ---------------------------------------------------------
        """
        assert self._root is not None, "Cannot locate a parent in an empty BST"


        parent = None
        current = self._root
        while current is not None and current._value != key:
            parent = current
            if key < current._value:
                current = current._left
            else:
                current = current._right
        if current is None:
            value = None
        else:
            if parent is None:
                value = None
            else:
                value = parent._value
        return value



    def parent_r(self, key):
        """
        ---------------------------------------------------------
        Returns the value of the parent node in a bst given a key.
        ---------------------------------------------------------
        Parameters:
            key - a key value (?)
        Returns:
            value - a copy of the value in a node that is the parent of the
            key node, None if the key is not found.
        ---------------------------------------------------------
        """
        assert self._root is not None, "Cannot locate a parent in an empty BST"


        _, parent = self._parent_r_aux(self._root, key)
        return parent
    
    def _parent_r_aux(self, node, key):
        """
        ---------------------------------------------------------
        Returns the parent node and value of a key node in a bst.
        Helper function for parent_r.
        ---------------------------------------------------------
        Parameters:
            node - a bst node (_BST_Node)
            key - a key value (?)
        Returns:
            parent - a bst node (_BST_Node)
            value - a copy of the value in a node that is the parent of the
            key node, None if the key is not found.
        ---------------------------------------------------------
        """
        parent = None
        if node is not None:
            if node._value == key:
                value = None
            elif key < node._value:
                parent, value = self._parent_r_aux(node._left, key)
            else:
                parent, value = self._parent_r_aux(node._right, key)
            if value is None:
                value = node._value
        else:
            value = None
        return parent, value


    def max(self):
        """
        -------------------------------------------------------
        Finds the maximum value in BST. (Iterative algorithm)
        Use: value = bst.max()
        -------------------------------------------------------
        Returns:
            value - a copy of the maximum value in the BST (?)
        -------------------------------------------------------
        """
        assert self._root is not None, "Cannot find maximum of an empty BST"

        # your code here


    def max_r(self):
        """
        ---------------------------------------------------------
        Returns the largest value in a bst. (Recursive algorithm)
        Use: value = bst.max_r()
        ---------------------------------------------------------
        Returns:
            value - a copy of the maximum value in the BST (?)
        ---------------------------------------------------------
        """
        assert self._root is not None, "Cannot find maximum of an empty BST"


        # your code here


    def min(self):
        """
        -------------------------------------------------------
        Finds the minimum value in BST. (Iterative algorithm)
        Use: value = bst.min()
        -------------------------------------------------------
        Returns:
            value - a copy of the minimum value in the BST (?)
        -------------------------------------------------------
        """
        assert self._root is not None, "Cannot find minimum of an empty BST"
        value = None
        current = self._root
        while current._left is not None:
            current = current._left 
        if not self._root is None:
            value = deepcopy(current._value)
        return value


    def min_r(self):
        """
        ---------------------------------------------------------
        Returns the minimum value in a bst. (Recursive algorithm)
        Use: value = bst.min_r()
        ---------------------------------------------------------
        Returns:
            value - a copy of the minimum value in the BST (?)
        ---------------------------------------------------------
        """
        assert self._root is not None, "Cannot find minimum of an empty BST"

        # your code here


    def leaf_count(self):
        """
        ---------------------------------------------------------
        Returns the number of leaves (nodes with no children) in bst.
        Use: count = bst.leaf_count()
        ---------------------------------------------------------
        Returns:
            count - number of nodes with no children in bst (int)
        ---------------------------------------------------------
        """
        return self._leaf_count_aux(self._root)
    
    def _leaf_count_aux(self, node):
        """
        ---------------------------------------------------------
        Returns the number of leaves (nodes with no children) in bst.
        Helper function for leaf_count
        ---------------------------------------------------------
        Parameters:
            node - a bst node (_BST_Node)
        Returns:
            count - number of nodes with no children in bst (int)
        ---------------------------------------------------------
        """
        if node is None:
            count = 0
        elif node._left is None and node._right is None:
            count = 1
        else:
            count = self._leaf_count_aux(node._left) + self._leaf_count_aux(node._right)
        return count



    def two_child_count(self):
        """
        ---------------------------------------------------------
        Returns the number of the three types of nodes in a BST.
        Use: count = bst.two_child_count()
        -------------------------------------------------------
        Returns:
            count - number of nodes with two children in bst (int)
        ----------------------------------------------------------
        """

        return self._two_child_count_aux(self._root)

    def _two_child_count_aux(self, node):
        """
        ---------------------------------------------------------
        Returns the number of nodes with two children in a bst.
        Helper function for two_child_count
        ---------------------------------------------------------
        Parameters:
            node - a bst node (_BST_Node)
        Returns:
            count - number of nodes with two children in bst (int)
        ---------------------------------------------------------
        """
        if node is None:
            count = 0
        elif node._left is not None and node._right is not None:
            count = 1 + self._two_child_count_aux(node._left) + self._two_child_count_aux(node._right)
        else:
            count = self._two_child_count_aux(node._left) + self._two_child_count_aux(node._right)
        return count
    
    def one_child_count(self):
        """
        ---------------------------------------------------------
        Returns the number of the three types of nodes in a BST.
        Use: count = bst.one_child_count()
        -------------------------------------------------------
        Returns:
            count - number of nodes with one child in bst (int)
        ----------------------------------------------------------
        """

        return self._one_child_count_aux(self._root)

    def _one_child_count_aux(self, node):
        """
        ---------------------------------------------------------
        Returns the number of nodes with one child in a bst.
        Helper function for one_child_count
        ---------------------------------------------------------
        Parameters:
            node - a bst node (_BST_Node)
        Returns:
            count - number of nodes with one child in bst (int)
        ---------------------------------------------------------
        """
        if node is None:
            count = 0
        elif node._left is not None and node._right is None:
            count = 1 + self._one_child_count_aux(node._left)
        elif node._left is None and node._right is not None:
            count = 1 + self._one_child_count_aux(node._right)
        else:
            count = self._one_child_count_aux(node._left) + self._one_child_count_aux(node._right)
        return count
    def node_counts(self):
        """
        ---------------------------------------------------------
        Returns the number of the three types of nodes in a BST.
        Use: zero, one, two = bst.node_counts()
        -------------------------------------------------------
        Returns:
            zero - number of nodes with zero children (int)
            one - number of nodes with one child (int)
            two - number of nodes with two children (int)
        ----------------------------------------------------------
        """

        # your code here


    def is_balanced(self):
        """
        ---------------------------------------------------------
        Returns whether a BST is balanced, i.e. the difference in
        height between all the BST's node's left and right subtrees
        is <= 1.
        Use: b = bst.is_balanced()
        ---------------------------------------------------------
        Returns:
            balanced - True if the BST is balanced, False otherwise (boolean)
        ---------------------------------------------------------
        """
        # Check if the tree is empty
        if self._root is None:
            return True
        
        # Call the recursive helper method to check if the BST is balanced
        return self._is_balanced(self._root)[0]

    def _is_balanced(self, node):
        """
        ---------------------------------------------------------
        Recursive helper method to determine if a BST is balanced.
        ---------------------------------------------------------
        Parameters:
            node - a BST node (_BST_Node)
        Returns:
            balanced - True if the BST is balanced, False otherwise (boolean)
            height - height of the node's subtree (int)
        ---------------------------------------------------------
        """
        # Base case: an empty tree is balanced
        if node is None:
            return True, 0
        
        # Recursively check if the left subtree is balanced
        left_balanced, left_height = self._is_balanced(node._left)
        
        # Recursively check if the right subtree is balanced
        right_balanced, right_height = self._is_balanced(node._right)
        
        # Calculate the height of the current node's subtree
        height = max(left_height, right_height) + 1
        
        # Check if the height difference between left and right subtrees is greater than 1
        balanced = left_balanced and right_balanced and abs(left_height - right_height) <= 1
        
        return balanced, height

    def _node_height(self, node):
        """
        ---------------------------------------------------------
        Helper function to determine the height of node - handles empty node.
        Private operation called only by _is_valid_aux.
        Use: h = self._node_height(node)
        ---------------------------------------------------------
        Parameters:
            node - the node to get the height of (_BST_Node)
        Returns:
            height - 0 if node is None, node._height otherwise (int)
        ---------------------------------------------------------
        """
        if node is None:
            height = 0
        else:
            height = node._height
        return height

    def retrieve_r(self, key):
        """
        -------------------------------------------------------
        Retrieves a _value in a BST. (Recursive)
        Use: v = bst.retrieve(key)
        -------------------------------------------------------
        Parameters:
            key - data to search for (?)
        Returns:
            value - If bst contains key, returns value, else returns None.
        -------------------------------------------------------
        """

        # your code here


    def is_valid(self):
        """
        ---------------------------------------------------------
        Determines if a tree is a valid BST, i.e. the values in
        all left nodes are smaller than their parent, and the
        values in all right nodes are larger than their parent,
        and the height of any node is 1 + max height of its children.
        Use: b = bst.is_valid()
        ---------------------------------------------------------
        Returns:
            valid - True if the tree is a BST, False otherwise (boolean)
        ---------------------------------------------------------
        """
        # Call the recursive helper method to check if the BST is valid
        return self._is_valid(self._root)
    
    def _is_valid(self, node):
        """
        ---------------------------------------------------------
        Recursive helper method to determine if a tree is a valid BST.
        ---------------------------------------------------------
        Parameters:
            node - a BST node (_BST_Node)
        Returns:
            valid - True if the tree rooted at node is a valid BST,
                    False otherwise (boolean)
        ---------------------------------------------------------
        """
        # Base case: an empty tree is a valid BST
        if node is None:
            return True
        
        # Check if the left subtree is a valid BST
        if node._left is not None and node._left._value >= node._value:
            return False
        
        # Check if the right subtree is a valid BST
        if node._right is not None and node._right._value <= node._value:
            return False
        
        # Recursively check if both left and right subtrees are valid BSTs
        return (self._is_valid(node._left) and self._is_valid(node._right))


    def inorder(self):
        """
        -------------------------------------------------------
        Generates a list of the contents of the tree in inorder order.
        Use: a = bst.inorder()
        -------------------------------------------------------
        Returns:
            a - copy of the contents of the tree in inorder (list of ?)
        -------------------------------------------------------
        """

        a = []
        self._inorder_aux(self._root, a)
        return a 
    
    def _inorder_aux(self, node, a):
        """
        ---------------------------------------------------------
        Traverse a bst in inorder, applying function to each node.
        Private recursive operation.
        ---------------------------------------------------------
        Parameters:
            node - a bst node (_BST_Node)
            a - target list of returned values (list)
        Returns:
            None
        ---------------------------------------------------------
        """
        if node is not None:
            self._inorder_aux(node._left, a)
            a.append(deepcopy(node._value))
            self._inorder_aux(node._right, a)
        return


    def preorder(self):
        """
        -------------------------------------------------------
        Generates a list of the contents of the tree in preorder order.
        Use: a = bst.preorder()
        -------------------------------------------------------
        Returns:
            a - copy of the contents of the tree in preorder (list of ?)
        -------------------------------------------------------
        """

        a = []
        self._preorder_aux(self._root, a)
        return a

    def _preorder_aux(self, node, a):
        """
        ---------------------------------------------------------
        Traverse a bst in preorder, applying function to each node.
        Private recursive operation.
        ---------------------------------------------------------
        Parameters:
            node - a bst node (_BST_Node)
            a - target list of returned values (list)
        Returns:
            None
        ---------------------------------------------------------
        """
        if node is not None:
            a.append(deepcopy(node._value))
            self._preorder_aux(node._left, a)
            self._preorder_aux(node._right, a)
        return
    def postorder(self):
        """
        -------------------------------------------------------
        Generates a list of the contents of the tree in postorder order.
        Use: a = bst.postorder()
        -------------------------------------------------------
        Returns:
            a - copy of the contents of the tree in postorder (list of ?)
        -------------------------------------------------------
        """

        a = []
        self._postorder_aux(self._root, a)
        return a
    
    def _postorder_aux(self, node, a):
        """
        ---------------------------------------------------------
        Traverse a bst in postorder, applying function to each node.
        Private recursive operation.
        ---------------------------------------------------------
        Parameters:
            node - a bst node (_BST_Node)
            a - target list of returned values (list)
        Returns:
            None
        ---------------------------------------------------------
        """
        if node is not None:
            self._postorder_aux(node._left, a)
            self._postorder_aux(node._right, a)
            a.append(deepcopy(node._value))
        return

    def levelorder(self):
        """
        -------------------------------------------------------
        Copies the contents of the tree in levelorder order to a list.
        Use: values = bst.levelorder()
        -------------------------------------------------------
        Returns:
            values - a list containing the values of bst in levelorder.
            (list of ?)
        -------------------------------------------------------
        """
        values = []
        if self._root is not None:
            # Initialize a queue for level-order traversal
            queue = [self._root]

            # Traverse the tree level by level
            while queue:
                node = queue.pop(0)  # Dequeue the front node
                values.append(deepcopy(node._value))  # Append the value of the node

                # Enqueue left and right children if they exist
                if node._left:
                    queue.append(node._left)
                if node._right:
                    queue.append(node._right)

        return values

    def count(self):
        """
        ---------------------------------------------------------
        Returns the number of nodes in a BST.
        Use: number = bst.count()
        -------------------------------------------------------
        Returns:
            number - count of nodes in tree (int)
        ----------------------------------------------------------
        """

        # your code here


    def __iter__(self):
        """
        -------------------------------------------------------
        Generates a Python iterator. Iterates through a BST node
        in level order.
        Use: for v in bst:
        -------------------------------------------------------
        Returns:
            yields
            value - the values in the BST node and its children (?)
        -------------------------------------------------------
        """
        if self._root is not None:
            # Put the nodes for one level into a queue.
            queue = []
            queue.append(self._root)

            while len(queue) > 0:
                # Add a copy of the data to the sublist
                node = queue.pop(0)
                yield node._value

                if node._left is not None:
                    queue.append(node._left)
                if node._right is not None:
                    queue.append(node._right)
                    
