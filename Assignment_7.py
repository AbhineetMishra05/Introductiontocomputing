print("################# Question 1 #################")
from tkinter import *
from tkinter import ttk
win=Tk()
win.geometry("400x200")
net=IntVar()
org=IntVar()
def gst():
    x=net.get()
    y=org.get()
    gst=(x-y)*100/y
    gst_1="GST RATE: "+str(gst)
    label_3=Label(win,text=gst_1)
    label_3.grid(row=4,column=2,sticky=W)

label_1=Label(win,text="Net Price:",bg="light Green")
label_1.grid(ipady=20,ipadx=10,row=0,column=0,sticky=W)
label_2=Label(win,text="Original Price:",bg="yellow")
label_2.grid(ipady=20,row=1,column=0,sticky=W)
en1=Entry(win,textvariable=net,bg="light green")
en1.grid(row=0,column=1,sticky=W,ipady=20)
en2=Entry(win,textvariable=org,bg="yellow")
en2.grid(row=1,column=1,sticky=W,ipady=20)
b1=Button(win,text="Calculate",command=gst)
b1.grid(row=6,column=2,sticky=W)
win.mainloop()


print("################# Question 2 #################")


from tkinter import *
import calendar
def cal():
    call=calendar.calendar(year.get())
    l2=Label(win,text=call,bg="black",fg="white",font=("Times new Roman",15))
    l2.grid(row=2,sticky=W,ipadx=50)
win=Tk()
win.geometry("800x900")
win.title("Calendar Finder")
year=IntVar()
l_1=Label(win,text="Enter the Year :",fg="white",bg="black",font=("Arial",20))
l_1.grid(row=0,column=0,sticky=W)
e=Entry(win,textvariable=year,font=("Arial",20),bg="black",fg="white")
e.grid(row=0,column=1,sticky=W)
b=Button(win,text="See Calendar",command=cal)
b.grid(row=1,column=1,sticky=W)
win.mainloop()


print("################# Question 3 #################")

from tkinter import *
from tkinter import ttk
win=Tk()
win.config(bg="light green")
win.geometry("300x250")
var=""
def press(x):
    global var
    if(x==100):
        var=""
    else:
        var=var+str(x)

    e.config(text=var)

def cal():
    s=0
    count=0
    l=0
    result=0
    exp=""
    global var
    for i in var:
        if(i.isnumeric() and count==0):
            s=s*10+int(i)
        elif(i.isnumeric() and count>0):
            l=l*10+int(i)
        else:
            count+=1
            if(count>1):
                if(exp=="/"):
                    result=s/l
                elif(exp=="*"):
                    result=s*l
                elif(exp=="+"):
                    result=s+l
                elif(exp=="-"):
                    result=s-l
                s=result
                l=0
            exp=i

    if(exp=="/"):
        result=s/l
    elif(exp=="*"):
        result=s*l
    elif(exp=="+"):
        result=s+l
    elif(exp=="-"):
        result=s-l  
    s=result
    e.config(text=str(result))
    var=str(result)
