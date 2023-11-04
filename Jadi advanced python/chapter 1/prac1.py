def primeNumbers(n):
    primes=[]
    for i in range(2, n+1):
        for j in range(2, int(i ** 0.5) + 1):
            if i%j == 0:
                break
        else:
            primes.append(i)
    return primes

inpNums = []
numsDivisor = []

for i in range(10):
    a = int(input())
    inpNums.append(a)

for num in inpNums:
    primeDivisorCounter = 0
    primeUntil = primeNumbers(num)
    for i in primeUntil :
        if num%i == 0:
            primeDivisorCounter += 1
    numsDivisor.append((primeDivisorCounter, num))

numsDivisor.sort()
numsDivisor = numsDivisor[::-1]
outList = list(numsDivisor[0])
print(outList[1], outList[0])