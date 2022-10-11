n=int(input("enter number"))
x=n
rev=0
while x>0:
    r=x%10
    rev=rev*10+r
    n=x//10
print("reverse of given no is",rev)
if rev==n:
    print(n,"is a palindrome")
else:
    print(n,"is not a palindrome")
    