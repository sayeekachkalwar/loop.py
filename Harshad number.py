n=int(input("enter number"))
x=n
sum=0
while x>0:
    r=x%10
    sum=sum+r
    x=x//10
if n%sum==0:
    print(n,"is harshad number")
else:
    print(n,"is not harshad number")
    