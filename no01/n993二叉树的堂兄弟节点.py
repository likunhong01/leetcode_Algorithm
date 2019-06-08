#coding=utf-8
#Version:python3.7.0
#Tools:Pycharm 2019
# Author:LIKUNHONG
__date__ = ''
__author__ = 'lkh'

import queue, math

# Definition for a binary tree node.
class TreeNode:
    def __init__(self):
        self.val = None
        self.left = None
        self.right = None

class Solution:
    def isCousins(self, root: TreeNode, x: int, y: int) -> bool:
        stack = []
        stack.append(root)
        deep = {}
        deep[root] = 0
        dx = dy = 0
        dxparent = None
        dyparent = None
        while len(stack) != 0:
            now = stack.pop()
            if not now:
                continue
            stack.append(now.right)
            deep[now.right] = deep[now] + 1
            stack.append(now.left)
            deep[now.left] = deep[now] + 1
            if (now.left and now.left.val == x) or (now.right and now.right.val == x):
                dx = deep[now] + 1
                dxparent = now
            if (now.left and now.left.val == y) or (now.right and now.right.val == y):
                dy = deep[now] + 1
                dyparent = now
            if not dy == 0 and not dx == 0:
                break
        if dyparent != dxparent and dy == dx:
            return True
        return False

s = Solution()
root = TreeNode()
root.val = 1
n1 = TreeNode()
n1.val = 2
root.left = n1
n2 = TreeNode()
n2.val = 3
root.right = n2
n3 = TreeNode()
n3.val = 4
n1.right = n3
n4 = TreeNode()
n4.val = 5
n2.right = n4

print(s.isCousins(root, 3, 2))