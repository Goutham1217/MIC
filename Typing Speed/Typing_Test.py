import time
import random


def speed():
    global time1
    global time2
    global ts
    f = 0
    for i in ts:
        f += 1
    t = (time2 - time1)/60
    f /= 5
    speed = f/t
    speed=str(speed)
    speed=speed[0:5]
    speed=float(speed)
    return speed


def accuracy():
    global text
    global ts
    l = len(ts)
    a=text.split()
    b=ts.split()
    q=0
    for i in range(len(a)):
        q+=len(a[i])
    c=0
    for i in range(len(b)):
        if len(b[i]) > len(a[i]):
            diff=len(b[i])-len(a[i])
            for j in range(diff):
                a[i] += " "
        else:
            diff=len(a[i])-len(b[i])
            for j in range(diff):
                b[i] += " "
    for f in range(len(a)):
        for j in range(len(a[f])):
            if b[f][j] == a[f][j]:
                c=c+1
            else:
                pass
    acc=(c/q)*100
    acc=str(acc)
    acc=acc[0:5]
    acc=float(acc)
    return acc
      
f1=open(r"C:\Users\gouth\Desktop\COMPUTER SCIENCE PROGRAMS\top 200 words.txt","r")
str1=f1.read()
l1=str1.split()
f1.close()
print("Welcome to the typing test program. Would you like to do a typing test? (y/n)")
ch = input("Enter your choice: ")
while ch == "y":
    flag = True
    if flag:
        n = int(input("Enter the number of words: "))
        if n > 100:
            print("Sorry you have reached the limit pls enter a valid no. next time")
            exit()
           
    ts = ""
    for i in range(n):
        ts += random.choice(l1)
        ts += " "
    print("Type this text as fast as possible and hit the enter key: ('x':To exit)")
    for i in range (3):
        time.sleep(1)
        print(i+1)
    time.sleep(1)
    print("GO!!")
    print("==========================================================================================")
    print(ts)
    time1 = time.time()
    text = input()
    time2 = time.time()
    if text=='x':
        print("See you next time pal((:")
        time.sleep(1)
        exit()
    if len(text.split())==len(ts.split()):
        speed2 = speed()
        accuracy2 = accuracy()
        print("Raw speed:", speed2, "wpm")
        actual = speed2*accuracy2/100
        actual=str(actual)
        actual=actual[0:5]
        actual=float(actual)
        print("Actual speed:",actual,"wpm" )
        print("Your accuracy:",accuracy2, "%")
        print("==========================================================================================")
        print("Another test? (y/n)")
        ch = input("Enter your choice: ")
    else:
        print("Pls try again!\nBut this time enter only ",len(ts.split())," words")
        for i in range (3):
            time.sleep(1)
            print(i+1)
        print("GO!!")
        print("==========================================================================================")
        print(ts)
        time1 = time.time()
        text = input()
        time2 = time.time()
        if text=='x':
            print("See you next time pal((:")
            time.sleep(1)
            exit()
        else:
            speed2 = speed()
            accuracy2 = accuracy()
            print("Raw Words per Minute:", speed2, "wpm")
            actual = speed2*accuracy2/100
            print("Actual Words per Minute:",actual,"wpm" )
            print("Your accuracy:",accuracy2, "%")
            print("==========================================================================================")
            print("Another test? (y/n)")
            ch = input("Enter your choice: ")
       
           
else:
    print("Thank you!!")
