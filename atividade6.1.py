n = input()
for e in range(n):
    a, b, mod = input()
    print a%mod, b%mod, (a+b)%mod, (a-b)%mod, (a*b)%mod
