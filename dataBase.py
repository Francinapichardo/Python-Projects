import sqlite3

connection = sqlite3.connect('pythonDB.db')

c = connection.cursor()

# Create the table

c.execute("""CREATE TABLE file (
    data text
)
""")

# list of files

list = [('informatio.docx', 'hello.txt', 'myImage.png',
         'myMovie.mpg', 'World.txt', 'data.pdf', 'myPhoto.jpg')
        ]


# List of files with .txt extensions
new_list = []

# For by the List in search of the extensions txt
for x in list[0]:

    # Find the file with .txt extension

    lista = x.find(".txt")

    # if x have the .txt estension will append the element (x) on the new_list

    if lista > 0:
        print(x + ': have TXT extension ')
        # c.execute("INSERT INTO file (data) VALUES (?)", x)
        new_list.append(x)

    # otherwise print the element without .txt extension
    else:
        print(x + ": Don't have TXT extension")


# Insert the element into new_list on the database
c.execute("INSERT INTO file (data) VALUES (?)", [new_list[0]])
c.execute("INSERT INTO file (data) VALUES (?)", [new_list[1]])


# SELECT ALL DATA on the table file with id
c.execute("SELECT rowid, * FROM file")
print(c.fetchall())

print("Command exectued succesfully...")
connection.commit()
connection.close()