e=Label(win,bg="grey",fg="white",font=20,width=30)
e.grid(row=0, column=0, sticky=W,columnspan=4)
b1=Button(win,text="1",font=20,command=lambda:press(1))
b1.grid(row=1,column=0,sticky=W,ipadx=10,ipady=10)
b2=Button(win,text="2",font=20,command=lambda:press(2))
b2.grid(row=1,column=1,sticky=W,ipadx=10,ipady=10)
b3=Button(win,text="3",font=20,command=lambda:press(3))
b3.grid(row=1,column=2,sticky=W,ipadx=10,ipady=10)
b4=Button(win,text="4",font=20,command=lambda:press(4))
b4.grid(row=2,column=0,sticky=W,ipadx=10,ipady=10)
b5=Button(win,text="5",font=20,command=lambda:press(5))
b5.grid(row=2,column=1,sticky=W,ipadx=10,ipady=10)
b6=Button(win,text="6",font=20,command=lambda:press(6))
b6.grid(row=2,column=2,sticky=W,ipadx=10,ipady=10)
b7=Button(win,text="7",font=20,command=lambda:press(7))
b7.grid(row=3,column=0,sticky=W,ipadx=10,ipady=10)
b8=Button(win,text="8",font=20,command=lambda:press(8))
b8.grid(row=3,column=1,sticky=W,ipadx=10,ipady=10)
b9=Button(win,text="9",font=20,command=lambda:press(9))
b9.grid(row=3,column=2,sticky=W,ipadx=10,ipady=10)
b0=Button(win,text="0",font=20,command=lambda:press(0))
b0.grid(row=4,column=1,sticky=W,ipadx=10,ipady=10)
b_eq=Button(win,text="=",font=20,command=lambda:cal())
b_eq.grid(row=4,column=2,sticky=W,ipadx=10,ipady=10)
b_ac=Button(win,text="AC",font=20,command=lambda:press(100))
b_ac.grid(row=4,column=0,sticky=W,ipadx=3,ipady=10)
bm=Button(win,text="*",font=20,command=lambda:press("*"))
bm.grid(row=1,column=3,sticky=W,ipadx=10,ipady=10)
bd=Button(win,text="/",font=20,command=lambda:press("/"))
bd.grid(row=2,column=3,sticky=W,ipadx=11,ipady=10)
ba=Button(win,text="+",font=20,command=lambda:press("+"))
ba.grid(row=3,column=3,sticky=W,ipadx=8,ipady=10)
bs=Button(win,text="-",font=20,command=lambda:press("-"))
bs.grid(row=4,column=3,sticky=W,ipadx=10,ipady=10)
win.mainloop()

print("################# Question 4 #################")


def quick_sort(arr):
    length=len(arr)
    if(length<=1):
        return arr
    else:
        lower=[]
        higher=[]
        pivot=arr.pop(length-1)
        for i in arr:
            if(i>pivot):
                higher.append(i)
            else:
                lower.append(i)
        return quick_sort(lower)+[pivot]+quick_sort(higher)
n=int(input("Enter the number of students: "))
list=[]
print("Enter the marks of all students.")
while(n>=1):
    a=int(input(""))
    list.append(a)
    n=n-1
print("Sorted marks list: ",quick_sort(list))


print("################# Question 5 #################")


def bubble(arr):
    for i in range(0,len(arr)-1):
        for j in range(0,len(arr)-1-i):
            if(arr[j]>arr[j+1]):
                temp=arr[j+1]
                arr[j+1]=arr[j]
                arr[j]=temp
    return arr
def binary(s,arr):
    low=0
    high=len(arr)-1
    while(low<=high):
        m=(high+low)//2
        if(s<arr[m]):
            high=m-1
        elif(s>arr[m]):
            low=m+1
        elif(s==arr[m]):
            return m
    return -1
def occurance(list):
    global index
    count=1
    n=True
    a=index-1
    b=index+1
    while(n):
        if(a>=0 and list[a]==list[index] ):
            count+=1
            a=a-1
        elif( b<len(list) and list[b]==list[index]):
            count+=1
            b+=1
        else:
            return count
n=int(input("Enter the number of elements:"))
print("Enter the elements:")
list=[]
for i in range(0,n):
    z=int(input(""))
    list.append(z)
list=bubble(list)
print("Sorted List: ",list)
search=int(input("Enter the element to be searched:"))
index=binary(search,list)
if(index==-1):
    print("Element not found.")
else:
    print("Element found at index ",index)
    print("Number of occurance: ",occurance(list))


print("################# Question 6 #################")


def remove(list):
    l=len(list)
    n=0
    while(n<l-1):
        j=n+1
        while(j<l):
            if(list[n]==list[j]):
                list.pop(j)
                l=l-1
            j+=1
        n=n+1
    return list
def bubble(arr):
    for i in range(0,len(arr)-1):
        for j in range(0,len(arr)-1-i):
            if(arr[j]>arr[j+1]):
                temp=arr[j+1]
                arr[j+1]=arr[j]
                arr[j]=temp
    return arr
n=int(input("Enter the number of items: "))
list=[]
for i in range(n):
    z=int(input(""))
    list.append(z)
list=remove(list)
print("List without duplicates: ",list)
print("Sorted list:",bubble(list))
