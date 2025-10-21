def sum(n):
    return n*(n+1)/2
print(sum(4))
#Space complexity: θ(1), Auxillary space=θ(1)
#Linear space
def arraysum(a):
    sum=0
    for i in a:
        sum=sum+i
    return (sum)
a=[12, 3, 4, 15]
print(arraysum(a))
#With the size of the array, the space also required increases

#Space complexity:θ(n), Auxiliary space= θ(1)
def summ(n):
    if(n<=0):
        return 0
    return n+summ(n-1)
print(summ(4))

