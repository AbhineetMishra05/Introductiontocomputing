print("######################### Question 1 ######################")
marks=float(input("Enter the marks to get the corresponding grade : "))
if(marks<25):
    print("The grade for the entered marks is : F")
elif(marks<45):
    print("The grade for the entered marks is : E")
elif(marks<50):
    print("The grade for the entered marks is : D")
elif(marks<60):
    print("The grade for the entered marks is : C")
elif(marks<80):
    print("The grade for the entered marks is : B")
else:
    print("The grade for the entered marks is : A")


print("######################### Question 2 ######################")
year=int(input("Enter the year to check whether it is a leap year or not : "))
if(year%4==0 and year%100!=0):
    print("It is a leap year!!!")
elif(year%100==0 and year%400==0):
    print("It is a leap year!!!")
else:
    print("It is not a leap year!!!")

print("######################### Question 3 ######################")
import random
list=[0,1,2,3,4,5,6,7,8,9]
n=1
while(n<=10):
    number_1=random.choice(list)
    number_2=random.choice(list)
    print("Question ",n,":",number_1," X ",number_2," = ",end="") 
    answer=int(input(""))
    if(number_1*number_2==answer):
        print("Right!")
    else:
        print("Wrong. The answer is ",number_1*number_2)
    n+=1

print("######################### Question 4 ######################")
n=0
while(n<200):
    if(n%5==2 and n%6==3 and n%7==2):
        print("The jar of halloween candy contains ",n," candies.")
    n+=1