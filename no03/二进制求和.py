#coding=utf-8
#Version:python3.7.0
#Tools:Pycharm 2019
# Author:LIKUNHONG
__date__ = ''
__author__ = 'lkh'


def addBinary(a: str, b: str) -> str:
    maxlength = max(len(a), len(b))
    minlength = min(len(a), len(b))
    result = ''
    for i in range(minlength):
        result = str(int(a[-(i+1)]) + int(b[-(i+1)]) if a[-i] and b[-i] else a[-i] or b[-i]) + result
    max_str = a if len(a) == maxlength else b
    result = '0' + max_str[:maxlength-minlength] + result

    print(result)
    for i in range(len(result) - 1, 0, -1):
        if result[i] != '1' and result[i] != '0':
            result = result[:i-1] + str(int(result[i-1])+1) + str(int(result[i])-2) + result[i+1:]
    return result[1:] if result.startswith('0') else result

print(addBinary('1010', '1011'))