#wap to print the second largest and second largest element in  alist of 10 integers without using sort fxn
arr=[]
x=int(input("enter the no. elements"))
for i in range(x):
    m = int(input("enter  the elements"))
    arr.append(m)
for j in range(len(arr)-1):
    for k in range(len(arr)-j-1):
        if arr[k]>arr[k+1]:
            arr[k],arr[k+1]=arr[k+1],arr[k]
print("the sorted array is :")
print(arr)
second_largest=arr[-2]
second_smallest=arr[1]
print("second largest no. is ",second_largest)
print("second smallest no. is ",second_smallest)

#wap to create two lists first list containing 5 integers and second list conatining 5 strings.print both the list one element from each list combined at a time
list1=[1,2,6,7,8]
list2=["a","b","c","d","e"]
s=[]
for i in range(len(list1)):
    s.append(str(list1[i]))
    s.append(list2[i])
print(s)

#wap top create an integer list of 20 elements increase the odd valued elements by 5.
s=[]
x=int(input("enter the no. of elements"))
for i in range(x):
    n=int(input("enter the elements"))
    s.append(n)
for i in range(x):
    if s[i]%2!=0:
        s[i]=s[i]+5
print(s)

#wap to create a fxn that prints the first 15 terms of the fibonacci series without using recurrsion
def fibo(n):
    a=0
    b=1
    for i in range(2,n):
        print(a,end=" ")
        a=b
        b=c
        c=a+b
num=int(input("enter the element"))
fibo(num)

#wap to craete a fxn that takes list as argument and returns the even values of the list.print the new list with even values
def even(n):
    s=[]
    for i in n:
        if i%2==0:
            s.append(i)
    return s
x=input("enter the list elements")
n=[int(i) for i in x.split(",")]
s=even(n)
print(s)