inp = int(input())
laptops = []
irsa_status = False

for i in range(inp):
    laptop = input()
    laptops.append(laptop.split())

for c1 in laptops:
    if irsa_status:
        break
    for c2 in laptops:
        if c1[0] < c2[0] and c1[1] > c2[1]:
            #print("happy irsa")
            irsa_status = True
            break

if irsa_status:
    print("happy irsa")
else:
    print("poor irsa")