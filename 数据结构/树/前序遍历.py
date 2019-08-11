# coding=utf-8
# Version:python3.7.0
# Tools:Pycharm 2019
# Author:LIKUNHONG
__date__ = ''
__author__ = 'lkh'


# Definition for a binary tree node.
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


# 返回一个链表int
def preorderTraversal(root: TreeNode):
    if root == None:
        return []
    stack = [root]

    result = []
    while stack:
        now_node = stack.pop()
        result.append(now_node.val)
        stack.append(now_node.right) if now_node.right else 0
        stack.append(now_node.left) if now_node.left else 0

    return result


print(preorderTraversal())


# 中序
def zhongxu(root: TreeNode):
    if not root: return []
    stack = [root]
    result = []
    while len(stack) > 0:
        top = stack[-1]
        if top.left:
            stack.append(top.left)
        else:
            result.append(stack.pop().val)
            stack.append(top.right) if top.right else 0

    return result
