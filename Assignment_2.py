print("#####Question 1#####")
a= "Python is a case sensitive language"
length=len(a)
print("Lenth of the String is:",length)
reverse = a[::-1]
print("Reverse of the String is:",reverse)
replace=a.replace("a case sensitive","object oriented",)
print("The replaced String is:",replace)
index=a.find("a")
print("Index of Substring 'a' is:",index)
remove= a.replace(" ","")
print("String with removed white spaces:",remove)
print("#################### \n")
print("#####Question 2#####")
name=input("Enter your Name:")
SID=int(input("Enter your SID:"))
department_name= input("Enter your department name:")
CGPA=float(input("Enter your CGPA:"))
print(" Hey, {} Here! \n My SID is {} \n I am from {} department and my CGPA is {}".format(name,SID,department_name,CGPA))
print("#################### \n")
print("#####Question 3#####")
a=56 
b=10
print("a&b: ",a&b)
print("a|b: ",a|b)
print("a^b: ",a^b)
print("Left shift a with 2 bits: ",a<<2)
print("Right shift a with 2 bits: ",a>>2)
print("Left shift b with 2 bits: ",b<<2)
print("Right shift b with 2 bits: ",b>>2)
print("#################### \n")
print("#####Question 4#####")
str=input("Enter a string: ")
print("The word 'name' is present in the string: ")
if 'name' in str:
    print("YES")
else:
    print("NO")
print("#################### \n")
print("#####Question 5#####")
a=float(input("Enter the length of the first side of the triangle:"))
b=float(input("Enter the length of the second side of the triangle:"))
c=float(input("Enter the length of the third side of the triangle:"))
d = a+b<c or b+c<a or c+a<b
match d:
  case True: print("The triangle cannot be formed")
  case False: print("The triangle can be formed")
print("#################### \n")
print("#####Question 6#####")
a=int(input("Enter the first number:"))
b=int(input("Enter the second number:"))
c=bin(a^b)
count=0
for i in c:
    if i=='1':
        count=count+1
print("Number of bits needed to be flipped to convert ‘a’ to ‘b’:",count)
print("#################### \n")
