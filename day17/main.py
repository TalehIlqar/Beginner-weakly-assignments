import sys
import datetime
date = datetime.date.today().strftime("%d-%m-%y")
a = sys.argv
arr = []


def count_id():
    with open("id.txt", "r") as k:
        count = int(k.read())
    new_c = count + 1
    with open("id.txt", "w") as l:
        count = l.write(str(new_c))
    return new_c




def add():
    if a[1] == "add":
        c = input("Enter book name: ")
        arr.append(c) 
        b = input("Enter writer name: ")
        arr.append(b)
        # print("Succesfully")
        with open("txt.txt", "a") as p:
            p.write(f"ID: {count_id()}\nBook name: {arr[0]}\nWriter: {arr[1]}\nAdded in : {date} \n \n*\n")
        print("Added Succesfully")

add()


def show_all():
    with open("txt.txt", "r") as d:
        p = d.read().split("*")
        for i in p:
            print(i)

if a[-1] == 'show':
    show_all()
    
    
def remove():
    remov_id = int(input("be delete id write "))
    with open("txt.txt", "r") as d:
        p = d.read().split("*")
        p[remov_id-1] = " "
 
    with open('txt.txt',"w+") as m:
        m.writelines(arr)


if a[-1] == "remove":
    remove()




