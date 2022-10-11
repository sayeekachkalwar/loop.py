n=int(input("enter number"))
for i in range(2,n):
    if n%11==0:
        print(n,"is not prime number")
        break
    else:
        print(n,"is prime number")
        