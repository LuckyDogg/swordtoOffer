import unittest


class TreeNode:
    def __init__(self, val):
        self.value = val
        self.left = None
        self.right = None

    def left_insert(self, tree_node):
        self.left = tree_node
        return self.left

    def right_insert(self, tree_node):
        self.right = tree_node
        return self.right


class Solution:

    @staticmethod
    def tree_re_init_by_front(treelist: list):
        def restruct_tree():
            pass

        if len(treelist) != 0:
            headnode = TreeNode(treelist[0])
            var_node = headnode

        else:
            return None
















