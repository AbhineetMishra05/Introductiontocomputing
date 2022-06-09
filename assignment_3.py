print("############## Question 1 #############")
number=int(input("Input a number to convert it into its binary equivalent :"))
print("Its binary equivalent is :",bin(number)[2:])
print("############## Question 2 #############")
expression=input("Enter a mathematical expression: ")
number_1=0
number_2=0
operator=""
expression.strip()
count=0
for i in expression:
    if(i.isnumeric()):
        if(count==0):
            number_1=number_1*10+int(i)
        else:
            number_2=number_2*10+int(i)
    else:
        operator=i
        count+=1
if(operator=="+"):
    print("The value of the expression is :",number_1+number_2)
elif(operator=="-"):
    print("The value of the expression is :",number_1-number_2)
elif(operator=="*" or operator=="x" or operator=="X"):
    print("The value of the expression is :",number_1*number_2)
elif(operator=="/"):
    print("The value of the expression is :",number_1/number_2)
elif(operator=="%"):
    print("The value of the expression is :",number_1%number_2)
else:
    print("Operator is not understandable by the program")
print("############## Question 3 #############")
import math
n=int(input("Enter a number for calculations: "))
print("a)",(n+n+1)*(n+2))
print("b)",n*(n-1)/2)
r=int(input("Enter the radius:"))
print("c)",4*math.pi*(r**2))
a=int(input("Enter the value of a :"))
b=int(input("Enter the value of b :"))
print("d)",math.sqrt(r*(math.cos(a)**2)+r*(math.cos(a)**2)))
y1=int(input("Enter the value of y1 :"))
y2=int(input("Enter the value of y2 :"))
x1=int(input("Enter the value of x1 :"))
x2=int(input("Enter the value of x2 :"))
print("e)",(y2-y1)/(x2-x1))
print("############## Question 4 #############")
print('4.(a)')
for i in range(5):
    print(i)
print('4.(b)')
for i in range(3,10):
    print(i)
print('4.(c)')
for i in range(4,13,3):
    print(i)
print('4.(d)')
for i in range(15,5,-2):
    print(i)
print('4.(e)')
for i in range(5,3):
    print(i)
print("############## Question 5 #############")
C = int(input('Enter number of carbon atoms in molecule:'))
H = int(input('Enter number of hydrogen atoms in molecule:'))
O = int(input('Enter number of oxygen atoms in molecule:'))
print('The molecular weight of the compound is',H*1.00794 + C*12.0107 + O*15.9994)
print("############## END #############")

