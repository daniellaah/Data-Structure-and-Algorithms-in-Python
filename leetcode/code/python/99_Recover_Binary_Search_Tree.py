"""99. Recover Binary Search Tree
Two elements of a binary search tree (BST) are swapped by mistake.

Recover the tree without changing its structure.

Note:
A solution using O(n) space is pretty straight forward. Could you devise a constant space solution?
"""
# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

from sys import maxsize
MIN_VALUE = -maxsize - 1
class Solution(object):
    last_node = TreeNode(MIN_VALUE)
    node1 = node2 = None
    def recursive(self, root):
        if root:
            self.recursive(root.left)
            if not self.node1 and root.val < self.last_node.val:
                self.node1 = self.last_node
            if self.node1 and root.val < self.last_node.val:
                self.node2 = root
            self.last_node = root
            self.recursive(root.right)

    def recoverTree(self, root):
        """
        :type root: TreeNode
        :rtype: void Do not return anything, modify root in-place instead.
        """
        self.recursive(root)
        self.node1.val, self.node2.val = self.node2.val, self.node1.val
