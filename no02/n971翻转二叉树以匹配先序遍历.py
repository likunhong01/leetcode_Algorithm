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

class Solution(object):
    count = 0
    def flipMatchVoyage(self, root, voyage):
        # 进行深度优先遍历。如果遍历到某一个节点的时候，节点值不能与行程序列匹配，那么答案一定是 [-1]。
        # 否则，当行程序列中的下一个期望数字 voyage[i] 与我们即将遍历的子节点的值不同的时候，
        # 我们就要翻转一下当前这个节点
        res = self.dfs(root, voyage, [])

        if res and res[0] == -1:
            return [-1]
        else:
            return res

    def dfs(self, node, voyage, res):
        if node:
            if node.val != voyage[self.count]:
                res = [-1]
                return res
            self.count += 1

            if (self.count < len(voyage) and
                    node.left and node.left.val != voyage[self.count]):
                res.append(node.val)
                res = self.dfs(node.right, voyage, res)
                res = self.dfs(node.left, voyage, res)
            else:
                res = self.dfs(node.left, voyage, res)
                res = self.dfs(node.right, voyage, res)
        return res

n1 = TreeNode(1)
n2 = TreeNode(2)
n3 = TreeNode(3)
n1.left = n2
n1.right = n3
s = Solution()
a = s.flipMatchVoyage(n1, [1, 3,2])
print(a)