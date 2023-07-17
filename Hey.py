av = 10
x = int(input("How many candies you want?"))

i = 1
while i<=x:
    if i>av:
        print("out of stock")
        break
    print("candy")
    i+=1

print("bye")

from array import*
arr = array('i', [])
n = int(input("enter the length of the array"))
for i in range (n):
    x = int(input("enter the next value"))
    arr.append(x)
print(arr) 
val = int(input("enter the next value"))
for e in arr:
    if e==val:
        print(k)
        k=11
        break 
    k+=1
print(arr.index(val))      
from numpy import*

arr = array('i' , [1,2,3,])
print(arr)