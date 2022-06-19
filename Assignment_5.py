print("################### Question 1 ##################")


str=input("Enter the string to be reversed : ")
end=len(str)-1
str_rev=""
for i in range(0,len(str)):
        str_rev=str_rev+str[end]
        end=end-1
print("Reverse of the string is : ",str_rev)


print("################### Question 2 ##################")

print("Enter the range to check for divisibility")
start=int(input("Enter the starting range: "))
end=int(input("Enter the ending range: "))
div=int(input("Enter the number from which we will check the divisibility: "))
for i in range(start,end+1):
    if(i%div==0):
        print(i,end="")
        print(",",end="")
print("\b is divisible by ",div)


print("################### Question 3 ##################")
 
import math
print("Heron's Formula to calculate area of the triangle:")
side_1=int(input("Enter the first side of the triangle: "))
side_2=int(input("Enter the second side of the triangle: "))
side_3=int(input("Enter the third side of the triangle: "))
if(side_1+side_2>side_3 and side_1+side_3>side_2 and side_3+side_2>side_1 ):
    s=(side_1+side_2+side_3)/2
    area=math.sqrt(s*(s-side_1)*(s-side_2)*(s-side_3))
    print("Area of the Triangle : ",area)
else:
    print("The following triangle cannot be formed.")


print("################### Question 4 ##################")

n=1
count=1
while(n!=0):
    m=n
    while(m!=0):
        print("*",end="")
        m=m-1
    print()
    if(count<5):
        count+=1
        n+=1
    else:
        n-=1

print("################### Question 5 ##################")

rows=int(input("Enter the number of rows :"))
char=65
for i in range(0,rows):
    for j in range(0,i+1):
        if(chr(char)=="Z"):
            char=65
        print(chr(char),end="")
        char=char+1
        if(chr(char)=="Z"):
            char=65
    print()


print("################### Question 6 ##################")

print("Program to show all the prime numbers in the user inputted range")
start=int(input("Enter the starting range : "))
end=int(input("Enter the ending range : "))
for i in range(start,end+1):
    count=0
    for j in range(2,int(math.sqrt(i))+1):
        if(i%j==0):
            count=1
    if(count==0):
        print(i,end="")
        print(",",end="")
print("\b is a prime number.")



print("################### Question 7 ##################")


for i in range(1,501):
    if(i%7==0 and i%11==0):
        print(i,end="")
        print(",",end="")
print("\b is divisible by 7 as well as 11.")


print("################### Question 8 ##################")


print("Input 10 nos to check whether it is positive/negative ,odd/even and no of times each inputted no. occurs")
print("Enter 10 nos.")
list=[]
for i in range(0,10):
    app=int(input(""))
    list.append(app)
l=10
n=0
while(n<l):
    count=1
    k=n+1
    while(k<l):
        if(list[n]==list[k]):
            count+=1
            del list[k]
            l=l-1
        else:
             k=k+1
    print(list[n]," is present ",count,"times in the list.")
    n=n+1
for i in range(0,len(list)):
    if(list[i]>0):
        print("The number ",list[i]," is positive and ",end=" ")
        if(list[i]%2==0):
            print("even. ")
        else:
            print("odd. ")
    elif(list[i]<0):
        print("The number ",list[i]," is negative and ",end="")
        if(list[i]%2==0):
            print("even. ")
        else:
            print("odd. ")
    else:
        print("The number is neither positive nor negative.")



print("################### Question 9 ##################")


print("Enter the words in the list and when completed enter 'quit' to stop")
list=[]
app=""
while(app!="quit"):
    app=input("")
    list.append(app)
l=len(list)
n=0
while(n<l):
    count=1
    k=n+1
    while(k<l):
        if(list[n]==list[k]):
            count+=1
            del list[k]
            l=l-1
        else:
             k=k+1
    if(list[n]!="quit"):
        print(list[n]," is present ",count,"times in the list.")
    n=n+1






