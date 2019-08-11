#coding=utf-8
#Version:python3.7.0
#Tools:Pycharm 2019
# Author:LIKUNHONG
__date__ = ''
__author__ = 'lkh'

class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


class Tree:
    def __init__(self):
        root = None

    def houxu(self, root: TreeNode):
        if not root:
            return None
        stack = []
        res = []
        stack.append(root)
        while len(stack) > 0:
            top = stack[-1]
            if top.left:
                stack.append(top.left)
            elif top.right:
                stack.append(top.right)
            else:
                res.append(stack.pop().val)
        return res