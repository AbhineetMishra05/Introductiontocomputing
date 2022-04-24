#Question 1
num1=float(input("Enter the first number:"))
num2=float(input("Enter the second number:"))
num3=float(input("Enter the third number:"))
avg=(num1+num2+num3)/3
print("The average of the three entered numbers is:",avg)

#Question 2
tax_rate=20/100
standard_deduction=10000
gross=float(input("Enter the gross income:"))
dependents=int(input("Enter the number of dependents:"))
taxable_income=gross-standard_deduction-(dependents*3000)
tax=taxable_income*tax_rate
print("Taxable income:",taxable_income)
print("Tax:",tax)

#Question 3
SID=input("Enter the SID of the Student: ")
Name=input("Enter the Name of the Student: ")
Gender=input("Enter the Gender of the Student(Use Gender values: F, M, U (For Unknown).): ")
Course_Code=input("Enter the Course Code of the Student: ")
CGPA=float(input("Enter the CGPA of the Student: "))
Student=[SID,Name,Gender,Course_Code,CGPA]
print(Student)

#Question 4
a=int(input("Enter Marks of 1st Student: "))
b=int(input("Enter Marks of 2nd Student: "))
c=int(input("Enter Marks of 3rd Student: "))
d=int(input("Enter Marks of 4th Student: "))
e=int(input("Enter Marks of 5th Student: "))
marks=[a,b,c,d,e]
print(sorted(marks))

#Question 5
color=['Red', 'Green', 'White', 'Black', 'Pink', 'Yellow']
a=color.pop(4)
print(color)
color=['Red', 'Green', 'White', 'Black', 'Pink', 'Yellow']
color=['Purple' if i=='Pink' or i=='Black' else i for i in color]
print(color)
