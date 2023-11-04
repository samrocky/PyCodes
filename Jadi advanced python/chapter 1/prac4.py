inpnum  = int(input())
inps = []
for i in range(inpnum):
    a = input()
    a = a.split('.')
    i = 1
    a[i] = a[i].lower()
    a[i] = a[i].capitalize()
    inps.append(a)

inps.sort()
for i in inps:
    print('{} {} {}'.format(i[0], i[1], i[2]))