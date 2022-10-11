user=int(input("enter the digit"))
sum=0
while user>0:
    n=user%10
    sum+=n
    user=user//10
print(sum)
