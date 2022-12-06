
lst = ['c=', 'c-', 'dz=', 'd-', 'lj', 'nj', 's=', 'z=']

strr = input()

for i in lst:
    strr = strr.replace(i, '*')

print(len(strr))