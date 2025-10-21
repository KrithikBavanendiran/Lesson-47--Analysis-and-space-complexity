n=4
def prints(n):
    if(n<=0):
        return
    print("Codingal")
    prints(n/2)
    prints(n/2)

prints(n)
print("The time complexity is n log(n)")