import sqlite3


def connect():
    conn = sqlite3.connect("books.db")
    cur = conn.cursor()
    cur.execute("CREATE TABLE IF NOT EXISTS book(id INTEGER PRIMARY KEY, title TEXT, author TEXT, year INTEGER, isbn INTEGER)")
    conn.commit()
    conn.close()


def insert(title, author, year, isbn):
    conn = sqlite3.connect("books.db")
    cur = conn.cursor()
    cur.execute("INSERT INTO book VALUES(NULL,?,?,?,?)",(title,author,year,isbn)) #null writen in id so as to make auto increment
    conn.commit()
    conn.close()

def view():
    conn = sqlite3.connect("books.db")
    cur=conn.cursor()
    cur.execute("SELECT * FROM book")
    rows=cur.fetchall()
    conn.close()
    return rows


def search (title="", author="", year="", isbn=""): #sometimes you will chose only one parameter hence the " "
    conn = sqlite3.connect("books.db")
    cur = conn.cursor()
    cur.execute("SELECT * FROM book WHERE title=? OR author =? OR year=? OR isbn=?",(title,author,year,isbn))
    rows= cur.fetchall()
    conn.close()
    return rows

def delete (id):
    conn = sqlite3.connect("books.db")
    cur = conn.cursor()
    cur.execute("DELETE FROM book WHERE id =?",(id,))
    conn.commit()
    conn.close()

def update (id,title,author,year,isbn):
    conn = sqlite3.connect("books.db")
    cur = conn.cursor()
    cur.execute("UPDATE book SET title=?, author=?, year=?,isbn=? WHERE id=?",(title,author,year,isbn,id))
    conn.commit()
    conn.close()





connect()
#insert("Murder of Roger Ackroyd","Agatha Christie",2011,929292)
print(view())
#update(1,"And Then There Were None","Agatha Christie",1962,2828)
print(view())
