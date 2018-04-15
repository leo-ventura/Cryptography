n = input()
for e in range(n):
    a, b = input()
    i = 0
    while a-i*b >=1:
        print i, a-i*b
        i = i+1
    print "---"