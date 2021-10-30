from django.template.defaultfilters import length
from numpy import arange

a = [[1,2,3], [4,5,6]]
print(a[0])
print(a[1])
for i in range(len(a)):
    for y in range(len(a[i])):
        print(a[i][y], end=',')
    print()

for i in a:
    for y in i:
        print(y, end=' ')
    print()


a = 15
d = 30
if a == d:
    print('они равны')
    if a < d:
        print('а меньше d')

def fact(x):
    if x == 1:
        return 1
    else:
        return x * fact(x-1)

a = fact(5)
print(a)
#
# s = list(range(1, 50, 5))
# (map(lambda y: y, s))
# ans = []
# print(ans)
# [print(i, end=',') for i in s]


firstname = 'John'
lastname = 'Ray'
print(firstname + ' ' + lastname)

a = firstname + lastname
a.join('')
print(a)
print(''.join(['John', 'Ray']))

