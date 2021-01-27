import sqlite3 as sql
def Show_all_blogs():
    con = sql.connect("dbputhon.db")
    cur = con.cursor()
    cur.execute("SELECT * FROM blog")
    return cur.fetchall()

def create_table():
    con = sql.connect("dbputhon.db")
    with con:
        cur = con.cursor()
        cur.execute("DROP TABLE user")
        query = "CREATE TABLE IF NOT EXISTS 'blog'('id' INTEGER, 'title' STRING, 'descr' STRING, 'author_name' STRING)"
        query1 = "CREATE TABLE IF NOT EXISTS 'user'('name' STRING, 'password' STRING, 'age' INTEGER, 'status' STRING)"
        cur.execute(query)
        cur.execute(query1)
        cur.execute("INSERT INTO user VALUES('admin', 'admin', 99, 'admin')")
        cur.execute("INSERT INTO blog VALUES(1, 'asd', 'asd', 'admin')")
        con.commit()

# create_table()

def Search_by_title(title):
    con = sql.connect("dbputhon.db")
    with con:
        cur = con.cursor()
        cur.execute("SELECT * FROM blog WHERE title = '{}'".format(title))
        new_list = cur.fetchall()
        con.commit()

def Search_by_descr(descr):
    con = sql.connect("dbputhon.db")
    with con:
        cur = con.cursor()
        cur.execute("SELECT * FROM blog WHERE descr = '{}'".format(descr))
        new_list = cur.fetchall()
        con.commit()

def Add_Blog(title,descr,date,author):
    con = sql.connect("dbputhon.db")
    with con:
        cur = con.cursor()
        cur.execute("INSERT INTO blog VALUES('{}','{}','{}','{}')".format(title,descr,date,author))
        con.commit()

def Delete_blog(title):
    con = sql.connect("dbputhon.db")
    with con:
        cur = con.cursor()
        cur.execute("DELETE FROM blog WHERE title =  '{}'".format(title))
        con.commit()

def Edit_blog(old_title,old_descr,title,descr):
    con = sql.connect("dbputhon.db")
    with con:
        cur = con.cursor()
        cur.execute("SELECT title FROM blog WHERE title = '{}' and descr = '{}'".format(old_title,old_descr))
        l = cur.fetchone()
        print(l)
        if cur.fetchone()== old_title:
            cur.execute("UPDATE blog SET title = '{}', descr = '{}' WHERE title = '{}' and descr = '{}'".format(title,descr,old_title,old_descr))
            con.commit()
            return  True
        else:
            return False
Edit_blog("asd","asd","2552","qwe")
def Sign_up(name,password,age):
    con = sql.connect("dbputhon.db")
    with con:
        cur = con.cursor()
        cur.execute("SELECT name FROM user WHERE name = '{}'".format(name))
    if cur.fetchone() == None:
        cur.execute("INSERT INTO user VALUES('{}', '{}',{},'{}')".format(name,password,age,"user"))
        con.commit()
        return True
    else:
        return False

def Sign_In(name,password):
    con = sql.connect("dbputhon.db")
    with con:
        cur = con.cursor()
        cur.execute("SELECT status FROM user WHERE name = '{}' and password='{}'".format(name,password))
        con.commit()
        return cur.fetchone()

def Show_all_users():
    con = sql.connect("dbputhon.db")
    with con:
        cur = con.cursor()
        cur.execute("SELECT * FROM user")
        con.commit()
        return cur.fetchall()
print(Show_all_users())
print(Sign_In("Amir","qwerty123"))

