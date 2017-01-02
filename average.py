def average(*args):
    n=0.0
    sum=0.0
    if args:
        for x in args:
            n=n+1
            sum=sum+x
        return sum/n
    else:
        return 0.0

print average(1)

print average(1,3,5)
print average(100,120,158)
