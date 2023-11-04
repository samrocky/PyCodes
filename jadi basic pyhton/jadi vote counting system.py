from collections import OrderedDict
num = int(input())
lst = []
for i in range(num):
    a = input()
    lst.append(a)


lst = sorted(lst)
candids = sorted(list(set(lst)))
number_of_candids = len(candids)
for i in range(number_of_candids):
    print(candids[i], lst.count(candids[i]))
