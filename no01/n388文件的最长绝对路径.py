#coding=utf-8
#Version:python3.7.0
#Tools:Pycharm 2019
# Author:LIKUNHONG
__date__ = ''
__author__ = 'lkh'

str1 = 'dir\n\tsubdir1\n\t\tfile1.ext\n\t\tsubsubdir1\n\tsubdir2\n\t\tsubsubdir2\n\t\t\tfile2.ext'+'\n'
str1 = 'dir\n\tsubdir1\n\tsubdir2\n\t\tfile.ext' + '\n'
longest = 0
table_count = 0
stack = []
isfile = False
child_len = 0
for ch in str1:
    if ch == '\n':
        # 首先把之前的兄弟文件夹（文件）的长度记录清除，只留父文件夹的长度
        while(len(stack) > table_count):
            stack.pop()
        # 当前长度=到上一级长度+'/'+当前文件名长度
        length = (stack[-1] + 1 if len(stack) != 0 else 0) + child_len
        if isfile:
            # 是文件，更新最长的
            longest = max(length, longest)
        else:
            # 不是文件，就把到这一级的前面字符长度入栈
            stack.append(length)
        # 最后把记录删掉
        child_len = table_count = 0
        isfile = False
    elif ch == '\t':
        table_count += 1
    else:
        # 如果是
        if ch == '.':
            isfile = True
        child_len += 1
print(longest)


class Solution:
    def lengthLongestPath(self, input: str) -> int:
        longest = 0
        table_count = 0
        stack = []
        isfile = False
        child_len = 0
        input += '\n'
        for ch in input:
            if ch == '\n':
                while (len(stack) > table_count):
                    stack.pop()
                length = (stack[-1] + 1 if len(stack) != 0 else 0) + child_len
                if isfile:
                    longest = max(length, longest)
                else:
                    stack.append(length)
                child_len = table_count = 0
                isfile = False
            elif ch == '\t':
                table_count += 1
            else:
                if ch == '.':
                    isfile = True
                child_len += 1
        return longest
