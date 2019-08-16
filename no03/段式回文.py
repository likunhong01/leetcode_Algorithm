#coding=utf-8
#Version:python3.7.0
#Tools:Pycharm 2019
# Author:LIKUNHONG
__date__ = ''
__author__ = 'lkh'

def longestDecomposition(text: str) -> int:
    head = 0
    tail = len(text) - 1
    count = 0
    if head == tail: return 1
    while head < tail:
        str1 = str2 = ''
        while (str1 != str2 or str1 == '') and head < tail:
            str1 += text[head]
            str2 = text[tail] + str2
            head += 1
            tail -= 1
        if str1 == str2:
            count += 2
        else:
            count += 1
        if str1 == str2 and head == tail:
            count += 1
        # if head-1 > tail+1:
        #     count += 1
        # else:
        #     count += 2
        print('第',count,'对',str1,str2,head,tail)
    # return count + 1 if head == tail else count
    return count

print(longestDecomposition('a'))