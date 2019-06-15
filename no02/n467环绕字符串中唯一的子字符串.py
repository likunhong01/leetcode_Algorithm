#coding=utf-8
#Version:python3.7.0
#Tools:Pycharm 2019
# Author:LIKUNHONG
__date__ = ''
__author__ = 'lkh'

'''
int[] pSize = new int[p.length()];
        int[] count = new int[26];
        for (int i = 0; i < p.length() ; i ++) {
            pSize[i] = (int) (p.charAt(i) - 'a');
        }
        int num = 0;
        int sum = 0;
        for (int i = 0; i < pSize.length; i ++) {
            if (i > 0 && (pSize[i - 1] + 1) % 26 == pSize[i] ) {
                num ++;
            }
            else {
                num = 1;
            }
            count[pSize[i]] = Math.max(count[pSize[i]],num);
        }
        for (int i = 0; i < 26; i ++) {
            sum = sum + count[i];
        }
        return sum;'''
class Solution:
    def findSubstringInWraproundString(self, p):
        count = [0 for i in range(26)]
        pSize = [ord(i) - ord('a') for i in p]
        num = 0
        sum = 0
        for i in range(len(p)):
            if i > 0 and (pSize[i-1] + 1) % 26 == pSize[i]:
                num += 1
            else:
                num = 1
            count[pSize[i]] = max(count[pSize[i]], num)
        for i in count:
            sum += i
        return sum

so = Solution()
a = so.findSubstringInWraproundString('abcdefghijklmnopqrstuvwxyzabcdefghijklmnopqrstuvwxyzabcdefghijklmnopqrstuvwxyzabcdefghijklmnopqrstuvwxyzabcdefghijklmnopqrstuvwxyzabcdefghijklmnopqrstuvwxyzabcdefghijklmnopqrstuvwxyzabcdefghijklmnopqrstuvwxyzabcdefghijklmnopqrstuvwxyzabcdefghijklmnopqrstuvwxyzabcdefghijklmnopqrstuvwxyzabcdefghijklmnopqrstuvwxyzabcdefghijklmnopqrstuvwxyzabcdefghijklmnopqrstuvwxyzabcdefghijklmnopqrstuvwxyzabcdefghijklmnopqrstuvwxyzabcdefghijklmnopqrstuvwxyzabcdefghijklmnopqrstuvwxyzabcdefghijklmnopqrstuvwxyzabcdefghijklmnopqrstuvwxyzabcdefghijklmnopqrstuvwxyzabcdefghijklmnopqrstuvwxyzabcdefghijklmnopqrstuvwxyzabcdefghijklmnopqrstuvwxyzabcdefghijklmnopqrstuvwxyzabcdefghijklmnopqrstuvwxyzabcdefghijklmnopqrstuvwxyzabcdefghijklmnopqrstuvwxyzabcdefghijklmnopqrstuvwxyzabcdefghijklmnopqrstuvwxyzabcdefghijklmnopqrstuvwxyzabcdefghijklmnopqrstuvwxyzabcdefghijklmnopqrstuvwxyzabcdefghijklmnopqrstuvwxyzabcdefghijklmnopqrstuvwxyzabcdefghijklmnopqrstuvwxyzabcdefghijklmnopqrstuvwxyzabcdefghijklmnopqrstuvwxyzabcdefghijklmnopqrstuvwxyzabcdefghijklmnopqrstuvwxyzabcdefghijklmnopqrstuvwxyzabcdefghijklmnopqrstuvwxyzabcdefghijklmnopqrstuvwxyzabcdefghijklmnopqrstuvwxyzabcdefghijklmnopqrstuvwxyzabcdefghijklmnopqrstuvwxyzabcdefghijklmnopqrstuvwxyzabcdefghijklmnopqrstuvwxyzabcdefghijklmnopqrstuvwxyzabcdefghijklmnopqrstuvwxyzabcdefghijklmnopqrstuvwxyzabcdefghijklmnopqrstuvwxyzabcdefghijklmnopqrstuvwxyz')
print(a)