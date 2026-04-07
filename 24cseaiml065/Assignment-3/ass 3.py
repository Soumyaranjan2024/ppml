#wap to print twin prime numbers betn 1 to N
N=int(input("enter the number"))
for i in range(2,N):
    d=0
    for j in range(1,i+1):
        if i%j==0:
            d=d+1
    if d==2:
        d=0
        N=i+2
        for j in range(1,N+1):
            if N%j==0:
                d=d+1
        if d==2:
            print("(%d,%d)"%(i,N))

#wap to find then factorial of a number
x=int(input("enter the number"))
fact=1
if x<0:
    print("it is a negative number")
elif x==0:
     print("factorial is ",fact)
else:
    for i in range(1,x+1):
        fact=fact*i
    print("the factorial is ",fact)

#wap to check the leap year
x=int(input("enter the year"))
if(x%4==0)and(x%100!=0)or(x%400==0):
    print(x,"it is a leap year")
else:
    print(x,"it is not a leap yaer")

#04)wap to check whether a string is symmetrical or palindrome

x=input("enter the string")
z=(str(str(x)[::-1]))
if x==z:
    print(x,"is palindrome")
else:
    print("not palindrome")

#05)wap to print even length words in a string
x=input("enter the string")
y=""
for c in x:
    if c!=" ":
        y=y+c
    else:
        if len(y)%2==0:
            print(y)
        y=""
if len(y)%2==0:
    print(y)

#06)wap to remove all duplicates from a given string
x=input("enter the string")
result=""
for char in x:
    if char not in result:
        result=result+char
print(result)