from math import sqrt
inp = int(input())
output_numbers = []

for i in range(inp):
    number = float(input())
    output_numbers.append(sqrt(number))
    
for root in output_numbers:
    root = str(root)
    root = root.split('.')
    if len(root[1]) >= 4 :
        print(root[0]+"."+root[1][0:4])
    elif len(root[1]) == 3 :
        print(root[0]+"."+root[1]+"0")
    elif len(root[1]) == 2 :
        print(root[0]+"."+root[1]+"00")
    elif len(root[1]) == 1 :
        print(root[0]+"."+root[1]+"000")