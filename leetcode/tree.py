"""
the main module for tree 
>>>tree insertion
"""


class node:
    # BST data structure
    def __init__(self, val):
        self.val = val
        self.left = None
        self.right = None

    def insert(self, val):
        # if self.val==val:
        #     if self.left is None:
        #             self.left = node(val)
        #     if self.right is None:
        #         self.left = node(val)

        #     else:
        #             self.left.insert(val)
        if self.val:
            if val < self.val:
                if self.left is None:
                    self.left = node(val)
                else:
                    self.left.insert(val)
            elif val > self.val:
                if self.right is None:
                    self.right = node(val)
                else:
                    self.right.insert(val)
            elif val== self.val:
                if self.right is None:
                    self.right = node(val)
                else:
                    self.right.insert(val)
        else:
            self.val = val


def inorder(root, res):
    # Recursive traversal
    if root:
        inorder(root.left, res)
        res.append(root.val)
        print(root.val)
        inorder(root.right, res)

def preorder(root):
    if root.left:
        preorder(root.left)
    print(root.val)
    if root.right:
        preorder(root.right)

def tree_sort(arr):
    # Build BST
    if len(arr) == 0:
        return arr
    root = node(arr[0])
    for i in range(1, len(arr)):
        root.insert(arr[i])
    # Traverse BST in order.
    res = []
    inorder(root, res)
    return res

