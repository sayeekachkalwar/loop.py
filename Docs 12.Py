user=int(input("enter the digit"))
pro=1
while user>0:
    n=user%10
    pro=pro*n
    user=user//10
print(pro)