import mysql.connector

mydb = mysql.connector.connect(
    host = "127.0.0.1",
    user = 'root',
    password = 'root',
    database = 'openAI'
)


mycursor = mydb.cursor()
mycursor.execute("SELECT title FROM blog")

data = ["Kathmandu city of temples",
        "new sample data",
        "iphone vs samsung",
        "new sample data",
        "new sample data",
        "another",
        "ok",
        "chance",
        'forever',
        "last only"
        ]

table=mycursor.fetchall()
# print(type(table))
# print(table[0])
# for j,i in enumerate(table):
#     print(i[0])

#     print(data[j])

#     if i[0] == data[j]:
#         print("exist")

#     else:
#         sql = "INSERT INTO blog (title, blog_desc ,image_summary,image_url) VALUES (%s,%s,%s,%s)"
#         val = (data[j],"updated","updated","updated")
#         mycursor.execute(sql,val)
#         mydb.commit()
#         print("=================")
#         print(mycursor.rowcount,"row added")
#         print("===================")

# for j,i in enumerate(table):
#     print(i[0])

#     if i[0] in data:
#         print("exist")

#     else:
#         print("doesn't exist")

# list = []
# for i in 

for j,i in enumerate(data):
    # print(i)
    try:
        print(table[j][0])
        if table[j][0] in data:
            print("exist")
        else:
            sql = "INSERT INTO blog (title, blog_desc ,image_summary,image_url) VALUES (%s,%s,%s,%s)"
            val = (data[j],"updated","updated","updated")
            mycursor.execute(sql,val)
            mydb.commit()
            print("=================")
            print(mycursor.rowcount,"row added")
            print("===================")
    except IndexError:
        sql = "INSERT INTO blog (title, blog_desc ,image_summary,image_url) VALUES (%s,%s,%s,%s)"
        val = (i,"updated","updated","updated")
        mycursor.execute(sql,val)
        mydb.commit()
        print("=================")
        print(mycursor.rowcount,"row added")
        print("===================")

# for m,n in enumerate(data):
#     try:
#         print(table[m][0])
#         if table[m][0] in data:
#             print("exist")
#         else:
#             print("doesn't exist")
#             # sql = "INSERT INTO blog (title, blog_desc ,image_summary,image_url) VALUES (%s,%s,%s,%s)"
#             # val = (n,"updated","updated","updated")
#             # mycursor.execute(sql,val)
#             # mydb.commit()
#             # print("=================")
#             # print(mycursor.rowcount,"row added")
#             # print("===================")
#     except IndexError:
#         # print("now we can update the data")
#         # print(n)
#         sql = "INSERT INTO blog (title, blog_desc ,image_summary,image_url) VALUES (%s,%s,%s,%s)"
#         val = (n,"updated","updated","updated")
#         mycursor.execute(sql,val)
#         mydb.commit()
#         print("=================")
#         print(mycursor.rowcount,"row added")
#         print("===================")
