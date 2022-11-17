import os

def writeData():
    data = '\nDATABASE SUBMISSION!'
    with open('test8.txt', 'a') as f:
        f.write(data)
        f.close()


def openFile():
    with open('test8.txt', 'r') as f:
        data = f.read()
        print(data)
        f.close()


if __name__== "__main__":
    writeData()
    openFile()


import sqlite3


conn = sqlite3.connect('test.db')

with conn:
    cur = conn.cursor()
    cur.execute ("CREATE TABLE IF NOT EXISTS tbl_persons( \
            ID INTEGRER PRIMARY KEY AUTOINCREMENT, \
            col_fname TEXT, \
            col_lname TEXT, \
            col_email TEXT \
            )")
    conn.commit()
conn.close()

conn = sqlite3.connect('test.db')

with conn:
    cur = conn.cursor()
    cur.execute("INSERT INTO tbl_persons(col_fname, col_lname, col_email) VALUES (?,?,?)", \
                        ('Sara', '  Jones ', 'bsmith@gmail.com'))
    cur.execute("INSERT INTO tbl_persons(col_fname, col_lname, col_email) VALUES (?,?,?)", \
                        ('Sally', 'Smith', 'bsmith@gmail.com'))
    cur.execute("INSERT INTO tbl_persons(col_fname, col_lname, col_email) VALUES (?,?,?)", \
                        ('Bob', 'Smith', 'bsmith@gmail.com'))
    conn.commit()
conn.close()


conn = sqlite3.connect('test.db')

with conn:
    cur = conn.cursor()
    cur.execute("SELECT  col_fname, col_lname, col_email FROM tbl_persons WHERE col_fname = 'Sara' ")
    varPerson = cur.fetchali()
    for item in varPerson:
        msg = "First Name: ()\nLast Name: ()\nEmail:()".format(item[0], item[1], item[2])
        print(msg)



