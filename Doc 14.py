# user=int(input("enter the number"))
# i=1
# while i<=user:
#     if i%2==0:
#         user=user//2
#     print(i)
#     i=i+1
    
    

n=int(input("enter number"))
x=n
rev=0
while x>0:
    r=x%10
    rev=rev*10+r
    n=x//10
print("Reverse of given number is",rev)
if rev==n:
    print(n,"is a palindrome")
else:
    print(n,"is not a palindrome")
    