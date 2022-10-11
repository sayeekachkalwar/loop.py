n=int(input("enter a number"))
len=len(str(n))
sum=0
i=n
while n>0:
    digit=n%10
    sum+=digit**len
    n=n//10
if i==sum:
    print(i,"it is a armstrong number")
else:
    print(i,"it is not a armstrong number")
    