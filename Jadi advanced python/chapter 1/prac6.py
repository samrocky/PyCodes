import re
import string
n = int(input())
wordlist = []
for i in range(n):
    inp = input()
    inp = inp.split()
    wordlist.append(inp)
inp = input()
inp = inp.split()
for i in range(len(inp)):
     for j in wordlist:
         if inp[i] in j:
             inp[i] = j[0]

inp = " ".join(inp)
print(inp)