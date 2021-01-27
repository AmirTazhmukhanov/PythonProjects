import sqlite3 as sql
import funcBlog as f
class Blog:
    def __init__(self,title,descr,date,author):
        self.title = title
        self.descr = descr
        self.date = date
        self.author = author

class User:
    def __init__(self,name,password,status,age):
        self.name = name
        self.password = password
        self.status = status
        self.age = age
            
while True:
    print("1. Sing In")
    print("2. Sing Up")
    print("0. Exit")
    x = int(input("Enter number:"))
    if x == 1:
        name = input("Your name:")
        password = input("Your password:")
        if f.Sign_In(name,password)[0] == "user":
            print("1. Show all blogs")
            print("2. Search by title")
            print("3. Search by description")
            print("0. Exit")
            xs = int(input("Enter num:"))
            if xs == 0:
                break
            elif xs == 1:
                for i in f.Show_all_blogs():
                    print(i)
            elif xs == 2:
                title = input("Enter title:")
                print(f.Search_by_title(title))

            elif xs == 3:
                descr = input("Enter description:")
                for i in f.Search_by_descr(descr):
                    print(i)
        else:
            print("aaaaa")

        if f.Sign_In(name,password)[0] == "admin":
            while True:
                print("1. Show all blogs")
                print("2. Search by title")
                print("3. Search by description")
                print("4. Add blog")
                print("5. Edit blog")
                print("6. Delete blog")
                print("0. Exit")
                xs = int(input("Enter num:"))
                if xs == 0:
                    break
                elif xs == 1:
                    for i in f.Show_all_blogs():
                        print(i)
                elif xs == 2:
                    title = input("Enter title:")
                    print(f.Search_by_title(title))

                elif xs == 3:
                    descr = input("Enter description:")
                    for i in f.Search_by_descr(descr):
                        print(i)
                elif xs == 4:
                    title = input("Enter title:")
                    date = input("Enter date:")
                    descr = input("Enter description:")
                    author = input("Input author's name:")
                    f.Add_Blog(title,descr,date,author)
                elif xs == 5:
                    old_title = input("Enter the title of blog:")
                    old_descr = input("Enter the descr of blog:")
                    new_title = input("Enter new title:")
                    new_descr = input("Enter new description:")
                    # date = input("Enter date:")
                    # author = input("Enter author:")
                    f.Edit_blog(old_title,old_descr,new_title,new_descr)
                elif xs == 6:
                    title = input("Enter title of blog:")
                    f.Delete_blog(title)

        else:
            print("Ошибка")
    elif x == 2:
        try:
            name = input("Enter name:")
            password = input("Enter password:")
            age = int(input("Enter age:"))
            if f.Sign_up(name,password,age) == True:
                print("Succesfully signed up")
            else:
                print("This account already exists")
        except:
            print("Ошибка")
    elif x == 0:
        break

