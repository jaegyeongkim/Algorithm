n=1000000
a = [False,False] + [True]*(n-1)
primes=[]

for i in range(2,n+1):
  if a[i]:
    primes.append(i)
    for j in range(2*i, n+1, i):
        a[j] = False
for i in range(len(primes)-1):
    print(primes[i], end=' ')
print(primes[-1])