s = ''
num1 = '12348'
num2 = '42352'
len1 = len(num1)
len2 = len(num2)
len3 = max(len1,len2) + 1
for i in range(len3 - len2):
    num2 = '0' + num2
for i in range(len3 - len1):
    num1 = '0' + num1
num3 = [0 for i in range(len3)]
for i in range(1,len3):
    num3[len3 - i] += int(num1[len3-i]) + int(num2[len3-i])
    if num3[len3-i] > 9:
        num3[len3-i] = num3[len3-i] % 10
        num3[len3-i-1] += 1
s = ''
for i in range(len3):
    if i == 0 and num3[0] == 0:
        continue
    else:
        s += str(num3[i])
print(s)